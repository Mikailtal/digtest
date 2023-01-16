list_a = ["car", "place", "tree", "under", "grass", "price"]

letter="a"
final_list = list(filter(lambda x:letter not in x,list_a))
print(final_list)