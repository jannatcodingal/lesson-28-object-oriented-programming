class Employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destructer called")
def create_obj():
        print("making object")
        object=Employee()
        print("function end")
        return object
print("calling create_object() function")
obj = create_obj()
print("program ended")