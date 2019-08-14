import threading,time

event = threading.Event()


def lighter():
    count = 0
    event.set()
    while True:
        if count > 5 and count < 10:
            event.clear() #变成红灯
            print('红灯停')
        elif count > 10:
            event.set() #变成绿灯
            print('绿灯行')
            count = 0
        else:
            print('绿灯行')
        time.sleep(1)
        count += 1



def car(name):
    while True:
        if event.is_set():
            print('%s is running ...'%name)
            time.sleep(1)
        else:
            print('%s is stop wait'%name)
            event.wait()


light = threading.Thread(target=lighter(),)
light.start()

car1 = threading.Thread(target=car,args=('tesla',))
car1.start()