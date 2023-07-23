import re
from modules import getAge, getDGA, getDNS, getRoot

def is_domain(value):
    domain_pattern = r'^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return bool(re.match(domain_pattern, value))

def process_domain(domain, quiet):
    if is_domain(domain):
        if not quiet:
            print(f"Analyzing domain: {domain} ..")  # Print the domain being analyzed
        age_days = getAge.get_age(domain)
        dga_status = getDGA.is_dga(domain)
        ip_count = getDNS.aRecNum(domain)
        ip_ttl = None
        if (ip_count != 0):
            ip_ttl = getDNS.ipTTL(domain)

        return (domain, age_days, dga_status, ip_count, ip_ttl)
    if not quiet:
            print(f"Skipping invalid domain: {domain} ..")  # Print invalid domain value
    return (domain, None, None, None, None)