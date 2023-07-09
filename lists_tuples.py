#Lists
#mutables and immutables
#mylistOne=[1,2,"priya",3,"priyanka"]
#mylistTwo=[1,2,"Rahul",44,"Randy"]
#print(mylistOne*2) #creates duplicates inside the list . having the same items
#print(mylistOne+mylistTwo)#concatinates both the strings
#mylistOne[1]="john"  #Since they are mutable(Lists)
#print(mylistOne)


#Tuples- Read only list-cannot modify

myTuple1=(1,23,"priya","thanks")
myTuple2=(1,233,"shriya","Hello")
# print(myTuple2*2)
# print(myTuple2 + myTuple1)
myTuple2[1]="Rahul"  #TODO: Not valid      #throws error cause tuple are immutable
print(myTuple2)




