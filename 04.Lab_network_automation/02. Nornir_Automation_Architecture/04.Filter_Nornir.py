from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result, NornirSubTaskError
from nornir.core.filter import F

nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/config_file/config.yaml")



### ----------------------------------------------------    Check data ---

host=nr_task.inventory.hosts
#print (host.keys())

for _host in host:
    data=nr_task.inventory.hosts[_host]
    _storeID = data['storeID']
    _city=data['city']

    _output = f"{_host} - {_city} - {_storeID}"

    print (_output)


#### -------------------------------------------------------- Define configuration command

def _config_deploy(task):
    results = task.run(task=send_configs_from_file,file="config_text.txt")


####  --------------- Filter


## filter target devices with value of field
host_target_field_filter = nr_task.filter(city="HCM", storeID="LAB001")

### -------  filter target devices with check field 

# host_target_field_check = nr_task.filter(F(firewall="T"))
host_target_field_check = nr_task.filter(firewall="T")



## Cross check
host=host_target_field_check.inventory.hosts
print (f"Target host: {host.keys()}")


#### Send config to target host --> change _deploy_task
_deploy_task=host_target_field_check.run(task=_config_deploy)
print_result(_deploy_task)


