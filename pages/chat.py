
import streamlit as st



add_sidebar_title = st.sidebar.write("Welcome to FinBudIO")

add_divider = st.sidebar.divider() 
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/visualize.py", label="Visualize data")
st.sidebar.page_link("pages/chat.py", label="Chat with data")

st.header('Chat with your data', divider='blue')
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("This feature will coming out soon"):
    # Display user message in chat message container
    # with st.chat_message("user"):
    #     st.markdown(prompt)
    # Add user message to chat history
    # st.session_state.messages.append({"role": "user", "content": prompt})
    pass

prompt="Meet FinChatBot, your personalized financial assistant designed to make managing your finances a breeze. \
    With FinChatBot, you can interact directly with your financial data, gaining insights and advice tailored to your unique financial situation. \
        Whether you're planning for retirement, budgeting for a major purchase, or just trying to stay on top of your daily expenses, \
            FinChatBot is here to provide expert guidance and support. Say goodbye to financial uncertainty and hello to a smarter, more informed approach to managing your money"
response = f"**FinChatBot**: {prompt}"
# Display assistant response in chat message container
with st.chat_message("assistant"):
    st.markdown(response)
# Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": response})