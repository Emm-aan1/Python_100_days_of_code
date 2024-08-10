user_num = int(input("Enter a number from 0 and 1000: "))

even_num = 0
for num in range(2, (user_num + 1), 2):
    even_num += num
    # print(even_num)

print("The total even number is ", even_num)