import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import about, data_viz, ml

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Demo for the paper:")
st.subheader("Comparative analysis of performance of Machine Learning and Transfer Learning models in detecting hate on Twitter")
# Add all your applications (pages) here
app.add_page("About the Project", about.app)
app.add_page("Machine Learning", data_viz.app)
app.add_page("Conclusion of the paper", ml.app)


# The main app
app.run()