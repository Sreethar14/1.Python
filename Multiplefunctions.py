classmultiplefunctions():
  def OddEven():
        num=int(input("Enter a number:"))
        if(num%2)==0:
            print("{0}is Even number".format(num))
        else:
            print("{0}is Odd number".format(num))
         return message

class OddEven():
  def OddEven():
        num=int(input("Enter a number:"))
        if(num%2)==0:
            print("{0}is Even number".format(num))
        else:
            print("{0}is Odd number".format(num))
        return message

class ElegiblityForMarriage():
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your age"))
        
        if(gender=='Male'):
            if(age>=21):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        elif(gender=='Female'):         
            if(age>18):
                    print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
            return message
        
def percentage():
    m1=int(input("Subject1=  "))
    m2=int(input("Subject2=  "))
    m3=int(input("Subject3=  "))
    m4=int(input("Subject4=  "))
    m5=int(input("Subject5=  "))
    Total = m1+m2+m3+m4+m5
    print("Total: " ,m1+m2+m3+m4+m5)
    Percent = (Total / 500) * 100
    print("Perentage : ",Percent) 
    return message


def triangle():
    Height=int(input("Height:"))
    Breadth=int(input("Breadth:"))
    print("Area formula: (Height*Breadth)/2")
    print("Area of Triangle:", (Height/Breadth)/2)
    Height1=int(input("Height1:"))
    Height2=int(input("Height2:"))
    Breadth=int(input("Breadth:"))
    print("Perimeter formula: Height1+Height2+Breadth")
    print("Perimeter of Triangle: ",Height1+Height2+Breadth)
    return message()



         
         
            