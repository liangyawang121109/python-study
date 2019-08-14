data = {
    '北京':{
        "昌平":{
            "沙河":["oldtest"],
            "天通苑":["链家地产"]
        },
        "朝阳":{
            "望京":["奔驰"],
            "国贸":["ccie"],
            "东直门":["飞信"]
        },
        "海淀":{}
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    }
}

exit_flag = False
while not exit_flag:
    for i in data:
        print(i)
    choice = input("进入第一层选项")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print(i2)
            choice2 = input("进入第二层选项")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print(i3)
                    choice3 = input("进入第三层")
                    if choice3 in data[choice][choice2]:
                        while not exit_flag:
                            for i4 in data[choice][choice2][choice3]:
                                print(i4)
                            choice4 = input("进入最后一层 按b返回")
                            if choice4 == "b":
                                break
                            elif choice4 == "q":
                                exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
