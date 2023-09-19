import uuid
import time
import random, string

localtime = time.asctime(time.localtime(time.time()))

def pass_word(arg1):
    myrg = random.SystemRandom()
    length = 15
    alphabet = string.ascii_letters + string.digits # a-z A-Z 0-9
    password = "".join(myrg.choice(alphabet) for _ in range(length))

appname = input("What is the name of the account/application is this password for? " + "\n")

file = open("/media/veracrypt1/totally_not_my_passwords.txt","a+")
file.write("--------------------------------------------\n")
file.write("PASSWORD GENERATED ON " + localtime +"\n")
file.write("PASSWORD IS FOR: "+appname+"\n")
file.write(pass_word()+"\n")
file.write("--------------------------------------------\n")
file.close()