#there are 4 types of argument
#1. default argument
#2. keyword argument
#3. required argument
#4 variable-length argument

#default argument
def name(fname,mname="jack",lname="johnson"):
    print("hello",fname,mname,lname)

# name("Amy")

#keyword argument

def friends(fname,lname,mname):
    print("hello bro",fname,mname,lname)

# friends(lname="shree",mname="Khot",fname="krish")

#3. required arguments

def three_idiots(one_id,two_id,three_id):
    print("the three masketiers;",one_id,two_id,three_id)

# three_idiots("nithya","priya","Priya")

#VARIABLE LENGTH AGUMENTS
#sometimes we need to pass more arguments than the that they are already defined

#two types
#1.Arbitary argumnet

def tree(*guys):
    print("hey",guys[1],guys[0],guys[2])
# tree("richi","dolu","khot")

#2. Keyword Arbitary argument





