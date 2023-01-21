WSL2 exposes ports on the local interface (which is why in Windows you can access localhost:8080 when your 8080 service is running in WSL2), but they listen on 127.0.0.1 (which is why you can't access yourhostname:8080 on other computers your LAN).

There's a tool to fix this called WSLHostPatcher, which you can find here (download via the Releases section): https://github.com/CzBiX/WSLHostPatcher

WSLHostPatcher changes the behaviour to listen on all IPs, exposing any WSL2 services to all computers on your network.

Download the latest release from https://github.com/CzBiX/WSLHostPatcher/releases (I tested v0.1.0)
Unzip the file
Run the WSLHostPatcher.exe
(Re)start your service in WSL2
The service should now be accessible via other computers on your network.



sudo service mosquitto start


rosrun mosquitto_python_client subscriber.py

or

roslaunch mosquitto_python_client subscriber.launch

