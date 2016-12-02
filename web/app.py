from __future__ import print_function
import sys
import web
import pkgutil
import handlers

urls = (
    '/', 'error',
    '/(Jdk7Installer)', 'default'
)

class Config(dict):
  def __getattr__(self, name):
    return super(Config, self).__getitem__(name)

c = Config()

class error:
  def GET(self):
    raise web.notfound("no such command")

class default:
  def GET(self, name):
    instance = getattr(c, name)()
    user_data = web.input(host=[])
    return instance.handle(*user_data.host)

# walk through handlers and register it
for _, mod, _ in pkgutil.iter_modules(handlers.__path__):
  handlers = __import__("%s.%s" % (handlers.__name__, mod))
  handler  = getattr(handlers, mod)
  cls = getattr(handler, handler.name)
  c[handler.name] = cls

# register cls from urls
def group2(iter):
  e1 = next(iter)
  e2 = next(iter)
  yield (e1, e2)

for url, cls_name in group2(iter(urls)):
  cls = getattr(sys.modules[__name__], cls_name)
  c[cls] = cls()

with open("config.py") as f:
  exec(compile(f.read(), "", "exec"), {'c': c})


if __name__ == '__main__':
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()

