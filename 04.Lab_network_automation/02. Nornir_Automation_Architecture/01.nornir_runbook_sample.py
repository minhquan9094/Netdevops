from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_config,send_configs,send_configs_from_file
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.task import Task, Result, NornirSubTaskError


nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/config_file/config.yaml")



### ----------------------------------------------------    Get something information in inventory

host=nr_task.inventory.hosts
print (host.keys())

data=nr_task.inventory.hosts["vIOS4"]
print (data.keys())

defaul_data_username=nr_task.inventory.defaults.username
print (defaul_data_username)


defaul_data_password=nr_task.inventory.defaults.password
print (defaul_data_password)


### ----------------------------------------------------  basic configuration using send_command
'''

results = nr_task.run(task=send_command, command="show version")
print_result(results)

'''



### ---------------------------------------------------- Use data as variable - using send_config
'''
def data_block_test(task):
    #print (task)
    results = task.run(task=send_config, config=f"ntp server {task.host['ntp_server']}")

results = nr_task.run(task=data_block_test)
print_result(results)

'''

### ---------------------------------------------------- Deploy config from file using Scrapli:
#   send_config_from file
#   send multiple config

'''

def send_config_sample(task):
    results = task.run(task=send_config,config=f"no snmp-server community send_single_config")

def send_configs_sample(task):
    results = task.run(task=send_configs,configs=[f"snmp-server community send_single_config", "snmp-server source-interface informs g0/0",
    "snmp-server host 192.168.88.1 send_configs_sample"])

def send_configs_fromfile_sample(task):
    results = task.run(task=send_configs_from_file,file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/config_file/config_fromtext.txt")


results = nr_task.run(task=send_configs_fromfile_sample)
print_result(results)
'''