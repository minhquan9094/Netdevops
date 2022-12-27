from pyats.topology import loader
#from genie.testbed import load
import json


testbed = loader.load('testbed.yaml')
device = testbed.devices['vIOS2']
device.connect()

output = device.learn('ospf')
with open("backup.json", "w") as fh:
    json.dump(output.to_dict(), fh, indent=2)