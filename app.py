import streamlit as st
import speech_recognition as sr
import streamlit.components.v1 as stc
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from transformers import pipeline
from streamlit_bokeh_events import streamlit_bokeh_events
import os

classifier = pipeline('sentiment-analysis')

new_title = '<p style="font-family:sans-serif; color:Orange; font-size: 42px;">Call Sentiment Analysis</p>'
st.markdown(new_title, unsafe_allow_html=True)

option = st.selectbox('How would you like to upload recording?',('','Record', 'Upload Audio'))

# st.write('You selected:', option)

if option == 'Upload Audio':
  st.write('You selected:', option)
  st.write('Please upload only .wav audio format file')
  r = sr.Recognizer()
  
  def save_uploaded_file(uploadedfile):
    with open(os.path.join(r"./",uploadedfile.name),"wb") as f:
      f.write(uploadedfile.getbuffer())
    return st.success("Uploaded file sucessfully:{}".format(uploadedfile.name))

  uploaded_file = st.file_uploader("Choose a file")
  if uploaded_file is not None:
      file_details = {"Filename":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
      audio_bytes = uploaded_file.read()
      st.audio(audio_bytes, format='audio/mp3')
      save_uploaded_file(uploaded_file)

  if st.button('Analyse'):
      # define the audio file
      audio_file = sr.AudioFile(uploaded_file.name)
      # speech recognition
      with audio_file as source: 
          r.adjust_for_ambient_noise(source) 
          audio = r.record(source)
          result = r.recognize_google(audio)
          new_title = '<p style="font-family:sans-serif; color:Orange; font-size: 22px;">Recognized Text:</p>'
          st.markdown(new_title, unsafe_allow_html=True)
          st.write(result)
          new_title = '<p style="font-family:sans-serif; color:Orange; font-size: 22px;">Text Analysis:</p>'
          st.markdown(new_title, unsafe_allow_html=True)
          st.write(classifier(result))

if option == "Record":
  stt_button = Button(label="Speak")

  stt_button.js_on_event("button_click", CustomJS(code="""
  var recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = true;

  recognition.onresult = function (e) {
      var value = "";
      for (var i = e.resultIndex; i < e.results.length; ++i) {
          if (e.results[i].isFinal) {
              value += e.results[i][0].transcript;
          }
      }
      if ( value != "") {
          document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
      }
  }
  recognition.start();
  """))

  result = streamlit_bokeh_events(
  stt_button,
  events="GET_TEXT",
  key="listen",
  refresh_on_update=False,
  override_height=75,
  debounce_time=0)

  if result:
    if "GET_TEXT" in result:
      new_title = '<p style="font-family:sans-serif; color:Orange; font-size: 22px;">Recognized Text:</p>'
      st.markdown(new_title, unsafe_allow_html=True)
      st.write(result.get("GET_TEXT"))

  if st.button('Analyse'):
      # define the audio file
      # new_title = '<p style="font-family:sans-serif; color:Orange; font-size: 22px;">Recognized Text:</p>'
      # st.markdown(new_title, unsafe_allow_html=True)
      # st.write(result)
      new_title = '<p style="font-family:sans-serif; color:Orange; font-size: 22px;">Text Analysis:</p>'
      st.markdown(new_title, unsafe_allow_html=True)
      result = str(result.get("GET_TEXT"))
      st.write(classifier(result))
