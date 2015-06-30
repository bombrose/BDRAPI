# -*- coding: utf-8 -*-
'''
Python 百度即用api sdk(http://apistore.baidu.com/apiworks/readyapiprefecture.html).
'''
__version__ = '0.1.0'
__author__ = 'czc(chenzhch@gmail.com)'

import urllib, urllib2, os, json

class BDRAError(StandardError):
    pass

class BDRAClient(object):
    _API_URL = 'http://apis.baidu.com/apistore/'

    def __init__(self, apikey='811ec1b9a080c8d7659725633c96629a', timeout=15):
        self._API_KEY = apikey
        self._TIMEOUT = timeout

    @staticmethod
    def _format_path(path):
        _path = urllib.pathname2url(os.path.join(path))
        _path = _path.strip("/")
        if _path.startswith("apistore/"):
            return _path[9:]
        return _path

    @staticmethod
    def _parse_data(data):
        if data:
            try:
                result = json.loads(data)
            except ValueError:
                return data
            if result.has_key('errNum'):
                errNum = result['errNum']
                if errNum and int(errNum) != 0:
                    raise BDRAError(errNum, result.get('errMsg'))
                if result.has_key("retData"):
                    return result["retData"]
            return result
        raise ValueError

    def _call(self, req):
        req.add_header("apikey", self._API_KEY)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36")
        resp = urllib2.urlopen(req, timeout=self._TIMEOUT)
        assert resp.code == 200, resp.msg
        return self._parse_data(resp.read())

    def _get_url(self, uri):
        if urllib.splittype(uri)[0]:
            return uri
        return "{0}{1}".format(self._API_URL, self._format_path(uri))

    def get(self, uri, **kwargs):
        params = urllib.urlencode(kwargs)
        url = "{0}?{1}".format(self._get_url(uri), params)
        req = urllib2.Request(url)
        return self._call(req)

    def post(self, uri, **kwargs):
        params = urllib.urlencode({k: str(v).replace("\n", '') for k, v in kwargs.iteritems()})
        url = self._get_url(uri)
        req = urllib2.Request(url, data=params)
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        return self._call(req)
