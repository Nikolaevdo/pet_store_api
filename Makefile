run:
	uvicorn app.main:app --reload
install_dep:
	poetry install
build:
	poetry build
