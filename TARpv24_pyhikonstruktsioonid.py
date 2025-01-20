def getMethods():
    methods = [method_name for method_name in dir(Program)
                         if callable(getattr(Program, method_name)) and method_name.startswith("run") and len(method_name) > 3]
    return methods

class Program:
    #def __init__:(self)

    def run(self, pId):
        #t = type(Program)
     

        if (pId == 0):
            self.runHello()
        if (pId == 1):
            self.runOps()
        else:
            print("Error: No program found!")
            return

        #print("\nProgram completed.")

    def runHello(self):
        print("Hello world!")

    def runOps(self):
        a = 5
        aste = 2
        tulemus = a**aste
        print(a, " ** ", aste, " = ", tulemus, "\n")

        #korraldamine
        a = int(input("Enter number a: "))
        b = int(input("Enter number b: "))

        print(a, " * ", b, " = ", a*b, "\n")

        #jagamine
        a = int(input("Enter number a: "))
        divider = int(input("Enter divider: "))

        print(a, " / ", divider, " = ", a/divider, "\n")

for method in getMethods():
    print(method)

print("0 - Hello World")
print("1 - Basic Operations")
    
pId = int(input("Select program: "))
prog = Program()
prog.run(pId)

print("test change")
