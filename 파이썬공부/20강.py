- 인덱스로 제거
1. del 연산자
2. pop()함수
- 값으로 제거
1. remove() 함수
#del 연산자
a = [1,2,3,4,5,6,7]
del a[1]
a= [1,3,4,5,6,7]
del a[0:3]
a= [5,6,7]
# pop 함수
a= [1,2,3,4,5,6,7]
a.pop(1)
=2
a=[1,3,4,5,6,7]
a.pop() #pop 함수는 매개변수 지정안하면 자동으로 -1이들어감
=7
a=[1,3,4,5,6]
#remove 함수
a = [100,200,300,400,500]
a.remove(100)
a = [200,300,400,500]
a=[1,1,1,1,1]
a.remove(1) #이경우에는 제일앞에있는 1만제거함
a=[1,1,1,1] #remove함수는 오직 한개의 요소만 제거할수있음
#clear 함수
a=[1,2,3,4,5]
a.clear[] 
a=[] 
