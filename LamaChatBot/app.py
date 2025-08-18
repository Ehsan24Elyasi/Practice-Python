import streamlit as st
import requests

st.title("🔥 LLama ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi How can I help?"}]

def call_llama(prompt):
    url = 'http://localhost:11434/v1/completions'
    data = {"model": "llama3.2", "prompt": prompt, "max_tokens": 150}
    try:
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()
        return response.json()['choices'][0]['text']
    except requests.exceptions.RequestException as e:
        return f"ERROR: {e}"

if prompt := st.chat_input("Ask anything ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    reply = call_llama(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
