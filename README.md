# Markov Chain Type 4 Rank Aggregation
**implementation of MC4 and MCT Rank Aggregation algorithm using Python**

## Description

This project is all about implementing two of the most popular rank aggregation algorithms, **Markov Chain Type 4** or **MC4** and **MCT**. In the field of Machine Learning and many other scientific problems, several items are often needed to be ranked based on some criterion. However, different ranking schemes order the items based on different preference criteria. Hence the rankings produced by them may differ greatly.

Therefore a rank aggregation technique is often used for combining the individual rank lists into a single aggregated ranking. Though there are many rank aggregation algorithms, MC4 and MCT are two of the most renowned ones.

## Resource

*Links to the original contents*

* [Rank Aggregation methods for Web: PDF version](https://www.stat.uchicago.edu/~lekheng/meetings/mathofranking/ref/kumar.pdf)
* [Rank Aggregation methods for Web: web version](http://www10.org/cdrom/papers/577/)


## Installation

For the latest release, `pip install mc4`

For a specific release, `pip install mc4=={version}` such as `pip install mc4==1.0.0`

## General Usage

Using this package is very easy.

1. Prepare a dataset containing ranks of all the items provided by different algorithms. See [here](https://github.com/kalyaniuniversity/MC4/blob/master/test_datasets/README.md) for sample datasets and more info.

2. Use following lines of code to use the package. Make sure to pass arguments according to your dataset otherwise answers will be incorrect.

```python
from mc4.algorithm import mc4_aggregator
import pandas as pd

# Method 1
aggregated_ranks = mc4_aggregator('test_dataset_1.csv', header_row = 0, index_col = 0) 

# or Method 2
df = pd.read_csv('test_dataset_1.csv', header = 0, index_col = 0)
aggregated_ranks = mc4_aggregator(df, header_row = 0, index_col = 0) 

print(aggregated_ranks)
```
here `test_dataset_1.csv` is a sample dataset containing ranks of different items provided by different algorithms.

`mc4_aggregator` takes some mandatory and optional arguments -

* `algo (string)`: algorithm for rank aggregation, `mc4` or `mct`, default is `mc4`
* `order (string)`: order of the dataset, `row` or `column`, default is `row`. More on this, [here](https://github.com/kalyaniuniversity/MC4/blob/master/test_datasets/README.md).
* `header_row (int or None)`: row number of the dataset containing the header, default is `None`
* `index_col (int or None)`: column number of the dataset containing the index, default is `None`
* `precision (float)`: acceptable error margin for convergence, default is `1e-07`
* `iterations (int)`: number of iterations to reach stationary distribution, default is `200`
* `erg_number (float)`: small, positive number used to calculate ergodic transition matrix, default is `0.15`

## Command Line Usage

You can directly use this package from command line if you have the dataset prepared already.

* To get help and usage details,
    ```shell
    ~$ mc4_aggregator -h or --help
    ```

* Use with default settings,
    ```shell
    ~$ mc4_aggregator dataset.csv
    ```

* Specify the algorithm for rank aggregation using `-a` or `--algo`, options: `mc4` or `mct`, default is `mc4`
    ```shell
    ~$ mc4_aggregator dataset.csv -a mct
    ```

* Specify order using `-o`or `--order`, options: `row` or `column`, default is `row`
    ```shell
    ~$ mc4_aggregator dataset.csv -o column
    ```

* Specify header row using `-hr` or `--header_row`, default is `None`
    ```shell
    ~$ mc4_aggregator dataset.csv -hr 0
    ```

* Specify index column using `-ic` or `--index_col`, default is `None`
    ```shell
    ~$ mc4_aggregator dataset.csv -ic 0
    ```

* Specify precision using `-p` or `--precision`, default is `1e-07`
    ```shell
    ~$ mc4_aggregator dataset.csv -p 0.000001
    ```

* Specify iterations using `-i` or `--iterations`, default is `200`
    ```shell
    ~$ mc4_aggregator dataset.csv -i 300
    ```

* Specify ergodic number using `-e` or `--erg_number`, default is `0.15`
    ```shell
    ~$ mc4_aggregator dataset.csv -e 0.20
    ```

* All together,
    ```shell
    ~$ mc4_aggregator dataset.csv -a mct -o column -hr 0 -ic 0 -p 0.000001 -i 300 -e 0.20
    ```

## Output

Output of `mc4_aggregator` will be a dictionary containing itemwise ranks. In absence of item names, items will be represented using integers.

## Important Links
* For full documentation, please visit [Documentation Wiki](https://github.com/kalyaniuniversity/MC4/wiki)
* To report issues or request a feature, please visit [Issues](https://github.com/kalyaniuniversity/MC4/issues)
* Follow author, Ayan Kumar Saha - [GitHub](https://github.com/Ayan-Kumar-Saha) | [LinkedIn](https://www.linkedin.com/in/ayankumarsaha/)
