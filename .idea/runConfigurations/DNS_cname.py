import dns

import dns.rdtypes.nsbase
import dns.immutable
import dns.enum
import dns.exception


import dns.resolver
result = dns.resolver.resolver('mail.google.com', 'CNAME')
for cnameval in result:
    print(" cname target address:, cnameval.target")







