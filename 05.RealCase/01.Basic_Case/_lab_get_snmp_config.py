from nornir import InitNornir
from nornir_scrapli.tasks import send_command,send_commands, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
import ipdb


nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/05.RealCase/01.Basic_Case/config_file/config.yaml")


def _deploy_snmp(task):

    template = task.run(task=template_file, template="_change_SNMP.j2",path="/home/quandm/DATA/Git/netdevops/05.RealCase/templates")
    task.host["change"]=template.result
    rendered = task.host["change"]
    configuration = rendered.splitlines()
    print (configuration)
    task.run (task=send_configs,configs=configuration)



def _get_SNMP_config(task):

    template = task.run(task=template_file, template="_check_snmp_config.j2",path="/home/quandm/DATA/Git/netdevops/05.RealCase/templates")
    task.host["change"]=template.result
    rendered = task.host["change"]
    configuration = rendered.splitlines()
    #print (configuration)

    _snmp_result = task.run (task=send_commands, commands=configuration)
    # _snmp_result = task.run (task=send_command, command="show running-config | include community")
    
    task.host['snnp_conf'] = _snmp_result.scrapli_response.result





results=nr_task.run(task=_get_SNMP_config)
# for i in nr_task.inventory.hosts:
#     print (nr_task.inventory.hosts[i]['facts'])

print_result(results)

ipdb.set_trace()