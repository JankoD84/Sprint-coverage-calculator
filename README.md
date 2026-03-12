# Sprint Coverage Calculator

A planning tool that compares **team capacity** against **planned sprint scope** (in Story Points) to determine whether a sprint is realistically covered, underloaded, or overloaded.

## Assumption

> **1 Story Point = 4 hours of work**

---

## Project Structure

```
Sprint-coverage-calculator/
├── calculator.py       # Core calculation logic (shared by both frontends)
├── sprint_cli.py       # Interactive CLI version
├── sprint_app.py       # Streamlit web app version
├── requirements.txt    # Python dependencies
└── README.md
```

---

## How It Works

### Inputs

| Input | Description |
|---|---|
| Sprint length (days) | Total calendar length of the sprint |
| Working days | Actual days the team works (no holidays) |
| Team members | Number of people contributing Story Points |
| Productive hours/day | Focused hours per person per day |
| Availability % | Team availability (leave, part-time, etc.) |
| Buffer % | Reserve for unexpected work / incidents |
| Planned Story Points | Total SP of all tickets in the sprint |

### Formulas

```
Team Capacity (h)         = members × working_days × hours/day × (availability / 100)
Capacity After Buffer (h) = team_capacity × (1 − buffer / 100)
Capacity in SP            = capacity_after_buffer / 4
Coverage %                = (planned_SP / capacity_SP) × 100
Remaining Capacity SP     = capacity_SP − planned_SP
```

### Status Rules

| Coverage | Status | Meaning |
|---|---|---|
| < 80% | Underloaded Sprint | Free capacity remains |
| 80 – 100% | Healthy Sprint Load | Realistic and achievable |
| > 100% | Overloaded Sprint | Scope exceeds capacity |

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

### CLI

```bash
python sprint_cli.py
```

Example output:

```
========================================
   Sprint Coverage Calculator
========================================
Please enter the sprint details below.

Sprint length (days, e.g. 10 for a 2-week sprint): 10
Working days in the sprint (≤ 10): 10
Number of team members: 5
Productive hours per person per day (e.g. 6): 6
Team availability percentage (e.g. 80 for 80%): 80
Buffer percentage for unexpected work (e.g. 15 for 15%): 15
Planned sprint scope in Story Points: 40

Sprint Coverage Summary
----------------------------------------
Team Capacity (hours)         : 240.0 h
Capacity After Buffer (hours) : 204.0 h
Capacity in Story Points      : 51.0 SP
Planned Sprint Scope          : 40.0 SP
Coverage                      : 78.4%
----------------------------------------
Status  : Underloaded Sprint
Detail  : The sprint has extra free capacity.
----------------------------------------
Remaining Capacity  : 11.0 SP  (free capacity)
----------------------------------------

Note: This calculator is a planning aid. Story points are relative estimates
and should support discussion, not replace team judgment.
```

### Streamlit Web App

```bash
streamlit run sprint_app.py
```

Then open **http://localhost:8501** in your browser.

---

## Disclaimer

This calculator is a planning aid. Story points are relative estimates and should support discussion, not replace team judgment.
