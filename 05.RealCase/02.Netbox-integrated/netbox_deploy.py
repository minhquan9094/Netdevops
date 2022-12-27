import pynetbox
from pprint import pprint
import json

nb = pynetbox.api(
    'http://192.168.90.185:8000',
    token='2383b8b90214e17e4dfdfa81e658c479ad3c57a7'
)


devices = nb.dcim.devices.all()
