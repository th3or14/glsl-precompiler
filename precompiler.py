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
    read_data = None
    with open(args.i, encoding='utf-8') as input_file:
        read_data = input_file.read()
    version = re.search(r'#\s*version\s+[0-9]+.*', read_data)[0]
    split_data = read_data.split(version, maxsplit=1)
    final_data = split_data[0] + version + defines + split_data[1]
    with open(args.o, 'w', encoding='utf-8') as output_file:
        output_file.write(final_data)
