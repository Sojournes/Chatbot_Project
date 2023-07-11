import streamlit as st
from streamlit_chat import message
from bardapi import Bard

token = 'YAhUzVY1NRIOcyssp5DAbwI8p37J4IxM_fPlVXhlYabBTW3eikWRSerQiIhGr2-m-clSFg.'

#function to generate the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response
#function to recieve user queries
def get_text():
    input_text=st.text_input("CN bot: ",key="input")
    return input_text
#title of the steamlit app
st.title('personal tutoring bot')

#url='https://images.unsplash.com/photo-1497124401559-3e75ec2ed794?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'
#data-testid="stAppViewContainer"

changes = '''
<style>
[data-testid="stAppViewContainer"]
    {
    background-image:url('https://images.unsplash.com/photo-1630588605884-0f6b41505180?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1632&q=80');
    background-size:cover;
    }
    .st-bx {
    background-color: rgba(255, 255, 255, 0.05);
    }
    html{
    background:transparent
    }
    div.esravye2 > iframe
    {
    background-color:transparent
    }

</style>
'''
st.markdown(changes, unsafe_allow_html=True)
print(st.session_state)
if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

#accepting user input
user_input=get_text()
if user_input:
    print(user_input)
    output=generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state['generated'][i],key=str(i))
        message(st.session_state['past'][i], key="user_"+str(i),is_user=True)