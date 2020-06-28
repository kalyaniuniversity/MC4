# Test Datasets for MC4


These are some test datasets to test the package. All these datasets are prepared from ranks provided by **5** different ranking algorithms on **100** different items.


| Dataset | No of rows | No of columns | Index column | Header row | Order |
|:---:|:---:|:---:|:---:|:---:|:---:|
| [test_dataset_1.csv](test_datasets/test_dataset_1.csv) | 100 | 5 | 0 | 0 | row-major |
| [test_dataset_2.csv](test_datasets/test_dataset_2.csv) | 5 | 100 | 0 | 0 | column-major |
| [test_dataset_3.csv](test_datasets/test_dataset_3.csv) | 100 | 5 | None | 0 | row-major |
| [test_dataset_4.csv](test_datasets/test_dataset_4.csv) | 5 | 100 | None | 0 | column-major |
| [test_dataset_5.csv](test_datasets/test_dataset_5.csv) | 100 | 5 | 0 | None | row-major |
| [test_dataset_6.csv](test_datasets/test_dataset_6.csv) | 5 | 100 | 0 | None | column-major |
| [test_dataset_7.csv](test_datasets/test_dataset_7.csv) | 100 | 5 | None | None | row-major |
| [test_dataset_8.csv](test_datasets/test_dataset_8.csv) | 5 | 100 | None | None | column-major |


*****row-major** means rank holders or **items** are in **rows** and rank providers or **lists** are in **columns***
*****column-major** means rank holders or **items** are in **columns** and rank providers or **lists** are in **rows***