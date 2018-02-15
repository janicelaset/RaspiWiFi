import subprocess
import fileinput
import os
import sys

project_path = os.path.dirname(os.path.abspath(__file__))

def install_prereqs():  	
	print("Updating Apt...")
	os.system('apt update')
	print("Installing prerequisites via Apt...")
	os.system('apt install python3 bundler libsqlite3-dev isc-dhcp-server hostapd libxml2-dev libxslt-dev -y')
	print("Installing necessary Ruby Gems. This can take a few minutes...")
	os.system('gem install nokogiri --no-document -v 1.6.6.2 -- --use-system-libraries')
	os.system('bundle install --gemfile=' + project_path + '/Configuration\ App/Gemfile')

print()
print("###################################")
print("##### RaspiWiFi Intial Setup  #####")
print("###################################")
print()
print()
install_prereqs_ans = input("Would you like to install the required files (This can take up to 5 minutes)? (y/n): ")

if(install_prereqs_ans == 'y'):
	print()
	print("Updating system...")
	install_prereqs()
else:
	print()
	print()
	print("===================================================")
	print("---------------------------------------------------")
	print()
	print("No Prerequisites installed. Continuing to configuration file installation...")
	print()
	print("---------------------------------------------------")
	print("===================================================")
	print()
	print()
	
print()
print()
print()
print()
run_setup_ans = input("Would you like to run the initial setup for RaspiWiFi? (y/n): ")

if(run_setup_ans == 'y'):
	print("Updating config files...")
	os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/dhcpd.conf /etc/dhcp/')
	os.system('sudo cp -r ' + project_path + '/Reset\ Device/static_files/hostapd.conf /etc/hostapd/')
	os.system("sed -i -e '$i \python3 '" + project_path + "'/wifi_init.py &\n' /etc/rc.local")
else:
	print()
	print()
	print("===================================================")
	print("---------------------------------------------------")
	print()
	print("RaspiWiFi initial setup cancelled. No changes made.")
	print()
	print("---------------------------------------------------")
	print("===================================================")
	print()
	print()
	sys.exit(0)

print("Initial setup is complete. To enter Wifi Configuration mode, power off the device, set DIP switch x to ON and power the device back on.")
reboot_ans = input("Shut down the device now?  (y/n): ")

if(run_setup_ans == 'y' and reboot_ans == 'y'):
	os.system('sudo shutdown')
