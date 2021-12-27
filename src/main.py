import argparse
import sys
import os
import shutil

import commands as cmd


parser = argparse.ArgumentParser(usage='%(prog)s [options] <command>')

# create commands as a mutually exclusive group
parser.add_argument('Command',
                    metavar='command',
                    type=str,
                    help='build workspace using configs provided [build, teardown]')

# other args
parser.add_argument('-t',
                    '--test',
                    action='store_true',
                    help='enter test mode')

# return help screen if no commands provided
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

mode = 'test' if args.test is True else 'prod'

if args.Command == 'build':
    cmd.build(mode)
elif args.Command == 'teardown':
    cmd.teardown('fake_path')