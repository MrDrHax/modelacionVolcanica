import streamlit as st
import time
import pages.dataCreator as dataCreator 
import pages.pandasMannager as pandasMannager

class tcolour:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'
    YELLOW = '\033[93m'
    GRAY = '\033[90m'
    PURPLE = '\033[95m'
    LIGHTBLUE = '\033[96m'
    RESET = '\u001b[0m'

def page():
    st.title('The omega cool thing of volcano madness')

    fila1,fila2,fila3 = st.beta_columns(3)

    with fila1:
        st.text('time variables')
        delta_t = st.slider('delta t(s):',min_value= 0.01 ,max_value= 1.0,step= 0.01, value= 0.02)
        rangeInTime = (0.0,st.slider('range in time(s):',min_value= 1 ,max_value= 1000,step= 1, value= 60)) 

    with fila2:
        st.text('mod variables')
        densityRho = st.slider('density (rho, kg/m^3):',min_value= 0.01 ,max_value= 5.0,step= 0.01, value= 1.29)
        gravity = st.slider('gravity (m/s^2):',min_value= 0.01 ,max_value= 20.0,step= 0.01, value= 9.8)
        dragCoeficient = st.slider('drag coeficient:',min_value= 0.01 ,max_value= 5.0,step= 0.01, value= 0.45)

    dataCreator.updateBaseData(delta_t,rangeInTime,densityRho,dragCoeficient,gravity)

    with fila3:
        st.text('line variables')
        doLines = st.checkbox('create extra lines?', True)

        amountOfLines = st.number_input('amount of lines:',min_value=1,max_value=100000,value=1,step=1)

        st.text('Be cautios with \namount of lines, \nmany lines requiere \nmore computing power')

    st.subheader('launch speeds:')

    x,y,z = st.beta_columns(3)

    minInitialVel = [0,0,0]
    maxInitialVel = [0,0,0]

    with x:
        st.text('X velocity')
        minInitialVel[0] = st.number_input('minimum X velocity(m/s):',min_value=-100000,max_value=100000,value=100,step=1)
        maxInitialVel[0] = st.number_input('maximum X velocity(m/s):',min_value=minInitialVel[0],max_value=100000,value=minInitialVel[0],step=1)

    with y:
        st.text('Y velocity')
        minInitialVel[1] = st.number_input('minimum Y velocity(m/s):',min_value=-100000,max_value=100000,value=100,step=1)
        maxInitialVel[1] = st.number_input('maximum Y velocity(m/s):',min_value=minInitialVel[1],max_value=100000,value=minInitialVel[1],step=1)

    with z:
        st.text('Z velocity')
        minInitialVel[2] = st.number_input('minimum Z velocity(m/s):',min_value=-100000,max_value=100000,value=0,step=1)
        maxInitialVel[2] = st.number_input('maximum Z velocity(m/s):',min_value=minInitialVel[2],max_value=100000,value=minInitialVel[2],step=1)

    rangeInArea = [0.0,0.0]

    st.subheader('launch weights:')

    minRangeSurface, maxRangeSurface = st.beta_columns(2)

    with minRangeSurface:
        st.text('range in area')
        rangeInArea[0] = st.slider('minimum range(m): ',min_value= 0.1 ,max_value= 5.0,step= 0.01, value= 0.1)
        rangeInArea[1] = st.slider('minimum range(m):',min_value= rangeInArea[0] ,max_value= 5.0,step= 0.01, value= 0.1, key='lol')
        '_do not make max less than min!!!_'

    with maxRangeSurface:
        st.text('aditional variables')
        dataCreator.densityOfRock = st.slider('density of rock:',min_value= 100 ,max_value= 10000,step= 100, value= 2600)
        '_in kg/m^3_'


    line1 = dataCreator.plotter(amount= amountOfLines , doParabolicLines= doLines, maxForceRange= tuple(maxInitialVel),minForceRange= tuple(minInitialVel), areaRange=tuple(rangeInArea))

    line1.plotWithWeb()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")

    toConvert = []
    print(tcolour.RESET)
    for i in range(len(line1.lines)):
        filler = []
        filler.append(line1.lines[i].x)
        filler.append(line1.lines[i].y)
        filler.append(line1.lines[i].z)

        filler.append(line1.lines[i].x_velocity)
        filler.append(line1.lines[i].y_velocity)
        filler.append(line1.lines[i].z_velocity)

        filler.append(line1.lines[i].x_acceleration)
        filler.append(line1.lines[i].y_acceleration)
        filler.append(line1.lines[i].z_acceleration)

        if (doLines):
            filler.append(line1.lines[i].x_withoutDrag)
            filler.append(line1.lines[i].y_withoutDrag)
            filler.append(line1.lines[i].z_withoutDrag)

        toConvert.append(filler)

    dataframes = pandasMannager.exportToPandas(dataCreator.time, toConvert, doLines)

    for df in dataframes:
        st.dataframe(df)

    saveAsName = st.text_input('name of file (save in excel):',value='my chart', max_chars=50)
    if st.button(f'save as: "{saveAsName}.xlsx"'):
        pandasMannager.saveIntoExcel(dataframes, saveAsName)

    saveAsNameJSON = st.text_input('name of file (save in JSON, can be used later):',value='my chart', max_chars=50)
    if st.button(f'save as: "{saveAsNameJSON}.json"', key='JSON button'):
        pandasMannager.saveIntoJSON(saveAsNameJSON,dataframes, delta_t = delta_t, rangeInTime = rangeInTime, densityRho = densityRho, gravity = gravity, dragCoeficient = dragCoeficient )
