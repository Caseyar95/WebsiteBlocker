import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True: #infinite loop
    #if between 8am-4pm
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content: #if blocking is already there
                    pass
                else:
                    file.write(redirect + "   " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content: #copies host file line for line except where there's a website from list
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun")

    time.sleep(60)
