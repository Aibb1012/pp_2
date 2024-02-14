# date4
# Write a Python program to calculate two date difference in seconds.
import datetime
# day_now = datetime.datetime.now()
day_1 = datetime.datetime(2020 , 5 , 17 , 16 , 30 , 56)
day_2 = datetime.datetime(2022 , 12 , 14 , 10 , 42 , 12)
# print((day_now - day_1).total_seconds())
print((day_2 - day_1).total_seconds())