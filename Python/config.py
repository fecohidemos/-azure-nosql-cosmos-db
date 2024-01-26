import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://catcosmosdbdemo.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'hqwRiYpnW0JwgtwyuLhe9a78cjrghZXc6QsPNzakapEvlGeDvgzFiluWnTLEQJgGWs9xUgyDwcxEACDb51SZaQ=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ecommerce'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'orders'),
}