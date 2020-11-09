'''
    commands.py
    register command in '/commands' file
    and execute command
'''
#!/usr/bin/env/python

import os
import sys
import script.conf as conf

class JPCommand(object):

    command_name = []

    def __init__(self):
        '''
            first, Get Commands and save self.command_name
            second, import command file
        '''
        self.command_name = []
        ls_com = self.getCommandFileList()

        for files in ls_com:
            filext = os.path.splitext(files)
            for ext in ['.py', '.pyc', '.pyo']:
                if ext == filext[-1]:
                    self.command_name.append(filext[0])

        self.importCommand()


    def getCommandFileList(self):
        '''
            Get file list in script/commands/
            and path append script/commands/
        '''
        path = os.path.dirname(__file__) + conf.commandFileName
        sys.path.append(path)
        file_list = os.listdir(path)
        return file_list

    def importCommand(self):
        '''
            import command files
            command file must '/script' folder
        '''
        if self.command_name is None:
            return

        for command in self.command_name:
            try:
                __import__(command)
                print(dir())
                print(command)
            except Exception:
                print("[-] fail import " + command)

    
    def execute(self):
        print(dir())
        #func()

