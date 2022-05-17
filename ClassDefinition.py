class MyClass:
    # class variable
    class_var = "This is a class variable common to all instances"

    def __init__(self, inst_var1, inst_var2):
        self.inst_var1 = inst_var1
        self.inst_var2 = inst_var2

    def print_all_variables(self):
        print("inst_var1: " + self.inst_var1)
        print("inst_var2: " + self.inst_var2)


c1 = MyClass("a", "b")
c1.class_var = "Change in C1 class_var"
c2 = MyClass("c", "d")
c2.class_var = "Change in C2 class_var"

c1.print_all_variables()
c2.print_all_variables()

print("MyClass class_var", MyClass.class_var)
print("C1 class_var", c1.class_var)
print("C2 class_var", c2.class_var)

# Check class inheritance
class MyInheritedClass(MyClass):

    def print_all_variables(self):
        print("\n\nInside inherited class")


inherited_class = MyInheritedClass("e", "f")
print(inherited_class.print_all_variables())
print("Done")
