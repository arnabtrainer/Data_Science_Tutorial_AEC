# Portfolio and Project Presentation Guide

A strong portfolio project demonstrates judgement, not only model variety.

## Recommended repository structure

```text
project/
├── README.md
├── pyproject.toml or requirements.txt
├── notebooks/
├── src/
├── tests/
├── configs/
├── data/README.md
├── artifacts/
├── model_card.md
└── reports/
```

## README sequence

1. Decision and user
2. Data coverage and restrictions
3. Reproduction commands
4. Baseline and evaluation
5. Main result and uncertainty
6. Error/slice analysis
7. Limitations and excluded uses
8. Architecture and artifacts
9. Monitoring and next experiment

## Presentation sequence

- One slide/minute on the decision
- One on data and leakage boundary
- One on baseline/evaluation
- Two on results and errors
- One on architecture/reproducibility
- One on limitations, risk, and next action

## Evidence reviewers value

- Correct split and preprocessing
- Clear baseline
- Reproducible package
- Tests and assertions
- Error analysis
- Honest limitations
- Decision-aware metric/threshold
- Simple architecture justified by requirements
