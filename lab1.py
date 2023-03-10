def reverse (r):
    str =""
    for a in r:
        str = a + str
        return str 
    
    r = "rania"
    print("The original string is : ", end="")
    print (r)
    
    print("The reversed string After using loops is : ", end="")
print(reverse(r))

#////////////////////////q2////////////////////////

num1 = 2
num2 = 4
sum = num1 + num2
print ('the sum of {0} and {1} is {2}'.format(num1, num2, sum))

#/////////////////////////q3//////////////////////////


def large():
    list= []
    num=int(input('enter number'))
    for i in range(num):
        list.append
        #//////////////////q4/////////////////
        
        age =int (input("your eage: "))
        if (eage >18):
            print("Eligible to Vote")
        else:
            print("Not eligible to vote" )
            
            #////////////////////////q5//////////////////
            def string():
                list=[]
                str =str(input("enter the string: "))
                for i in range (str):
                    list.append
                    #////////////////////q6/////////////
        num =int (input("number: "))
        if (num >0):
            print("positive")
        elif (num <0):
            print ("negative")
        elif (num == 0):
            print ("Zero")
            
            #///////////////////////////q7/////////////////////////
            
            
            vowles = 'aeiou'
            text ="Ryhan"
            def getvowelsnum(string):
            length = len (string)
            countvowels =0
            for i in range(length):
                if string [i] in vowels:
                    countvowels += 1
                    return countvowels
                r = getvowelsnum (text)
                print("number of vowels are", r)
            #/////////////////q8//////////////////////////
            
            def upperstr():
    str=input("Enter a String: ")
    print(str.upper())
    
upperstr()

#///////////////////q9///////////////////

def newlist():
    lst=[]
    lstnew=[]
    n=int(input("enter number of elements in the list: "))
    for i in range(0,n):
        ele=int(input("Enter elements of the list: "))
        lst.append(ele)
    print("old list is :",lst)
    
    for i in lst:
        if (i%2==0):
            lstnew.append(i)
    print("New list is :",lstnew)
    
newlist()

#//////////////////////////////q10////////////////////


def stringSort():
    lst=[]
   
    x=int(input("Enter Number of elements: "))
    for i in range(0,x):
        ele=input("Enter elements of the list: ")
        lst.append(ele)
    print("Old list: ")
    print(lst)
    lst.sort()
    print("Sorted list: ")
    print(lst)
    
stringSort()