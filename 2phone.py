#!usr/bin/env python

# 2 - Change of Phone Number
# Implement a script to update the phone number embedded in many of the store’s HTML pages.
# Over the years, the content authors have embedded the number on pages using a wide variety
# 	of punctuation (i.e., 800 438-4357 or 800.438.4357) while others used letter mnemonics (e.g., 800-GET-HELP).
# Some inserted the US country code, with or without surrounding parentheses.
# The store has >50K HTML files, all under an NFS /var/www mount point shared by all servers.
# Your job is to replace all the old number with one version of the new number: 202-456- 1414.
# The job needs to be done tonight, while the web servers are running.
# You do NOT have to convert the new number to the existing format used on the page.
# Bonus points for a solution that is implemented as a single pipeline of Linux commands.

import csv
import re
import pprint
import argparse
import ipaddress
from collections import OrderedDict

# NFS Python Library example:
# https://pypi.org/project/libnfs/
#
import libnfs

nfs = libnfs.NFS('nfs://127.0.0.1/var/www')
a = nfs.open('/test.html', mode='w+')
a.write('Test string')
a.close()

# print(nfs.open('/foo-test', mode='r').read())








# parser = argparse.ArgumentParser(
# 	description="Determine if IPv4 address is in the given CIDR subnet")
# parser.add_argument('-i', dest='ipAddress',
# 	help='IP address ex: -i 0xc0a80101')
# parser.add_argument('-c', dest='cidrSubnet',
# 	help='CIDR Subnet ex: -c 192.168.1.0/24')
# parser.add_argument('-s', dest='srcCSV',
# 	help='Source CSV ex: -s ~/Desktop/fileName.csv')
# parser.add_argument('-d', dest='dstCSV',
# 	help='Destination CSV ex: -d ~/Desktop/fileName.csv')

# # parser.add_argument('-t', dest='TIME', nargs=2, help='Populate lead creation start & end time filter.')
# # # ex: lead_bulk_export.py -t start_time end_time
# args = parser.parse_args()

# def convertIP(ip):
# 	# ipString = re.compile('.*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

# 	# try:
# 	# 	isIp = ipString.match(ip)
# 	# 	if isIp:
# 	# 		print(isIp.group(0))
# 	# 	else:
# 	# 		print(ip, 'is not a string IP address')

# 	# except:
# 	# 	print('not a normal IP.')

# 	# # process string IP address
# 	# try:
# 	# 	ip = ipaddress.ip_address(ip)
	
# 	# # process hexidecimal
# 	# else ValueError:
# 	ip = int(ip, 16) % 2**32
# 	ip = ipaddress.ip_address(ip)

# 	# 	# process string hexidecimal
# 	# 	ip = 
# 	# 	# ip = 'c0.a8.78.01'
	
# 	return ip

# def checkSubnet(subnet, ip):
# 	subnet = ipaddress.ip_network(subnet, strict=False)
# 	for address in subnet.hosts():
# 		if ip == address:
# 			return True

# 	return False

# def processCSV(inputFile):
# 	with open(inputFile, encoding="utf-8-sig") as csvFile:
# 		csvData = csv.reader(csvFile)
# 		inputFile = OrderedDict()
# 		cnt = 0

# 		for row in csvData:
# 			ip = convertIP(row[0])
# 			sub = row[1]
# 			isIn = checkSubnet(sub, ip)
# 			inputFile[cnt] = [ip, sub, isIn]
# 			cnt += 1

# 	return inputFile

# def processOut(outputFile, inputFile):
# 	CSV = open(outputFile, 'w')
# 	with CSV:
# 		csvData = csv.writer(CSV)

# 		for row in inputFile.values():
# 			csvData.writerow(row)

# 	return outputFile

# def main():
# 	# if args.ipAddress and args.cidrSubnet:
# 	# 	ip = convertIP(''.join(args.ipAddress))
# 	# 	subnet = ''.join(args.cidrSubnet)
# 	# 	isIn = checkSubnet(subnet, ip)
# 	# 	if isIn:
# 	# 		print('{} is in the same subnet as {}'.format(ip, subnet))
# 	# 	else:
# 	# 		print('{} is not in the same subnet as {}'.format(ip, subnet))

# 	# elif args.srcCSV and args.dstCSV:
# 	# 	inputFile = processCSV(''.join(args.srcCSV))
# 	# 	outputFile = processOut(''.join(args.dstCSV), inputFile)

# 	# else:
# 	# 	print('Specify arguments correctly.  If you need help, run this:'	\
# 	# 		'\n    python3 1subnet.py -h')

# 	print('test')

# if __name__ == "__main__":
# 	main()
