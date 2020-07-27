#-*- coding = utf-8 -*-
#@Time: 27-Jul-20 6:10 PM
#@File:  p9.py
#@Software: PyCharm

products = [["iphone",6888], ["MacPro",14800],["小米6", 2499], ["Coffee",31],["Book",60],["Nike",666]]

# print("-"*6, end= "\t")
# print("商品列表", end = "\t")
# print("-"*6)
#
# for i in range(len(products)):
#     print("%d\t%s\t%d"%(i,products[i][0],products[i][1]))
my_list = []
while True:
    id = input("请选择一个商品编号(退出请输入q):")
    if id == "q":
        print(my_list)
        print("-"*6, end= "\t")
        print("商品列表", end = "\t")
        print("-"*6)
        for i in range(len(my_list)):
            print("%d\t%s\t%d" % (i, my_list[i][0],my_list[i][1]))
        break
    my_list.append(products[int(id)])
    print(my_list)





