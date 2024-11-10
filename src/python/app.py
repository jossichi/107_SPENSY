from flask import Flask, jsonify, request
import json
import pandas as pd
import os
import gspread
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    return response

# Đường dẫn hiện tại của file script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the correct path to the Excel file
excel_file_path = os.path.join(r'src/python/IDP_DATA_MENTEE.xlsx')

# Print the constructed file path to verify
print(f"Excel file path: {excel_file_path}")

excel_file = pd.ExcelFile(excel_file_path)
df_mentor = pd.read_excel(excel_file, sheet_name='Mentor')
df_mentee = pd.read_excel(excel_file, sheet_name='Mentee')

# Chuyển đổi cột 'Giới tính' thành số nguyên (1 cho 'Nữ', 0 cho 'Nam')
df_mentor['Giới tính'] = df_mentor['Giới tính'].apply(lambda x: 1 if x == "Nữ" else 0)
df_mentee['Giới tính'] = df_mentee['Giới tính'].apply(lambda x: 1 if x == "Nữ" else 0)

# Tạo các cột giả định cho các giá trị trong 'Chuyên Môn' và đảm bảo tất cả các cột đều có trong cả mentor và mentee
df_mentor = pd.get_dummies(df_mentor, columns=["Chuyên Môn"])
df_mentee = pd.get_dummies(df_mentee, columns=["Chuyên Môn"])


all_columns = set(df_mentor.columns).union(set(df_mentee.columns))
df_mentor = df_mentor.reindex(columns=all_columns, fill_value=0)
df_mentee = df_mentee.reindex(columns=all_columns, fill_value=0)

# Định nghĩa lớp nút cho cây k-ary
class KaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

# Định nghĩa lớp cây k-ary
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
        print(" " * level * 2 + node.value )
        for child in node.children:
            self.print_tree(child, level + 1)

# Đọc dữ liệu từ file JSON để xây dựng cây k-ary
json_file_path = os.path.join(r'src/python/list.json')

data = {}
with open(json_file_path, 'r', encoding='utf-8') as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

tree = KaryTree()
tree.build_tree(data)

# Hàm lấy danh sách con chuyên mục từ cây k-ary
def get_subcategories(tree_node, category):
    if tree_node.value == category:
        return [child.value for child in tree_node.children]
    for child in tree_node.children:
        subcategories = get_subcategories(child, category)
        if subcategories:
            return subcategories
    return []

# Hàm ghép cặp mentor và mentee dựa trên cây k-ary và giới tính
def match_mentor_mentee_kary_using_data(df_mentor, df_mentee, tree):
    matches = []
    
    for _, mentor in df_mentor.iterrows():
        # Lấy chuyên môn và giới tính của mentor
        mentor_specialty = mentor.filter(like="Chuyên Môn_").idxmax().replace("Chuyên Môn_", "")
        mentor_subcategories = get_subcategories(tree.root, mentor_specialty)
        mentor_subcategories.append(mentor_specialty)  # Thêm chuyên môn của chính mentor vào danh sách
        mentor_gender = mentor["Giới tính"]
        
        for _, mentee in df_mentee.iterrows():
            # Lấy chuyên môn và giới tính của mentee
            mentee_specialty = mentee.filter(like="Chuyên Môn_").idxmax().replace("Chuyên Môn_", "")
            mentee_gender = mentee["Giới tính"]
            
            if mentee_specialty in mentor_subcategories and mentee_gender == mentor_gender:
                matches.append((mentor["Họ tên"], mentee["Họ tên"], mentor_specialty, mentee_specialty))
    
    return matches

def match_mentor_mentee_kary(df_mentor, user_specialty, user_gender, tree):
    matches = []
    
    # Kiểm tra nếu user_specialty là None hoặc chuỗi rỗng
    if not user_specialty:
        raise ValueError("Chuyên môn của người dùng không được để trống.")
    
    # Lọc danh sách mentor
    user_subcategories = get_subcategories(tree.root, user_specialty)
    user_subcategories.append(user_specialty)

    # Chuẩn hóa đầu vào của user (chuyển thành chữ thường)
    user_specialty = user_specialty.lower().strip()
    user_subcategories = [category.lower().strip() for category in user_subcategories]

    for _, mentor in df_mentor.iterrows():
        # Chuẩn hóa chuyên môn của mentor (chuyển thành chữ thường)
        mentor_specialty = mentor.filter(like="Chuyên Môn_").idxmax().replace("Chuyên Môn_", "").lower().strip()
        mentor_gender = mentor["Giới tính"]

        # Kiểm tra nếu mentor phù hợp với user (dựa trên chuyên môn và giới tính)
        if mentor_specialty in user_subcategories and mentor_gender == user_gender:
            print(f"Match found for User: {mentor['Họ tên']}, Specialty: {mentor_specialty}")
            matches.append((mentor["Họ tên"], mentor_specialty))

    return matches

# Endpoint API để trả về danh sách matches
@app.route('/api/matches', methods=['GET'])
def get_matches():
    matches = match_mentor_mentee_kary_using_data(df_mentor, df_mentee, tree)
    serialized_matches = []
    for mentor, mentee, mentor_spec, mentee_spec in matches:
        serialized_matches.append({
            'mentor': mentor,
            'mentee': mentee,
            'mentor_specialty': mentor_spec,
            'mentee_specialty': mentee_spec
        })
    return jsonify(serialized_matches)

@app.route('/api/find_mentors', methods=['POST'])
def find_mentors():
    try:
        data = request.get_json()
        print("Received data:", data)

        # Extract input data
        full_name = data.get("fullName")
        specialization = data.get("specialization")
        gender = data.get("gender")

        # Filter mentors based on specialization and gender
        matching_mentors = []

        for _, mentor in df_mentor.iterrows():
            mentor_specialty = mentor.filter(like="Chuyên Môn_").idxmax().replace("Chuyên Môn_", "")
            mentor_gender = "female" if mentor["Giới tính"] == 1 else "male"

            # Check if the mentor matches the provided specialization and gender
            if mentor_specialty.lower() == specialization.lower() and mentor_gender == gender:
                matching_mentors.append({
                    "mentor": mentor["Họ tên"],
                    "mentor_specialty": mentor_specialty
                })

        if not matching_mentors:
            return jsonify({"message": "Hệ thống chưa cập nhật mentor phù hợp với chuyên ngành của bạn"}), 404

        return jsonify(matching_mentors)

    except Exception as e:
        print(f"Error processing the request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
