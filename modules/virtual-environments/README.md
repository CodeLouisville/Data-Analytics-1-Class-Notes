# Git & Github
>Navigation:  [Home](../../README.md)

## Contents
1. [Virtual Environments Overview](#virtual-environments-overview)
2. [Demo Overview](#demo-overview)
3. [Manage Dependencies](#manage-dependencies)
## Virtual Environments Overview
A virtual environment is an isolated directory for dependencies of a specific python project to live.
It allows for easier management of project dependencies and it avoids problems with conflicting dependencies across projects.

## Demo Overview
Prerequisite: Have python installed

For shell users: (MacOS and git bash)
1. Ensure pip (a python package manager) is installed. Pip is commonly bundled with python installations. `pip install --upgrade pip`
2. Use pip to install virtualenv. `pip install --user virtualenv`*
3. Create a new virtual environment. Navigate to the directory in which you want to use the virtual environment
4. Execute `virtualenv env`. Here `virtualenv` is the create command and `env` is the name of the environment. Common naming conventions are `env` and `venv`
4. You can now "activate" the virtual environment with `source env/bin/activate`
5. To deactivate simply exectute `deactivate`
6. You can use `which python` to demonstrate which python environment you are using

*If you get a warning saying that your python 3 bin is not in your path you will need to add it to your path.
This can occur if you have both python2 and python3 installed. https://linuxhint.com/add-a-directory-to-path-in-zsh/

For Windows Powershell:
1. Ensure pip (a python package manager) is installed. Pip is commonly bundled with python installations. `py -m pip install --upgrade pip`
2. Use pip to install virtualenv. `py -m pip install --user virtualenv`
3. Create a new virtual environment. Navigate to the directory in which you want to use the virtual environment
4. Execute `py -m venv env`. `env` is the name of the environment. Common naming conventions are `env` and `venv`
4. You can now "activate" the virtual environment with `Scripts/activate`*
5. To deactivate simply exectute `deactivate`
6. You can use `where python` to demonstrate which python environment you are using

*You may need to allow scripts to run to allow this command to execute: https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

## Manage Dependencies
- To install dependencies within your virtual environment you must have the environment activated.
- You can then use `pip install <name-of-package>`
- You want to make sure that your `env`  is not commited to your git repository (see .gitignore)
- You can save your dependencies to a file called requirements.txt" like so: `pip freeze > requirements.txt`
- `pip install -r requirements.txt` will install all dependencies from `requirements.txt`
