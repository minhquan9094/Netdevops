from jinja2 import Environment, FileSystemLoader
loader = FileSystemLoader("templates")

environment = Environment(loader=loader)

# define var in template
ports = []
port_1 = {
 "type": "ethernet",
 "slot": 1,
 "port_num": 1,
 "intf_type": "access"
}
ports.append(port_1)


port_2 = {
 "type": "ethernet",
 "slot": 1,
 "port_num": 2,
 "intf_type": "trunk"
}
ports.append(port_2)



tpl = environment.get_template("if_template.tpl")

out = tpl.render(ports=ports)
print(out)

# generate to config file
tpl.stream(ports=ports).dump("if_rendered.conf")
