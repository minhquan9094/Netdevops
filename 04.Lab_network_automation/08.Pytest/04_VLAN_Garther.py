from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import json
nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/08.Pytest/config_sw.yaml")


vlan_count={
    "1":7,
    "230": 1

}


def check_connection(task):
    result = task.run(task = send_command, command = "show vlan")
    task.host['facts'] = result.scrapli_response.genie_parse_output()
    print_result(result)

def pull_vlan(task):
    vlan_list=[]
    
    result = task.run(task = send_command, command = "show vlan")
    task.host['facts'] = result.scrapli_response.genie_parse_output()

    vlans = task.host["facts"]["vlans"]
    num_vlans=len(vlans)
    print (f"Total vlan of {task.host}: {num_vlans}")

    for vlan in vlans:
        interface_vlan=[]
        #vlan_list.append(vlan)
        _vlans_info = vlans[vlan]
        _vlan_id=_vlans_info['vlan_id']
        if _vlan_id in ["1002","1003","1004","1005"]:
            continue
        try:
            _interface=_vlans_info['interfaces']
        except:
            _interface=""
            pass
        number_interface=len(_interface)
        _expect_num_int=vlan_count[_vlan_id]


        print (f" Vlan {_vlan_id} has {number_interface} interfaces vs {_expect_num_int}")
    
    
results=nr_task.run(task=pull_vlan)
# print_result(results)
# import ipdb
# ipdb.set_trace()