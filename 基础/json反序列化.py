import pickle
with open('test.txt','rb') as f:
    data = pickle.loads(f.read())
   
print(data["age"])