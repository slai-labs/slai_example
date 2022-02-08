#! /bin/bash
set -e

#ensure the following environment variables are set. SLAI_PROJECT_URL, SLAI_CLIENT_ID, SLAI_CLIENT_SECRET
if [ -z "$SLAI_PROJECT_URL" ]; then
  echo "SLAI_PROJECT_URL is not set"
  exit 1
fi

if [ -z "$SLAI_CLIENT_ID" ]; then
  echo "SLAI_CLIENT_ID is not set"
  exit 1
fi

if [ -z "$SLAI_CLIENT_SECRET" ]; then
  echo "SLAI_CLIENT_SECRET is not set"
  exit 1
fi

export FLASK_APP=app
export FLASK_ENV=development

flask run --port=4242