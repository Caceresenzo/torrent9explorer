from torrent9explorer import Utils

from cmd2 import Cmd
import re


class Terminal(Cmd):

    prompt = "t9explore $> "

    def __init__(self):
        Cmd.__init__(self)

    def do_search(self, line):
        from torrent9explorer import Explorer, Searcher
        ''' "name of the serie" limit X '''

        limit = Utils.argument(name="limit", default=1, min=1, line=line)
        stack = Utils.argument(name="stack", default=10, min=1, line=line)

        match = re.search(r"^\"(.*?)\"", line, re.MULTILINE)

        if (match == None or len(match.groups()) < 1):
            # TODO: Error
            print("Error, no name found")
            return

        query = match.group(1)

        print("query: " + query + ", limit: " +
              str(limit) + ", stack: " + str(stack))

        searcher = Searcher(query=query, limit=limit)
        Explorer.get().executeSearch(searcher.prepare().getUrls(), stack)

    def do_dl(self, line):
        # download function #
         ### syntaxe :  downloadlist 105,230,123,(110-120) ###
        if (line == None or not line):
            print("Error, suitable argument")
            return

        itemIds = line.split(",")

        for id in itemIds:
            # tester si id contient -
            if ("-" in id):
                # si il contient:
                idSplited = (id.split("-"))
                print(idSplited)
                idSplitedStartRange = idSplited[0]
                idSplitedEndRange = idSplited[1]
                print("Start of range at : " + idSplitedStartRange +
                      " End of range at : " + idSplitedEndRange)

            else:
                print("caracters not found ")
            #
            # si il contient:
            #      id.splt(-)
            #       test si string == chiffre
            #       test si 1er chiffre pas plus grand que 2e
            #       boucle qui recup tout les chiffre entre ces 2 chiffre
            #       # rajoter commentaire des que id pret
            # sinon
            #       tester si chiffre == nombre
            #       # rajoter commentaire des que id pret

    def do_exit(self, line):
        exit()
