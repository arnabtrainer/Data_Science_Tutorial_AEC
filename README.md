# Data Science, Machine Learning, Deep Learning, and MLOps Master Course

A complete, offline-first self-study package covering **beginner foundations through advanced modelling and production ML**.

## Package at a glance

- **10 structured phases**
- **88 detailed lesson notebooks**
- **10 phase overview notebooks**
- **10 guided labs**
- **10 separate reference solutions**
- **10 assessments**
- **10 separate assessment answer keys**
- **10 portfolio project briefs**
- **10 fully worked capstones**
- **5 orientation notebooks plus `START_HERE.ipynb`**
- **9 main synthetic datasets plus bundled image tensors and support files**
- **production-style Python package, tests, FastAPI service, Dockerfile, CI workflow, and verification tools**
- approximately **177.8 guided lesson hours**, excluding exercises, projects, assessments, and capstones

All core datasets are bundled and synthetic, so the main learning path does not require an internet connection.

## Start here

1. Create and activate a Python 3.11 environment.
2. Install dependencies:
   ```bash
   python -m pip install -r requirements-advanced.txt
   ```
3. Launch Jupyter from this folder:
   ```bash
   jupyter lab
   ```
4. Open `START_HERE.ipynb`.
5. Complete the environment verification and entry diagnostic.
6. Begin Phase 1 or the first phase where your diagnostic/assessment score is below 80%.

## Course structure

```text
Data_Science_ML_DL_Master_Course/
├── START_HERE.ipynb
├── 00_Course_Orientation/
├── 01_Python_Foundation/
├── 02_NumPy_and_Pandas/
├── 03_Data_Visualization/
├── 04_Statistics_and_Mathematics/
├── 05_Exploratory_Data_Analysis/
├── 06_Machine_Learning_Fundamentals/
├── 07_Supervised_Learning/
├── 08_Unsupervised_Learning/
├── 09_Deep_Learning/
├── 10_Real_World_ML_and_MLOps/
├── 11_Worked_Capstones/
├── datasets/
├── exercises/
├── solutions/
├── assessments/
├── projects/
├── templates/
├── reference/
├── src/
├── tests/
├── tools/
├── artifacts/
├── requirements-core.txt
├── requirements-advanced.txt
├── environment.yml
├── Dockerfile
├── Makefile
└── COURSE_INDEX.md
```

## Ten phases

| Phase | Focus | Outcome |
|---:|---|---|
| 1 | Python Foundation | Write clean, validated, tested, reusable Python |
| 2 | NumPy and Pandas | Manipulate numerical and tabular data correctly |
| 3 | Data Visualization | Create truthful, decision-oriented visual stories |
| 4 | Statistics and Mathematics | Reason about probability, inference, algebra, and optimization |
| 5 | Exploratory Data Analysis | Audit data and turn exploration into modelling decisions |
| 6 | ML Fundamentals | Design leakage-safe experiments, pipelines, and metrics |
| 7 | Supervised Learning | Master regression, classification, ensembles, and explanations |
| 8 | Unsupervised Learning | Validate clustering, representations, and anomalies |
| 9 | Deep Learning | Build neural networks, CNNs, recurrent models, attention, and transformers |
| 10 | Real-World ML and MLOps | Package, deploy, monitor, govern, and operate ML systems |

The complete notebook-by-notebook navigation is in [`COURSE_INDEX.md`](COURSE_INDEX.md).

## What every lesson includes

Each detailed lesson notebook contains:

1. level, study time, prerequisites, and objectives;
2. business relevance and a running case;
3. mental model and first-principles workflow;
4. operational vocabulary;
5. formal or mathematical treatment;
6. reproducible environment setup;
7. executable Python example;
8. interpretation and challenge checklist;
9. foundation, practitioner, and advanced exercises;
10. practice workspace;
11. common mistakes and safeguards;
12. knowledge-check and interview questions;
13. readiness checklist.

## Dependency choices

### Core
Python, Jupyter, NumPy, Pandas, Matplotlib, SciPy, Statsmodels, Scikit-learn, Joblib, Pytest, Nbformat, and Nbclient.

### Advanced
PyTorch, XGBoost, SHAP, Plotly, FastAPI, Uvicorn, Pydantic, and HTTPX.

The main deep-learning track uses **PyTorch**. Core visualization examples use Matplotlib and create each chart as a separate figure.

## Datasets

The package contains synthetic data for:

- student performance;
- clean and intentionally messy retail sales;
- house-price regression;
- customer churn;
- customer segmentation;
- operations anomaly detection;
- daily demand forecasting;
- text sentiment;
- small grayscale image classification.

Read [`datasets/DATA_DICTIONARY.md`](datasets/DATA_DICTIONARY.md) before using them.

## Recommended learning method

Use:

```text
Predict → Execute → Observe → Explain → Vary → Test → Transfer
```

Do not mark a notebook complete merely because every cell runs. Completion requires reconstruction, assumption analysis, edge cases, and transfer to a new scenario.

## Labs, solutions, and assessments

- Labs are under `exercises/`.
- Reference implementations are under `solutions/`.
- Assessments are under `assessments/`.
- Answer keys are separate under `solutions/`.
- Project briefs are under `projects/`.

Attempt each lab and assessment before opening its solution/key.

## Worked capstones

The worked capstones cover:

1. Retail EDA and visual storytelling
2. Statistical process comparison
3. House-price regression
4. Churn classification and thresholding
5. Customer segmentation
6. Operations anomaly detection
7. Time-aware demand forecasting
8. CNN image classification
9. Text sentiment classification
10. Production churn service

Each capstone includes scope, risk register, data/contract checks, method, evaluation, artifacts, limitations, and model/project-card prompts.

## Production example

`src/production_example/` demonstrates:

- centralized feature definitions;
- schema validation;
- a complete Scikit-learn training pipeline;
- serialization;
- batch prediction;
- a typed FastAPI service;
- tests;
- container and CI configuration.

Useful commands:

```bash
make test
make verify
make train
make api
```

On systems without `make`, run the corresponding commands shown in `Makefile`.

## Validation

Run:

```bash
python tools/verify_course.py
pytest -q
```

`verify_course.py` parses every notebook, compiles every code cell, checks required files, and writes `verification_report.json`.

A separate generated verification report is included in the final package.

## Responsible use

The datasets and outputs are educational. Do not use the bundled models for medical, employment, credit, insurance, immigration, safety-critical, or other consequential decisions.

For real systems, define governance, privacy, security, human oversight, abstention, outcome monitoring, incident response, and decommissioning before launch.

## Suggested study schedules

See [`reference/STUDY_PLANS.md`](reference/STUDY_PLANS.md) for 12-month, 24-week, and 12-week revision paths.
