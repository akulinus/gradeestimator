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
    for module in st.session_state.module:
        st.write(f"{module['Modulname']} – {module['ECTS']} ECTS – Note {module['Note']}")


# TODO: Write method that calculates median of examined subjects 


def calculateModuleSum(passedModules):
    # calculate ECTS and grade
    for module in passedModules: 
        modulesSum += module['ECTS'] * module['Note']
    return modulesSum

def calculateCreditSum(passedModules):
    # calculate ECTS 
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
    passedModules = storePassedModules()
    gradeGoal = storeGradeGoal()
    passedMedian = calculatePassedMedian()
    moduleSum = calculateModuleSum()
    creditSum = calculateCreditSum()
    creditsLeft = 180 - creditSum


    # calculate Median to achieve goal 
    neededMedian = (creditSum * passedMedian - 180 * gradeGoal) / creditsLeft



# TODO: Write method that computes acchievability of goal 
def goalAchievability(neededMedian, passedMedian): 
    match neededMedian: 
        case n if n < 1.0:
            print("Ziel nicht erreichbar.")
        case n if n <= 1.7:
            print(f"Ziel unwahrscheinlich erreichbar. Benötigter Durchschnitt in Zukunft ist {neededMedian}")
        case n if n <= 2.5: 
            print(f"Ziel wahrscheinlich erreichbar. Benötigter Durchschnitt in Zukunft ist {neededMedian}")
        case n if n <= 4.0: 
            print(f"Ziel sehr wahrscheinlich erreichbar. Benötigter Durchschnitt in Zukunft ist {neededMedian}")
        case n if n > 4.0: 
            print(f"Ziel ist bereits erreicht.")


    



