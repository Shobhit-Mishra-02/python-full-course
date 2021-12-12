# break
# for i in range(10):
#     print(i)

# for shop in range(1, 11):
#     print("shop no.", shop)
#     if shop == 5:
#         break

# shop = 1
# while shop <= 10:
#     print("shop no.", shop)
#     if shop == 7:
#         break
#     shop += 1

# continue
# for shop in range(1, 11):
#     if (shop == 5) or (shop == 7):
#         continue
#     print('shop no.', shop)
shop = 1
while shop <= 10:
    if shop == 5:
        shop += 1
        continue
    print('shop no.', shop)
    shop += 1
