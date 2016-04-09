## Usage of process.py
    
convert CFI commodity price data to a data package resource
    
### Reqirements

Data preperation requires Python 2.
Also needs xlrd module to be installed for Python

Install with pip:
```
$ pip install xlrd
```
Or Follow this link for download: https://pypi.python.org/pypi/xlrd

### Processing

Run the following script from dataset's directory (in this case /commodity-prices) to download and process the data:

```bash
make data
```

The processed data is output to ../data
