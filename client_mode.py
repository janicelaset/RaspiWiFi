import os

project_path = os.path.dirname(os.path.abspath(__file__))
wpa_file = Path("/etc/wpa_supplicant/wpa_supplicant.conf")

if wpa_file.is_file() == 0:
  os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/wpa_supplicant.conf /etc/wpa_supplicant/')

os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/interfaces.apclient /etc/network/interfaces')
os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/isc-dhcp-server.apclient /etc/default/isc-dhcp-server')
