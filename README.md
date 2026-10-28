# P1 — Linear Congruential Generator (LCG) Web Project

## Overview
An interactive Streamlit web application that demonstrates the Linear Congruential Generator recurrence:

`X_(n+1) = (a * X_n + c) % m`

It includes parameter inputs, a step-by-step sequence table, normalized values, a chart, full-cycle/period analysis, CSV export, validation, and a security warning.

## Requirements
- Python 3.10 or newer
- Packages listed in `requirements.txt`

## Run locally
1. Install Python.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended):
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the website: `streamlit run app.py`
6. Open the local URL printed in the terminal, usually `http://localhost:8501`.

## Example
Use `X0=7`, `a=5`, `c=3`, `m=16`, count `8`.
The generated values are: `6, 1, 8, 11, 10, 5, 12, 15`.

For these parameters, the recurrence has a full cycle of length 16 when starting from seed 7? The exact cycle is calculated by the app; do not assume a full period from the first eight displayed values.