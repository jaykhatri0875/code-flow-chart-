import re

read = re.compile(r"([a-zA-Z]+) = input\(\)")
write = re.compile(r"print\((.+)\)")
loop = re.compile(r"while(.+)")
loop = re.compile(r'for(.+)')
branch = re.compile(r"if(.+)")
#write = re.compile(r'#(.+)')
