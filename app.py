import streamlit as st
from datetime import datetime
import os

st.set_page_config(page_title="AI Reel Factory", page_icon="🎥", layout="wide")
st.title("🎬 My AI Daily Reel Factory")
st.write("Automatically creates professional Instagram Reels every day based on demand")

# Sidebar Configuration
with st.sidebar:
    st.header("Settings")
    niche = st.text_input("Your Niche", value="Fitness Motivation")
    style = st.selectbox("Content Style", ["Motivational", "Educational", "Funny", "Luxury", "Minimal"])
    target_audience = st.text_input("Target Audience", value="18-35 years old")
    instagram_handle = st.text_input("Your Instagram Handle", value="@yourhandle")
    auto_post = st.checkbox("Enable Auto Post to Instagram (requires API setup)", value=False)

# Main Button
if st.button("🚀 Generate Today's Reel", type="primary"):
    with st.spinner("Researching trends and creating professional Reel..."):
        # Simulate AI Agent Workflow
        st.success(f"✅ Trend detected in **{niche}** niche for {datetime.now().strftime('%B %d, %Y')}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📝 Professional Caption")
            caption = f"Stop scrolling! This one change transformed my {niche.lower()} game 🔥\n\nWhat’s your biggest struggle with {niche.lower()}? Comment below 👇\n\n#fyp #{niche.replace(' ','').lower()}"
            st.write(caption)
            
            st.subheader("🏷️ Hashtags")
            hashtags = f"#{niche.replace(' ','')} #Reels #{niche.replace(' ','')}Tips #Viral #fyp #Trending #Motivation"
            st.code(hashtags, language=None)
        
        with col2:
            st.subheader("🎵 Recommended Audio / Song")
            st.write("**Trending Audio:** 'Original Sound - Motivational Beat 2026' or Suno track 'Rise Above'")
            st.write("**Style:** Epic motivational music with strong beat drop at 3-second mark")
            
            st.subheader("🎥 Visual Direction")
            st.write("• Fast cuts every 0.8 seconds\n• Cinematic color grade (teal & orange)\n• Text overlays with bold font\n• Start with strong hook in first 1.5 seconds")
        
        st.subheader("📋 Full Reel Brief")
        st.info(f"""
        **Hook (0-3s):** Question or bold statement about {niche}
        **Main Content:** Show transformation / tip / story
        **CTA:** Ask for comment + follow
        **Length:** 15–25 seconds
        """)
        
        if auto_post:
            st.success(f"✅ Reel would be automatically posted to {instagram_handle} right now (API needed)")
        
        st.download_button("Download Brief as TXT", f"Reel for {datetime.now().date()}\n\n{caption}", file_name="daily_reel_brief.txt")

st.divider()
st.caption("This dashboard can be connected with CrewAI + Kling AI + Suno + Meta API for full end-to-end automation (video generation + auto upload).")
