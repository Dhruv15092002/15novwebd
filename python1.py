#Q 1st
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6 == 6)
a=20
a+=30
a%3
print(a)
print(True*False)
print(True&False)
print(True and False)
print((6>3)and(7<4)or(18==3)and(9>3))
print(True is False)
#print(False in 'False')
#thsi gives error
#but print(False is 'False')
#this doesnt
print(((True==False)or(False>True))and(False<=True))



#Q 3
s1='Nice to have it'
s2='here'
print(s1+' '+s2)

#Q 4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#Q 5
a.insert(0,s1)
a.insert(8,s2)
print(a)

#Q 6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
for  i in numbers:
    if(i==237):
        break
    elif(i%2==0):
        print(i)
    else:
        pass

# Q 7
cl1 = {'White', 'Black', 'Red' }
cl2 = {'Red', 'Green'}
last=cl1.intersection(cl2)
last=cl1-last
print(last)

# Q 8
string = input("Enter the string")
string = set(string)
alpha = list('abcdefghijklmnopqrstuvwxyz')
i=0
for word in string:
    if(word in alpha):
        i+=1
if(i==26):
    print('String is Pangram')
else:
    print('String is not Pangram')


# Q 9
n=int(input())
n=n+(10*n+n)+(100*n+10*n+n)
print(n)

# Q 10

string1=eval(input("Enter string in the given fashion"))     # "23 54 12#98 3 17"
string1=string1.strip()
string1+=" "
num=""
x=[]
y=[]
flag=0
for i in string1:
    if(i!=" "):
        if(i!="#"):
            num+=i
        else:
            flag=1
            x.append(int(num))
            num=""
    
    else:
        if(flag==0):
            x.append(int(num))
            num=""
        else:
            y.append(int(num))
            num=""
print(x)
print(y)


#Q 11


string2=(input("enter the words"))
string2=string2.strip()
string2+=","
word=""
l=[]
for i in string2:
    if(i!=","):
        word+=i
    else:
        l.append(word)
        word=""
l.sort()
print(l)

# Q 12
    
d={'Student' : ['Rahul','Kishore','Vidhya','Raakhi'],'Marks' : [57,87,67,79]}
maximum=0
idx=-1
for i in d['Marks']:
    idx+=1
    if(maximum<i):
        maximum=i
        pos=idx
print(d['Student'][pos])

#Q 13

string3=(input("enter the sentence"))
letters=0
digits=0
for i in string3:
    if(i.isalpha()):
        letters+=1
    if(i.isdigit()):
        digits+=1
print("LETTERS",letters)
print("DIGITS",digits)

# Q 14


d={'Name':['Akash','Soniya','Vishakha','Akshay','Rahul','Vikas'],
   'Subject':['Python','Java','Python','C','Python','Java'],
   'Ratings':[8.4,7.8,8,9,8.2,5.6]}
inp=input("enter subject name")
idx=-1
pos=[]
for i in d['Subject']:
    idx+=1
    if(inp==i):
        pos.append(idx)
newData={'Name':[],'Subject':[],'Ratings':[]}
for i in pos:
    newData['Name'].append(d['Name'][i])
    newData['Subject'].append(d['Subject'][i])
    newData['Ratings'].append(d['Ratings'][i])
    
print(newData)

#Q 16


x=0
y=0
while(True):
    string4=(input("enter the instructions"))
    if (string4 == ""):
        break
    else:
        string4=string4.split(' ')
        if string4[0]=="UP":
            y+=int(string4[1])
        elif string4[0]=="DOWN":
            y-=int(string4[1])
        elif string4[0]=="RIGHT":
            x+=int(string4[1])
        elif string4[0]=="LEFT":
            x-=int(string4[1])
dist=(((x**2)+(y**2))**(1/2))
print('DISTANCE:',int(dist))












