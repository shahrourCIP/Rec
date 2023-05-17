# import the streamlit library
import streamlit as st
import pandas as pd
from serpapi import GoogleSearch

data = pd.read_csv("skill1.csv")

# give a title to our app
st.title('AutoRecruiterEngine - 0.1')
 # Insert containers separated into tabs:
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Engine", "Final Results", "Results 1", "Results 2", "Results 3"])
tab1.write("this is Engine")
tab2.write("this is results")

def scrap(q):
    search = GoogleSearch({
        "q": q, 
        "api_key": "1835fadd674bcb5f97ec8bbf2c66cd388599e307ab40ab27f3d49b0f8345e107",
        "num": "40"
    })
    result = search.get_dict()
    result.get("organic_results")
    link, name, PosComp, snippet_highlighted_words, snippet = [], [], [], [], []
    for item in result.get("organic_results"):
        link.append(item.get("link"))
        x = item.get("title").split('-')
        name.append(x[0])
        PosComp.append(x[1:])
        snippet_highlighted_words.append(item.get("snippet_highlighted_words"))
        snippet.append(item.get("snippet"))
        print('===========================\n')
        
    data = pd.DataFrame({"name":name, "link":link, "Pos and Comp":PosComp, "snippet_highlighted_words":snippet_highlighted_words, "snippet":snippet})
    return data

with tab1:
    st.write("## Is Must")
    col1, col2, col3 = st.columns(3)
    with col1:
        must1 = st.text_input('Skill 1')
    with col2:
        must2 = st.text_input('Skill 2')
    with col3:
        must3 = st.text_input('Skill 3')

    st.write("## Is Plus")
    col4,col5, col6 = st.columns(3)
    with col4:
        plus1 = st.text_input('Skill 4')
    with col5:
        plus2 = st.text_input('Skill 5')
    with col6:
        plus3 = st.text_input('Skill 6')

    btn = st.button('Click me')
with tab2:
    if btn:
        q1 = f""" site:jo.linkedin.com/in  "{must1}" AND "{must2}" AND "{must3}" AND "{plus1}" """
        q2 = f""" site:jo.linkedin.com/in  "{must1}" AND "{must2}" AND "{must3}" AND "{plus2}" """
        q3 = f""" site:jo.linkedin.com/in  "{must1}" AND "{must2}" AND "{must3}" AND "{plus3}" """
        print(q1)
        data1 = scrap(q1)
        print(q2)
        data2 = scrap(q2)
        print(q3)
        data3 = scrap(q3)
        # st.write(data)
        data = pd.concat([data1, data2, data3], axis=0)
        datafreq = pd.Series(data[['link', 'name']].value_counts(), name='Applications')
        st.write(data)
        st.write(datafreq)

    else:
        st.warning('Not found results yet')

with tab3:
    if btn:
        st.write(data1)
    else:
        st.warning('Not found results yet')
with tab4:
    if btn:
        st.write(data2)
    else:
        st.warning('Not found results yet')
with tab5:
    if btn:
        st.write(data3)
    else:
        st.warning('Not found results yet')