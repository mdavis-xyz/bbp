from wrapper import paginator
from pprint import pprint
for lam in paginator('lambda', 'list_functions', 'Functions'):
        pprint(lam) # process a single resource
