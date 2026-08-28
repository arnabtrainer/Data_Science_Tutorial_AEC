.PHONY: setup lab test verify train api
setup:
	python -m pip install -r requirements-advanced.txt
lab:
	jupyter lab
test:
	pytest -q
verify:
	python tools/verify_course.py
train:
	python -m src.production_example.train
api:
	uvicorn src.production_example.api:app --reload
