# CULTURAL-E Data Visualization Library

The present project makes use of a standard structure for data science projects, that aims at correctness and reproducibility. The results are multiple and comprise: an installable Python library, Jupiter notebooks and HTML reports, data clean-up scripts for the standard input data, and an effective development environment.

For more information, please refer to the homepage of the project on which this work is based: [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/).

## Usage

First, you need to install Python on your machine (`v3.5` or above). Python comes preinstalled on many operating system, but you can find more information [here](https://wiki.python.org/moin/BeginnersGuide/Download).

Notice that the following instructions may vary among operating systems, and an easier solution for some of them might be using [Anaconda](https://www.anaconda.com/).

Once you get Python running on your machine, you should be ready to use also its package manager `pip` (you can find more information [here](https://pip.pypa.io/en/stable/installing/)). So let's try to install our project's dependecies.

Open a terminal in the top folder of the project (if you need help take a look [here](https://www.stugon.com/open-terminal-in-current-folder-location-mac/)), copy the following line, then press enter.

```bash
pip install -r requirements.txt
```

If you are familiar with Python, I strongly suggest yuo use a ```virtualenv``` when doing this.

The last piece of software that you need is Jupyter. You can find detailed instructions [here](https://jupyter.org/install), but it is very similar to the previous step.
Open a terminal and run the following command:

```bash
pip install jupyterlab
```

Once the command terminates, in the same terminal, run:

```bash
jupyter-lab
```

A browser tab should open with the Jupyter editor. Just navigate your folders to `/simviz/notebook/1.0-report.ipynb` and you are ready to work on the simulation report.

From now on, whenever you need Jupyter, just open a terminal and run the previous command.

## Custom Data

The /data/raw folder contains some example data from a simulation respecting the naming conventions. This is where you will have to move your simulation’s output files. Once you added your files to the folder head to the /src/data/make_dataset.py script and adapt it to the names of the new files if different. You can clean-up the data, and have it ready for the analysis, by running the following command in a terminal:

```bash
make data
```

Finally, head to the /notebooks folder and open the file 1.0-report.ipynb in your Jupiter Notebook editor. Running this notebook will output a standardized set of graphs describing the main results of the simulation in the data folder.
Feel free to modify the notebook at your convenience in order to tailor the analysis to your needs.

## Acknowledgments

**Acknowledgement of EU funding**: This project has received funding from the European Union’s Horizon 2020 research and innovation program under grant agreement n° 870072.

**Disclaimer excluding Commission responsibility**: The content of this repository does not reflect the official opinion of the European Union. Responsibility for the information and views expressed therein lies entirely with the author(s).

## License

Licensed under MIT license.
Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in this crate by you, shall be licensed as above, without any additional terms or conditions.

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
