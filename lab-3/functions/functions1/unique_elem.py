# unique_elem
a = [1 , 2, 1 , 3 , 3 ,4 ,5]
def unique_elem(a):
    unique_el = []
    for i in a:
        if i not in unique_el:
            unique_el.append(i)
    for x in unique_el:
        print(x , end=" ")
unique_elem(a)
