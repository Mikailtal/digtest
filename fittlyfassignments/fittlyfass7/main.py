class Errorforindex(Exception):
    "The index 10 is incorrect and index should lie between -5 and 4."
    pass
class Errorforvalue(Exception):
    "Use an Integer value as the input."
    pass


list_a = [1, 2, 3, 4, 5]

try:
    x=input("Enter the index")
    if not x.isnumeric():
        raise Errorforvalue
    elif int(x)>4 or int(x)<0:
        raise Errorforindex
except Errorforindex:
    print("The index 10 is incorrect and index should lie between 0 and 4")
except Errorforvalue:
    print("Use an Integer value as the input.")