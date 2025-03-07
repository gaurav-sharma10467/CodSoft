class calculator:
    def __init__(self):
        print("It is a Simple Calculator using OOPS")
    #It return the sum
    def sum(self,x,y):
        return x+y
    
    #It return the difference
    def subtract(self,x,y):
        return x-y

    #It return the multiplication
    def multiply(self,x,y):
        return x*y
    
    #It return the deivision
    def division(self,x,y):
        if(y==0):
            return "Invalid input"
        return x/y
    
#__Main Code__
Cal=calculator()

x=int(input("Enter 1st number:-"))
y=int(input("Enter 2nd number:-"))

print("Addition:-",Cal.sum(x,y))
print("Subtraction:-",Cal.subtract(x,y))
print("Multiplication:-",Cal.multiply(x,y))
print("Division:-",Cal.division(x,y))