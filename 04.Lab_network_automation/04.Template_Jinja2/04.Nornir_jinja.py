from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file



nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/04.Template_Jinja2/config.yaml")


def check_template(task):
    template = task.run(task=template_file, template="ospf.j2",path="templates")
    task.host["ospf_config"]=template.result
    rendered = task.host["ospf_config"]
    configuration = rendered.splitlines()
    print (configuration)
    task.run (task=send_configs,configs=configuration)

results=nr_task.run(task=check_template)
print_result(results)

