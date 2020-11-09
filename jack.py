
import script.conf as conf
config = conf.ConfClass()
import script.commands as command


import sys

def main():
    sys.stderr.write("JACKPOT_FUZZER - A unicorn engine fuzzer {0}\n".format(conf.VERSION))
    sys.stderr.flush()

    #co = command.JPCommand()
    command.JPCommand()
    print(dir('dump'))


if __name__ == "__main__":
    config.set_usage(usage = "JACKPOT_FUZZER - A unicorn engine fuzzer platform.")
    main()
