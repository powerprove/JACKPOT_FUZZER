'''
    dumper.py
    Dump the program using gdb, ida, lldb, etc.
    Options include bp, us, etc. BP is breakpoint and default is main
    USE default is gdb
    -----------
    In order to run script 
    gdb_dump need to gef
    -----------

'''
import os
import sys
import optparse
import subprocess

option = None

def parseOption():
    parser = optparse.OptionParser("python3 dump.py --breakpoint <breakpoint=main> --us <tools=gdb> -p <program>")
    parser.add_option("--breakpoint", dest="bp", default="main", type='string', help="default is main")
    parser.add_option("--us", dest="us", default="gdb", type='string', help="default is gdb")
    parser.add_option("-p", "--program", dest="dump_program", type='string', help="dump prgram")
    global option
    (option, args) = parser.parse_args()

    if option.dump_program == None:
        print(parser.usage)
        sys.exit(-1)

def dump_gdb():
    try:
        source_file = os.path.dirname(os.path.realpath(__file__)) + "/dumper_gdb.py"
        command = bytes('b ' + option.bp + '\nr\nsource ' + source_file, 'ascii')
        p = subprocess.Popen(['gdb', '-q', option.dump_program], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        std = p.communicate(input=command)
    except Exception as e:
        print(e)
        return -1

def main():
    parseOption()
    print("----- Unicorn Context Main Dump -----")
    print("breakpoint="+option.bp +" use="+option.us)

    if option.us == "gdb":
        dump_gdb()
    else:
        print("ERROR : not support ", option.us)


if __name__ == "__main__":
    main()
