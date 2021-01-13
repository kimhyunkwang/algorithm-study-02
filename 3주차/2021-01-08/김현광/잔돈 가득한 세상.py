# 방법 1
price = int(input())
change = 10000 - price

thousand_count = change // 1000
hundred_count = change % 1000  // 100
ten_count = change % 1000 % 100 // 10
one_count = change % 1000 % 100 % 10

answer = thousand_count + hundred_count + ten_count + one_count
print(answer)


# 방법 2
price = int(input())
change = 10000 - price
str_change = str(change)
answer = int(str_change[0]) + int(str_change[1]) + int(str_change[2]) + int(str_change[3])
print(answer)