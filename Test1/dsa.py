#tree
class Node:
def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

    class TreeStructure:
        def createRoot(self, data):
            self.root = Node(data)

            def insertNode(self,data):
                self.new_node = Node(data)

                #logic 1
                if self.root.left == None :
                    self.root.left = self.new_node
                elif self.root.right == None:
                    self.root.right = self.new_node
                else:
                    print("move to next level as the root is connected to two nodes")
                    