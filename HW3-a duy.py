#LIST
#Bài 1:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
set_a=set(a)
set_b=set(b)
print(set_a.intersection(set_b))
#Bài 2:
n=int(input("Nhập một số n:"))
k=int(input("Nhập một số k:"))
list1=list(input("Nhập một list:").split(' '))
case=0
if n==len(list1):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if int(a[i]+a[j]==k) and i<j:
                return True, i, j
return False, -1, -1
print(int(a[i]), "and" , int(a[j]))
print("Số trường hợp", case)


#MATH
#Bài 1:
so_du=0
while True:
    a=input("Nhập số tiền muốn giao dịch:")
    b=a.split(" ")
    if not a:
        break
    if b[0]=="D":
        so_du+=int(b[1])
    elif b[0]=="W":
        so_du-= int(b[1])
print(so_du)
#Bài 2:
def f(n):
    if n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    return f(n-1)+f(n-2)


#DICTIONARY
#Bài 1:
n=int(input("Nhập một số nguyên:"))
print({i: i *i for i in range (1, n+1)})
#Bài 2:
print({i: i *i for i in range (1, 11)})
#Bài 3+4:
dict = {1:'a', 5:'h', 3:'x', 2:'l'}
=sorted(dict.item(), reverse=True)
print(a)
b=sorted(dict.keys())
c=sorted(dict, reverse=True)
print(b)
print(c)
#Bài 5:
T=int(input("Nhập số lần thử:"))
list1=[ ]
while T!=0:
    password=str(input("Nhập mật khẩu:"))
    list1.append(password)
    if list1.count(password)==1:
        print("OKE")
    else:
        list1.append(password+str((list1.count(password)-1)))
        print(password+str((list1.count(password)-1)))
    T-=1


#SET
#Bài 1:
height=[161,182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]
no_student=len(height)
print("Số học sinh trong lớp:",no_student)
c=0
for i in height:
    c+=i
print("Chiều cao trung bình của lớp:",c//no_student)
diff_height=set(height)
no_height=len(diff_height)
d=0
for i in diff_height:
    d+=i
print("Giá trị trung bình của chiều cao:",d//no_height)
#Bài 3:
A=[1, 'a', 5, 7, 'f', 0, 89, 'g', 'I', 11, 88, 3, 'p']


#TUPLE
#Bài 1:
tuple1=(1,2,3,4,5,6,7,8,9,10)
saved_tuple=[ ]
for i in tuple1:
    if i%2==0:
        saved_tuple.append(i)
print(tuple(saved_tuple))
Bài 2:
    n=int(input("Nhập một số n:"))
list1=[ ]
list2=[ ]
for i in range (1, (n//2)+1):
    list1.append(i)
print(list1)
for i in range((n//2)+1, n+1):
    list2.append(i)
    list2.sort(reverse=True)
print(list2)


#Problem1:
K=int(input("Nhập số lượt xe đỗ:"))
i=1
while i<=K:
    license_plate=int(input("Nhập biển số xe"))
    i+=1
list1=[ ]
list1.append(license_plate)

monthly_profit=0
for i in list1:
    if list1.count(i)<=5:
        fee=100//(list1.count(i))
    elif list1.count(i)>5:
        fee=(100//(list1.count(i))+((list1.count(i)-5)/list.count(i))
    monthly_profit+=fee
print("Phí thu được trong tháng này", int(monthly_profit))  

    
    
      


