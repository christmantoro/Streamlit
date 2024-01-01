""" This line imports the streamlit library 
and allows you to use its functions and features in your code. """

import streamlit as st

import pandas as pd

isi_data = pd.DataFrame(
    [[1, 2], [10, 20], [100, 200]], columns=['col1', 'col2'], index=['row1', 'row2', 'row3']
)

# This line sets the title of your Streamlit app to "Ini adalah title".
st.title('Ini adalah title')

# This line to show the image in our Streamlit app.
st.image("https://streamlit.io/images/brand/streamlit-mark-color.svg", width=200)

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

st.write ("### ini heading 3 mengunakan write")

st.markdown ("---")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.table(isi_data)
st.dataframe(isi_data)

#this code to show image
st.image("dharmendra-sahu-Ia2Kjtrx8y4-unsplash.jpg", caption="dharmendra-sahu-Ia2Kjtrx8y4-unsplash.jpg")

#this code to show audio
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# this code to show video from youtube
st.video("https://www.youtube.com/watch?v=JGwWNGJdvx8")

# this code to show video from local
st.video("production_id_4210523 (2160p).mp4")
