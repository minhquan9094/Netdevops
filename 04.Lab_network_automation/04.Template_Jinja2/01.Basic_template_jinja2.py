from jinja2 import Environment, FileSystemLoader
loader = FileSystemLoader("templates")

environment = Environment(loader=loader)

tpl = environment.get_template("first.conf.tpl")

out = tpl.render(name="quan")
print(out)

# generate to config file
tpl.stream(name="quan").dump("rendered.conf")
