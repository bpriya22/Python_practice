#task ->1
# a=[1,2,3,[1,2,3]]
# b=a
# print(a,b)
# print(id(a),id(b))
# b.append(10)
# print(a)
# print(b)

#conclusion to the above task=>a is assigned to b-> whichmeans both a and b refers to the same object in the memory.
#so any modifications made to list through 'b' will be reflected on 'a'.
#the value gets changed because lists are 'mutable'.

#task->2

a=1
b=a
print(a,b)
b+=1
print(a,b)

#conclusion=> a value remains same because 'integers' are 'immutable' the cannot be change.
#if they were 'lists', 'a' value will be changed.
