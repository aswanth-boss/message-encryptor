import streamlit as st
import base64

# --- Website Header ---
st.set_page_config(page_title="Secret Message Tool")
st.title("🔒 Secret Message Tool")
st.write("Enter your text and choose an action:")

# --- Create Tabs for Encrypt and Decrypt ---
tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

# --- TAB 1: ENCRYPT ---
with tab1:
    st.subheader("Encrypt your message")
    
    # This is a text input box (like the HTML form you are learning)
    user_input = st.text_input("Type your message here...", key="enc_input")
    
    # When the button is clicked, this runs
    if st.button("Encrypt 🚀"):
        if user_input:
            # Convert text to bytes, then encode it in base64
            message_bytes = user_input.encode('utf-8')
            cipher_bytes = base64.b64encode(message_bytes)
            cipher_text = cipher_bytes.decode('utf-8')
            
            st.success("Encrypted successfully!")
            st.code(cipher_text) # Shows the characters in a nice copyable box
            st.info("Copy this encrypted text and send it to your friend.")
        else:
            st.warning("Please type a message first.")

# --- TAB 2: DECRYPT ---
with tab2:
    st.subheader("Decrypt a message")
    
    cipher_input = st.text_input("Paste the encrypted characters here", key="dec_input")
    
    if st.button("Decrypt 🔑"):
        if cipher_input:
            try:
                # Decode the base64 characters back to normal text
                cipher_bytes = cipher_input.encode('utf-8')
                message_bytes = base64.b64decode(cipher_bytes)
                decrypted_message = message_bytes.decode('utf-8')
                
                st.success("Decoded message:")
                st.write(f"### {decrypted_message}")
            except Exception:
                st.error("Invalid code! Make sure you pasted the exact characters.")
        else:
            st.warning("Please paste the code first.")