# How to install

First time only:
1. Install miniconda (don't add to PATH)
2. Open Anaconda Powershell Promt (on Windows) and install [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
3. Add poetry to PATH

To install project dependencies:

1. Create new conda environment
```
conda create --name env-flight-route-planner
```
2. Activate new environment
```
conda activate env-flight-route-planner
```
3. Install python in the environment
```
conda install python=3.9
```
4. Install poetry packages
```
poetry install
```

To add a new package:
```
poetry add pandas
```

