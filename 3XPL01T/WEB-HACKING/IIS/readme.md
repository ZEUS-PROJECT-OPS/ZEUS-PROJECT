
Syarif

RECON WORKFLOW

Trade name/Organization name > ASN ((AS7182, AS...) ) >  CIDR (17.84.0.0/16) > IP/Subdomain (17.84.76.128, test.apple.com) > Port (17.84.76.128:3000)    
domain > subdomain > IP > Port > endpoint > https://17.84.76.128:3000/admin/dashboard.aspx 
TRADE NAME >> Organisasi (O)	AT&T Services, Inc.

ASN ENUMERATION <br> 
https://whois.ipip.net/search/ATT <br>
ASN Number : AS797  <br>
ASN Name : blablabla <br>



CIDR <br>
https://bgp.he.net/AS797#_prefixes <br>
ASN Number <br>
Trade name <br> 
CIDR <br>


SHODAN <br>
ssl:”Trade Name” <br>
ssl:”Organization Name” <br> 
ssl.cert.subject.CN:”target.com” <br> 
asn:AS9999 <br> 
http.favicon.hash:-1274734426 <br>


CENSYS
<img width="1142" height="716" alt="image" src="https://github.com/user-attachments/assets/ac21ceba-66a2-4b0e-9ff4-7467e7b5834d" />
<img width="705" height="184" alt="image" src="https://github.com/user-attachments/assets/0b4c6ebd-d66b-4fd9-99f3-433f222c93a4" />
<img width="873" height="578" alt="image" src="https://github.com/user-attachments/assets/516c7421-7c26-4dbc-9bd3-b8df1b054a3b" />

FOCUS TO UNCOMMON PORT
3000,5000,5010,5001,8081,9000,567,
10000,7000,8089,4455, etc..



$ ffuf -w fuzz.txt -u https://IP:5010/FUZZ -c -v -recursion


IIS ENUMERATION
product:"Microsoft IIS httpd" (shodan) <br>
https://github.com/bitquark/shortscan <br>
https://github.com/orwagodfather/WordList/blob/main/iis.txt <br>
$ shortscan url <br>
<img width="1050" height="301" alt="image" src="https://github.com/user-attachments/assets/43967c06-2a64-423f-961c-49f1c98000a3" /> <br>
<img width="821" height="463" alt="image" src="https://github.com/user-attachments/assets/a9e1f079-1a25-4cd3-a199-2c2c99d8e2ed" /> <br>


$ ffuf -w iis.txt -u https://site.com/gpsgatFUZZ <br>
$ ffuf -w iis.txt -u https://site.com/gpsgat_FUZZ <br> 
$ ffuf -w iis.txt -u https://site.com/gpsgat.FUZZ <br>
$ ffuf -w iis.txt -u https://site.com/gpsgat-FUZZ <br>
$ ffuf -w iis.txt -u https://site.com/gpsgat%20FUZZ <br>
https://github.com/bitquark/shortscan <br> 
https://github.com/orwagodfather/WordList/blob/main/iis.txt <br>
$ ffuf -w iis.txt -u https://site.com/gps.gatFUZZ <br>


DEFAULT CREDENTIALS OR RESPONSE MANIPULATION <br>
admin:admin
test:test
username:password
root:root
user:pwd
subdomain.att.com:subdomain.att.com


SOURCE CODE ANALYSIS <br>
.dll, .exe, .dac, .dat, .jnlp, .jar, extract
using decompiler.com

URL: https://IP/ <br>
Running: Microsoft-IIS/10.0 (ASP.NET v4.0.30319)
Vulnerable: Yes!
══════════════════════════════════════
webadmin~1.DLL webadmin.DLL?





https://otx.alienvault.com/api/v1/indicators/domain/target.com/url_list?limit=100&page=1 <br>
https://web.archive.org/cdx/search/cdx?url=*.target.com/*&output=text&fl=original&collapse=urlkey <br>
https://urlscan.io/api/v1/search/?q=domain:target.com&size=10000 <br>


ONELINER FOR COLLECTING ENDPOINT <br>
$ curl -sk "https://urlscan.io/api/v1/search/?q=domain:att.com&size=10000" | grep '"url"' | sort -u | sed -n 's/.*"url": "\(.*\)".*/\1/p' <br>
$ curl -sk "https://otx.alienvault.com/api/v1/indicators/domain/target.com/url_list?limit=100&page=1" | jq | grep '"url"' | sort -u | sed -n 's/.*"url": "\(.*\)".*/\1/p'










