# from abc import ABCMeta, abstractmethod
# class BaseNodePrinter(metaclass=ABCMeta):
#     @abstractmethod
#     def get_level_printer(self):
#         raise NotImplementedError

# class LevelOnePrinter(BaseNodePrinter):
#     def get_level_printer(self):
#         indent = self.get_level() * " " *3
#         print(f"{indent} {self.data}")            
#         for child in self.children:
#             child.print()
#         pass


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        count = 0
        parent = self.parent
        while parent:
            count +=1
            parent = parent.parent
        return count
    
    def print(self, type: str = "all"):

        if type == "all":
            indent = self.get_level() * " " *3
            print(f"{indent} {self.data}")            
            for child in self.children:
                child.print()
        elif type =="level1":
            level = self.get_level()

            print(f"{indent} {self.data}")            
            for child in self.children:
                child.print()





        







root = TreeNode("Global")
l1 = TreeNode("Nepal")
l1.add_child(TreeNode("Provience 1"))
l1.add_child(TreeNode("Provience 2"))
l1.add_child(TreeNode("Provience 3"))

l2 = TreeNode("USA")
l2.add_child(TreeNode("California"))
l2.add_child(TreeNode("Texas"))
l2.add_child(TreeNode("New York"))
root.add_child(l1)
root.add_child(l2)

root.print()
    

