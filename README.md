![Housing Estimator Screenshot](https://github.com/slai-labs/slai_example/blob/main/static/screenshot.png?raw=true)                                

## About
This is the companion app for the [Slai Get Started](https://docs.slai.io/slai/) guide. Check out a working example at [https://slai-example-app.herokuapp.com/](https://slai-example-app.herokuapp.com/)

## Setup
1. `git clone https://github.com/slai-labs/slai_example`
2. `cd slai_example`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
4. `pip install .`
5. `export SLAI_CLIENT_ID=[YOUR_SLAI_ID_HERE]` ([Slai API admin](https://www.slai.io/settings/api-keys))
6. `export SLAI_CLIENT_SECRET=[YOUR_KEY_HERE]`
7. `export SLAI_PROJECT_URL=[<EMAIL>/<PROJECT>/<BRANCH>]`
8. `./run.sh`
9. Open http://localhost:4242

## Explore
Open up a jupyter notebook to explore the model.
1. Run `./jupyter.sh`
2. Open `Model Exploration.ipynb` within Jupyter.

More info at [Slai Get Started](https://docs.slai.io/slai/)
