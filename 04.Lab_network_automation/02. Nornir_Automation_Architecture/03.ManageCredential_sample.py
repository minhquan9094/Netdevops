from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result, NornirSubTaskError
import getpass

nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/config_file/config.yaml")


### --------------------------------------------------- using getpass


'''
password= getpass.getpass()
nr_task.inventory.defaults.password = password

def send_command_sample(task):
    results = task.run(task=send_command,command=f"show ip int br")

results = nr_task.run(task=send_command_sample)
print_result(results)

'''





### --------------------------------------------------- Handle multiple password