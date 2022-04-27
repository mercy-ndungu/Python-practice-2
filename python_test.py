x = [100,110,120,130,140,150]
mynewlist=[n*5 for n in x]
print(mynewlist)
def divisible_by_three(n):
    for g in range(1,n):
        if (g%3==0):
            print(g)
            divisible_by_three(90)
nested_list= [[1,2],[3,4],[5,6]]
flatlist=nested_list[0]+nested_list[1]+nested_list[2]
print(flatlist)
smallest=[3,6,8,2,4,1,5,7]
small=min(smallest)
print(small)
p= ['a','b','a','e','d','b','c','e','f','g','h']
my_set=list(set(p))
print(my_set)
divisible_by_seven=[]
for num in range(100,200):
    if (num% 7==0):
        divisible_by_seven.append(num)
print((divisible_by_seven))
students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
for my_students in students
