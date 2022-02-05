# Data Development Pathway with Python and SQL
This is an example project for the Code Louisville Python Data Development Course.

# My Project
Using Google's BigQuery DataSet from the Ethereum blockchain this package will evaluate the top 10 most popular collectibles (ERC-721 contracts), by number of transactions.  Each project will receive a ranking of confidence, so folks can have helpful data when evaluating projects.

## Requirements
* a working Python environment using Python 3.9.6 or newer

## Instructions
1. Pull the code down:  `git clone git@github.com:CodeLouisville/Data-Analytics-1-Class-Notes.git`
1. Enter project folder:
  * mac/linux/gitbash: `cd Data-Analytics-1-Class-Notes/modules/putting-it-together/mypackage`
  * windows: `cd Data-Analytics-1-Class-Notes\modules\putting-it-together\mypackage`
1. Install required Python packages:  `pip install -r requirements`
1. Execute:
  * mac/linux/gitbash:  `python ./src/main.py`
  * windows:  `python .\src\main.py`

## Expectation
(WIP) - Data will be pulled from [BigQuery](https://console.cloud.google.com/marketplace/product/ethereum/crypto-ethereum-blockchain?pli=1&project=unifi-254402), the Ethereum Blockchain will be inspected, and a chart for visualization will be displayed.

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

## Features Implemented
Category 1:
  1. Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
  1. Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code.

Category 2:
  1. TBD

Category 3:
  1. Visualize data in a graph, chart, or other visual represenation of data.

Category 4:
  1. TBD

NOTE:  While reviewing the project requirements document, I confirmed there are four categories of requirements and learned the three I originally planned on does not cover all four.  Your project will need one in each category.

# Core Python Documentation References
  * Setting up a proper Python package: https://packaging.python.org/tutorials/packaging-projects/
  * [python.org](python.org)
  * [PEP8](python.org/dev/peps)