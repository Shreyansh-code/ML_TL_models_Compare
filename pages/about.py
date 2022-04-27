import streamlit as st
import webbrowser


def app():
    
    st.write("\n")
    
    st.markdown("##### ABOUT")
    st.write("\n")
    st.markdown('''A total of 4.48 billion people were active on social
                    media in 2021, which is an increment of 13.13 percent
                    from last year. As so many people are actively interacting
                    on social media it is a massive and very difficult task to
                    monitor everything and make sure the platform is safe to
                    use. To provide a safe environment we require to use the
                    power of Machine Learning to deal with this issue. In this
                    paper, I have trained four models on a dataset namely:
                    ”Sentiment140 dataset with 1.6 million tweets”. It
                    contains 1,600,000 tweets extracted using the Twitter API.
                    The tweets have been annotated (0 = negative, 4 =
                    positive) and they can be used to detect sentiment. Model
                    1 is a Logistic Regression model followed by the 2nd
                    model which is Neural Network. Model 3 uses transfer
                    Learning to train Bidirectional Encoder Representations
                    from Transformers (BERT) on the dataset and later we
                    modify our BERT model(Model 4) in an attempt to
                    improve our accuracy.''')
    st.write("\n")
    st.markdown("The paper for this project can be viewed by clicking on the button below:")
    url = "https://drive.google.com/drive/folders/1kpGRcgtqfdMegpJVnkoaSaoope1VWZ7A?usp=sharing"
    if st.button("Paper"):
        webbrowser.open_new_tab(url)
    st.write("\n")
    st.markdown("This paper is accepted by the International Conference On Advance Technology In Engineering (ICACITE2022)")
    st.write("\n")
    st.markdown("Developed by Shreyansh Khandelwal")
    st.markdown("Under the guidance of: Dr. M. Aruna")