import streamlit as st



def page():
    body = """
Here you will be able to learn about the physics of projectiles in motion.

To start, click on one of the options to the left!

***
The learn page will take you into the main learning page, where interactive graphs will teach you how physics work

The load page will allow you to open saved graphs, and will allow you to test them

The volcano editor will allow you to create your own volcanoes for you to experiment with, and you will be able to export them to excel afterwards for you to experiment!
***

During this project I learned a lot. 
One of the main things I learned was that particles the size of 1 meter can't go very far up, meaning that something else has to be in play for the smoke cloud to rise that far.
I think it is a combination of the air having itself speed, and many more particles shooting at the same time.
At the same time, I feel I have a greater understanding on numpy, and how it works. 
I wanted to also add GPU support for bigger data-sets, but due to lack of knowledge, I was unable to do so, however, if I do end up knowing how, I will update this code to support it.
Thanks for sticking by, I hope you enjoy it!

I do not plan on updating this project, however, if you do have a suggestion, I can add it and give you credit.

If you are interested in checking the rest of my projects, go to [my personal web-page](https://mrdrhax.github.io/)
"""
    st.title('Hello and welcome.')
    st.markdown(body)
