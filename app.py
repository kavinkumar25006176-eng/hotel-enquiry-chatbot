import streamlit as st
import Hotel_Enquiry_Chatbot as bot

# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------
st.set_page_config(
    page_title="Hotel Enquiry Chatbot",
    page_icon="🏨",
    layout="centered"
)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------
st.title("🏨 Hotel Enquiry Chatbot")
st.write("Ask me about hotels, rooms, prices, facilities, locations, check-in and cancellation.")

# ---------------------------------------------------------
# CHAT HISTORY
# ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---------------------------------------------------------
# USER INPUT
# ---------------------------------------------------------
user_input = st.chat_input("Type your hotel enquiry here...")

if user_input:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Get response from your existing chatbot
    response = bot.chatbot_response(user_input)

    # Show bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.header("🏨 Hotel Chatbot")
    st.write("You can ask about:")

    st.write("• Hotel locations")
    st.write("• Room types")
    st.write("• Room prices")
    st.write("• Facilities")
    st.write("• Check-in")
    st.write("• Cancellation")
    st.write("• Hotel information")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()# hotel-enquiry-chatbot
