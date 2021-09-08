import requests
import re
import os

url = input("\n Enter Web Address : ")
req = requests.get(url).content.decode("utf-8")

extention = input(" Enter File Extention : ")
data = re.findall(rf'<a[ ]href="(https?://.+.{extention}.+)">.+</a>', req)

name = (f"Links [.{extention}].txt")
f = open(name, "w+")

for element in data:
	f.write(url + element + "\n")

f.close()

print(f" Links Saved to  : ( {os.getcwd()}\\" + name + " )")
