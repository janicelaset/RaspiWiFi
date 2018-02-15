RaspiWiFiConfig

RaspiWiFiConfig is a program to headlessly configure a Raspberry Pi's WiFi 
connection using using any other WiFi-enabled device. RaspiWiFiConfig has been 
tested with the Raspberry Pi 3.



INSTALLATION INSTRUCTIONS:

1. Navigate to the directory you downloaded or cloned RaspiWiFi to

2. Run `sudo python3 initial_setup.py`

   *This script will install all necessary prerequisites, update configuration files, and shut down. To enter Wifi Configuration mode, power off the device, set DIP switch x to ON and power the device back on. The device will operate in standard mode if DIP switch x is OFF.*


USAGE:

1. Connect to the "RaspiWiFi Setup" access point using any other WiFi enabled device.

2. Navigate to http://10.0.0.1 using any web browser on the device you connected with.

3. Select the WiFi connection you'd like your Raspberry Pi to connect to from the drop down list and enter its wireless password on the page provided. If no encryption is enabled, leave the password box blank.

4. Click the "Save" button.
