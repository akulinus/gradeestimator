# /// creditestimator
# Input: passed subjects and their ects, to be examined subjects and their ects, ranking of subjects that may rank better or worse, grade goal
# Output: grade so far and overall grade needed to achieve goal 
# ///

import streamlit as st    

# UI Functions 
def storeGradeGoal(): 
    goal = st.number_input("Zielschnitt", 1.0, 4.0)
    return goal 

def storePassedModules():
    if "module" not in st.session_state:
        st.session_state.module = []

    # information about new module
    module = st.text_input("Name des Moduls", key="module_input")
    ects = st.number_input("ECTS", 1, 30, key="ects_input")      
    grade = st.number_input("Note", 1.0, 4.0, key="grade_input")   

    # Add new Module - Button
    if st.button("Modul hinzufügen"):
        st.session_state.module.append({
            "Modulname": module,
            "ECTS": ects,
            "Note": grade
        })

    # Show List
    for modul in st.session_state.module:
        st.write(f"{modul['Modulname']} – {modul['ECTS']} ECTS – Note {modul['Note']}")   
    return st.session_state.module      


# calculations 
def calculateModuleSum(passedModules):
    # calculate ECTS and grade
    modulesSum = 0
    for module in passedModules: 
        modulesSum += module['ECTS'] * module['Note']
    return modulesSum

def calculateCreditSum(passedModules):
    # calculate ECTS 
    ectsSum = 0
    for module in passedModules: 
        ectsSum += module['ECTS']
    return ectsSum

def calculatePassedMedian(passedModules): 
    #calculate median 
    passedMedian = calculateModuleSum(passedModules) / calculateCreditSum(passedModules)
    return passedMedian 

 
def calculateNeededMedian(gradeGoal, passedModules): 
    passedMedian = calculatePassedMedian(passedModules)
    creditSum = calculateCreditSum(passedModules)
    creditsLeft = 180 - creditSum

    # calculate Median to achieve goal 
    neededMedian = (180 * gradeGoal - creditSum * passedMedian) / creditsLeft
    return neededMedian


def goalAchievability(neededMedian): 
    match neededMedian: 
        case n if n < 1.0:
            st.write(f"Ziel nicht erreichbar. Benötigter Durchschnitt: {neededMedian:.2f}")
        case n if n <= 1.7:
            st.write(f"Ziel schwer erreichbar. Benötigter Durchschnitt: {neededMedian:.2f}")
        case n if n <= 2.5: 
            st.write(f"Ziel machbar erreichbar. Benötigter Durchschnitt: {neededMedian:.2f}")
        case n if n <= 4.0: 
            st.write(f"Ziel sehr gut erreichbar. Benötigter Durchschnitt: {neededMedian:.2f}")
        case _: 
            st.write(f"Ziel bereits erreicht. Benötigter Durchschnitt: {neededMedian:.2f}")


# Main-Methode 
def main(): 
    passedModules = storePassedModules()
    gradeGoal = storeGradeGoal()

    if passedModules:
        passedMedian = calculatePassedMedian(passedModules)
        neededMedian = calculateNeededMedian(gradeGoal, passedModules)
        st.write(f"Aktueller Notendurchschnitt: {passedMedian:.2f}")
        goalAchievability(neededMedian)



main()