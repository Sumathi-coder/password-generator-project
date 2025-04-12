import random
import string
length= int(input("enter the length of the password: "));
lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
num=string.digits
symbols=string.punctuation
all=lowercase+uppercase+num+symbols
temp=random.sample(all,length)
password="".join(temp)
print(password)