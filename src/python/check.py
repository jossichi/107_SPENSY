import graphviz

class KaryTreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
        self.parent = None  # Initialize parent to None

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

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

    def render_tree(self, output_file="tree_output.png"):
            """
            Phương thức để xuất cây thành file PNG với kích thước 4K.
            """
            dot = graphviz.Digraph(comment='Cây chuyên môn')

            def add_edges(node):
                for child in node.children:
                    dot.edge(node.value, child.value)
                    add_edges(child)

            # Thêm các cạnh của cây vào đồ thị
            add_edges(self.root)

            # Thiết lập các thuộc tính cho kích thước đồ thị (4K)
            dot.attr(size="3840,2160", dpi="300")  # Điều chỉnh kích thước và độ phân giải
            dot.attr('graph', ratio='compress')  # Giảm tỷ lệ đồ thị để phù hợp với kích thước 4K

            # Lưu đồ thị dưới dạng PNG với kích thước 4K
            dot.render(output_file, format="png", cleanup=True)
            print(f"Cây đã được lưu thành file PNG tại: {output_file}")
# Ví dụ sử dụng
tree = KaryTree()
data = {
  "Kinh tế": {
    "Quản trị kinh doanh": {
      "Sales": [],
      "Management": [],
      "Kinh doanh quốc tế": []
    },
    "Kinh tế học": [],
    "Tài chính": {
      "Tài chính doanh nghiệp": [],
      "Quản lý tài chính": [],
      "Tài chính ngân hàng": {
        "Đầu tư ngân hàng": [],
        "Tín dụng ngân hàng": []
      },
      "Công nghệ tài chính": []
    },
    "Ngân hàng": [
    "Tín dụng ngân hàng",
    "Đầu tư ngân hàng",
    "Tài chính ngân hàng",
    "Quản lý tài chính ngân hàng",
    "Ngân hàng đầu tư",
    "Ngân hàng thương mại",
    "Quản lý rủi ro ngân hàng",
    "Phân tích tín dụng",
    "Ngân hàng số",
    "Dịch vụ ngân hàng điện tử"
  ],
    "Marketing": {
      "Content creator": [],
      "SEO": []
    },
    
  }
}
tree.build_tree(data)
tree.render_tree("tree_output.png")
