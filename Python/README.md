---
page_type: sample
languages:
- python
products:
- azure
description: "Azure Cosmos DB is a globally distributed multi-model database."
---

# Developing a Python app using the Azure Cosmos DB SQL API
Azure Cosmos DB is a globally distributed multi-model database. One of the supported APIs is the SQL API, which provides a JSON document model with SQL querying and JavaScript procedural logic. This sample shows you how to use Azure Cosmos DB with the SQL API to store and access data from a Node.js application.

## Running this sample
* Before you can run this sample, you must have the following perquisites:
	* An active Azure Cosmos DB account - If you don't have an account, refer to the [Create an Azure Cosmos DB account](https://learn.microsoft.com/azure/cosmos-db/nosql/quickstart-python?tabs=azure-portal%2Cpasswordless%2Cwindows%2Csign-in-azure-cli%2Csync) article.
	* [Python](https://www.python.org/downloads/) version v3.7 or higher.
	* [Git](http://git-scm.com/).


1. There is no need to change the credentials from the extracted app.  We have entered the Azure Cosmos DB endpoint URL and the key into your `config.py` file.

2. Run `pip3 install -r requirements.txt` in a terminal to install required python packages.
 
3. Run `python3 run.py` in a terminal to start your start your node application.

## About the code
The code included in this sample is intended to get you quickly started with a Node.js console application that connects to Azure Cosmos DB with the SQL API.

## More information

- [Azure Cosmos DB](https://docs.microsoft.com/azure/cosmos-db/introduction)
- [Azure Cosmos DB: SQL API](https://docs.microsoft.com/en-us/azure/cosmos-db/sql-api-introduction)
- [Azure Cosmos DB Node.js SDK](https://docs.microsoft.com/en-us/azure/cosmos-db/sql-api-sdk-node)
- [Azure Cosmos DB Node.js SDK Reference Documentation](http://azure.github.io/azure-documentdb-node/)
