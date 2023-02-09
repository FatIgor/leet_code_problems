class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class q0589_nary_tree:
    def traverse(self, root:'Node'):
        output = []

        self.dfs(root, output)

        return output

    def dfs(self, root, output):

        if root is None:
            return

        output.append(root.val)

        for child in root.children:
            self.dfs(child, output)

    def tests(self):
        print(self.__class__.__name__)
        root = Node(1,[])
        root.children.append(Node(2,[]))
        root.children.append(Node(3,[]))
        root.children.append(Node(4,[]))
        root.children[0].children.append(Node(5,[]))
        root.children[0].children[0].children.append(Node(10,[]))
        root.children[0].children.append(Node(6,[]))
        root.children[0].children[1].children.append(Node(11,[]))
        root.children[0].children[1].children.append(Node(12,[]))
        root.children[0].children[1].children.append(Node(13,[]))
        root.children[2].children.append(Node(7,[]))
        root.children[2].children.append(Node(8,[]))
        root.children[2].children.append(Node(9,[]))

        n0=self.traverse(root)
        print(n0)