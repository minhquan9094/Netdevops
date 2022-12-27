from nornir import InitNornir
import pytest


@pytest.fixture(scope="session",autouse=True)
def nr():
    nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/08.Pytest/config.yaml")
    yield nr_task
    nr_task.close_connections()


@pytest.fixture(scope="session",autouse=True)
def nr_sw():
    nr_task = InitNornir(config_file="/home/quandm/DATA/Git/netdevops/04.Lab_network_automation/08.Pytest/config_sw.yaml")
    yield nr_task
    nr_task.close_connections()


