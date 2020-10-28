import requests
import os
from sys import platform
slash = ""
def decideslash(): #decides whether to use forwardslash or backslash according to filepath in different operating systems
    global slash
    if platform == "linux" or platform == "linux2":
        slash = "/"
    elif platform == "win32":
        slash = chr(92)
    elif platform == "darwin":
        slash = "/"
decideslash()

def create_pathfile():
    file_open = open("pathtoserverfolder.txt", "w") #creates the pathtoserverfolder.txt file
    file_open.close()
create_pathfile()


path_to_server = "" #had to declare in global scope
path_to_file = os.getcwd() #gets the Current Working Directory
file_size = os.path.getsize(path_to_file + slash +"pathtoserverfolder.txt") #gets the size of the pathtoserverfolder.txt file that is next to this python file

def pathcheck():
    global path_to_server

    if file_size > 0:
        file_open = open("pathtoserverfolder.txt", "r")
        path_to_server = file_open.read()
        file_open.close()

    else:
        file_open = open("pathtoserverfolder.txt", "w")
        path_to_server = input("Input your Minecraft Server folder directory: ")

    def pathlastcharcheck(): #checks what the last character of the directory string is,and if it's a backslash (doesnt do anything) and if its not a backslash then it puts one at the end
        file_open = open("pathtoserverfolder.txt", "r+")
        lastchar = path_to_server[-1]
        if lastchar == slash:
            file_open.write(path_to_server) #always the first line in the file if it hasn't been tempered with by the user
            file_open.close()
        else:
            file_open.write(path_to_server + slash)  #always the first line in the file if it hasn't been tempered with by the user
            file_open.close()
    pathlastcharcheck()

pathcheck()

def download_file():
    url = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
    file_open = open("pathtoserverfolder.txt", "r") #opens the file to be able to read path to server
    path_to_server = file_open.readlines()[0] # reads the first line (index pos 0) which contains the path to the server directory

    print(path_to_server)
    r = requests.get(url) # create the HTTP response object
    rstr = str(r) #makes it into a string (debug purposes,and feedback for the user)

    if rstr == "<Response [200]>":
        print("Successfully grabbed URL! Downloading!!!")
    else:
        print("Something is wrong with the URL!")
    with open(path_to_server + "BuildTools.jar",'wb') as f: 
  
        # Saving received content as a jar file in 
        # binary format 
        # write the contents of the response (r.content) 
        # to a new file in binary mode.
        f.write(r.content)
    
    file_open.close()
download_file()