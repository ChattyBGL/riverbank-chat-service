import os
import streamlit as st
from groq import Groq
# -----------------------------------------------------------------------
# HINT 1: Observability Imports
# You need `register` from `phoenix.otel` and `GroqInstrumentor` from
# `openinference.instrumentation.groq`.
# -----------------------------------------------------------------------
from phoenix.otel import register
from openinference.instrumentation.groq import GroqInstrumentor
# Method to use: register(project_name=" .", endpoint="http: /127.0.0.1:6006/v1/traces")
# Then call: GroqInstrumentor().instrument(tracer_provider=tracer_provider)
# > Write your code below:
tracer_provider = register(project_name="riverbank chat service", endpoint="http://127.0.0.1:6006/v1/traces")
GroqInstrumentor().instrument(tracer_provider=tracer_provider)

# -----------------------------------------------------------------------
# HINT 2: Environment Guard & Client Setup
# Check `os.environ.get("GROQ_API_KEY")`. If missing, use `st.error( .)`
# and `st.stop()`.
# Instantiate the Groq client: Groq(api_key= .)
# -----------------------------------------------------------------------
MODEL = "openai/gpt-oss-120b"
SYSTEM_PROMPT = (
"You are a professional banking assistant for RiverBank. "
"Provide accurate, helpful, and concise customer support."
)
st.title("🏦 RiverBank Customer Assistant")
if os.environ.get("GROQ_API_KEY") is None:
    st.error("GROQ_API_KEY environment variable not set")
    st.stop()
else:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# -----------------------------------------------------------------------
# HINT 3: Sidebar Controls (The Sampling Dials)
# Use `st.sidebar.slider( .)` to create two dials:
# 1. Temperature: range 0.0 to 2.0, default 0.2, step 0.1
# 2. Top-P: range 0.05 to 1.0, default 0.9, step 0.05
# -----------------------------------------------------------------------
st.sidebar.header("️ Sampling Dials")

temperature = st.sidebar.slider("Temperature",0.0, 2.0, 0.2, 0.1)
top_p = st.sidebar.slider("Top-P",0.05, 1.0, 0.9, 0.05)

# -----------------------------------------------------------------------
# HINT 4: Session State Management
# Check if "messages" is NOT in st.session_state.
# If not, initialize it as a list containing a dict for the system prompt:
# [{"role": "system", "content": SYSTEM_PROMPT}]
# -----------------------------------------------------------------------
# > Write your code below:

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# (Hint: Skip the message if its role is "system". For other roles, use:
# with st.chat_message(msg["role"]): st.markdown(msg["content"]))
# > Write your code below:

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]): st.markdown(msg["content"])


# -----------------------------------------------------------------------
# HINT 5: Chat Input & API Execution
# Use `if prompt = st.chat_input(" ."):`
# Inside the block:
# 1. Immediately render the user's prompt using with st.chat_message("user"): .
# 2. Append the user message dict to st.session_state.messages
# 3. Call client.chat.completions.create() passing:
# model=MODEL, messages=st.session_state.messages,
# temperature=temperature, top_p=top_p
# 4. Extract reply: response.choices[0].message.content
# 5. Render reply in assistant bubble and append to st.session_state.messages
# -----------------------------------------------------------------------
# > Write your code below:

if prompt := st.chat_input("Ask RiverBank a question..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=MODEL,
        messages=st.session_state.messages,
        temperature=temperature,
        top_p=top_p,
    )
    reply = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})


