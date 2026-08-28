# Validation Report

## Structural validation

- All 164 Jupyter notebooks parse as notebook format version 4.
- All 394 code cells compile as valid Python.
- The package contains 1,939 instructional Markdown cells.
- Required setup, data, source, test, and reference files are present.
- `verification_report.json` records the machine-readable result.

## Runtime validation

The runtime smoke harness executed every code cell in:

- 88 detailed lesson notebooks;
- 10 phase reference-solution notebooks;
- 10 fully worked capstone notebooks.

**Result: 108 of 108 runtime-tested notebooks passed.**

Representative notebooks were also executed through Jupyter kernels during generation, including statistical inference, cross-validation, explainability, anomaly detection, CNN training, Transformer components, forecasting, FastAPI contract testing, and production monitoring examples.

## Unit tests

The included test suite passes:

```text
5 passed
```

It covers common utilities, model-feature ordering, and training-frame validation.

## Scope

Exercise notebooks intentionally contain TODOs and, in their implementation workspace, may raise `NotImplementedError` until the learner completes them. Assessments and project briefs are instructional artifacts rather than worked programs. They are structurally and syntactically validated but are not counted among the 108 fully runtime-tested notebooks.

## Commands

```bash
python tools/verify_course.py
python tools/runtime_smoke_test.py lessons_1_5
python tools/runtime_smoke_test.py lessons_6_10
python tools/runtime_smoke_test.py solutions
python tools/runtime_smoke_test.py capstones
pytest -q
```
