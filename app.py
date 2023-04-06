import streamlit as st
from transformers import pipeline

# Initialize the question-answering pipeline with a pre-trained model
qa_pipeline = pipeline("question-answering")

# Define the question and context
question = st.text_input("Enter your question here:")
context = st.text_area("Enter the context here:")

# Run the pipeline
if st.button('Get Answer'):
    result = qa_pipeline(question=question, context=context)
    # Print the result
    st.write(result)