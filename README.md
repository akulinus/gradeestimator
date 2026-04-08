# What is the Gradeestimator ?

This is a Streamlit app that calculates the average grade needed in remaining modules to hit a selected target grade.

> Built for Bachelor students with **180 ECTS** to be achieved and a grade scale of **1.0 - 4.0**

---

## Features

- Add completed modules with their names, ECTS and grades
- Set a grade goal
- See your **current grade median**
- Get a clear answer on whether your goal is still **achievable**, and what average you need to maintain to maintain your goal

---

## How to use Gradeestimator

### Requirements

- Python 3.10+
- [Streamlit](https://streamlit.io/)

### Installation

```bash
git clone https://github.com/your-username/creditestimator.git
cd creditestimator
pip install streamlit
```

### Run the App in your terminal

```bash
streamlit run creditestimator.py
```

### Alternative: Run the App through URL 
[Gradeestimator](https://gradeestimator-by9i7wle9basxwbesvazdp.streamlit.app/)

---

## How It Works

1. **Enter your completed modules** — provide the module name, ECTS, and grade received.
2. **Set your grade goal** you want to finish your degree with
3. The app calculates:
   - Your **current grade average** across the entered modules
   - The **average grade required** in your remaining credits to achieve your goal
   - A **likelyhood of achievability**

### Achievability Scale

| Required Average | Assessment |
|---|---|
| Below 1.0 | Goal no longer achievable |
| 1.0 – 1.7 | Very hard to achieve |
| 1.7 – 2.5 | Achievable with effort |
| 2.5 – 4.0 | Very easily achievable |
| Already met | Goal already reached |

---

## Assumptions

- Total degree credits: **180 ECTS** 
- Grade scale: **1.0** to **4.0**
- all given modules contribute to the average 

---

## Project Structure

```
creditestimator/
└── creditestimator.py   # Main application
```

---

## Tests 
- to be added

## Extensions 
- to be added 
