
## Init
resourceGroupName='rgCosmosDBDemo'
accountName='catcosmosdbdemo'
databaseName='ecommerce'
containerName='orders'
partitionKey='/partitionKey'
throughput=400

az group create --location westus --resource-group $resourceGroupName

az cosmosdb create -n $accountName -g $resourceGroupName --default-consistency-level Session --locations regionName='West US' failoverPriority=0 isZoneRedundant=False --locations regionName='East US' failoverPriority=1 isZoneRedundant=False

az cosmosdb sql database create -a $accountName -g $resourceGroupName -n $databaseName

az cosmosdb sql container create -a $accountName -g $resourceGroupName -d $databaseName -n $containerName -p $partitionKey --throughput $throughput


## Error: AttributeError: 'NoneType' object has no attribute 'ConsistencyPolicy'?
sudo hwclock -s