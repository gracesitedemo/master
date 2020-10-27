from urllib import request
import json
import datetime
dt_now = datetime.datetime.now()
web_hook_url = 'https://hooks.slack.com/services/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'
msg = {
    'text':'Hey, test results result available %s' % dt_now,
}
data=json.dumps(msg)
data= str(data)
data = data.encode('utf-8')
req = request.Request(url=web_hook_url, data=data )
res = request.urlopen(req)
print(res.status)
