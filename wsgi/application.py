#!/usr/bin/env python
import os
try:
    from libs.dbfunc import *
except ImportError:
    from ..libs.dbfunc import *

    
from wsgi.routing import router



def application(environ, start_response):
    
    return router(environ, start_response)


# Below for testing only
#
if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	httpd = make_server('localhost', 8051, application)
	# Wait for a single request, serve it and quit.
	httpd.handle_request()
