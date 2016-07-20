try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import simplejson

def all_urls():
    response = urllib2.urlopen("http://localhost:4567/json/allurls")
    data = simplejson.load(response)
    print (data)
    for i in data:
        print(i)

all_urls()