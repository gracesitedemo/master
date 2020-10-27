import unittest
from urllib import request
import requests
import os, json
from pyunitreport import HTMLTestRunner
from utils.utilfunc import EzUtil


class TestRESTDemo(unittest.TestCase):
    def setUp(self):
        self.url = 'https://hooks.slack.com/services/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'
        self.msg = {'text':'Hey, test results result available to review'}
        self.response = None
        self.cityId = 5375478
        self.weatherurl = 'http://api.openweathermap.org/data/2.5/weather?id=%d&appid=%s' % (self.cityId, '07ab78ab428650375abbbede2d452a20')

    def sendInvalidUrlRequest(self):
        invalid_url ='https://hooks.slack.com/services百科/T02CTQY6K/B0161UHKKS4/pGDLljT4ed9wlTJf93PdGim3'
        data = json.dumps(self.msg)
        data = str(data)
        data = data.encode('utf-8')
        req = request.Request(url=invalid_url, data=data)
        response = request.urlopen(req)
        print('response=', str(response))
        return response

    def sendPostRequest(self):
        data = json.dumps(self.msg)
        data = str(data)
        data = data.encode('utf-8')
        req = request.Request(url=self.url, data=data)
        response = request.urlopen(req)
        print('response=', str(response))
        return response

    def sendGetRequest(self, toFile=True):
        resp = requests.request(
            method='GET', url=self.weatherurl)
        print('resp.text=', resp.text)
        if toFile:
            jsonobj = json.loads(resp.text)
            EzUtil.jsonToFile(jsonobj, outfile='output/weather.json')
        return resp

    def xtestInvalidUrl(self):
        response = self.sendInvalidUrlRequest()
        self.response = response
        status_code = self.response.status
        expected = 200
        self.assertEqual(status_code, expected,'Error: status_code expected=200, actual=%s' % status_code)

    def testResponseCode(self):
        response = self.sendPostRequest()
        self.response = response
        actual_status_code = self.response.status
        expected = 200
        self.assertEqual(actual_status_code, 200,
                         'Error: status_code expected=200, actual=%s' % actual_status_code)

    def testResponseHeaders(self):
        response = self.sendPostRequest()
        expected = 'text/html'
        actual = response.headers.get('content-type')
        self.assertEqual(actual, expected,
                         'Error: expected=%s, actual=%s' % (expected, actual))

    def testResponseMsg(self):
        response = self.sendPostRequest()
        expected = 'OK'
        actual = response.msg
        self.assertEqual(actual, expected,
                         'Error: expected=%s, actual=%s' % (expected, actual))

    def testResponseReason(self):
        response = self.sendPostRequest()
        expected = 'OK'
        actual = response.reason
        self.assertEqual(actual, expected,
                         'Error: expected=%s, actual=%s' % (expected, actual))
    def testFailDemo(self):
        actual = 200
        expected = 301
        self.assertEqual(actual, expected,
                         "Test Failed: test not equal: actual=%s, expected=%s" % (actual, expected))

    def testWeatherGet(self):
        response = self.sendGetRequest()
        jsonobj = json.loads(response.text)
        EzUtil.jsonToFile(jsonobj)
        longitude = jsonobj['coord']['lon']
        expected_long, expected_lat = -122.12, 38.01
        actual_latitude = jsonobj['coord']['lat']
        actual_longitude = jsonobj['coord']['lon']
        self.assertTrue(
            expected_long==actual_longitude and expected_lat==actual_latitude,
            'Test Failed: coord is not the same as expected.')

if __name__ == '__main__':
    output_name = './test_result'
    unittest.main(verbosity=1,
                  testRunner=HTMLTestRunner(output=output_name))