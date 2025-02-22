import streamlit as st


st.set_page_config(page_title= "Growth MindSEt Project" )
st.title("Growth Mindset challenge : web app with streamlit")

st.header("welcom to my Growth journey")
st.write("Embrace Challenge, Learn from Mistake, and unlock your full potential. This AI-Powered app help you more: ")

# quote section
st.header("Today's Growth Mindset Quote")
st.write("success is not a final, failure is not fetal: it is the courage to continue that counts. -whinson dobley")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


# condition
if user_input:
    st.success(f"You are facing : {user_input}. Keep continue your hard working!")
else:
    st.warning("Tell us about your challenge to get started")    
# reflexing
st.header("Reflection on your learning")
reflection = st.text_area("write your reflection here.kk")
if reflection:
    st.success(f" Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past Experience help you grow day bby day. ! Share YOur Difficulties")    



#Achievments
st.header("celebrate Your Wins!")
acheivment = st.text_input("Share something You have recently accomplished:")

if acheivment:
    st.success(f" ✨Amazing You Achieved: {acheivment}")
else: 
    st.info("Big or Small , Every achievment counts! share one Now!")   

#footer
st.write("_ _ _")
st.write("You Are DOing Amazing ! Every Step ")
st.write("Created by HIna mughal")
 
