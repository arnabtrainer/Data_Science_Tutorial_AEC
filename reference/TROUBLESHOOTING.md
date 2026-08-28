# Troubleshooting Guide

## Notebook state
**Symptom:** a variable exists only after running unrelated cells.  
**Fix:** restart kernel, Run All, then move initialization into the notebook or a shared import.

## File paths
**Symptom:** dataset not found.  
**Fix:** launch Jupyter from the extracted course root. The setup cell walks parent directories, but isolated notebook copies are unsupported.

## Environment
**Symptom:** imports differ across terminal and notebook.  
**Fix:** inspect `sys.executable` in the notebook and install/use the matching kernel.

## Pandas
- `SettingWithCopyWarning`: create an explicit `.copy()` and assign with `.loc`.
- Unexpected merge row growth: inspect key duplicates and use `validate=` in `merge`.
- Date parsing failures: use `errors="coerce"` only when the invalid-date policy is explicit.

## Machine learning
- Suspiciously strong validation: investigate leakage and split identity.
- CV fails on categories: use `OneHotEncoder(handle_unknown="ignore")`.
- Accuracy is high but positives are missed: inspect prevalence, recall, PR-AUC, and threshold.
- Results change greatly by seed: quantify variability and simplify or gather data.
- Train score high, validation low: reduce capacity, regularize, inspect leakage/distribution, gather data.

## Deep learning
- Loss is NaN: inspect input ranges, labels, learning rate, loss use, and gradients.
- Loss does not decrease: overfit one tiny batch; verify shapes, optimizer step, and labels.
- Validation changes under repeated evaluation: call `model.eval()` and use `torch.no_grad()`.
- Shape mismatch: print/annotate every tensor shape from batch to logits.
- Memory problems: reduce batch size, resolution, sequence length, or model capacity.

## MLOps
- Training and API disagree: compare complete preprocessing/feature code and schema versions.
- Model loads locally only: pin runtime/package versions and containerize the artifact.
- Drift alert fires without impact: connect it to outcomes, score behaviour, and operational action.
- Rollback is unclear: keep immutable prior artifacts and define release ownership before launch.
