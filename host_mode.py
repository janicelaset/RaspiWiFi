import os

project_path = os.path.dirname(os.path.abspath(__file__))

os.system('sudo rm -f /etc/wpa_supplicant/wpa_supplicant.conf')
os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/interfaces.aphost /etc/network/interfaces')
os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/isc-dhcp-server.aphost /etc/default/isc-dhcp-server')
os.system('cd ' + project_path + '/Configuration\ App/ && sudo rails s -b 0.0.0.0 -e production -p 80 -d')
os.system('sudo hostapd /etc/hostapd/hostapd.conf &')
