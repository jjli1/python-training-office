# 有序可變動列表 List
grades=[12,60,15,70,90]
print(grades)
print(grades[0])
grades[0]=55
print(grades)
grades[1:4]=[]
print(grades)
grades=grades+[12,33]
grades[0]=[[12,33]]
print(grades)
length=len(grades)
print(length)

data=[[3,4,5],[6,7,8]]
data[0][0:2]=[5,5,5]
print(data[0])

# 有序不可變動列表 Tuple