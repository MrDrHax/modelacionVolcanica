import pages.pandasMannager as pandasMannager
import pages.dataCreator as data
import streamlit as st

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def page():
    st.title("Welcome")

    st.markdown("Today we are gonna learn how a projectile's spped affects its treajectory, follow the page to see what changes are made to projectiles.")

    st.header("Part 1, projectile speeds:")

    st.markdown("Depending on the launch speed, is how fat the projectuile will reach")

    plot1 = data.plotter(3,False,(100,100,0),(50,50,0),(10,10),0)

    plot1.plot2D()

    st.markdown(f"As you can see, above, there are 3 different launches, each with different variables, line 0 had a launch speed of {math.sqrt(plot1.lines[0].x_velocity[0] ** 2 + plot1.lines[0].y_velocity[0] ** 2)} $m/s$ at an angle of {math.degrees(math.atan(plot1.lines[0].x_velocity[0]/plot1.lines[0].y_velocity[0]))} degrees, the line 1 had an initial velocity of {math.sqrt(plot1.lines[1].x_velocity[0] ** 2 + plot1.lines[1].y_velocity[0] ** 2)} $m/s$at an angle of {math.degrees(math.atan(plot1.lines[1].x_velocity[0]/plot1.lines[1].y_velocity[0]))} degrees, and the last line had a speed of {math.sqrt(plot1.lines[2].x_velocity[0] ** 2 + plot1.lines[2].y_velocity[0] ** 2)} $m/s$at an angle of {math.degrees(math.atan(plot1.lines[2].x_velocity[0]/plot1.lines[2].y_velocity[0]))} degrees.")

    st.markdown("As you can see, we have multiple values that we can give a parabolic line to throw a projectile. This includes angle, and launch speed. \nNext up, try launching one yourself!")

    initialVel = st.slider("initial velocity",10,1000,20,5)
    angle = st.slider("launch angle",0,90,45,5)

    speed = (int(initialVel * math.cos(math.radians(angle))),int(initialVel * math.sin(math.radians(angle))),0)

    plot2 = data.plotter(1,False,speed,speed,(10,10),0)
    plot2.plot2D()

    st.header("Part 2, getting components")

    st.markdown("Another way to see the graph is to look at different objects, more specifically, the X and Y components of the line. To get these, we use the formulas:")
    st.latex("initial x vel = {magnitude} \cdot {cos(angle)}")
    st.latex("initial y vel = {magnitude} \cdot {sin(angle)}")

    st.markdown("From here, we continue our adventure through geting the rest of the line, since we do not expect a change in spped from the x component, we try to use a uniform rectilinear motion, or URM, while on the y component, we see that the acceleration changes depending on the point in time. \nTo get these formulas, we will need a new measure, gravity, and time:")
    st.text("on the x component:")
    st.latex("x = distance")
    st.latex("t = time")
    st.latex("v = velocity")
    st.text("and we get the following formula:")
    st.latex("x = {v} \cdot {t}")
    st.text("on the y component:")
    st.latex("\Delta y = distance")
    st.latex("t = time")
    st.latex("v_{o} = initialvelocity")
    st.latex("a = acceleration(gravity)")
    st.latex("h = initialheight")
    st.text("and to get the position where y is on a certain point, we use:")
    st.latex("\Delta y = v_{o}t + ({1}/{2}) at^2 + h")

    st.header("Part 3, using drag")

    st.markdown("To start using drag, we first need to understand how drag works. Drag, while it looks like a simple task, requires much more than just an easy coeficient to reduce. The best way to do so, is to take into account one important thing, drag is a force, that goes against the main force.")
    st.text("figure 1")
    st.image("images/fig1.png")

    st.markdown('As we can see, the drag force makes the ball go back, just a bit, but there is still a problem, how do we calculate the next problems?\nWell, there is an easy solution, use a timeframe, where you can make each jump in time, and calculate each point.')

    st.text('figure 2')
    st.image("images/fig2.png")

    st.markdown('However, as we can see on figure 2, this method is not prefect, and it may require a lot of datapoints for it to be the most acurate, meaning that we either have to use tremendus computation power, or in general, get a different approach.')

    st.subheader('Velocity Verlet')

    st.markdown("")

