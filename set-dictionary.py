# 集合的運算
# s1={3,4,5}
# print(3 in s1)

s1 = {3,4,5}
s2 = {4,5,6,7}
# s3 = s1 & s2
# s3 = s1 | s2
# s3 = s1 - s2
# s3 = s1 ^ s2
# print(s3)

s = set("Hello")
print(s)

# 字典的運算 key-value 配對
dic = {"apple":"蘋果","banana":"香蕉"}
dic["apple"]="小蘋果"
print(dic["apple"])
print("apple" in dic)
print(dic)
del dic["apple"]
print(dic)

dic={x:x*2 for x in [3,4,5]}
print(dic)