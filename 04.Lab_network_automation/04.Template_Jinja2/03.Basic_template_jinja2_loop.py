from jinja2 import Environment, FileSystemLoader
loader = FileSystemLoader("templates")

environment = Environment(loader=loader)

# define var in template
allowed = [
 "10.10.0.10",
 "10.10.0.11",
 "10.10.0.12"
]

disallowed = [
 "10.10.0.50",
 "10.10.0.62"
]
intf = "ethernet0"

tpl = environment.get_template("loop_template.tpl")

out = tpl.render(allowed=allowed, disallowed=disallowed, intf=intf)
print(out)

# generate to config file
tpl.stream(allowed=allowed, disallowed=disallowed, intf=intf).dump("loop_rendered.conf")
