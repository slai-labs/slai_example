#! /bin/bash

# check that venv is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Please activate your virtual environment first"
    exit 1
fi

python -m ipykernel install --name slai_example_venv --display-name "Slai Example Virtualenv" --prefix .venv

# set variable dir to the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export JUPYTER_CONFIG_DIR="${DIR}/.jupyter"
jupyter notebook
