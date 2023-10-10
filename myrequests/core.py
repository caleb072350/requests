# -*- coding: utf-8 -*-

"""
    requests.core

    This module implements the main Requests system.
"""
import urllib
import urllib.request
import urllib2

__title__ = 'requests'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'caleb'
__license__ = ''
__copyright__ = 'Copyright ...'

AUTOAUTHS = []


class Request(object):
    """The :class: `Request` object. It's awesome.
    """

    _METHODS = ('get', 'head', 'put', 'post', 'delete')

    def __init__(self):
        self.url = None
        self.headers = dict()
        self.method = None
        self.params = {}
        self.data = {}
        self.reponse = Response()
        self.auth = None
        self.sent = False

    def __setattr__(self, name, value):
        if (name == 'method') and (value):
            if not value.lower() in self._METHODS:
                raise InvalidMethods()
        
        object.__setattr__(self, name, value)

    def _checks(self):
        pass
    
    def send(self, anyway=False):
        """Sends the requests.

            :param anyway: If True, request will be sent, even if it has already been sent.
        """
        self._checks()
        if self.method.lower() == 'get':
            if (not self.sent) or anyway:
                try:
                    r = urllib.request.urlopen('http://www.baidu.com')
                    self.response.headers = r.headers.dict
                    self.response.status_code = r.code
                    self.response.content = r.read()

                    success = True
                
                except Exception:
                    raise RequestException

        elif self.method.lower() == 'head':
            if (not self.sent) or anyway:
                try:
                    pass 
                    success = True
                except Exception:
                    raise RequestException
        elif self.method.lower() == 'put':
            if (not self.sent) or anyway:
                try:
                    pass
                    success = True
                except:
                    raise RequestException
        elif self.method.lower() == 'post':
            if (not self.sent) or anyway:
                try:
                    req = 
                    success = True
                except Exception:
                    raise RequestException
        elif self.method.lower() == 'delete':
            if (not self.sent) or anyway:
                try:
                    pass
                    success = True
                except Exception:
                    raise RequestException
        else:
            raise InvalidMethod
        
        self.sent = True if success else False

        return success

class Response(object):
    """The :class:`Request` object. It's awesome.
    """

    def __init__(self):
        self.content = None
        self.status_code = None
        self.headers = dict()

class AuthObject(object):
    """The :class: `AuthObject` is a simple HTTP Authentication token.

    :param username: Username to authenticate with.
    :param password: Password for given username.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
def get(url, params={}, headers={}, auth=None):
    """Sends a GET requests. Returns :class:`Response` object.
    """
    r = Request()

    r.method = 'GET'
    r.url = url 
    r.headers = headers
    r.auth = _detect_auth(url, auth)
    r.send()

    return r.response

def head(url, params={}, headers={}, auth=None):
    """Sends a HEAD request. Returns :class:`Response` object
    """
    r = Request()
    r.method = 'HEAD'
    r.url = url
    r.headers = headers
    r.auth = _detect_auth(url, auth)
    r.send()

    return r.response

def post(url, params={}, headers={}, auth=None):
    """Sends a POST request. Returns :class:`Response` object
    """
    r = Request()
    r.method = 'POST'
    r.url = url
    r.headers = headers
    r.auth = _detect_auth(url, auth)

    r.send()

    return r.response

def put(url, data='', headers={}, auth=None):
    """Sends a PUT requests. Returns :class:`Response` object
    """
    r = Request()

    r.url = url
    r.method = 'PUT'
    r.headers = headers
    r.auth = _detect_auth(url, auth)
    r.send()

    return r.response()

def delete(url, params={}, headers={}, auth=None):
    """Sends a DELETE request. Returns :class:`Response` object
    """
    r = Request()

    r.url = url
    r.method = 'DELETE'
    r.headers = headers
    r.auth = _detect_auth(url, auth)

    r.send()

    return r.response()

def add_autoauth(url, authobject):
    global AUTHOAUTHS

    AUTHOAUTHS.append((url, authobject))

def _detect_auth(url, auth):
    return _get_autoauth(url) if not auth else auth

def _get_autoauth(url):
    for (authauth_url, auth) in AUTHOAUTHS:
        if authauth_url in url:
            return auth
    return None


class InvalidMethod(Exception):
    """An innappropriate method was attemped."""

class AuthenticationError(RequestException):
    """The authentication credentials provided were invalid."""

class URLRequired(RequestException):
    """A valid URL is required to make a request."""

class InvalidMethod(RequestException):
    """An inappropriate method was attempted."""

