
user,passwd = "abc","abc123"

def login(func):
    def hommer(*args, **kwargs):
        username = input("username:")
        password = input("password")
        if username == user and password == passwd:
            func(*args, **kwargs)
            print("装饰器执行完毕")
        else:
            exit("invalid your input user or passwd")
    return hommer


@login
def home():
    print("welcome to home page")

@login
def home1():
    print("welcome to home1 page ")

home()
