import spacy
import streamlit as st

# Load spaCy's pre-trained language model
nlp = spacy.load("en_core_web_sm")

# Streamlit app layout
st.title("Clinical Text Summarizer and Entity Extractor")

st.write("""
### Input your clinical text below:
""")

clinical_input = st.text_area("Clinical Text:")

if st.button("Analyze"):
    doc = nlp(clinical_input)
    
    # Extract named entities
    st.write("## Extracted Medical Entities:")
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    for entity in entities:
        st.write(f"{entity[0]} - {entity[1]}")

    # Summarize the text
    st.write("## Summary:")
    sentences = [sent.text for sent in doc.sents]
    summary = " ".join(sentences[:2])
    st.write(summary)
