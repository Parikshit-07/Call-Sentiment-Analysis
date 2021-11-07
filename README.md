## Call Sentiment Analysis :calling:
The objective of this project is to help us understand the sentiment of incomming customer call and analyze it.

### Installation
***Note:*** ***Make sure you have *Python 3.8 or higher* installed on your machine :computer:***<br/><br/>
*After clonning the repository on your local machine* <br/>
Step 1: Create a Virtual Environment
```ruby
  python -m venv myenv
```
Step 2: Activate the environment
```ruby
  myenv\Scripts\activate
```
Step 3: Install all the depedencies
```ruby
  pip install -r requirements.txt
```
Step 4: Run the Program Locally
```ruby
  streamlit run app.py
```

**:tada: Hooray :tada:**

There are 2 modes in which the audio can be analyzed:
1. Upload an audio file in .wav format
2. Record your voice and then analyze it (still work under progress).

##################################################################################<br/>

#### Future Scope 	:rocket:	:rocket:
1. We can implement DeepSpeech to improve speect-to-text conversion due to time and computation limitation :floppy_disk: we did not implement that.<br/>
2. We can further analyze the converted text to find insights using Spacy and Bert.
