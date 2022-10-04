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
    # subprocess.run(['sudo', 'addgroup', ssh_group])
    # subprocess.run(['sudo', 'addgroup', ftp_group])

    for i in range(0, 1001):
        username = "user" + str(i)
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        adduserstr = 'sudo adduser ' + username + ' --gecos ' + '"' + "First Last,RoomNumber,WorkPhone,HomePhone" + '"' + " --disabled-password "
        print(adduserstr)
        output, error = subprocess.Popen(adduserstr, universal_newlines=True, shell=True,
                                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        userpass = "echo " + '"' + username + ':' + password + '" | sudo chpasswd'
        print(output)
        subprocess.Popen(userpass, universal_newlines=True, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        if i % 2 == 0:
            adduserftpstr = "sudo adduser " + username + " " + ftp_group

            output, error = subprocess.Popen(adduserftpstr, universal_newlines=True, shell=True,
                                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
            print(output)

        else:
            addusrsshstr = "sudo adduser " + username + " " + ssh_group

            output, error = subprocess.Popen(addusrsshstr, universal_newlines=True, shell=True,
                                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
            print(output)

        if is_prime(i):
            lockusrstr = "sudo usermod -L " + username
            output, error = subprocess.Popen(lockusrstr, universal_newlines=True, shell=True,
                                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
            print(output)

        file.write(username + "  " + password + "\n")
        print("user" + str(i) + " Created............")
    file.close()
    subprocess.run(['systemctl restart sshd'])


add_user()
