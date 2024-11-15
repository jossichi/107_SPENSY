from flask import Flask, jsonify, request
import json
import pandas as pd
import os
from flask_cors import CORS
import requests
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

class KaryTreeNode:
    def __init__(self, value, depth=0):
        self.value = value
        self.children = []
        self.depth = depth

    def add_child(self, node):
        self.children.append(node)

# Định nghĩa lớp cây k-ary
class KaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, data):
        self.root = KaryTreeNode("Cây chuyên môn", 0)
        self._build_tree_recursive(self.root, data)
        
    def _build_tree_recursive(self, node, data, depth=1):
        for key, value in data.items():
            child_node = KaryTreeNode(key, depth)
            node.add_child(child_node)
            if isinstance(value, dict):
                self._build_tree_recursive(child_node, value, depth + 1)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self._build_tree_recursive(child_node, item, depth + 1)
                    else:
                        child_node.add_child(KaryTreeNode(item, depth + 1))

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        # In giá trị của nút cùng với độ sâu
        print(" " * level * 2 + f"{node.value} (Độ sâu: {node.depth})")
        for child in node.children:
            self.print_tree(child, level + 1)
    
    def get_max_depth(self, node=None):
        if node is None:
            node = self.root
        # Nếu nút không có con, độ sâu là chính nó
        if not node.children:
            return node.depth
        # Tính độ sâu tối đa từ các con
        child_depths = [self.get_max_depth(child) for child in node.children]
        return max(child_depths)

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

def match_mentor_mentee_kary_using_data(df_mentor, df_mentee, tree):
    matches = []
    
    # Hàm đệ quy để duyệt cây và so khớp mentor-mentee
    def match_node(node):
        if not node.children:
            return
        
        for child in node.children:
            if isinstance(child.value, str):  # Chỉ tìm kiếm trong các node chuyên môn
                for _, mentor in df_mentor.iterrows():
                    mentor_specialty = mentor.filter(like="Chuyên Môn_").idxmax().replace("Chuyên Môn_", "")
                    mentor_subcategories = get_subcategories(tree.root, mentor_specialty)
                    mentor_subcategories.append(mentor_specialty)
                    mentor_gender = mentor["Giới tính"]

                    for _, mentee in df_mentee.iterrows():
                        mentee_specialty = mentee.filter(like="Chuyên Môn_").idxmax().replace("Chuyên Môn_", "")
                        mentee_gender = mentee["Giới tính"]

                        # So khớp dựa trên chuyên môn và giới tính
                        if mentee_specialty in mentor_subcategories and mentee_gender == mentor_gender:
                            # Sử dụng độ sâu đã có từ cây
                            mentor_depth = node.depth
                            mentee_depth = child.depth

                            if mentor_depth < mentee_depth:  # Mentor's depth must be smaller (closer to root)
                                matches.append((mentor["Họ tên"], mentee["Họ tên"], mentor_specialty, mentee_specialty))
            # Tiếp tục duyệt cây mà không cần phải gọi DFS lại
            match_node(child)

    # Bắt đầu từ root node
    match_node(tree.root)

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

class Node:
    def __init__(self, mentor, mentee, mentor_specialty, mentee_specialty):
        self.mentor = mentor
        self.mentee = mentee
        self.mentor_specialty = mentor_specialty
        self.mentee_specialty = mentee_specialty
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, mentor, mentee, mentor_specialty, mentee_specialty):
        new_node = Node(mentor, mentee, mentor_specialty, mentee_specialty)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"Mentor: {current.mentor}, Mentee: {current.mentee}, "
                  f"Mentor Specialty: {current.mentor_specialty}, Mentee Specialty: {current.mentee_specialty}")
            current = current.next

    def find_matches_for_user(self, user_full_name, user_specialty):
        matches = []
        current = self.head
        while current:
            # Kiểm tra nếu mentee trong node trùng với tên người dùng và specialty
            if current.mentee == user_full_name and current.mentee_specialty == user_specialty:
                matches.append({
                    "mentor": current.mentor,
                    "mentee": current.mentee,
                    "mentor_specialty": current.mentor_specialty,
                    "mentee_specialty": current.mentee_specialty
                })
            current = current.next
        return matches

@app.route('/matches', methods=['GET'])
def get_matches():
    matches = match_mentor_mentee_kary_using_data(df_mentor, df_mentee, tree)
    
    # Create an instance of LinkedList
    linked_list = LinkedList()

    # Populate the LinkedList with match results
    for mentor, mentee, mentor_spec, mentee_spec in matches:
        linked_list.append(mentor, mentee, mentor_spec, mentee_spec)

    # Display the linked list (for debugging or verification)
    linked_list.display()

    # Serialize the linked list into a list for JSON response
    serialized_matches = []
    current = linked_list.head
    while current:
        serialized_matches.append({
            'mentor': current.mentor,
            'mentee': current.mentee,
            'mentor_specialty': current.mentor_specialty,
            'mentee_specialty': current.mentee_specialty
        })
        current = current.next

    return jsonify(serialized_matches)

def preprocess_user_data(user_data, reference_df):

    try:
        # Tạo DataFrame từ dữ liệu người dùng
        user_df = pd.DataFrame([{
            'Họ tên': user_data.get('fullName', ''),
            'Chuyên Môn': user_data.get('specialization', ''),
            'Giới tính': 1 if user_data.get('gender', '').lower() == 'female' else 0
        }])

        # Chuyển đổi cột 'Chuyên Môn' thành dummies
        user_df = pd.get_dummies(user_df, columns=['Chuyên Môn'])

        # Đảm bảo các cột của user_df khớp với reference_df (thêm cột còn thiếu)
        all_columns = set(reference_df.columns)
        user_df = user_df.reindex(columns=all_columns, fill_value=0)

        # Loại bỏ các cột không liên quan (nếu có)
        user_df = user_df[reference_df.columns]

        return user_df
    except Exception as e:
        raise ValueError(f"Lỗi khi chuẩn hóa dữ liệu người dùng: {e}")

def save_user_data_to_excel(user_data):
    try:
        # Đường dẫn đến file Excel
        file_path = r'src\python\IDP_DATA_MENTEE.xlsx'

        # Đọc dữ liệu hiện tại từ file Excel
        try:
            mentee_df = pd.read_excel(file_path, sheet_name='Mentee', engine='openpyxl')
        except FileNotFoundError:
            mentee_df = pd.DataFrame(columns=["Họ tên", "Giới tính", "Chuyên môn", "Chức vụ"])

        # Lấy giá trị giới tính từ user_data và xử lý chính xác
        gender = user_data.get('gender', '').lower()
        if gender == 'female' or gender == 'nữ':
            gender_label = 'Nữ'
        else:
            gender_label = 'Nam'

        # Chuyển dữ liệu người dùng thành một dòng DataFrame
        new_row = pd.DataFrame([{
            "Họ tên": user_data.get('fullName', ''),
            "Giới tính": gender_label,
            "Chuyên Môn": user_data.get('specialization', '').capitalize(),
            "Chức vụ": "Mentee"
        }])

        # Thêm dữ liệu vào DataFrame
        mentee_df = pd.concat([mentee_df, new_row], ignore_index=True)

        # Ghi lại vào file Excel
        with pd.ExcelWriter(file_path, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            mentee_df.to_excel(writer, sheet_name='Mentee', index=False)

        print("Lưu dữ liệu người dùng thành công.")

        # Reload lại file Excel để cập nhật df_mentor và df_mentee
        reload_excel_data()

    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu vào Excel: {e}")
        raise e

def reload_excel_data():
    global df_mentor, df_mentee

    try:
        # Đọc lại dữ liệu từ file Excel
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

        print("Dữ liệu Excel đã được reload thành công.")

    except Exception as e:
        print(f"Lỗi khi reload dữ liệu từ Excel: {e}")

def check_user_in_mentees(user_full_name):
    """ Kiểm tra xem người dùng có trong sheet Mentee và API /matches không """
    try:
        # Đọc dữ liệu từ file Excel
        file_path = r'src\python\IDP_DATA_MENTEE.xlsx'
        mentee_df = pd.read_excel(file_path, sheet_name='Mentee', engine='openpyxl')

        # Tìm kiếm người dùng theo tên (làm sạch khoảng trắng)
        matched_user = mentee_df[mentee_df['Họ tên'].str.strip() == user_full_name.strip()]

        # In ra kết quả để debug
        print(f"Tìm thấy người dùng {user_full_name.strip()} trong sheet Mentee? {'Có' if not matched_user.empty else 'Không'}")

        # Kết quả từ sheet Mentee
        if not matched_user.empty:
            # Nếu tìm thấy người dùng, lấy thông tin Mentor và Chuyên môn
            mentor = matched_user.iloc[0]['Chức vụ']  # Giả sử cột 'Chức vụ' chứa thông tin Mentor
            specialty = matched_user.iloc[0]['Chuyên Môn']  # Giả sử cột 'Chuyên Môn' chứa thông tin Chuyên môn
            print(f"Thông tin từ sheet Mentee: Mentor = {mentor}, Specialty = {specialty}")
            mentee_info = {"mentor": mentor, "specialty": specialty}
        else:
            mentee_info = None
            print("Không tìm thấy người dùng trong sheet Mentee.")

        # Kiểm tra thông tin người dùng trong API /matches
        try:
            # Gửi yêu cầu GET đến API /matches
            response = requests.get('http://localhost:5000/matches')
            if response.status_code == 200:
                matches = response.json()

                # Tìm trong danh sách matches để tìm người dùng
                for match in matches:
                    if match['mentee'] == user_full_name.strip():
                        print(f"Thông tin từ API /matches: {match}")
                        return {"mentor": match['mentor'], "specialty": match['mentor_specialty']}
                
                # Nếu không tìm thấy người dùng trong matches
                print(f"Không tìm thấy người dùng {user_full_name} trong API /matches.")
                return mentee_info

            else:
                print("Không thể lấy thông tin từ /matches, status code:", response.status_code)
                return mentee_info

        except Exception as e:
            print(f"Lỗi khi gửi yêu cầu đến API /matches: {e}")
            return mentee_info

    except Exception as e:
        print(f"Lỗi khi kiểm tra người dùng trong sheet Mentee: {e}")
        return None

@app.route('/api/find_mentors', methods=['POST'])
def find_mentors():
    try:
        # Lấy dữ liệu từ yêu cầu POST
        user_data = request.json
        print("Thông tin người dùng nhập:", user_data)

        # Chuẩn hóa dữ liệu người dùng
        user_df = preprocess_user_data(user_data, df_mentor)
        user_df = user_df.reindex(columns=df_mentee.columns, fill_value=0)

        # Lưu dữ liệu người dùng vào Excel
        save_user_data_to_excel(user_data)
        print("Lưu dữ liệu người dùng thành công. Dữ liệu Excel đã được reload thành công.")

        # Kiểm tra người dùng trong sheet Mentee
        user_full_name = user_data.get('fullName', '').strip()
        match_info = check_user_in_mentees(user_full_name)
        if match_info:
            print(f"Tìm thấy người dùng {user_full_name} trong sheet Mentee? Có")

        # Lấy thông tin chuyên môn của người dùng
        user_specialty = user_data.get('specialization', '').strip()

        # Tìm chuyên môn phụ
        related_specialties = get_subcategories(tree.root, user_specialty)
        user_df = user_df.apply(lambda col: 1 if col.name in related_specialties else col)

        gender_value = user_data.get('gender', '').strip().lower()
        user_gender = 1 if gender_value in ['female', 'woman', 'f'] else 0

        # Ghép cặp mentor - mentee
        matched_mentors = match_mentor_mentee_kary(df_mentor, user_specialty, user_gender, tree)

        # Tạo LinkedList
        linked_list = LinkedList()
        for mentor, mentee, mentor_spec, mentee_spec in matched_mentors:
            linked_list.append(mentor, mentee, mentor_spec, mentee_spec)

        linked_list.display()

        # Kiểm tra LinkedList với người dùng
        filtered_matches = []
        match_count = 0
        current = linked_list.head

        while current:
            if current.mentee.strip() == user_full_name.strip():
                filtered_matches.append({
                    "mentor": current.mentor,
                    "mentee": current.mentee,
                    "mentor_specialty": current.mentor_specialty,
                    "mentee_specialty": current.mentee_specialty
                })
                match_count += 1
            current = current.next

        if not filtered_matches:
            filtered_matches.append({
                "message": f"Không tìm thấy người dùng {user_full_name} trong danh sách mentor-mentee."
            })

        print(f"Không tồn tại {user_full_name} trong linked list.")

        # Kiểm tra tồn tại trong API
        print(f"Đang kiểm tra sự tồn tại của {user_full_name} trong API /matches...")
        try:
            response = requests.get('http://localhost:5000/matches')
            if response.status_code == 200:
                matches = response.json()

                # Kiểm tra sự tồn tại của user_full_name trong kết quả API
                user_matches = [
                    match for match in matches
                    if match['mentee'].strip().lower() == user_full_name.strip().lower() and 
                    match['mentee_specialty'].strip().lower() == user_specialty.strip().lower()
                ]

                if user_matches:
                    print(f"Đã tìm thấy mentee {user_full_name} trong API /matches.")
                    return jsonify({
                        "message": f"Tìm thấy {len(user_matches)} kết quả cho {user_full_name} trong API.",
                        "matches": user_matches
                    }), 200
                else:
                    print(f"Không tìm thấy mentee {user_full_name} trong API /matches.")
                    return jsonify({
                        "message": f"Không tìm thấy {user_full_name} trong API."
                    }), 404
            else:
                print(f"Không thể lấy thông tin từ /matches, status code: {response.status_code}")
                return jsonify({
                    "error": f"Không thể truy cập API /matches, status code: {response.status_code}"
                }), 500

        except Exception as e:
            print(f"Lỗi khi gửi yêu cầu đến /matches: {e}")
            return jsonify({"error": f"Lỗi khi gọi API: {str(e)}"}), 500

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)