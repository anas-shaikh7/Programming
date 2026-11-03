l = [4, 3, 532, 900, 1000]
     # these no.s become the items upon calling the function
#index = 0
#for item in l:
#    print(f"The item at the index no {index} is {item}")
#    index +=1 


# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item at the index no {index} is {item}")
