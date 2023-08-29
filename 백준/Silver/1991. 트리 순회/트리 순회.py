class BinaryTree:
    def __init__(self):
        self.root = None
        self.tree = None

    def pre_order(self):
        order = ""
        
        def __pre_order(node):
            nonlocal order
            
            order += node
            if self.tree[node]["L"]:
                __pre_order(self.tree[node]["L"])
            if self.tree[node]["R"]:
                __pre_order(self.tree[node]["R"])
                        
        __pre_order(self.root)
        
        return order

    def in_order(self):
        order = ""
        
        def __in_order(node):   
            nonlocal order
            
            if self.tree[node]["L"]:
                __in_order(self.tree[node]["L"])
            order += node
            if self.tree[node]["R"]:
                __in_order(self.tree[node]["R"])
                
        __in_order(self.root)
        
        return order

    def post_order(self):
        order = ""
        
        def __post_order(node):
            nonlocal order
            
            if self.tree[node]["L"]:
                __post_order(self.tree[node]["L"])
            if self.tree[node]["R"]:
                __post_order(self.tree[node]["R"])
            order += node
            
        __post_order(self.root)
        
        return order


if __name__ == "__main__":
    N = int(input())
    T = {
        P: {
            "L": L if L is not "." else None
            , "R": R if R is not "." else None
        } for P, L, R in [input().split() for _ in range(N)]
    }

    binary_tree = BinaryTree()
    binary_tree.root = "A"
    binary_tree.tree = T
    
    print(binary_tree.pre_order())
    print(binary_tree.in_order())
    print(binary_tree.post_order())