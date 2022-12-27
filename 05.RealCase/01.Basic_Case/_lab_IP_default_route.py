from nornir import InitNornir
from nornir_scrapli.tasks import send_command,send_commands, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file



nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/05.RealCase/01.Basic_Case/config_file/config.yaml")


def _change_IP_default_route(task):

    template = task.run(task=template_file, template="_change_ip_default_route.j2",path="/home/quandm/DATA/Git/netdevops/05.RealCase/templates")
    task.host["change"]=template.result
    rendered = task.host["change"]
    configuration = rendered.splitlines()
    print (configuration)
    task.run (task=send_configs,configs=configuration)


results=nr_task.run(task=_change_IP_default_route)
print_result(results)