# FastAPIBoilerPlate

### Locally:

1. Create a .env file and fill it with appropriate values, check dist.env about the needed attributes.
2. Use a python 3.11 environment: `poetry env use 3.11`
3. Install dependencies: `poetry install`
4. Run app: `make run_app`

### Creation of pre-commit hook

After you installed all dependencies(including dev dependencies):

1. Create `.pre-commit-config.yaml` file with your settings.
   We usually use [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
2. run `pre-commit install` to activate tour pre-commit hook
