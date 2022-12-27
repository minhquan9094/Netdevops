from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/08.Pytest/config.yaml")



def pull_ospf(task):
    ospf_list=[]
    result = task.run(task = send_command, command = "show ip os neig")
    task.host['facts'] = result.scrapli_response.genie_parse_output()
    interfaces = task.host["facts"]["interfaces"]

    for interface in interfaces:
        ospf_neighbor = interfaces[interface]['neighbors']
        # print (ospf_neighbor)
        for _ospf_neighbor_id in ospf_neighbor:
            ospf_list.append(_ospf_neighbor_id)
    
    num_of_neighbor = len(ospf_list)
    #print (ospf_list)
    output=f"{task.host} - {num_of_neighbor} OSPF Neighbors"
    print (output)




results=nr_task.run(task=pull_ospf)
# print_result(results)
# import ipdb
# ipdb.set_trace()