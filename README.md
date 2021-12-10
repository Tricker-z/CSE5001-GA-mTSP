# CSE5001-GA-mTSP
This is the code repository for *Genetic Algorithm for Multiple Traveling Salesmen Project* in CES5001, Advanced Artificial Intelligence Fall 2021 in SUSTech.

## Getting Started
This project is running in Python environment.
### Prerequisites

* Python 3.x

## Run With

### Run baseline 

Python3 GA/baseline/main.py -i *filepath*

### Run VNS-GA 

Python GA/vns-ga/main.py -i *filepath*

other optimal parameters:
* -n/--pop: the number of population, 100 in default 
* -m/--sales: the number of salesmen, 5 in default

### Run IPGA 

Python GA/IPGA/main.py -i *filepath*

other optimal parameters:
* -n/--pop: the number of population, 100 in default 
* -m/--sales: the number of salesmen, 5 in default
* -t/--time: the maximum time for running, 300 in default (should be changed according to the baseline running time)


