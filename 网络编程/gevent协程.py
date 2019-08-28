import gevent

#gevent 是一个第三方库 可以通过gevent轻松的实现并发同步或异步编程
def foo():
    print('foo home page')
    gevent.sleep(2)
    print('foo page exten done ')

def bar():
    print('bar home page')
    gevent.sleep(2)
    print('bar page exten done')

gevent.joinall(  #遇到io即切换
    [gevent.spawn(foo),
    gevent.spawn(bar),
    ]
)