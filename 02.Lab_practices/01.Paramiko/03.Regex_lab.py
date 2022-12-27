import re


with open('show_version.txt') as ver_data:
    ver_output = ver_data.read()

my_pattern = r"Cisco.+, Version (\d\S+)"
re_output = re.search(pattern=my_pattern, string=ver_output)
print(re_output.group(0))
print(re_output.group(1))