class invalidName(Exception):
    pass


number=18

try:
    int_num=int(input("enter a number:"))
    if int_num <number:
        raise invalidName
    else:
        print("elegible to vote..")
except invalidName:
    print("exception occured invalid age..")



