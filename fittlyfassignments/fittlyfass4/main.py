listA=[1,2,3,4]
tup_A=(1,2,3,4)
print("The list is ",listA)
print("The tuple is",tup_A)

try:
    listA[2]=5
    print("List is  not immutable")
except:
    print("List is immutable")

try:
    tup_A[2]=5
    print("Tuples are not immutable beacause once declared we cannot change the values or modify thr contents of it")
except:
    print("Tuples are immutable")


# tup_A[2]=5
