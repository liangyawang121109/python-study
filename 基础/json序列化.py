import pickle
info = {
    "name":"liangyawang",
    "age":22
}
with open('test.txt','wb') as f:
    f.write(pickle.dumps(info))

