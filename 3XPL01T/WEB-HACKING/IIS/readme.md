
Syarif

RECON WORKFLOW

Trade name/Organization name > ASN ((AS7182, AS...) ) >  CIDR (17.84.0.0/16) > IP/Subdomain (17.84.76.128, test.apple.com) > Port (17.84.76.128:3000)    
domain > subdomain > IP > Port > endpoint > https://17.84.76.128:3000/admin/dashboard.aspx 
TRADE NAME >> Organisasi (O)	AT&T Services, Inc.

ASN ENUMERATION
https://whois.ipip.net/search/ATT
ASN Number : AS797 
ASN Name : blablabla



CIDR
https://bgp.he.net/AS797#_prefixes
ASN Number
Trade name
CIDR


SHODAN
ssl:”Trade Name”
ssl:”Organization Name”
ssl.cert.subject.CN:”target.com”
asn:AS9999
http.favicon.hash:-1274734426


CENSYS
<img width="1142" height="716" alt="image" src="https://github.com/user-attachments/assets/ac21ceba-66a2-4b0e-9ff4-7467e7b5834d" />
<img width="705" height="184" alt="image" src="https://github.com/user-attachments/assets/0b4c6ebd-d66b-4fd9-99f3-433f222c93a4" />
<img width="873" height="578" alt="image" src="https://github.com/user-attachments/assets/516c7421-7c26-4dbc-9bd3-b8df1b054a3b" />

FOCUS TO UNCOMMON PORT
3000,5000,5010,5001,8081,9000,567,
10000,7000,8089,4455, etc..



$ ffuf -w fuzz.txt -u https://IP:5010/FUZZ -c -v -recursion


IIS ENUMERATION
product:"Microsoft IIS httpd" (shodan)
https://github.com/bitquark/shortscan
https://github.com/orwagodfather/WordList/blob/main/iis.txt
$ shortscan url


$ ffuf -w iis.txt -u https://site.com/gpsgatFUZZ
$ ffuf -w iis.txt -u https://site.com/gpsgat_FUZZ
$ ffuf -w iis.txt -u https://site.com/gpsgat.FUZZ
$ ffuf -w iis.txt -u https://site.com/gpsgat-FUZZ
$ ffuf -w iis.txt -u https://site.com/gpsgat%20FUZZ
https://github.com/bitquark/shortscan
https://github.com/orwagodfather/WordList/
blob/main/iis.txt
$ ffuf -w iis.txt -u https://site.com/gps.gatFUZZ


DEFAULT CREDENTIALS OR RESPONSE MANIPULATION
admin:admin
test:test
username:password
root:root
user:pwd
subdomain.att.com:subdomain.att.com


SOURCE CODE ANALYSIS
.dll, .exe, .dac, .dat, .jnlp, .jar, extract
using decompiler.com

URL: https://IP/
Running: Microsoft-IIS/10.0 (ASP.NET v4.0.30319)
Vulnerable: Yes!
══════════════════════════════════════
webadmin~1.DLL webadmin.DLL?





https://otx.alienvault.com/api/v1/indicators/domain/target.com/url_list?limit=100&page=1
https://web.archive.org/cdx/search/cdx?url=*.target.com/*&output=text&fl=original&collapse=urlkey
https://urlscan.io/api/v1/search/?q=domain:target.com&size=10000


ONELINER FOR COLLECTING ENDPOINT
$ curl -sk "https://urlscan.io/api/v1/search/?q=domain:att.com&size=10000" | grep '"url"' | sort -u | sed -n 's/.*"url": "\(.*\)".*/\1/p'
$ curl -sk "https://otx.alienvault.com/api/v1/indicators/domain/target.com/url_list?limit=100&page=1" | jq | grep '"url"' | sort -u | sed -n 's/.*"url": "\(.*\)".*/\1/p'










