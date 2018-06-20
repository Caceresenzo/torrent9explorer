from torrent9explorer import Torrent9Item
import re


class Regexer():

    @staticmethod
    def createItemFromHtml(html):
        list = []

        regex = r"\<tr\>[ \t\n]*\<td\>\<i\sclass=\"fa\sfa-(.*?)\"\sstyle=\".*?\"\>\<\/i\>[ \t\n]*\<a title=\".*?\"\shref=\"(.*?)\".*?\>(.*?)\<\/a\>\<\/td\>[ \t\n]*\<td\sstyle=\".*?\">(.*?)\<\/td\>[ \t\n]*\<td\sstyle=\".*?\"\>\<span\sclass=\"seed_ok\">(.*?)\<img.*?\>\<\/span\>\<\/td\>[ \t\n]\<td\sstyle=\".*?\"\>(.*?)\<img.*?\>\<\/td\>[ \t\n]*\<\/tr\>"
        matches = re.finditer(regex, str(html), re.MULTILINE | re.DOTALL)

        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1
            list.append(Torrent9Item(type=match.group(1), url=match.group(2), name=match.group(3), size=match.group(4), seed=match.group(5), leech=match.group(6)))

        return list
