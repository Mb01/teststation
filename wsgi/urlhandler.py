import os


import jinja2
jinja_environment = jinja2.Environment(autoescape=True,
        loader=jinja2.FileSystemLoader(
            os.path.join( os.path.dirname(__file__), 'templates') )
            )

class Handler(object):
    ctype = 'text/plain'
    
    def __init__(self, environ):
        self.environ = environ
        
        
    def render_str(self, template, **params):
        t = jinja_environment.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        return self.render_str(template, **kw)
    