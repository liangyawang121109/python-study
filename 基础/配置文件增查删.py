action = [
    "update",
    "select",
    "delete",
    "added"
]
print(action)
need = input("请输入您的需求")
with open("conf","r",encoding="utf-8") as f,\
    open("test","a+",encoding="utf-8") as f1:
    if need == "select":
        for line in f:
            print(line)
