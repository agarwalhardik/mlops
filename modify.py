import os

os.system("sed '/^model.add(Dense(units=10,.*/i model.add(Dense(units=128, activation=relu))' /root/mlops_model.py>/root/model.txt")

f=open("/root/model.txt",'r')
filedata=f.read()
f.close()
newdata = filedata.replace('relu)','"relu")')

f=open("/root/model.txt",'w')
f.write(newdata)
f.close()
os.system('mv /root/model.txt /root/mlops_model.py')
