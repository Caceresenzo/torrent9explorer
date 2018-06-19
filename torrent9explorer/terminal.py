from cmd2 import Cmd
import re


class Terminal(Cmd):

    def __init__(self):
        Cmd.__init__(self)

    def do_search(self, line):
        ''' "name of the serie" limit X '''

        limit = 1

        if ("limit" in line):
            match = re.search(r"^.*?[ \t]+[-]{0,2}limit[ \t:=]+([\d]+)", line, re.MULTILINE)

            if (match != None and len(match.groups()) == 1):
                limit = int(match.group(1))

        match = re.search(r"^\"(.*?)\"", line, re.MULTILINE)

        if (match == None or len(match.groups()) < 1):
            # TODO: Error
            print("Error, no name found")
            return;

        name = match.group(1)

        print("name: " + name + ", limit: " + str(limit))
