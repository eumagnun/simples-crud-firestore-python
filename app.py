
import streamlit as st
from services.service_firestore import save_feedback
import datetime


def save(modulo ,feature, sentiment, comment):
    save_feedback(modulo ,feature, sentiment, comment)
    st.info("Feedback salvo")
  

with st.popover("Avaliar"):
    sentiment_mapping = ["Ruim", "Bom"]
    sentiment_selected = st.feedback("thumbs",key="feedback_sentiment1")
    if sentiment_selected is not None:
        st.markdown(f"You selected: {sentiment_mapping[sentiment_selected]}")
        comment = st.text_input(label="Comente por favor...")
        if st.button("Salvar"):
            save("modulo1", "feature-chat",sentiment_mapping[sentiment_selected], comment)
            st.rerun()


  
@st.dialog("Avaliar")
def vote():
    sentiment_mapping = ["Ruim", "Bom"]
    sentiment_selected = st.feedback("thumbs")
    if sentiment_selected is not None:
        st.markdown(f"You selected: {sentiment_mapping[sentiment_selected]}")
        comment = st.text_input(label="Comente por favor...")
        if st.button("Salvar"):
            save("modulo1", "feature-chat",sentiment_mapping[sentiment_selected], comment)       
            st.rerun()


st.write(datetime.datetime.now(tz=datetime.timezone.utc))

if st.button("A"):
   vote()