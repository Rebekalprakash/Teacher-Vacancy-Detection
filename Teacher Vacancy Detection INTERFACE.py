import streamlit as st
import pickle
import numpy as np


st.title("TEACHER VACANCY DETECTION")
with open(r'C:\Users\LENOVO\rebe.pkl', 'rb') as file:
    dfc= pickle.load(file)

    #a=st.selectbox("Enter District Your Options are:(MADURAI,TIRUNELVELI,THOOTHUKUDI,THANJAVUR,ERODE,COIMBATORE,KANCHEEPURAM,KARUR,SALEM,KANYAKUMARI,NAGAPATINAM,THENI,NAMAKKAL,DHARAMAPURI,CUDDALORE,THIRUVARUR,ARIYALUR,TENKASI,CHENGALPATTU,DINDIGUL")
    

    a = st.selectbox('Enter District Name:',('MADURAI','TIRUNELVELI','THOOTHUKUDI','THANJAVUR','ERODE','COIMBATORE','KANCHEEPURAM','KARUR','SALEM','KANYAKUMARI','NAGAPATINAM','THENI','NAMAKKAL','DHARAMAPURI','CUDDALORE','THIRUVARUR','ARIYALUR','TENKASI','CHENGALPATTU','DINDIGUL'))
    SUBJECT1 = st.selectbox('Select Subject:',('PHYSICS','TAMIL','CHEMISTRY','COMPUTER SCIENCE','MATHS','ENGLISH','BIOLOGY'))
    SUBJECT2 = st.selectbox('Select Subject:',('BIOLOGY','PHYSICS','CHEMISTRY','MATHS','ENGLISH','TAMIL','COMPUTER SCIENCE'))
    QUALIFICATION = st.selectbox('Select Qualification:',('M.Sc B.Ed','M.Sc','B.Sc B.Ed','B.Sc'))
    #VACANCY = st.selectbox('Yes','No')


    btn=st.button("DETECT")
    if btn==True:
        if a == 'MADURAI':
            a=0
        elif a == 'TIRUNELVELI':
             a=1
        elif a == 'THOOTHUKUDI':
             a=2
        elif a == 'THANJAVUR':
             a=3
        elif a == 'ERODE':
             a=4
        elif a == 'COIMBATORE':
             a=5
        elif a == 'KANCHEEPURAM':
             a=6
        elif a == 'KARUR':
             a=7
        elif a == 'SALEM':
             a=8
        elif a == 'KANYAKUMARI':
             a=9
        elif a == 'NAGAPATINAM':
             a=10
        elif a == 'THENI':
             a=11
        elif a == 'NAMMAKKAL':
             a=12
        elif a == 'DHARAMAPURI':
             a=13
        elif a == 'CUDDALORE':
             a=14
        elif a == 'THIRUVARUR':
             a=15
        elif a == 'ARIYALUR':
             a=16
        elif a == 'TENKASI':
             a=17
        elif a == 'CHENGALPATTU':
             a=18
        elif a == 'DINDIGUL':
             a=19

        if SUBJECT1 == 'PHYSICS':
             SUBJECT1=0
        elif SUBJECT1 == 'TAMIL':
             SUBJECT1=1
        elif SUBJECT1 == 'CHEMISTRY':
             SUBJECT1=2
        elif SUBJECT1 == 'COMPUTER SCIENCE':
             SUBJECT1=3
        elif SUBJECT1 == 'MATHS':
             SUBJECT1=4
        elif SUBJECT1 == 'ENGLISH':
             SUBJECT1=5
        elif SUBJECT1 == 'BIOLOGY':
             SUBJECT1=6

        if SUBJECT2 == 'BIOLOGY':
           SUBJECT2=0
        elif SUBJECT2 == 'PHYSICS':
             SUBJECT2=1
        elif SUBJECT2 == 'CHEMISTRY':
             SUBJECT2=2
        elif SUBJECT2 == 'MATHS':
             SUBJECT2=3
        elif SUBJECT2 == 'ENGLISH':
             SUBJECT2=4
        elif SUBJECT2 == 'TAMIL':
             SUBJECT2=5
        elif SUBJECT2 == 'COMPUTER SCIENCE':
             SUBJECT2=6

        if QUALIFICATION == 'M.Sc B.Ed':
            QUALIFICATION=0
        elif QUALIFICATION == 'M.Sc':
             QUALIFICATION=1 
        elif QUALIFICATION == 'B.Sc B.Ed':
             QUALIFICATION=2
        elif QUALIFICATION == 'B.Sc':
             QUALIFICATION=3

        pred=dfc.predict([[a,SUBJECT1,SUBJECT2,QUALIFICATION]])
        if pred==1:
            st.write("YES")
        else:
            st.write("NO")



        


        



    
    



    
    
    


