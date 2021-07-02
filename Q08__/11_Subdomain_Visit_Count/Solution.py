from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainCnt = defaultdict(int)
        for cpdomain in cpdomains:
            cells = cpdomain.split()
            cnt = int(cells[0])
            domains = cells[1].split( '.' )
            domains.reverse()
            domainSuffix = None
            for domain in domains:
                if domainSuffix == None:
                    domainSuffix = domain
                else:
                    domainSuffix = domain + '.' + domainSuffix
                domainCnt[ domainSuffix ] += cnt
        outList = [ str( domainCnt[x] ) + ' ' + x for x in domainCnt ]
        return outList
