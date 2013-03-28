#!/usr/bin/env python
import os
from libs.dbfunc import *
from wsgi.routing import router



def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return routing(environ, start_response)


# Below for testing only
#
if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	httpd = make_server('localhost', 8051, application)
	# Wait for a single request, serve it and quit.
	httpd.handle_request()
