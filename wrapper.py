import boto3

# this is a 'generator'
#
# `service` is the AWS Service (used by boto3.client() ), e.g. 's3' or 'lambda'
# `paginator_name` is the name of the paginator called by client.get_paginator
# the actual elements from the normal pagination response are inside a list, inside
# a dictionary under element `key`
# `kwargs` are extra options to be passed to the paginator
def paginator(service, paginator_name, key, **kwargs):

    client = boto3.client(service)

    paginator = client.get_paginator(paginator_name)

    for page in paginator.paginate(**kwargs):
        if key in page:
            for element in page[key]:
                yield element
