""" This line imports the streamlit library 
and allows you to use its functions and features in your code. """

import streamlit as st

# This line sets the title of your Streamlit app to "Ini adalah title".
st.title('Ini adalah title')


# This line creates a header with the text "Ini adalah header".
st.header('Ini adalah header')

# This line creates a subheader with the text "Ini adalah subheader".
st.subheader('Ini adalah subheader')

# This line creates a text with the text "Ini adalah text".
st.text('Ini adalah text')

# This line creates a caption with the text "Ini adalah caption".
st.caption('Ini adalah caption')
st.markdown('**[Ini adalah markdown](https://www.markdownguide.org/cheat-sheet/)**')
st.markdown("---")
st.markdown('[Ini mathematical expression](https://katex.org/docs/supported.html)')
st.latex(r"x = \begin{cases}a &\text{if } b \\c &\text{if } d\end{cases}")
json={"name":"John","age":30,"city":"New York"}
st.json(json)

code = ''' print("Hello, Streamlit!") '''

st.code(code, language='python')

st.write ("## Ini adalah write")