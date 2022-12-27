from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_config,send_configs,send_configs_from_file,send_interactive
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result, NornirSubTaskError


nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/config_file/config.yaml")



### ---------------------------------------------------- Rollback configuration: using send_interactive

def backup_config_flash(task):
    cmds = [("copy run flash:backup_config","Destination filename"),("\n",f"{task.host}#")]
    task.run(task=send_interactive, interact_events=cmds)


def rollback_config_from_flash(task):
    cmds = "configure replace flash:backup_config force"
    task.run(task=send_command, command=cmds)


results = nr_task.run(task=rollback_config_from_flash)
print_result(results)
