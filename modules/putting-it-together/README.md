# Putting it all together
Let's take some of the tools we've learned thus far in the course and start assembling them into cohesive components that work together to do something.  In this example we're examining smart contracts of NFT projects on the Ethereum Blockchain.

## Contents
1. [Demo Overview](#demo-overview)
1. [Prerequisites](#prerequisites)
1. [Topic Overview](#topic-overview)
1. [Demo](#demo)

## Demo Overview

This demo covers a basic project implementation to model what a perspective class project could look like.

## Prerequisites

- python installed on your computer


## Topic Overview

This demo outlines an example class project to show how a class project could be composed.  There are many additional items included under the [`mypackage`](../putting-it-together/mypackage/) directory that are not required in the final project, but are components of a proper Python package and are good to be aware of.

1. Define the question
1. Find the data
1. Interact with data structures
1. Analyze the data

### The Question

Of the top 10 Ethereum NFT projects, which are `above the bar` and which are `below the bar` based on whether the metadata for each is decentralized or not.

### The Data Source

Google hosts the entire Ethereum Blockchain dataset in [BigQuery](https://cloud.google.com/blog/products/data-analytics/ethereum-bigquery-public-dataset-smart-contract-analytics) that is powered by this Python ETL [package](https://github.com/blockchain-etl/ethereum-etl).

Access this [console](https://console.cloud.google.com/marketplace/product/ethereum/crypto-ethereum-blockchain?project=codelouisville2022) to access the most up-to-date Ethereum Blockchain DataSet using the following query.

```
SELECT contracts.address, COUNT(1) AS tx_count
FROM `bigquery-public-data.crypto_ethereum.contracts` AS contracts
JOIN `bigquery-public-data.crypto_ethereum.transactions` AS transactions ON (transactions.to_address = contracts.address)
WHERE contracts.is_erc721 = TRUE
GROUP BY contracts.address
ORDER BY tx_count DESC
LIMIT 10
```

The query results are likely to change as the data is updated daily based off of usage (`tx_count`).

### Sample Data
```
[
    {
      "address": "0x06012c8cf97bead5deae237070f9587f8e7a266d",
      "tx_count": "4895135"
    },
    {
      "address": "0x06a6a7af298129e3a2ab396c9c06f91d3c54aba8",
      "tx_count": "646168"
    },
    {
      "address": "0xd73be539d6b2076bab83ca6ba62dfe189abc6bbe",
      "tx_count": "442927"
    },
    {
      "address": "0x1a94fce7ef36bc90959e206ba569a12afbc91ca1",
      "tx_count": "180701"
    },
    {
      "address": "0xf5b0a3efb8e8e4c201e2a935f110eaaf3ffecb8d",
      "tx_count": "147728"
    },
    {
      "address": "0x7fdcd2a1e52f10c28cb7732f46393e297ecadda1",
      "tx_count": "119608"
    },
    {
      "address": "0x8c9b261faef3b3c2e64ab5e58e04615f8c788099",
      "tx_count": "108286"
    },
    {
      "address": "0x2a46f2ffd99e19a89476e2f62270e0a35bbf0756",
      "tx_count": "101077"
    },
    {
      "address": "0xf915bbfbb6c097dc327e64eec55e9ef4d110d627",
      "tx_count": "78763"
    },
    {
      "address": "0xd2f81cd7a20d60c0d558496c7169a20968389b40",
      "tx_count": "60858"
    }
  ]
```

## Demo
Refer to the [README.md](./mypackage/README.md) in [mypackage](../putting-it-together/mypackage/) for more details.

### Mentor Demo: Structuring our data
Google's Big Query returns a JSON option that is a list of dictionaries.  For this demo we will keep the data structure as-is and in static form within our Python module.  In future versions, this can be replaced with a BigQuery API call using something like the `sqlalchemy` library.

### Student Exercise: Other data structures
A list of dictionaries is one type of data structure, can you think of another that would work for the project?  Can you create one, or modify the one in this demo?

### Mentor Demo: Working with classes
In this demo a `Project` class is created in order to interact with each Project's data attributes.  Object-oriented design is not a requirement, but it's a great skillset to have when organizing code.

Some of the class methods are leveraging the `random` library to return a value for the given attribute.  `random` is emulating a result until an API call can be added.  

Note, inside of the contructor three class attributes are calling a method aka function inside of a class, and calling 3 of them is one of the requirements.

### Student Exercise:  Create a class of your own
Open an interactive Python session and try creating a class of your own or adding onto `main.py` in [mypackage](../putting-it-together/mypackage/).

### Mentor Demo: Execute the script
1. Navigate to [mypackage](../putting-it-together/mypackage/) in a terminal, and execute: 
* mac/linux/gitbash: `python src/main.py`
* windows:  `python src\main.py`

```
Below the bar: {'address': '0x06012c8cf97bead5deae237070f9587f8e7a266d', 'tx_count': '4895135', 'rank': 1}
Above the bar: {'address': '0x06a6a7af298129e3a2ab396c9c06f91d3c54aba8', 'tx_count': '646168', 'rank': 5}
Above the bar: {'address': '0xd73be539d6b2076bab83ca6ba62dfe189abc6bbe', 'tx_count': '442927', 'rank': 3}
Above the bar: {'address': '0x1a94fce7ef36bc90959e206ba569a12afbc91ca1', 'tx_count': '180701', 'rank': 3}
Above the bar: {'address': '0xf5b0a3efb8e8e4c201e2a935f110eaaf3ffecb8d', 'tx_count': '147728', 'rank': 3}
Above the bar: {'address': '0x7fdcd2a1e52f10c28cb7732f46393e297ecadda1', 'tx_count': '119608', 'rank': 4}
Above the bar: {'address': '0x8c9b261faef3b3c2e64ab5e58e04615f8c788099', 'tx_count': '108286', 'rank': 4}
Below the bar: {'address': '0x2a46f2ffd99e19a89476e2f62270e0a35bbf0756', 'tx_count': '101077', 'rank': 2}
Above the bar: {'address': '0xf915bbfbb6c097dc327e64eec55e9ef4d110d627', 'tx_count': '78763', 'rank': 4}
Below the bar: {'address': '0xd2f81cd7a20d60c0d558496c7169a20968389b40', 'tx_count': '60858', 'rank': 2}
```
Content details may be different since some of the data is randomized.

