# Cultural-e Visualization Library - simviz

The present project makes use of a standard structure for data science projects, that aims at correctness and reproducibility. The results are multiple and comprise: an installable Python library, Jupiter notebooks and HTML reports, data clean-up scripts for the standard input data, and an effective development environment.

For more information, please refer to the homepage of the project on which this work is based: [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/).

## Requirements

```python >=3.5``` and all the libraries listed in ```requirements.txt```.

## Installation

Install ```python``` on your machine and its package manager ```pip```, then you can proceed to the installation of the requirements in ```requirements.txt``` with:

```bash
pip install -r requirements.txt
```

Consider using a ```virtualenv``` before doing this (strongly suggested).

Now you are ready to go. The ```/data``` folder contains some example data that you can cleanup with:

```bash
make data
```

and then head to the ```/notebooks``` folder and open the file ```1.0-report.ipynb``` in your [Jupiter Notebook](https://jupyter.org/) editor. Running this notebook will give a standardized set of graphs describing the main results of the simulation in the data folder.
Feel free to modify the notebook at your convenience in order to tailor the analysis to your needs.

## Project Organization

```txt
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
