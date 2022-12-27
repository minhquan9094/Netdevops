from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
import ipdb

'''

Lab: 
    - Get CDP neighbor information
    - Set interface description



'''

nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/config_file/config.yaml")


def save_config(task):
    results = task.run(task=send_command,command="wr")


def send_configs_from_enableinterface(task):
    results = task.run(task=send_configs_from_file,file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/config_file/enable_interface.txt")

def auto_description_interface_cdpinfor(task):
    output_result= task.run(task=send_command, command="show cdp nei")
    task.host["facts"] = output_result.scrapli_response.genie_parse_output()
    cdp_index=task.host["facts"]['cdp']['index']
    for index in cdp_index:
        local_intf=cdp_index[index]["local_interface"]
        remote_intf=cdp_index[index]["port_id"]
        remote_devce=cdp_index[index]["device_id"]

        config_commands=[f"interface {local_intf}",f"description ## Connect to {remote_devce} - {remote_intf}"]
        deploy_command= task.run(task=send_configs, configs=config_commands)


    #print (task.host['facts'])
    #g0_0_ip = task.host["facts"]["interface"]["GigabitEthernet0/0"]['ip_address']
    #print (g0_0_ip)

results = nr_task.run(task=save_config)
print_result(results)

#ipdb.set_trace()