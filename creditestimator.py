# /// creditestimator
# Input: passed subjects and their ects, to be examined subjects and their ects, ranking of subjects that may rank better or worse, grade goal
# Output: grade so far and overall grade needed to achieve goal 
# ///

import streamlit as st    #GUI 


# TODO: Write method that stores given User informations 
def storeGradeGoal(): 
    goal = st.number_input("Zielschnitt", 1.0, 4.0)

def storePassedModules():
    # initialize Stored Modules in Dynamic List
    if "module" not in st.session_state:
        st.session_state.module = []

    # information about new module
    module = st.text_input("Name des Moduls")
    ects = st.number_input("ECTS", 1, 30)        # minimal 1, maximal 30 Credits
    note = st.number_input("Note", 1.0, 4.0)     # minimal 1.0, maximal 4.0

    # Add new Module - Button
    if st.button("Modul hinzufügen"):
        st.session_state.module.append({
            "Modulname": module,
            "ECTS": ects,
            "Note": note
        })

    # Show List
    for modul in st.session_state.module:
        st.write(f"{modul['Modulname']} – {modul['ECTS']} ECTS – Note {modul['Note']}")   
    return st.session_state.module      


# TODO: Write method that calculates median of examined subjects 


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
    # set passedModules
    passedModules = storePassedModules()
    #calculate median 
    passedMedian = calculateModuleSum / calculateCreditSum
    return passedMedian 


# TODO: Wrtie method that calculates median of future grades to achieve goal 
def neededMedian(gradeGoal, passedModules): 
    # set passedModules and gradeGoal 
    passedModules = storePassedModules(passedModules)
    gradeGoal = storeGradeGoal(passedModules)
    passedMedian = calculatePassedMedian(passedModules)
    moduleSum = calculateModuleSum(passedModules)
    creditSum = calculateCreditSum(passedModules)
    creditsLeft = 180 - creditSum


    # calculate Median to achieve goal 
    neededMedian = (creditSum * passedMedian - 180 * gradeGoal) / creditsLeft
    return neededMedian



# TODO: Write method that computes acchievability of goal 
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



def main(): 
    passedModules = storePassedModules()
    gradeGoal = storeGradeGoal()
    passedMedian = calculatePassedMedian(passedModules)
    neededMedian = neededMedian(passedModules, gradeGoal)


    st.write(f"Aktueller Notendurchschnitt: {passedMedian: .2f}")
    st.write(f"Erreichbarkeit des Zielschnittes: {goalAchievability(neededMedian): .2f}")



main()