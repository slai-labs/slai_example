#! /bin/bash

# check that venv is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Please activate your virtual environment first"
    exit 1
fi

# Check if a kernel has not been installed for this virtual environent and if not install one.
if [ ! -f "$VIRTUAL_ENV/share/jupyter/kernels/slai_example_venv/kernel.json" ]; then
    echo "Installing kernel for local virtual environment..."
    python -m ipykernel install --name slai_example_venv --display-name "Slai Example Virtualenv" --prefix .venv
fi


# set variable dir to the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export JUPYTER_CONFIG_DIR="${DIR}/.jupyter"
jupyter notebook
