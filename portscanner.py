import socket
import termcolor

banner ='''
 #####    ####   #####   #####    #####
 #    #  #    #  #    #  #    #     #
 #    #  #    #  #    #  #    #     #
 #####   #    #  #####   #####      #
 #       #    #  #   #   #   #      #
 #        ####   #    #  #    #     #
'''

print(banner)
def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass
        # print("[-] Port Closed " + str(port))


targets = input("[*] Enter Targget To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    for ipaddress in targets.split(','):
        scan(ipaddress.strip(' '), ports)

else:
    scan(targets, ports)