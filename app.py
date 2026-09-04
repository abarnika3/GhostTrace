import streamlit as st

st.set_page_config(page_title="GhostTrace", page_icon="👻")
st.title("👻 GhostTrace - LinkedIn Fake Profile Hunter")

name = st.text_input("Enter Name")
bio = st.text_area("Paste Bio")

if st.button("Analyze"):
    risk = 0
    if name.lower() in ["babloo", "test", "abc"]:
        risk += 80
    if "of a company" in bio.lower():
        risk += 50
    if len(name.split()) < 2:
        risk += 20
    if len(bio) < 20:
        risk += 20
    
    if risk > 90: risk = 95
    
    if risk >= 70:
        st.error(f"🚨 FAKE PROFILE! Risk {risk}%")
    elif risk >= 40:
        st.warning(f"⚠️ SUSPICIOUS! Risk {risk}%")
    else:
        st.success(f"✅ REAL! Risk {risk}%")