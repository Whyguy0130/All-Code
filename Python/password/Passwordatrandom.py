import random as rand
import time
import pyautogui as gui
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=<>,.;:[{]}|?"
allchar = list(chars)
pwd = gui.password("\/ Enter Your Password \/")
sample_pwd = ""
start = time.time()
while (sample_pwd != pwd):
    sample_pwd = rand.choices(allchar, k=len(pwd))
    print("<====", str(sample_pwd), "====>")
    if (sample_pwd == list(pwd)):
        end = time.time()
        elapsed = end - start
        elapsed = int(elapsed)
        file1 = open(r"C:\Users\KittellWyL\Desktop\Confidential_Items\Confidential_File.txt","w")
                            #   ^^^^^^^^^^Your Username Here
        file1.write("Your Password Was Cracked At: \n")
        file1.write(time.strftime("%I:%M:%S %p on ")),file1.write(time.strftime("%m/%d/%Y \n"))
        file1.write("It took: "),file1.write(str(elapsed)),file1.write(" seconds\n")
        file1.write("The Password is: "),file1.write("".join(sample_pwd)),file1.write("\n")
        file1.write("==================\n")
        file1.close()
        a = input("Want to crack another? (Y/N) ")
        if a == 'Y':
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=<>,.;:[{]}|?"
            allchar = list(chars)
            pwd = gui.password("\/ Enter Your Password \/")
            sample_pwd = ""
            start = time.time()
            while (sample_pwd != pwd):
                sample_pwd = rand.choices(allchar, k=len(pwd))
                print("<====", str(sample_pwd), "====>")
                if (sample_pwd == list(pwd)):
                    end = time.time()
                    elapsed = end - start
                    elapsed = int(elapsed)
                    file1 = open(r"C:\Users\KittellWyL\Desktop\Confidential_Items\Confidential_File.txt","w")
                                        #   ^^^^^^^^^^Your Username Here
                    file1.write("Your Password Was Cracked At: \n")
                    file1.write(time.strftime("%I:%M:%S %p on ")),file1.write(time.strftime("%m/%d/%Y \n"))
                    file1.write("It took: "),file1.write(str(elapsed)),file1.write(" seconds\n")
                    file1.write("The Password is: "),file1.write("".join(sample_pwd)),file1.write("\n")
                    file1.write("==================\n")
                    file1.close()
                    break
        elif a == 'N':
            break