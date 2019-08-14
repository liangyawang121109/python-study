data = {}
try:
    data['name']
except (KeyError,IndexError) as e: #指定单个错误或者多个错误抓取
    print('meiyoukey',e)
except Exception as e: #抓取所有类型的错误 被用于错误抓取的最后面 用于抓取未知错误
    print('未知错误',e)
else:
    print('一切正常') #当没有任何错误的时候执行这一步

finally:
    print('不管有没有错都执行')
    #缩进错误和语法错误是没有办法呗抓取的

raise #触发异常

assert #断言 判断 如果什么什么 然后就什么  如果判断错误就报错

