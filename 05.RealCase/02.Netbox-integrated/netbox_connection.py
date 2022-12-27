import pynetbox
from pprint import pprint
import json

import ipdb

class create_dict(dict):
    # __init__ function 
    def __init__(self):
        self = dict()
    # Function to add key:value 
    def add(self, key, value):
        self[key] = value


def _device_type_export(nb):

    devices = nb.dcim.device_types.all()
    _device_type=create_dict()
    for device in devices:
        #print(type(devices))
        _dict= dict(device)
        _id=_dict['id']
        _display=_dict['display']
        _device_type.add(_display,_id)
        #json_object = json.dumps(_dict, indent = 4)
        #print(json_object)
    print (_device_type)
    return _device_type

def _device_role_export(nb):

    devices = nb.dcim.device_roles.all()
    _device_role=create_dict()
    for device in devices:
        #print(type(devices))
        _dict= dict(device)
        _id=_dict['id']
        _display=_dict['display']
        _device_role.add(_display,_id)
        #json_object = json.dumps(_dict, indent = 4)
        #print(json_object)
    print (_device_role)
    return _device_role

def _site_export(nb):

    _sites = nb.dcim.sites.all()
    _site=create_dict()
    for _key in _sites:
        _dict= dict(_key)
        _id=_dict['id']
        _display=_dict['display']
        _site.add(_display,_id)
        #json_object = json.dumps(_dict, indent = 4)
        #print(json_object)

    print (_site)
    return _site


def _device_export(nb):

    _devices = nb.dcim.devices.all()
    _device=create_dict()
    for _key in _devices:
        _dict= dict(_key)
        
        _id=_dict['id']
        _display=_dict['name']
        _serial=dict['serial']
        _site=_dict['site']['name']


        _device.add(_display,_id)
        # json_object = json.dumps(_dict, indent = 4)
        # print(json_object)

    print (_device)
    return _device


_template_device ={
        "name": "R2",
        "device_role": 1,
        "site": 1,
        "device_type": 1
    }


nb = pynetbox.api(
    'http://192.168.90.185:8000',
    token='2383b8b90214e17e4dfdfa81e658c479ad3c57a7'
)


# nb.dcim.devices.create(dict(_template_device))

_device_role_export(nb)
_site_export(nb)
_device_type_export(nb)
_device_export(nb)