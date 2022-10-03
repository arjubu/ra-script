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
    file = open('user_credentials.txt', 'a+')
    ssh_group = "task1-ssh-group"
    ftp_group = "task1-ftp-group"
    ftp_com_drc = "/home/ftp-docs"
    subprocess.run(['sudo', 'addgroup', ssh_group])
    subprocess.run(['sudo', 'addgroup', ftp_group])
    # subprocess.run(['mkdir', ftp_com_drc])
    # subprocess.run(['chmod', '750', ftp_com_drc])
    # subprocess.run(['chown', 'root:task1-ftp-group', ftp_com_drc])
    for i in range(1001, 1005):
        username = "user" + str(i)
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        subprocess.run(['sudo', 'adduser', username, '--gecos "First Last,RoomNumber,WorkPhone,HomePhone"', '--disabled-password'])
        userpass = "".join(username + ":" + password)
        subprocess.run(['echo', userpass, '| sudo', password])
        if i % 2 == 0:
            subprocess.run(['sudo adduser', username, ftp_group])
            # subprocess.run(['useradd', '-p', password, '-d', ftp_com_drc, username])
            # with open("/etc/vsftpd/user_list", "a") as f:
            # f.write(username + "\n")
        else:
            subprocess.run(['sudo adduser', username, ssh_group])
            #subprocess.run(['useradd', '-p', password, '-g', ssh_group, username])
            # with open("/etc/ssh/sshd_config", "a") as f:
            # f.write("AllowUsers " + username + "\n")
        if is_prime(i):
            # subprocess.run(['useradd', '-p', password, username])
            subprocess.run(['sudo usermod', '-L', username])
        file.write(username + "  " + password + "\n")
        print("user" + str(i) + " Created............")
    file.close()
    # subprocess.run(['chmod', '740', ftp_com_drc + "/*"])
    # subprocess.run(['chown', 'root:task1-ftp-group', ftp_com_drc + "/*"])
    subprocess.run(['systemctl restart vsftpd'])
    subprocess.run(['systemctl restart sshd'])


add_user()
