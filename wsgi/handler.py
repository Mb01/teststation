


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
