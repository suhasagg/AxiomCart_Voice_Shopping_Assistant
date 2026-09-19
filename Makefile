install:
	pip install -r requirements.txt
run:
	uvicorn app.main:app --reload --port 8080
test:
	pytest -q
