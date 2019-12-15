from bbp import paginator
from pprint import pprint
bucket_name = 'reddit-amp-bot-code'
for obj in paginator('s3', 'list_objects_v2', 'Contents', Bucket=bucket_name):
        pprint(obj) # process a single resource
