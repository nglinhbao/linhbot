import urllib, urllib2
import json

api_key, userip = None, None
query = {'q' : 'search google python api'}
referrer = "https://stackoverflow.com/q/3900610"

if userip:
    query.update(userip=userip)
if api_key:
    query.update(key=api_key)

url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % (
    urllib.urlencode(query))

request = urllib2.Request(url, headers=dict(Referer=referrer))
json = json.load(urllib2.urlopen(request))

results = json['responseData']['results']
for r in results:
  print (r['title'] + ": " + r['url'])


