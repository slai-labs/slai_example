#! /bin/bash
set -x -e

export FLASK_APP=server
export FLASK_ENV=development

flask run --port=4242