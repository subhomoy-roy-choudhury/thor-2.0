# thor-2.0

# ISSUES
1. At first ,sometimes float_input or take_command is returning NONE or string for wrong 
inputs on returning during the first iteration and its not updating the float values
as its updating the error string in the param list instead.
FIXED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

2. gender_age integration failed due to opening of multiple cam window confusing the opencv software. so we must make a central script for all opencv integrations.
FIXED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

3. voice indentification in take command needs work. 

4. facial recogniton is not working quite well . must use the VGG model for facial recognition.

5. In pyttsx there is run and wait function which is creating problem in app.py in returning the json. So it was changed from pyttsx to gtts .
FIXED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

6. Implemented threading and multiprocessing in voice command so that it can interrupt an existing command for an important command.
FIXED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# MODULES TO DO :-
a. Text Detection and Recognition.
b. Hand Writing Recognition 
c. Mask Detection.
d. Sign Language Detection.
e. Read books using tesseract
f. Cycle indicator.

# MODULES DONE :-
a. Facial Recognition(improvement needed) :- https://github.com/subhomoy-roy-choudhury/Facial-Recognition-OpenCV<br>
b. Speaker Recognition(improvement needed)<br>
c. Gender Recognition using Speech for adding title (Sir/Maam).(improvement needed):- https://github.com/subhomoy-roy-choudhury/Gender-Age-Recognition<br>
d. Mood/Emotion Recognition using Face Recogniton :- https://github.com/subhomoy-roy-choudhury/Facial-Emotion-Recognition-OpenCV  <br>
e. Chatbot(improvement needed):- https://github.com/subhomoy-roy-choudhury/Pytorch-Chatbot<br>
f. Heart Disease Prediction :- https://github.com/subhomoy-roy-choudhury/Heart-Disease-Predict <br>
g. Multithreading and Multiprocessing<br>
h. Magic Scripts :- https://github.com/subhomoy-roy-choudhury/Magic-Scripts<br>
i. Web Scraping :- https://github.com/subhomoy-roy-choudhury/Web-Scraping <br>