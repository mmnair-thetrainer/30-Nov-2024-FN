class Items:
    def __init__(self, item):
        self.item = item

    def __add__(self, other):
        return self.item + other.item

    def __gt__(self, other):
        return len(self.item) > len(other.item)

obj1 = Items([6,7,5,2,8,9])
obj2 = Items([17,21,16])

print("obj1 + obj2 :", obj1+obj2)
print("obj1 > obj2 :", obj1>obj2)