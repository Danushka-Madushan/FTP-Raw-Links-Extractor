import requests
import re
import os

url = input("\n Enter (IP/Directory) Address : ")
req = requests.get(url).content.decode("utf-8")

extention = input(" Enter File Extention : ")
data = re.findall(rf'<li><a[ ]href="(.+.{extention})">.+</a></li>', req)

name = (f"Links [.{extention}].txt")
f = open(name, "w+")

for element in data:
	f.write(url + element + "\n")

f.close()

print(f" Links Saved to  : ( {os.getcwd()}\\" + name + " )")
