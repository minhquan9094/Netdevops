from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file,send_command
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from tqdm import tqdm


nr_task = InitNornir(config_file="config_lab.yaml")


def create_config(task,progress_bar):
    task.run(task=send_configs_from_file,file="config_file/config.txt")
    progress_bar.update()


# result = nr_task.run(task=napalm_get, getters=["get_facts"])
# print_result(result)


# results= nr_task.run(task=send_command, command="show version", strip_prompt=True)
# print_result(results)




with tqdm(total=len(nr_task.inventory.hosts)) as progress_bar:
    results=nr_task.run(task=create_config,progress_bar=progress_bar)

print_result(results)