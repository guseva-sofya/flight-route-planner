# flight-route-planner

![build-lint-test-workflow](https://github.com/guseva-sofya/flight-route-planner/actions/workflows/lint_and_test.yml/badge.svg)

## Introduction

In this program I build a flight route planner that uses a graph algorithm (Dijkstra's algorithm) to find the shortest route between two airports. I implement algorithm creating classes, using the clean coding practices, unit testing and setting a CI/CD workflow on a GitHub.

A simplified scheme of a bidirectional graph represents connections between the airports:

![graph](https://github.com/guseva-sofya/flight-route-planner/images/graph.jpg)

where, A &rarr; C &rarr; F &rarr; B - the fastest route between A and B. Numbers above the arrows indicate the weights (time in hours).

## How to install

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

## Static analysis:

To run static type/annotation analysis:
```
mypy .
```

To run linter statis analysis:
```
pylint flight_route_planner tests 
```

Run the tests:
```
pytest tests
```

To update conda, run Anaconda Powershell Prompt from admnistrator.
 ```
 conda update --all
 ```
 This will update conda and Python in its current package (3.8 -> to the latest version in 3.8).
 To update python in conda completely you need to run: 
 ```
 conda install python=3.10
 ```

 To run all static checks and unit tests in one go, use this command:
 ```sh
./run_checks.sh
 ```

 ## Materials used creating this project

 1. https://www.youtube.com/watch?v=pVfj6mxhdMw