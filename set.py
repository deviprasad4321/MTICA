sample_set={"Yellow","orange","Black"}
sample_list=["Blue","Green","Red"]
sample_set.update(sample_list)
print(sample_set)

s1={10,20,30,4,50,60,70}
s2={1,2,3,4,5,6,7,8,9}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1^s2)
print(s1.difference(s2))
s1.difference_update({10,20,30,40,50,60,70})
print(s1)
a={10,20,30,40,50}
a.difference_update({10,20,30,35})
print(a)




