user = "abc"
passwd = "abc123"

def login(auth_type):
    """
    添加认证类型的判断
    """
    def out_hommer(func):
        """
        定义一个装饰器
        """
        def hommer(*args, **kwargs):
            """
            装饰器内部功能 整个函数体
            """
            if auth_type == "local":
                username = input("username:")
                password = input("password")
                if username == user and password == passwd:
                    func(*args, **kwargs)
                    print("装饰器执行完毕")
                else:
                    exit("invalid your input user or passwd")
            elif auth_type == "ldap":
                exit("ldap功能暂未上线 敬请期待。。。")
        return hommer
    return out_hommer
@login(auth_type="local")
def home():
    print("welcome to home page")

@login(auth_type="ldap")
def home1():
    print("welcome to home1 page ")

home()
home1()
