import streamlit as st
from PIL import Image

def app():
    st.markdown("### Conclusion of the paper")
    st.write("\n")
    st.markdown('''In this paper, we saw 3 different Machine Learning
                    models(Logistic Regression, Simple Neural Network, and
                    BERT) performance on the same dataset, Sentiment140
                    dataset with 1.6 million tweets, and were used to predict if
                    the tweets contain any kind of hate speech or have a
                    negative sentiment attached to it. Logistic regression
                    performed fairly well and gave a decent accuracy of 80%.
                    Simple Neural Network on the other hand didn’t perform as
                    well as we were expecting and only gave an accuracy of
                    79.4% on the validation set. Training BERT was a challenge
                    in itself as the process is very resource-heavy. We showed
                    5% data or 80 thousand tweets only and ran it for 3 epochs
                    and it still took almost 7 hours to train the model. Another
                    issue we noticed was overfitting. Model 2(Neural Network)
                    and Model 3(BERT) both faced this issue and we had to
                    decrease epochs and add more dropout layers to overcome
                    it. Below is a table (TABLE I) depicting the results of all the
                    models we trained. The numbers are in percentage.
                    ''')
    image1 = Image.open('C:\\Users\\shrey\\BlockTweeter\\streamLIT\\new webapp\\pages\\images\\table1.jpg')
    st.image(image1)
    st.write("\n")
    image2 = Image.open('C:\\Users\\shrey\\BlockTweeter\\streamLIT\\new webapp\\pages\\images\\table2.jpg')
    st.image(image2)
    st.write("\n")

