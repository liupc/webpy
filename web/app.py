from __future__ import print_function
import web
import pkgutil
import handlers

urls = (
    '/(.*)', 'default'
)

class Config(dict):
    def __getattr__(self, name):
        return super(Config, self).__dict__[name]

c = Config()
class default:
    def GET(self, name, *args):
        for _, mod, _ in pkgutil.iter_modules(handlers.__path__):
            handler = __import__("%s.%s" % (handlers.__name__, mod))
            cls = getattr(handler, handler.name)
            c[handler.name] = cls
        with open("config.py") as f:
            exec(compile(f.read(), "", "exec"), {'c': c})
        instance = c.name()
        instance.handle(*args)

if __name__ == '__main__':
    app = web.application(urls, golbals())
    app.internalerror = web.debugerror
    app.run()

