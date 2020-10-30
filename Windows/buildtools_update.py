###################
#       LOGO      #
###################
print(" .d8888b.           d8b                   888         888     888               888          888                    ")
print("d88P  Y88b          Y8P                   888         888     888               888          888                    ")
print("Y88b.                                     888         888     888               888          888                    ")
print(" \"Y888b.   88888b.  888  .d88b.   .d88b.  888888      888     888 88888b.   .d88888  8888b.  888888 .d88b.  888d888 ")
print("    \"Y88b. 888 \"88b 888 d88P\"88b d88\"\"88b 888         888     888 888 \"88b d88\" 888     \"88b 888   d8P  Y8b 888P\"   ")
print("      \"888 888  888 888 888  888 888  888 888         888     888 888  888 888  888 .d888888 888   88888888 888     ")
print("Y88b  d88P 888 d88P 888 Y88b 888 Y88..88P Y88b.       Y88b. .d88P 888 d88P Y88b 888 888  888 Y88b. Y8b.     888     ")
print(" \"Y8888P\"  88888P\"  888  \"Y88888  \"Y88P\"   \"Y888       \"Y88888P\"  88888P\"   \"Y88888 \"Y888888  \"Y888 \"Y8888  888     ")
print("           888               888                                  888                                               ")
print("           888          Y8b d88P                                  888                                               ")
print("           888           \"Y88P\"                                   888                                               ")
print("888     888                           d8b                         d888        .d8888b.                              ")
print("888     888                           Y8P                        d8888       d88P  Y88b                             ")
print("888     888                                                        888       888    888                             ")
print("Y88b   d88P  .d88b.  888d888 .d8888b  888  .d88b.  88888b.         888       888    888                             ")
print(" Y88b d88P  d8P  Y8b 888P\"   88K      888 d88\"\"88b 888 \"88b        888       888    888                             ")
print("  Y88o88P   88888888 888     \"Y8888b. 888 888  888 888  888        888       888    888                             ")
print("   Y888P    Y8b.     888          X88 888 Y88..88P 888  888        888   d8b Y88b  d88P                             ")
print("    Y8P      \"Y8888  888      88888P' 888  \"Y88P\"  888  888      8888888 Y8P  \"Y8888P\"                              ")

######################
#       Imports      #
######################
import requests
import os
import subprocess
from sys import platform
import sys

###############################
#       Global Variables      #
###############################
slash = ""
currentDirectory = ""
serverDirectory = ""
systemType = ""
##############################
#       Main functions       #
##############################
def systemtypef(): #decides whether to use forwardslash or backslash according to filepath in different operating systems
    global slash
    global systemType
    if platform == "linux" or platform == "linux2":
        systemType = "linux"
        print("OS DETECTED: GNU/LINUX\n\n\n")
        slash = "/"
    elif platform == "win32":
        systemType = "win"
        print("OS DETECTED: WINDOWS\n\n\n")
        slash = chr(92)
    elif platform == "darwin":
        systemType = "osx"
        print("OS DETECTED: OSX\n\n\n")
        slash = "/"

def get_cwd():
    global currentDirectory
    currentDirectory = os.getcwd() #gets the Current Working Directory
    print("This script is located in " + currentDirectory + "\nIt will be used as the install directory!")

def pathconf():
    global currentDirectory
    global serverDirectory

    answer = input("Would you like to change that? (Y/N) ")
    if answer == "Y":
        serverDirectory = input("Input path to the server directory: ")
    elif answer == "N":
        serverDirectory = currentDirectory
    else:
        print("Invalid input!")
        pathconf()

def slashcheck():
    global serverDirectory
    if serverDirectory[-1] != slash:
        serverDirectory = serverDirectory + slash

def download_file():
    url = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"

    print("Downloading BuildTools.jar to " + serverDirectory)
    r = requests.get(url) # create the HTTP response object
    rstr = str(r) #makes it into a string (debug purposes,and feedback for the user)

    if rstr == "<Response [200]>":
        print("Successfully grabbed URL! Downloading!!!")
    else:
        print(rstr)
        print("HTTP Response code abnormal! Aborting!!!\nIF THIS ISSUE PERSISTS github.com/szabi1035/Minecraft-spigot-updater/issues")
        sys.exit(0)

    with open(serverDirectory + "BuildTools.jar",'wb') as f: 
        # Saving received content as a jar file in 
        # binary format 
        # write the contents of the response (r.content) 
        # to a new file in binary mode.
        f.write(r.content)

def run_buildtoolsjar():
    subprocess.call(['java', '-jar', 'BuildTools.jar'])

def rename_serverfile():
    filenames = os.listdir()
    for filename in filenames:
        if "spigot-1." in filename:
            print("Server file found: " + filename + "\nRenaming " + filename + " to server.jar")
            os.rename(serverDirectory + slash + filename, serverDirectory + slash + "server.jar")

def runprompt():
    answer = input("Would you like to run the server now? (Y/N) ")
    if answer == "Y":
        runserver.py
    elif answer == "N":
        sys.exit(0)
    else:
        print("Invalid input!")
        runprompt()

##########################
#       Main execs       #
##########################
systemtypef()
get_cwd()
pathconf()
slashcheck()
download_file()
run_buildtoolsjar()
rename_serverfile()
runprompt()