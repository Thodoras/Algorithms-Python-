from BKTree import BKTree

tree = BKTree()

tree.insert("food")
tree.insert("good")
tree.insert("cook")
tree.insert("fowl")
tree.insert("spoon")
tree.insert("fork")

print(tree._tree)
print(tree.search("aork",1))
