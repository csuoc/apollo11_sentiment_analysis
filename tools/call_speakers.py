# IMPORT BOX

import pandas as pd
import requests

# NEIL ARMSTRONG (CDR)

def armstrong_full():
    response_arm = requests.get(url="http://127.0.0.1:9000/sql/all/CDR&CDRTRAN&CDREVA")
    armstrong_full = pd.DataFrame(response_arm.json())
    response_arm_com = requests.get(url="http://127.0.0.1:9000/sa/CDR&CDRTRAN&CDREVA")
    armstrong_compound = response_arm_com.json()
    armstrong_full["compound"] = armstrong_compound
    return armstrong_full

def armstrong_orbit():
    response_arm = requests.get(url="http://127.0.0.1:9000/sql/all/CDR")
    armstrong_orbit = pd.DataFrame(response_arm.json())
    response_arm_com = requests.get(url="http://127.0.0.1:9000/sa/CDR")
    armstrong_compound = response_arm_com.json()
    armstrong_orbit["compound"] = armstrong_compound
    return armstrong_orbit

def armstrong_tran():
    response_arm = requests.get(url="http://127.0.0.1:9000/sql/all/CDRTRAN")
    armstrong_tran = pd.DataFrame(response_arm.json())
    response_arm_com = requests.get(url="http://127.0.0.1:9000/sa/CDRTRAN")
    armstrong_compound = response_arm_com.json()
    armstrong_tran["compound"] = armstrong_compound
    return armstrong_tran

def armstrong_eva():
    response_arm = requests.get(url="http://127.0.0.1:9000/sql/all/CDREVA")
    armstrong_eva = pd.DataFrame(response_arm.json())
    response_arm_com = requests.get(url="http://127.0.0.1:9000/sa/CDREVA")
    armstrong_compound = response_arm_com.json()
    armstrong_eva["compound"] = armstrong_compound
    return armstrong_eva

# MICHAEL COLLINS (CMP)

def collins_full():
    response_collins= requests.get(url="http://127.0.0.1:9000/sql/all/CMP")
    collins_full = pd.DataFrame(response_collins.json())
    response_collins_com = requests.get(url="http://127.0.0.1:9000/sa/CMP")
    collins_compound = response_collins_com.json()
    collins_full["compound"] = collins_compound
    return collins_full

# BUZZ ALDRIN (LMP)

def aldrin_full():
    response_aldrin= requests.get(url="http://127.0.0.1:9000/sql/all/LMP&LMPTRAN&LMPEVA")
    aldrin_full = pd.DataFrame(response_aldrin.json())
    response_aldrin_com = requests.get(url="http://127.0.0.1:9000/sa/LMP&LMPTRAN&LMPEVA")
    aldrin_compound = response_aldrin_com.json()
    aldrin_full["compound"] = aldrin_compound
    return aldrin_full

def aldrin_orbit():
    response_aldrin= requests.get(url="http://127.0.0.1:9000/sql/all/LMP")
    aldrin_orbit = pd.DataFrame(response_aldrin.json())
    response_aldrin_com = requests.get(url="http://127.0.0.1:9000/sa/LMP")
    aldrin_compound = response_aldrin_com.json()
    aldrin_orbit["compound"] = aldrin_compound
    return aldrin_orbit

def aldrin_tran():
    response_aldrin= requests.get(url="http://127.0.0.1:9000/sql/all/LMPTRAN")
    aldrin_tran = pd.DataFrame(response_aldrin.json())
    response_aldrin_com = requests.get(url="http://127.0.0.1:9000/sa/LMPTRAN")
    aldrin_compound = response_aldrin_com.json()
    aldrin_tran["compound"] = aldrin_compound
    return aldrin_tran

def aldrin_eva():
    response_aldrin= requests.get(url="http://127.0.0.1:9000/sql/all/LMPEVA")
    aldrin_eva = pd.DataFrame(response_aldrin.json())
    response_aldrin_com = requests.get(url="http://127.0.0.1:9000/sa/LMPEVA")
    aldrin_compound = response_aldrin_com.json()
    aldrin_eva["compound"] = aldrin_compound
    return aldrin_eva

# PRESIDENT NIXON

def president_nixon():
    response_nixon= requests.get(url="http://127.0.0.1:9000/sql/all/NIXON")
    nixon_full = pd.DataFrame(response_nixon.json())
    response_nixon_com = requests.get(url="http://127.0.0.1:9000/sa/NIXON")
    nixon_compound = response_nixon_com.json()
    nixon_full["compound"] = nixon_compound
    return nixon_full