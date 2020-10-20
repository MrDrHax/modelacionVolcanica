import pages.dataCreator as data
import streamlit as st

import math

def page():
    st.title("Welcome")

    st.markdown("Today we are gonna learn how a projectile's speed affects its trajectory, follow the page to see what changes are made to projectiles.")

    st.header("Part 1, projectile speeds:")

    st.markdown("Depending on the launch speed, is how fat the projectile will reach")

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

    st.markdown("From here, we continue our adventure through getting the rest of the line, since we do not expect a change in speed from the x component, we try to use a uniform rectilinear motion, or URM, while on the y component, we see that the acceleration changes depending on the point in time. \nTo get these formulas, we will need a new measure, gravity, and time:")
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

    st.markdown("To start using drag, we first need to understand how drag works. Drag, while it looks like a simple task, requires much more than just an easy coefficient to reduce. The best way to do so, is to take into account one important thing, drag is a force, that goes against the main force.")
    st.text("figure 1")
    st.image("images/fig1.png")

    st.markdown('As we can see, the drag force makes the ball go back, just a bit, but there is still a problem, how do we calculate the next problems?\nWell, there is an easy solution, use a time frame, where you can make each jump in time, and calculate each point.')

    st.text('figure 2')
    st.image("images/fig2.png")

    st.markdown('However, as we can see on figure 2, this method is not prefect, and it may require a lot of data-points for it to be the most accurate, meaning that we either have to use tremendous computation power, or in general, get a different approach.')

    st.subheader('Velocity Verlet')

    st.markdown("I will glance over the details, but in general, it is a way to get much closer to real life results, this way, we can save some computing power, and get much better results. The formula we would end up with, is a 3 part formula:")

    st.latex(r"acceleration = F_{d} \cdot \vec{V}^2")
    st.latex(r"velocity = V(t-\Delta t) + a(t-\Delta t) \cdot \Delta t")
    st.latex(r"position = V(t) \cdot \Delta t + \frac{a(t)}{2} \cdot \Delta t^2")

    st.markdown("To get the actual values, we have to separate _x_ values and _y_ values, here is an example of it")

    st.latex(r"a_x = F_{d} \cdot \vec{V}^2")
    st.latex(r"V_x = V_x(t-\Delta t) + a_x(t-\Delta t) \cdot \Delta t")
    st.latex(r"x = V_x(t) \cdot \Delta t + \frac{a_x(t)}{2} \cdot \Delta t^2")

    st.markdown("\n\n")

    st.latex(r"a_y = F_{d} \cdot \vec{V}^2")
    st.latex(r"V_y = g - V_y(t-\Delta t) + a_y(t-\Delta t) \cdot \Delta t")
    st.latex(r"y = V_y(t) \cdot \Delta t + \frac{a_y(t)}{2} \cdot \Delta t^2")

    st.markdown("In general, after doing all the things, and passing to code, our function would end up as:")

    st.code("""for i in range(1,globalArrayLength):
    x_acceleration[i] = - (dragForceCoeficient/mass) * np.sqrt(x_velocity[i-1] ** 2 + y_velocity[i-1] ** 2 + z_velocity[i-1] ** 2) * x_velocity[i-1]
    x_velocity[i] = x_velocity[i-1] + x_acceleration[i-1] * delta_t
    x[i] = x[i-1] + x_velocity[i] * delta_t + 0.5 * x_acceleration[i] * delta_t ** 2 
    
    y_acceleration[i] = - gravity - (dragForceCoeficient/mass) * np.sqrt(x_velocity[i-1] ** 2 + y_velocity[i-1] ** 2 + z_velocity[i-1] ** 2) * y_velocity[i-1]
    y_velocity[i] = y_velocity[i-1] + y_acceleration[i-1] * delta_t
    y[i] = y[i-1] + y_velocity[i] * delta_t + 0.5 * y_acceleration[i] * delta_t ** 2 
    """)

    st.markdown("We are making a for loop, to ensure that the entire code runs as an algorithm, that we always have the last one, and we run it for the entire array length. \nIf you're still wondering more about this method, [HERE](https://www.youtube.com/watch?v=g55QvpAev0I&t=9s) you can find more about it.")

    st.header("Part 4, understanding more variables")

    st.markdown("As you have probably seen, in the volcano editor, there is more than just a single initial launch, there are also many more variables such as delta t, density, drag coefficient, gravity, initial velocity, and radios. All of these variables go into D, more specifically, we use these variables to calculate the mass of the object, the coefficient of drag is also changed depending on the shape form. We can actually play with these, but for simplicity reasons, we will assume our projectile is a perfect sphere.\nNow that we know this, we can calculate both D, and get the drag coefficient. Let's start with drag coefficient, to get this value, there is no mathematical way that we know of, the only way to know it, is by testing, so using a cheat-sheet we get that drag coefficient of a sphere is around 0.45.")
    st.markdown("Okay, but what should we do now?\nWell, it's easy, the only thing to do now is calculate D. The formula for D (or drag force) is:")
    st.latex(r"\frac{\rho \cdot A \cdot C}{2}")
    st.text('where:')
    st.latex(r"C \rightarrow \text{is the drag coefficient}")
    st.latex(r"A \rightarrow \text{is the area of impact, or} \pi r^2")
    st.latex(r"\rho \rightarrow \text{is the air density. In mexico, it is equal to 1.29}")

    st.markdown("Now lets make some experiments!\nTo start off, we will start with a simple comparison, of a projectile with a initial velocity of _X_ and _Y_ of 20, the radius of the object will be of 0.2m")

    plot3 = data.plotter(1,True,(20,20,0),(20,20,0),(0.2,0.2),0)
    plot3.plot2D()

    st.markdown("As we can see, the projectile experiences loss of distance, now lets try and decrease the area to 0.01:")

    plot4 = data.plotter(1,True,(20,20,0),(20,20,0),(0.01,0.01),0)
    plot4.plot2D()

    st.markdown("Wow, the lighter it is, the more drag affects it. This also happens with free-falling objects, their maximum velocity is limited by the drag forces.\nLet's try and check if the past is real with a heavier object, this time lets give it a radius of 1m. ")

    plot5 = data.plotter(1,True,(20,20,0),(20,20,0),(1,1),0)
    plot5.plot2D()

    st.markdown("Look at that, the difference in distances is almost negligible, if you wish to continue experimenting, use the crazy editor!")

    st.markdown("One last launch to compare all of what we have done: (all projectiles are launches at the same speed and angle)")
    plot6 = data.plotter(5,True,(20,20,0),(20,20,0),(0.01,1),0)
    plot6.plot2D()

    st.markdown("Now, what else can affect out launch? \nWe can also give the throw different launch heights, lets try that!")

    height = st.slider("height",0,20,0,1)
    plot7 = data.plotter(1,True,(20,20,0),(20,20,0),(0.01,0.01),height)
    plot7.plot2D()

    st.markdown("Let's now go 3D!, what we need is a Z axis, we will treat this axis just like the X axis, but we will give it its own velocity non equal to 0:")

    plot8 = data.plotter(1,True,(20,20,20),(20,20,20),(0.01,0.01),0)
    plot8.plotWithWeb()

    st.markdown("That is great, now we got _X_, _Y_ and _Z_!\nWe can now give it it's own different set of values, for example, lets try and make it look more like a volcano... To do this, lets give the starting values a range of possible difference in _XYZ_ values. X and Z is easy, we can give them a range between a positive and a negative value, lets say +-100 m/s. To get the _Y_ value, we do not want it to go underground, so lets give it a range between 100 and 200: ")

    plot9 = data.plotter(5,False,(100,200,100),(-100,100,-100),(0.1,0.1),0)
    plot9.plotWithWeb()

    st.markdown("Okay, now let's rise our volcano... about... 3200m, the height of the Mexican volcano Popocatepetl")

    plot10 = data.plotter(5,False,(100,500,100),(-100,100,-100),(0.1,0.1),3200)
    plot10.plotWithWeb()
    plot10.plot2D()

    st.markdown("Finally, let's edit the range in possible volcano rock sizes. The maximum size of a volcano rock launched by a volcano was in Italy, with a diameter of 2m, so let's make our theoretical maximum 1m in radius, and since we do not want to count every single particle, let's make the minimum possible radius equal .1m, or 10 cm:")

    plot11 = data.plotter(5,False,(100,200,100),(-100,100,-100),(0.1,1),3200)
    plot11.plotWithWeb()

    st.markdown("I hope you have learned something new. If you wish to try more possibilities, go to the crazy volcano editor, there, you will be able to change every single value this code has to offer.")
