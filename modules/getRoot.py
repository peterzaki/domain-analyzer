import tldextract

def get_root(domain):
    extracted = tldextract.extract(domain)
    return "{}.{}".format(extracted.domain, extracted.suffix)

