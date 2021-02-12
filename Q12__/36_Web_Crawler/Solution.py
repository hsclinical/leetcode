# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from typing import List

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        slashPos = startUrl.find('/', 7)
        if slashPos == -1:
            coreUrl = startUrl
        else:
            coreUrl = startUrl[:slashPos]

        included = set()
        included.add( startUrl )
        self.crawlProcess(included, coreUrl, htmlParser, startUrl)
        return list(included)

    def crawlProcess(self, included, coreUrl, htmlParser, startUrl):
        urls = htmlParser.getUrls(startUrl)
        for singleUrl in urls:
            if singleUrl.startswith(coreUrl) and singleUrl not in included:
                included.add( singleUrl )
                self.crawlProcess(included, coreUrl, htmlParser, singleUrl)

