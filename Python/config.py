import os

settings = {
    'host': os.environ['ACCOUNT_HOST'],
    'master_key': os.environ['ACCOUNT_KEY'],
    'database_id': os.environ.get('COSMOS_DATABASE', 'ecommerce'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'orders'),
}