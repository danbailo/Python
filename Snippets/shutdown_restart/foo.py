import os

platform = os.uname()

def restart():
    if platform.sysname == "Windows":
        os.system("shutdown /r /t 0")
    else:
        os.system("reboot")

def shutdown():
    if platform.sysname == "Windows":
        os.system("shutdown /r /t 1")
    else:
        os.system("shutdown now")

if __name__ == "__main__":
    while True:
        try:  
            option = str(input("shutdown or reboot? (ctrl+c or ctrl+d to exit)\n")).lower()
            if option == "shutdown" : shutdown()
            if option == "reboot" : restart()
        except KeyboardInterrupt:
            break
        except EOFError:
            break
