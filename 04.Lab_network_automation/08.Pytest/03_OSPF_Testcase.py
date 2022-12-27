from nornir_scrapli.tasks import send_command
from nornir.core.filter import F
from pytest_check import check_func

#### running command: pytest 03_OSPF_Testcase.py --disable-warnings

neighbor_count={
    "office":3,
    "MFG":1

}


@check_func
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
    
    role=task.host["role"]
    expected_neighbor=neighbor_count[role]

    num_of_neighbor = len(ospf_list)
    output=f"{task.host} - {num_of_neighbor} OSPF Neighbors"
    print (output)
    assert num_of_neighbor == expected_neighbor, f"{task.host} - {num_of_neighbor} FAILED"



def testcase_OSPF(nr):
    nr.run(task=pull_ospf)
