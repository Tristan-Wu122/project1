first_Str = input().split(",")
range_and_price_Str = input()

range_number = int(first_Str[0])   #級距個數
minimum_kilogram = int(first_Str[1])  #肉品需求量

range_and_price = range_and_price_Str.split(",")
for j in range(range_number * 2):
    range_and_price[j] = int(range_and_price[j])

money_payable = 0
t1 = 0
for a in range(range_number):
    range = int(range_and_price[a])      #級距
    price = range_and_price[a + range_number]   #級距對應價格

    if minimum_kilogram >= range:   #當需求肉品大於級距時要加的需付金額如下
        money_payable += (range - t1) * price
    else:    #當需求肉品小於級距時
        if minimum_kilogram - t1 >= 0:  #當需求肉品剛小於級距時，需付金額計算方式如下
            money_payable += (minimum_kilogram - t1) * price
        else:      #若上一個級距已超出需求肉品，則不納入計算
            money_payable = money_payable
    t1 = range     #將t1改為舊一輪的級距

print(money_payable)
print("no money")
print("many money")


