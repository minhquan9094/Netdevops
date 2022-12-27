from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.task import Task, Result, NornirSubTaskError
import json


nr_task = InitNornir(config_file="config_lab.yaml")

def get_facts_infor(task):
    result = task.run(task=napalm_get, getters=["get_facts"])
    print_result(result)
    for i in result:
        print (i)
        # print(f"Iterating through result object of type{type(result[i])} for item {i}")

        # print(f"\tGet the top level key(s) for the device:")

        # top_result_keys = result[i].result.keys()
        # print(f"\t{top_result_keys}")
        
        # Example output: dict_keys(['get_facts'])

        # print(f"\n\tGet the next level of key(s):")
        next_keys = result[i].result['get_facts'].keys()
        print(f"\t{next_keys}")
        # Example output: dict_keys(['uptime', 'vendor', 'os_version', 'serial_number', 'model', 'hostname', 'fqdn', 'interface_list'])

        # Iterate through the keys and values
        # print(f"\tDecomposing Result Object for hostname {i}...")
        for k in next_keys :
            print(f"\t\tKey {k} \t: {result[i].result['get_facts'][k]}")

        print("\n")

    # print(f"\nPrint run results with the print_result module."
    #        "\nThis is a built-in Ansible like run status that will format the output for easy viewing...")
    
    # print_result(result)



get_facts_infor(nr_task)