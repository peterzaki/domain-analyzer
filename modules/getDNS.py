import dns.resolver
from modules import getRoot

def aRecNum(domain):
    try:
        recordsNum = 0
        A = dns.resolver.resolve(domain, 'A')
        for answer in A.response.answer:
            for ip in answer.items:
                recordsNum += 1
        return recordsNum
    except:
        return 0

def ipTTL(domain):
    try:
        try:
            response = dns.resolver.resolve(domain, 'SOA')
            return response[0].minimum
        except:
            root_domain = getRoot.get_root(domain)
            response = dns.resolver.resolve(root_domain, 'SOA')
            return response[0].minimum
    except:
        return None