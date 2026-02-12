import streamlit as st
import os
from openai import OpenAI
from serpapi import GoogleSearch

# --- PAGE CONFIGURATION (Must be the first command) ---
st.set_page_config(
    page_title="ShopBot AI",
    page_icon="🛍️",
    layout="wide",  # This makes it look like a real dashboard
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS STYLING ---
st.markdown("""
<style>
    /* Hide the default Streamlit menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Style the Chat Input */
    .stChatInput {
        border-radius: 20px;
    }
    
    /* Product Card Styling */
    div[data-testid="stContainer"] {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 10px;
        transition: transform 0.2s;
    }
    /* Dark mode adjustment */
    @media (prefers-color-scheme: dark) {
        div[data-testid="stContainer"] {
            background-color: #262730;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (SETTINGS) ---
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Securely ask for the API Key (so it's not hardcoded)
    api_key_input = st.text_input("SerpApi Key", type="password", placeholder="Paste key here...")
    
    # Store key in session
    if api_key_input:
        st.session_state.SERPAPI_KEY = api_key_input
    elif "SERPAPI_KEY" not in st.session_state:
        # Default placeholder (Replace this with your actual key if you want)
        st.session_state.SERPAPI_KEY = "Your SerpAPI Key here!"

    st.divider()
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.info("💡 **Tip:** Ask for 'best headphones under $50' or 'red running shoes'.")

# --- AI SETUP ---
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama', 
)

# --- FUNCTIONS ---
def search_google_shopping(query):
    """
    Searches Google Shopping via SerpApi.
    """
    if st.session_state.SERPAPI_KEY == "YOUR_SERPAPI_KEY_HERE" or not st.session_state.SERPAPI_KEY:
        st.error("⚠️ Please enter your SerpApi Key in the sidebar!")
        return []

    params = {
        "engine": "google_shopping",
        "q": query,
        "api_key": st.session_state.SERPAPI_KEY,
        "location": "India",
        "gl": "in",
        "hl": "en",
        "num": 6  # Fetch 6 items for a nice 3x2 grid
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        return results.get("shopping_results", [])
    except Exception as e:
        st.error(f"Search Error: {e}")
        return []

def display_product_grid(products):
    """
    Displays products in a responsive 3-column grid.
    """
    # Create 3 columns
    cols = st.columns(3)
    
    for idx, item in enumerate(products):
        # Calculate which column this product belongs to (0, 1, or 2)
        col_idx = idx % 3
        
        with cols[col_idx]:
            # Create a bordered container for the card
            with st.container(border=True):
                # Product Image
                img = item.get("thumbnail")
                if img:
                    st.image(img, use_container_width=True)
                else:
                    st.text("No Image")

                # Product Title (Truncated to keep it neat)
                title = item.get("title", "No Title")
                if len(title) > 50:
                    title = title[:50] + "..."
                st.markdown(f"**{title}**")
                
                # Price & Rating
                c1, c2 = st.columns([1, 1])
                with c1:
                    st.markdown(f"💰 **{item.get('price', 'N/A')}**")
                with c2:
                    st.caption(f"⭐ {item.get('rating', '-')}")
                
                # Store Name
                st.caption(f"📍 {item.get('source', 'Unknown Store')}")
                
                # Button
                st.link_button("View Deal ↗", item.get("link", "#"), use_container_width=True)

# --- MAIN APP LOGIC ---

st.title("🛍️ AI Shopping Assistant")
st.markdown("Powered by **Llama 3** & **Google Shopping**")

# Initialize Chat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! What are you looking to buy today?"}]

# Display History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "products" in msg:
            display_product_grid(msg["products"])

# Handle Input
if prompt := st.chat_input("Ex: Best mechanical keyboard under ₹5000"):
    
    # 1. User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Assistant Logic
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            
            # ROUTER: Ask Llama 3
            router_prompt = f"User Input: '{prompt}'. If asking for a product, reply with ONLY the search keywords. If chat, reply 'NO_SEARCH'."
            
            try:
                response = client.chat.completions.create(
                    model="llama3",
                    messages=[{"role": "user", "content": router_prompt}],
                    temperature=0
                )
                decision = response.choices[0].message.content.strip().replace('"', '')

                if "NO_SEARCH" in decision:
                    # Normal Chat
                    chat_res = client.chat.completions.create(
                        model="llama3",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    reply = chat_res.choices[0].message.content
                    st.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                
                else:
                    # Search
                    # Show a status update while searching
                    status = st.empty()
                    status.info(f"🔍 Searching Google for: **{decision}**...")
                    
                    products = search_google_shopping(decision)
                    status.empty() # Remove the status message
                    
                    if products:
                        summary = f"I found **{len(products)}** options for you:"
                        st.markdown(summary)
                        display_product_grid(products)
                        
                        st.session_state.messages.append({
                            "role": "assistant", 
                            "content": summary,
                            "products": products
                        })
                    else:
                        st.warning("I couldn't find any products matching that description.")
                        st.session_state.messages.append({"role": "assistant", "content": "I couldn't find any products."})

            except Exception as e:
                st.error(f"Error: {e}")

