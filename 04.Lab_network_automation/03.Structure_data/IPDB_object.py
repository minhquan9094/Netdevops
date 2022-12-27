from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
import ipdb

'''
Lib:

- pip install scrapli[genie]
- pip install ipdb


ipdb to running python and move to CLI to check data of dict

ipdb exports functions to access the IPython debugger, which features tab completion, syntax highlighting, better tracebacks, better introspection with the same interface as the pdb module.


'''



nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/config_file/config.yaml")

def pull_structure_data(task):
    output_result= task.run(task=send_command, command="show version")
    task.host["facts"] = output_result.scrapli_response.genie_parse_output()
    uptime = task.host["facts"]["version"]["uptime"]
    version_number=task.host["facts"]["version"]["version_short"]
    host_ip=task.host.hostname
    
    #print (f"{task.host} uptime: {uptime}")

    #print ("Screening OS version: ")

    if version_number != "13":
        print (f"{task.host} - {host_ip} VERSION: {version_number}")

    # print(task.host["facts"])


results = nr_task.run(task=pull_structure_data)
print_result(results)

#ipdb.set_trace()