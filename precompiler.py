#!/usr/bin/env python3

import argparse
import re

if __name__ == '__main__':
    usage = 'python precompiler.py -D A=1 -D B=2 -i in.glsl -o out.glsl'
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('-D', required=True, action='append')
    parser.add_argument('-i', required=True)
    parser.add_argument('-o', required=True)
    args = parser.parse_args()
    defines = ''
    for d in args.D:
        defines += ' '.join(['\n#define', *d.split('=', maxsplit=1)])
    input_data = None
    with open(args.i, encoding='utf-8') as input_file:
        input_data = input_file.read()
    output_data = None
    pattern = r'(?s:/\*.*?\*/)|(?://.*)|(#\s*version(\s+\w+)+)'
    for match in re.finditer(pattern, input_data):
        version = match.group(1)
        if version:
            before_version = input_data[:match.start()]
            after_version = input_data[match.end():]
            output_data = before_version + version + defines + after_version
            break
    with open(args.o, 'w', encoding='utf-8') as output_file:
        output_file.write(output_data)
