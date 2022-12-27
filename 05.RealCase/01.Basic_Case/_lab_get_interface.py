from nornir import InitNornir
from nornir_scrapli.tasks import send_command,send_commands, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_get
import ipdb

nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/05.RealCase/01.Basic_Case/config_file/config.yaml")



def _get_interface(task):
    result=task.run(task=napalm_get,getters=["interfaces"])
    interfaces=result.result["interfaces"]
    for interface in interfaces:
        print (f'{task.host} - {interface}')
    #print (f'{task.host} - {result.result["interfaces"]}')

results=nr_task.run(task=_get_interface)