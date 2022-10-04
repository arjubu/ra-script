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
    # subprocess.run(['mkdir', ftp_com_drc])
    # subprocess.run(['chmod', '750', ftp_com_drc])
    # subprocess.run(['chown', 'root:task1-ftp-group', ftp_com_drc])
    for i in range(1009, 10012):
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
            # subprocess.run(['sudo adduser', username, ftp_group])
            # subprocess.run(['useradd', '-p', password, '-d', ftp_com_drc, username])
            # with open("/etc/vsftpd/user_list", "a") as f:
            # f.write(username + "\n")
        else:
            addusrsshstr = "sudo adduser " + username + " " + ssh_group

            output, error = subprocess.Popen(addusrsshstr, universal_newlines=True, shell=True,
                                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
            print(output)
            # subprocess.run(['useradd', '-p', password, '-g', ssh_group, username])
            # with open("/etc/ssh/sshd_config", "a") as f:
            # f.write("AllowUsers " + username + "\n")
        if is_prime(i):
            # subprocess.run(['useradd', '-p', password, username])
            lockusrstr = "sudo usermod -L " + username
            output, error = subprocess.Popen(lockusrstr, universal_newlines=True, shell=True,
                                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
            print(output)
            # subprocess.run(['sudo usermod', '-L', username])
        file.write(username + "  " + password + "\n")
        print("user" + str(i) + " Created............")
    file.close()
    # subprocess.run(['chmod', '740', ftp_com_drc + "/*"])
    # subprocess.run(['chown', 'root:task1-ftp-group', ftp_com_drc + "/*"])
    # subprocess.run(['systemctl restart vsftpd'])
    subprocess.run(['systemctl restart ssh'])


add_user()
