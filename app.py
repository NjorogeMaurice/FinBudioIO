import pandas as pd
import streamlit as st
from io import StringIO

def is_pdf(file):
    return file.name.endswith('.pdf')

st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

st.header('Welcome to FinBudIO', divider='blue')
st.write("Empower Your Financial Journey \
At FinBudIO, we believe that managing your finances should be intuitive, insightful, and empowering. \
Our innovative platform transforms the way you interact with your financial data, \
providing you with the tools you need to make informed decisions and achieve your financial goals.")

st.divider()


col1, col2 = st.columns(2)

with col1:
   st.write("#### Visualize Your Financial Statements")
   st.image( "https://assets.toptal.io/images?url=https%3A%2F%2Fbs-uploads.toptal.io%2Fblackfish-uploads%2Fcomponents%2Fblog_post_page%2F4092285%2Fcover_image%2Fretina_500x200%2F0108-A_Guide_to_Chatbot_Terminology_Dan_Newsletter-00b8c714ab1835c965cc7357c2ca5325.png")
   st.write("With FinBudIO, you interact with your financial data. \
Our user-friendly interface allows you to visualize your financial statements with clarity and precision. \
Whether it's tracking your income, expenses, investments, or savings, our dynamic charts and graphs give you a comprehensive view of your financial health at a glance.")


with col2:
   
   st.write("#### Personalized Financial Advice")
   st.image("https://www.proprofschat.com/blog/wp-content/uploads/2024/01/Finance-Chatbots.png")
   st.write("Navigating the world of finance can be daunting, but you don’t have to do it alone. \
FinBudIO’s chat feature enables you to engage in meaningful conversations with your financial data. \
By analyzing your unique financial situation, our platform offers personalized advice tailored to your needs. \
Get insights on budgeting, investment opportunities, debt management, and more—all through a simple chat.")


# Adjust the width of the Streamlit page


# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

add_sidebar_title = st.sidebar.write("Welcome to FinBudIO")

add_divider = st.sidebar.divider() 
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/visualize.py", label="Visualize data")
st.sidebar.page_link("pages/playground.py", label="Playground")
st.sidebar.page_link("pages/chat.py", label="Chat with your data")


# uploaded_file = st.sidebar.file_uploader("Choose a file")
# if uploaded_file is not None:
#     if is_pdf(uploaded_file):
#         st.sidebar.success("File uploaded successfully!")
#     else:
#         st.sidebar.warning("Warning: Uploaded file is not a PDF.")
    # # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)
    
    # # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)

# add_divider = st.sidebar.divider() 

# add_button = st.sidebar.button("Chat with your data", type="primary")
 


