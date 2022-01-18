###list
friends = ["ankit", "ashish", "kartik"]
print(friends[1])
print(len(friends))

friends = [["ankit",10], ["ashish",12], ["kartik",15],]
print(friends[1][1])
print(len(friends[1]))

###append in list
friends = ["ankit", "ashish", "kartik"]
friends.append("vipin")
print(friends)
friends.remove("ankit")
print(friends)

##### Tuples
tuple_data = ("ank", "aed")
print(tuple_data)
tuple_data = [("ank", "aed")]
print(tuple_data)

### Sets- 1. No order and no duplicate
art_friends = {"ankit", "vipin"}
print(art_friends)
art_friends.add("Jen")
print(art_friends)
art_friends.remove("Jen")
print(art_friends)
art_friends.add("Jen")
print(art_friends)


### Comparision we use sets
science_fr = {"vipin", "akash", "shyam"}

not_in_science = art_friends.difference(science_fr)
print(not_in_science)
not_in_both = art_friends.symmetric_difference(science_fr)
print(not_in_both)
art_and_science = art_friends.union(science_fr)
print(art_and_science)




