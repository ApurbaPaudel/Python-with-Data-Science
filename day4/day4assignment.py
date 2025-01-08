#1 Create a set with the following elements:10,20,30,40,50
a={10,20,30,40,50}
print(a)

#2 Add the element 60 to the set
a.add(60)
print(a)

#3 Remove the element 20 from the set
a.remove(20)
print(a)

#4 Check of the element 30 is in the set
b={30}
c=b.issubset(a)
print(c) #True

#5 Find the length of the set.
print(len(a))

#6 Create two sets and perform following operations
a={1,2,3,4}
b={3,4,5,6}
#union
union=a.union(b)
print(union)

#intersection
inter=a.intersection(b)
print(inter)

#difference
diff1=a.difference(b)
print(diff1)
diff2=b.difference(a)
print(diff2)

#symmetric_difference
diff=a.symmetric_difference(b)
print(diff)

#subset
sub=a.issubset(b)
print(sub) #False
sub1=b.issubset(a)
print(sub1) #False

#superset
super=a.issuperset(b)
print(super) #False
super1=b.issuperset(a)
print(super1) #False

#disjoint
dis=a.isdisjoint(b)
print(dis) #False

#7 Given the set my_set={1,2,3} add the number 4 to the set
my_set={1,2,3}
my_set.add(4)
print(my_set)

#8 Given the set my_set={1,2,3,4} remove the number 2 from the set
my_set={1,2,3,4}
my_set.remove(2)
print(my_set)

#9 Given two set1={1,2,3} and set2={3,4,5} find union
set1={1,2,3}
set2={3,4,5}
set=set1.union(set2)
print(set)

#10 Given two sets find the intersection
set1={1,2,3}
set2={2,3,4}
set=set1.intersection(set2)
print(set)

#11 Find maximum and minimum value in a set
set={1,2,3,4}
b=max(set)
print(b)
c=min(set)
print(c)


