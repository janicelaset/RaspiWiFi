import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

project_path = os.path.dirname(os.path.abspath(__file__))

if GPIO.input(4) == 0:
  if os.path.exists("/etc/wpa_supplicant/wpa_supplicant.conf") == 0:
    os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/wpa_supplicant.conf /etc/wpa_supplicant/')
  
  os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/interfaces.apclient /etc/network/interfaces')
  os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/isc-dhcp-server.apclient /etc/default/isc-dhcp-server')
else:
  os.system('sudo rm -f /etc/wpa_supplicant/wpa_supplicant.conf')
  os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/interfaces.aphost /etc/network/interfaces')
  os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/isc-dhcp-server.aphost /etc/default/isc-dhcp-server')
  os.system('cd ' + project_path + '/Configuration\ App/ && sudo rails s -b 0.0.0.0 -e production -p 80 -d')
  os.system('sudo hostapd /etc/hostapd/hostapd.conf &')
