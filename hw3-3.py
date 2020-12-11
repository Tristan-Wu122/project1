first_Str = input().split(",")
range_and_price_Str = input().split(",")

range_number = int(first_Str[0])   #級距個數
minimum_kilogram = int(first_Str[1])  #肉品需求量

#用迴圈把需求數量到最終級距之間的每個正整數就因回圈計算價格
best_number = 0
best_cost = 10000000000
for i in range(minimum_kilogram, int(range_and_price_Str[range_number - 1]) + 1): #用迴圈計算每個購買數量跑出來的對應價格
    bought_kilogram = i
    money_payable = 0
    last_interval = 0

    for x in range(range_number):
        interval = int(range_and_price_Str[x])
        price = int(range_and_price_Str[x + range_number])

        if bought_kilogram >= interval:
            money_payable += (interval - last_interval) * price
        else:
            if bought_kilogram - last_interval >= 0:
                money_payable += (bought_kilogram - last_interval) * price
            else:
                money_payable = money_payable
        last_interval = interval

    if money_payable <= best_cost:     #若新的價格小於就的價格，則將價格及數量更改為新的價格及數量
        best_cost = money_payable
        best_number = bought_kilogram

print(str(best_number)+","+str(best_cost))
