commid=[("iphone",3000),
        ("bikd",1000),
        ("watch",500)
        ]
short_cart=[]
maney=input("请输入您的金额：") 
if maney.isdigit():
        maney = int(maney)
        while True:
                for index,item in enumerate(commid):
                        print(index,item)
                user_chioce = input("请输入商品序列号：")
                if user_chioce.isdigit():
                        user_chioce = int(user_chioce)
                        if user_chioce < len(commid) and user_chioce >= 0:
                                p_item = commid[user_chioce]
                                if p_item[1]  <=  maney:
                                        short_cart.append(p_item)
                                        maney -= p_item[1]
                                        print("已经将%s加入您的购物车，您的余额为%s"%(p_item,maney))
                                else:
                                        print("您的余额不足")
                        else:
                                print("您输入的商品不存在")
                elif user_chioce == "q":
                        print("--------------shopp list-----------")
                        for p in short_cart:
                                print(p)
                        print("您的余额为", maney)
                        exit()
else:
        print("您的输入有误")
        exit()