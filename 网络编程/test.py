import os

print(os.path.exists('haha3'))
with open('haha','rb') as f:
    with open('ha1','wb') as f2:
        print(os.stat('haha').st_size)