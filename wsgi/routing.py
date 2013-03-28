from wsgi.handler import Handler



def router(environ, start_response):
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
    start_response(status, response_headers)
    
