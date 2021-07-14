from datetime import datetime
name=input("enter your name:")

age=int(input("enter your age"))

prediction=int((100-age)+datetime.now().year)

print("hello %s you are %s years old and you will be 100 in %s"%(name,age,prediction))