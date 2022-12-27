from nornir import InitNornir
from nornir_scrapli.tasks import send_command,send_commands, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file



nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/05.RealCase/01.Basic_Case/config_file/config.yaml")


def _change_hostname(task):

    template = task.run(task=template_file, template="_change_hostname.j2",path="/home/quandm/DATA/Git/netdevops/05.RealCase/templates")
    task.host["hostname"]=template.result
    rendered = task.host["hostname"]
    configuration = rendered.splitlines()
    print (configuration)
    task.run (task=send_configs,configs=configuration)

def _save_config(task):
    results = task.run(task=send_command, command="wr")
    print_result(results)

def check_template(task):
    template = task.run(task=template_file, template="check_connection.j2",path="/home/quandm/DATA/Git/netdevops/05.RealCase/templates")
    task.host["show_version"]=template.result
    rendered = task.host["show_version"]
    configuration = rendered.splitlines()
    print (configuration)
    task.run (task=send_commands,commands=configuration)



results=nr_task.run(task=_change_hostname)
print_result(results)