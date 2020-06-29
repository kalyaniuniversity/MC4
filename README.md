# Markov Chain Type 4 Rank Aggregation
**implementation of MC4 Rank Aggregation algorithm using Python**

### Description

This project is all about implementing one of the most popular rank aggregation algorithms **Markov Chain Type 4** or **MC4**. In the field of Machine Learning and many other scientific problems, several items are often needed to be ranked based on some criterion. However, different ranking schemes order the items based on different preference criteria. Hence the rankings produced by them may differ greatly.

Therefore a rank aggregation technique is often used for combining the individual rank lists into a single aggregated ranking. Though there are many rank aggregation algorithms, MC4 is one of the most renowned ones.

## Resource

*Links to the original contents*

* [Rank Aggregation methods for Web: PDF](https://dl.acm.org/doi/pdf/10.1145/371920.372165)
* [Rank Aggregation methods for Web: web version](http://www10.org/cdrom/papers/577/)


## Installation

For the latest release, `pip install mc4`

For a specific release,`pip install mc4=={version}` such as `pip install mc4==1.0.0`

## Usage

Using this package is very easy. You just need the following three lines of code to use the package.

```python
from mc4.algorithm import mc4_aggregator

aggregated_ranks = mc4_aggregator('dataset.csv') 

# or 

aggregated_ranks = mc4_aggregator(df) 

print(aggregated_ranks)
```
here `dataset.csv` or `df` are lists of ranks provided by different ranking algorithms or rank lists. *You can refer [here](test_datasets/datasets.md) for more info and some test datasets.*

`mc4_aggregator` takes some additional arguments as well.

* `order (string)`: order of the dataset, default is `'row'`. More on this, [here](test_datasets/datasets.md).
* `header_row (int or None)`: row number of the dataset containing the header, default is `0`
* `index_col (int or None)`: column number of the dataset containing the index, default is `0`
* `precision (float)`: acceptable error margin for convergence, default is `1e-07`
* `iterations (int)`: number of iterations to reach stationary distribution, default is `200`
* `erg_number (float)`: small, positive number used to calculate ergodic transition matrix, default is `0.15`

## Output

Output of `mc4_aggregator` will be a list of itemwise aggregated ranks such as if the output is [5, 2, 4, 6] then 5 is the aggregated rank of item 0, 2 is the aggregated rank of item 1 and so on.

## Reference
* For full documentation, please visit [Documentation Wiki](https://github.com/kalyaniuniversity/MC4/wiki)
* To report issues or request a feature, please visit [Issues](https://github.com/kalyaniuniversity/MC4/issues)
* Follow author, Ayan Kumar Saha - [GitHub](https://github.com/Ayan-Kumar-Saha) | [LinkedIn](https://www.linkedin.com/in/ayankumarsaha/)

### Upcoming features
* command line support