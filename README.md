# Minecraft-spigot-updater
 
 A Spigot server updater Python script
 
## Requirements

On **Windows**:  
	https://www.python.org/downloads/  
	https://www.java.com/de/download/manual.jsp

```shell
pip install requests
```
On **Linux**:
```bash
sudo apt install python3
sudo apt install default-jre
pip3 install requests
```
## Usage
On **Windows**:
copy the contents of the *Windows* subfolder to the place where you want your server/where your server is  
double click the **update.bat** and follow any prompts given  
when it's done,double click **run-spigot-server.bat** and follow any prompts given.  
***Your server should be starting up. If not, https://github.com/szabi1035/Minecraft-spigot-updater/issues***  

On **Linux**:
copy the contents of the *Linux* subfolder to the place where you want your server/where your server is  
**First** You have to make the scripts executable by cd'ing to the directory and opening a terminal then typing:
```bash
chmod +x update.sh
chmod +x run-spigot-server-.sh
```
*Then*
```bash
./update.sh
./run-spigot-server.sh
```
Alternatively,when you're installing your server you can change the install directory in the script. If you have done that,then copy **run-spigot-server.sh** to the directory.  
  
***COPY LINE BY LINE***  
***Your server should be starting up. If not, https://github.com/szabi1035/Minecraft-spigot-updater/issues***


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
