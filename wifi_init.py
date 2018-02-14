import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if GPIO.input(4) == 0:
	os.system('rm -f ./tmp/*')
	# os.system('sudo cp -r ./Reset\ Device/static_files/dhcpd.conf /etc/dhcp/')
	# os.system('sudo cp -r ./Reset\ Device/static_files/hostapd.conf /etc/hostapd/')
	os.system('sudo cp -r ./Reset\ Device/static_files/interfaces.apclient /etc/network/interfaces')
	os.system('sudo cp -r ./Reset\ Device/static_files/isc-dhcp-server.apclient /etc/default/isc-dhcp-server')
	# os.system('sudo cp -r ./Reset\ Device/static_files/rc.local.aphost /etc/rc.local')
else:
  os.system('sudo rm -f /etc/wpa_supplicant/wpa_supplicant.conf')
	os.system('rm -f ./tmp/*')
	# os.system('sudo cp -r ./Reset\ Device/static_files/dhcpd.conf /etc/dhcp/')
	# os.system('sudo cp -r ./Reset\ Device/static_files/hostapd.conf /etc/hostapd/')
	os.system('sudo cp -r ./Reset\ Device/static_files/interfaces.aphost /etc/network/interfaces')
	os.system('sudo cp -r ./Reset\ Device/static_files/isc-dhcp-server.aphost /etc/default/isc-dhcp-server')
	os.system('cd Configuration\ App/ && sudo rails s -b 0.0.0.0 -e production -p 80 -d')
	os.system('hostapd -dd /etc/hostapd/hostapd.conf')
  
# su -c "cd [[project_dir]]/Configuration\ App/ && rails s -b 0.0.0.0 -e production -p 80 -d"

# hostapd -dd /etc/hostapd/hostapd.conf &