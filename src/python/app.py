from flask import Flask, jsonify, request
import json
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    return response

# Construct the correct path to the Excel file
excel_file_path = os.path.join('src/python/IDP_DATA_MENTEE.xlsx')

# Load Excel file
excel_file = pd.ExcelFile(excel_file_path)
df_mentor = pd.read_excel(excel_file, sheet_name='Mentor')
df_mentee = pd.read_excel(excel_file, sheet_name='Mentee')

# Convert 'Giới tính' to numeric
df_mentor['Giới tính'] = df_mentor['Giới tính'].apply(lambda x: 1 if x == "Nữ" else 0)
df_mentee['Giới tính'] = df_mentee['Giới tính'].apply(lambda x: 1 if x == "Nữ" else 0)

# Create dummy columns for "Chuyên Môn"
df_mentor = pd.get_dummies(df_mentor, columns=["Chuyên Môn"])
df_mentee = pd.get_dummies(df_mentee, columns=["Chuyên Môn"])

# Align columns
all_columns = set(df_mentor.columns).union(set(df_mentee.columns))
df_mentor = df_mentor.reindex(columns=all_columns, fill_value=0)
df_mentee = df_mentee.reindex(columns=all_columns, fill_value=0)

# Kary Tree Node and Tree Definitions
class KaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

class KaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, data):
        self.root = KaryTreeNode("Cây chuyên môn")
        self._build_tree_recursive(self.root, data)
        
    def _build_tree_recursive(self, node, data):
        for key, value in data.items():
            child_node = KaryTreeNode(key)
            node.add_child(child_node)
            if isinstance(value, dict):
                self._build_tree_recursive(child_node, value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self._build_tree_recursive(child_node, item)
                    else:
                        child_node.add_child(KaryTreeNode(item))

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level * 2 + node.value)
        for child in node.children:
            self.print_tree(child, level + 1)

# Load JSON data for the tree
json_file_path = os.path.join('src/python/list.json')

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

tree = KaryTree()
tree.build_tree(data)

print("Kary Tree structure:")
tree.print_tree() 

@app.route('/api/kary_tree', methods=['GET'])
def get_kary_tree():
    # Assuming `tree` is your KaryTree object
    def serialize_node(node):
        # Serialize each node with its children
        return {
            "name": node.value,
            "children": [serialize_node(child) for child in node.children]
        }
    
    # Start serialization from the root
    tree_structure = serialize_node(tree.root)
    
    return jsonify(tree_structure)


def get_subcategories(tree_node, category):
    # Tìm chuyên môn con của một chuyên môn gốc
    if tree_node.value == category:
        return [child.value for child in tree_node.children]
    
    for child in tree_node.children:
        subcategories = get_subcategories(child, category)
        if subcategories:
            return subcategories
    return []

def get_parent_categories(tree_node, category):
    """
    Hàm đệ quy tìm các node cha của chuyên môn trong cây.
    Trả về một danh sách các node cha từ chuyên môn đến gốc cây.
    """
    if tree_node.value == category:
        return [tree_node.value]
    
    for child in tree_node.children:
        parent_categories = get_parent_categories(child, category)
        if parent_categories:
            return parent_categories + [tree_node.value]
    
    return []

def match_mentor_mentee_kary(df_mentor, df_mentee, tree):
    matches = []
    no_matches = []  # List to track mentors without a match

    # Duyệt qua từng mentor
    for _, mentor in df_mentor.iterrows():
        mentor_specialty = mentor.filter(like="Chuyên Môn_").idxmax().replace("Chuyên Môn_", "")
        mentor_parent_categories = get_parent_categories(tree.root, mentor_specialty)
        mentor_subcategories = get_subcategories(tree.root, mentor_specialty)
        mentor_subcategories.append(mentor_specialty)
        
        # Lọc các chuyên môn trùng lặp
        mentor_specialties = list(set(mentor_subcategories + mentor_parent_categories))
        
        mentor_gender = mentor["Giới tính"]
        
        print(f"Checking mentor: {mentor['Họ tên']}, specialty: {mentor_specialty}, gender: {mentor_gender}")
        print(f"  Mentor's full specialty list: {mentor_specialties}")

        match_found = False
        # Duyệt qua từng mentee
        for _, mentee in df_mentee.iterrows():
            mentee_specialty = mentee.filter(like="Chuyên Môn_").idxmax().replace("Chuyên Môn_", "")
            mentee_gender = mentee["Giới tính"]

            print(f"  Checking mentee: {mentee['Họ tên']}, specialty: {mentee_specialty}, gender: {mentee_gender}")

            # Debugging the match condition
            if mentee_specialty in mentor_specialties and mentee_gender == mentor_gender:
                print(f"    Match found: {mentor['Họ tên']} <-> {mentee['Họ tên']}")
                matches.append((mentor["Họ tên"], mentee["Họ tên"], mentor_specialty, mentee_specialty))
                match_found = True
            else:
                print(f"    No match. Mentee's specialty not in mentor's specialties or genders do not match.")
        
        if not match_found:
            no_matches.append({
                'mentor': mentor["Họ tên"],
                'mentor_specialties': mentor_specialties,
                'gender': "Nữ" if mentor_gender == 1 else "Nam"
            })
    
    return matches, no_matches

print(df_mentor.head)

@app.route('/matches', methods=['GET'])
def get_matches():
    matches = match_mentor_mentee_kary(df_mentor, df_mentee, tree)
    serialized_matches = [{
        'mentor': mentor,
        'mentee': mentee,
        'mentor_specialty': mentor_spec,
        'mentee_specialty': mentee_spec
    } for mentor, mentee, mentor_spec, mentee_spec in matches]
    return jsonify(serialized_matches)

def find_specialization_path(tree, specialization):
    # Normalize the specialization input to lowercase and strip any leading/trailing spaces
    normalized_specialization = specialization.strip().lower()

    # Now check the tree for the normalized specialization in lowercase
    path = get_parent_categories(tree.root, normalized_specialization)
    
    if path:
        return path[::-1]  # Reverse to get the path from root to the specialization
    
    return None

@app.route('/api/find_mentors', methods=['POST'])
def find_mentors():
    data = request.get_json()

    # Normalize 'Giới tính'
    gender = data.get("gender", "").strip().lower()
    data['gender'] = 1 if gender in ["female", "nữ", "f"] else 0 if gender in ["male", "nam", "m"] else None

    # Normalize 'specialization' to match the dummy column format
    specialization = data.get("specialization", "").strip().lower()  # Normalize the specialization input
    if not specialization:
        return jsonify({"message": "Specialization is required"}), 400

    # Convert input data to DataFrame for processing
    data = pd.DataFrame([data])

    # Ensure the 'Giới tính' column exists and is correct
    data['Giới tính'] = data['gender']
    data['Họ tên'] = data['fullName']
    # Create dummy columns for "Chuyên Môn" based on the input specialization
    specialization_dummy = pd.get_dummies([specialization], prefix="Chuyên Môn")
    data = pd.concat([data, specialization_dummy], axis=1)

    # Debugging: Check the normalization of the input specialization
    print("Normalized data:", data)

    # Trước khi thực hiện matching, kiểm tra xem chuyên môn có trong cây KaryTree không
    path_to_specialization = find_specialization_path(tree, specialization)
    
    if path_to_specialization:
        print(f"Chuyên môn '{specialization}' đã được tìm thấy trong cây chuyên môn.")
        print("Đường đi của chuyên môn trong cây:")
        print(" -> ".join(path_to_specialization))
    else:
        print(f"Chuyên môn '{specialization}' không tồn tại trong cây chuyên môn.")
    
    # Perform the matching with mentor data
    matches, no_matches = match_mentor_mentee_kary(df_mentor, data, tree)

    # Return the matched mentors and mentees if matches found
    if matches:
        serialized_matches = [{
            'mentor': mentor,
            'mentee': data["fullName"].iloc[0],  # The mentee name is from the input data
            'mentor_specialty': mentor_spec,
            'mentee_specialty': specialization
        } for mentor, _, mentor_spec, _ in matches]

        return jsonify({"matches": serialized_matches}), 200
    else:
        return jsonify({
            "message": "No matches found.",
            "available_mentors": no_matches
        }), 200
    
if __name__ == '__main__':
    app.run(debug=True)
