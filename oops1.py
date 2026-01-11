# initiate a class
class employee:
    # special methods/magic method/dunder mrthod - constructor
    def __init__(self):
       print("Started executing attribute/data")
       self.id = 123
       self.salary = 50000
       self.designation = "SDE"
       print("attribute/data have been initiated")
    
    # method
    def travel(self,destination):
        print("This travel function was called manually")
        print(f"Employee is noe travelling to {destination}")

# create an obj/instance of the class
sam = employee()

# print(sam.salary)
# print(sam.id)

# calling a method
sam.travel("Kerala") 

print(type(sam))