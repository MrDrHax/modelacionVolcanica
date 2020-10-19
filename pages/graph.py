import pages.pandasMannager as pandasMannager
import streamlit as st
from os import walk

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from time import sleep

def page():
    st.title('Run the graphs you have saved!')
    
    f = []
    for (dirpath, dirnames, filenames) in walk('saves'):
        for name in filenames:
            name = name.replace('.json','')
            f.append(name)
        break

    option = st.selectbox(
        'What project do you want to run?',
        tuple(f))
    
    dataframes, info = pandasMannager.loadFromJSON(option)

    timeFrame = st.slider('launch simulation at time:',min_value=float(info['rangeInTime'][0]), max_value=float(info['rangeInTime'][1]), value=0.0,step=float(info['delta_t']))

    pos = int(timeFrame * (1/info['delta_t']))

    # plot

    plotThingy = st.pyplot(plt)

    plot(dataframes, pos,plotThingy)

    st.text(pos)

    st.text(info)

    for i in dataframes:
        st.dataframe(i)

def plot(dataframes, pos, plotThingy):
    if pos == 0:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for point in range(len(dataframes)):
            xs = dataframes[point]['x']
            zs = dataframes[point]['y']
            ys = dataframes[point]['z']
            ax.plot(xs, ys, zs)

        ax.set_xlabel('X ')
        ax.set_ylabel('Z ')
        ax.set_zlabel('Y ')

        ax.set_xlim3d(-5000,5000)
        ax.set_ylim3d(-5000,5000)
        ax.set_zlim3d(0,10000)

        plotThingy.pyplot(plt)
    
    else:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for point in range(len(dataframes)):
            xs = dataframes[point]['x'][pos]
            zs = dataframes[point]['y'][pos]
            ys = dataframes[point]['z'][pos]
            ax.scatter(xs, ys, zs, marker='^')

        ax.set_xlabel('X ')
        ax.set_ylabel('Z ')
        ax.set_zlabel('Y ')

        ax.set_xlim3d(-5000,5000)
        ax.set_ylim3d(-5000,5000)
        ax.set_zlim3d(0,10000)

        plotThingy.pyplot(plt)