# people-api

REST API to preform CRUD requests on Person entities in a people collection


#### Run application locally
Run `python run.py` in your terminal


### Run Unittests
Run `python -m unittest -v` in your terminal


### Generate test coverage
1. Run `coverage run -m unittest -v` in your terminal to run tests with coverage. If you have a virtual env folder (called 'env') `coverage run --omit 'env/*' -m unittest -v`.

2. Run `coverage report` in your terminal or `coverage html` to generate report in 'htmlcov' directory


#### Notes for setting up sqlite from the python REPL
`>>> from app import create_app, db`

`>>> app = create_app('dev')`

`>>> app.app_context().push()`

`>>> db.create_all()`
