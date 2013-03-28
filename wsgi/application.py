#!/usr/bin/env python
import os
from libs.dbfunc import *


import jinja2

jinja_environment = jinja2.Environment(autoescape=True,
        loader=jinja2.FileSystemLoader(
        	os.path.join( os.path.dirname(__file__), 'templates') )
			)
class Handler(object):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
	def render_str(self, template, **params):
		t = jinja_environment.get_template(template)
		return t.render(params)
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))
	

def application(environ, start_response):
	ctype = 'text/plain'
	if environ['PATH_INFO'] == '/health':
		response_body = "1"
	elif environ['PATH_INFO'] == '/env':
		response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
		response_body = '\n'.join(response_body)
	else:
		ctype = 'text/html'
		response_body = '''
		<!doctype html>
		<html>
		<head>
		<title>This is a title</title>
		<body>
		<h1>This is a heading</h1>
		<p>This works</p>
		</body>
		</html>
		'''

	status = '200 OK'
	response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
	#
	start_response(status, response_headers)
	return [response_body]

#
# Below for testing only
#
if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	httpd = make_server('localhost', 8051, application)
	# Wait for a single request, serve it and quit.
	httpd.handle_request()
