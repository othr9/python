print("#####################")
print("#  Coder By othr    #")
print("#####################\n\n")
print("(1)and(2)if+not(3)elif")
print("(4)for+in(5)pass(6)while")
print("(7)class(8)else(9)continue(10)excpt")



exa=('Example')
a=int(input('Chose Number: '))

def num1():
    print('Exampel to and :\n\nname=othr\nage=19\na=input("Enter name: ")\ns=input("Enter age: ")\nif a=="name" and s==19:\n   print("welcome othr")\n\nDid you understand (and)?')
def num2():
    print('Exampel to if:\n\nname=othr\nage=19\na=input("Enter name: ")\ns=input("Enter age: ")\nif a=="name" and s==19:\n   print("welcome othr")')
    print('\nExample to not:\na=input("you name: ")\nif not a=="othr"\n  print("not found")\nelse:\n   print("welcome")\nOutput:')
    print('you name: khaled\nnot found\nyou name: othr\nwelcome')
    print('\n(Everything is clear !)')
def num3():
    print('Example to elif: ')
    print("num=3\nif num > 0:\n   print('Positive number')\nelif num == 0:\n   print('Zero')\nelse:\n   print('Negative number')")
    print('\n(i think this is clear)')
def num4():
    print('Example to for,in:\nfor i in range(1,6):\n   print(i)\n1\n2\n3\n4\n5')
def num5():
    print("Example to pass:")
    print("while True:\n   pass")
def num6():
    print("Example to while:")
    print("count = 0\nwhile count < 4:\n   print('This count is:',count)\n   count = count + 1\n\nprint('Good bye!')")
    print("Output:")
    print("The count is: 0\nThe count is: 1\nThe count is: 2\nThe count is: 3\nGood bye!")
def num7():
    print("Example to Class:\n")
    print("class Car:\n   def __init__(self,Name):\n      self._Nmae=Name")
    print("   def GetOwner(self):\n      print('Owner is',self._Nmae)\ndef main():\nmycar=Car('khaled')\nmycar.GetOwner()")
    print("if __name__ == '__main__':main()")
    print("Output:\nOwner is khaled")
def num8():
    print(exa,"to else:")
    print('if 10<5:\n   print("yes")\nelse:\n   print("no")\nOutput:\nno')
def num9():
    print(exa,"to continue:\n")
    print("for num in range(2,6):\n   if num % 2==0:\n      print('Found an even number', num)\n      continue\n   print('Found a number',num)")
    print("Output:\nFound an even number 2\nFound a number 3\nFound an even number 4\nFound a number 5")
def num10():
    print(exa,'to Excpt\n')
    print("try:\n   with open('file', 'r') as file:\n       file = file.read()\nexcept OSError:\n   print('Not Exists')")
    print('Output:\nNot Exists')
def main():
    if a==1:
        num1()
    elif a==2:
        num2()
    elif a==3:
        num3()
    elif a==4:
        num4()
    elif a==5:
        num5()
    elif a==6:
        num6()
    elif a==7:
        num7()
    elif a==8:
        num8()
    elif a==9:
        num9()
    elif a==10:
        num10()
if __name__ == '__main__':main()
