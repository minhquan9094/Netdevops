from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import json
from pytest_check import check_func


vlan_count={
    "1":1,
    "230": 10

}

@check_func
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
        print (f" Vlan {_vlan_id} has {number_interface} interfaces")
        assert number_interface == _expect_num_int, f"{task.host} - {_vlan_id} FAILED"

def testcase(nr_sw):
    nr_sw.run(task=pull_vlan)
