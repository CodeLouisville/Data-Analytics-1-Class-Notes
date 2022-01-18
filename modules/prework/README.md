# Overview
This is a collection of my notes, and code while iterating through the following course links in week 1.

Course Links:
  * [Core Python: Big Picture](https://app.pluralsight.com/library/courses/6c463cc0-cb3f-43b3-be18-1372ea18cfb2)
  * [Visual Studio Code for Python Development](https://app.pluralsight.com/guides/visual-studio-code-for-python-development)
  * [Practical Python for Beginners](https://app.pluralsight.com/library/courses/162256df-2d1b-4100-9780-9a931bf22855)

Course Notes:
  * <a href="#Core Python: Big Picture">Core Python</a>
  * <a href="#Visual Studio Code for Python Development (improvement)">Visual Studio Code for Python Development</a>
  * <a href="#Practical Python for Beginners">Practical Python for Beginners</a>

# Core Python: Big Picture

### Why Python?
  - it can help anyone in just about any position
  - simple to learn
  - simple to use
  - great community
    - python.org
    - python.org/dev/peps
  - high demand
    - top 3 language world wide
  - widely used
    - web development
      - API
        - flask
        - bottle
        - pyramid
      - website
        - django
        - turbogears
        - web2py
      - CMS
        - plone
        - django-dms
        - mezzanine
    - data science
      - big data
        - tera/peta/exabyte sizes
      - machine learning
        - detect spam
        - network intrusion
        - optical recognition
        - face detection/object tracking
    - education and learning
      - used in stem
      - accepted for programming courses
      - jupyter notebooks
    - scripting
      - system
      - application

### What?
  - unique syntax
    - beautifu is better than ugly
    - readability counts
    - significant white space with the indentations can be controversial
  - generate-purpose
    - low vs high level style
  - multi-paradigm
    - structured programming
      - control structures
        - branching (if/else)
        - iterations (for/while)
      - subroutines
        - instruction grouping and code reuse (functions, methods)
    - objected oriented
    - functional programming
  - interpreted vs compiled (differences)
    - although interpreted, python does compile modules prior to execution.  See .pyc files.
  - garbage-collected
    - von Neumann Architecture (stored program computer)
      - cpu
      - memory
      - external storage
      - input/output devices
    - automatic with python
      - don't have to worry about memory leaks
      - don't have to worry about security
      - persistent data structures
  - static vs dynamic typing (differences)
    - prior to python 3 something, it was dynamic
    - now, static typing is supported

### Pros and Cons
  - Pro:  standard library
  - Pro:  community-driven via Python Enhancement Proposals aka PEPs. Checkout The Zen of Python
  - Pro:  3rd party libraries are plentiful.  Check out pypi.python.org for published packages
  - Pro:  3rd party tooling like PyDev, PyCharm, VSCode, Spyder, Sublime, Vim, Emacs, flake8, PyLint, black, v-tune suite
  - Con:  Interpreted means slow, not native means mem leaks and no sandbox, dynamic means errors ocurr at runtime


# Visual Studio Code for Python Development (improvement)
Install the Python VS Code extension at a minimum, and setup a virtual environment.  This is the bare minimum setup for Python, but is missing info on setting up virtual environments.  

I'm a fan of `miniconda` over `venv` for it's usability, but something should be in here, so students can start working.  To install miniconda, see https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation, then...
```
# conda create --name <ENV_NAME> python=<PY_VERSION>
conda create --name foobar python=3.9
conda activate foobar
```

Other suggested extensions:
* black
* prettier
* flake8
* pytest


# Practical Python for Beginners
* Data Types, Input, and Output
  * Variables and Numbers
  * Install Python
  * Tax Calculator - see [tax.py](./tax.py)
  * Strings, Inputs, and outputs
  * Age Calculator - see [decades.py](./decades.py)
* Conditionals and Imports
  * Conditionals
  * Rock, Paper, Scissors Game - see [rock_paper_scissors.py](./rock_paper_scissors.py)
  * Import Python Modules
* Lists and loops
  * Lists and Loops
  * Sum Expenses - see [expenses.py](./expenses.py)
  * Loops with range()
  * Loan Payment Calculator - see [loan.py](./loan.py)
* Dictionaries and Reading JSON
  * Dictionaries
  * Movie Schedule - see [movie_schedule.py](./movie_schedule.py)
  * Combining Lists and Dictionaries
  * Parse Nested Dictionary - see [contacts.py](./contacts.py)
  * Reading JSON and Installing packages with Pip
  * Create Python Virtual environment
    * native python
      ```
      # old by the book way
      python3 -m venv venv 
      # uncomment and use the one for your OS
      # source tutorial-env/bin/activate  # MAC
      # tutorial-env/Scripts/activate.bat  # WINDOWS

      # when done with the env
      deactivate
      ```
    * personal preference
      ```
      # install miniconda
      conda create --name foobar python=3.9
      conda activate foobar

      # when done with the env
      # conda deactivate foobar
      ```
  * Use an API - see [space_program.py](./space_program) and [weather.py](./weather.py)
* Functions
  * Functions
  * Dice Rolling Game - see [dice_game.py](./dice_game.py)
  * Add functions to Weather API module - see [weather2.py](./weather2.py)
