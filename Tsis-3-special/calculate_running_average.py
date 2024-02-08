# calculate_running_average
size = int(input("How many numbers? "))
a = []
total = 0
for i in range(size):
    x = float(input())
    a.append(x)
    total+=x
x = size
avg_list = []
while(x!=0):
    avg = total/x
    avg_list.append(avg)
    total = total-a[x-1]
    x = x-1
print("Running average is" , avg_list)