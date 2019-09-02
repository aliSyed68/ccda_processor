## Installation
```buildoutcfg
pip install ccda-processor
```

## Usage
```python
import ccda_processor
processsor = ccda_processor.CCDA('{path to input file}','{path to output directory}')
processsor.convert()
```

## Sample output
```buildoutcfg
processing...
finished...
total count of patient records: 2987
```


## Uninstall
```buildoutcfg
pip uninstall ccda-processor
```