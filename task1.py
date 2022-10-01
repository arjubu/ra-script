import subprocess
import random
import string
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def add_user():
    for i in range(5, 1001):
        username = "task1-usr" + str(i)
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        subprocess.run(['useradd', '-p', password, username])
        if i % 2 == 0:
            with open("/etc/vsftpd/user_list", "a") as f:
                f.write(username + "\n")
        else:
            with open("/etc/ssh/ssh_config", "a") as f:
                f.write("AllowUsers " + username + "\n")
        if is_prime(i):
            subprocess.run(['chage', '-E0', username])
        file = open('user_credentials.txt', 'a+')
        file.write(username+"  "+password)
        file.close()
    subprocess.run(['systemctl restart vsftpd'])
    subprocess.run(['systemctl restart sshd'])


add_user()
