import whois, re
from datetime import datetime
from dateutil.parser import parse
from modules import getRoot

def get_domain_creation_date(domain):
    try:
        try:
            w = whois.whois(domain)
        except:
            domain = getRoot.get_root(domain)
            w = whois.whois(domain)
        if w.creation_date:
            if isinstance(w.creation_date, list):
                creation_date_str = str(w.creation_date[0])
            else:
                creation_date_str = str(w.creation_date)
            try:
                return parse(creation_date_str)
            except:
                return parse_creation_date(creation_date_str)
    except whois.parser.PywhoisError:
        return None

# Function to manually parse the creation date string
def parse_creation_date(date_str):
    # Use regex to extract date information from the string
    match = re.search(r"\d{8,14}", date_str)
    if match:
        date_format = "%Y%m%d%H%M%S"[:len(match.group())]
        try:
            return datetime.strptime(match.group(), date_format)
        except ValueError:
            pass
    return None

def get_age(domain):
    creation_date = get_domain_creation_date(domain)
    if creation_date:
        now = datetime.now()
        return (now - creation_date).days
    else:
        return None