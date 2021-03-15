import os
import pickle
import numpy as np
from scipy.io.wavfile import read
import time
import sys
from modules.Speaker_Recognition.GMM.ExtractFeature import ExtractFeature
import warnings
import sounddevice as sd
from scipy.io.wavfile import write


warnings.filterwarnings("ignore")

def testPredict(audio_path):
    '''
    @:param audio_path : Path to the audio which needs to be predicted

    @:return: Returns the speaker thus detected by comparing to the model
    '''

    modelpath = "modules/Speaker_Recognition/GMM/speakers_model/"

    ef = ExtractFeature

    # list of gmm_files available
    gmm_files = [os.path.join(modelpath, fname) for fname in
                os.listdir(modelpath) if fname.endswith('.gmm')]

    # name of the model of speaker = same as the name of speaker
    speakers = [fname.split("/")[-1].split(".gmm")[0] for fname in gmm_files]


    #list of existing models
    models   = [pickle.load(open(gmm_file,'rb')) for gmm_file in gmm_files] # rb stands for  reading the binary file


    # features of the file to be predicted
    feature = ef.extract_features(audio_path)

    score_of_individual_comparision = np.zeros(len(models))
    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(feature))
        score_of_individual_comparision[i] = scores.sum()

    winner = np.argmax(score_of_individual_comparision)

    speaker_detected = speakers[winner]

    return speaker_detected



def predict(file_name):
    '''
    @param file_name : name of the file inside the dataset/predicted to be predicted
    @return: name of the speaker predicted
    '''
    speaker_predicted = testPredict(file_name)
    return speaker_predicted

# MAIN TASK
def voice_run():
    fs = 44110  # Sample rate
    seconds = 5  # Duration of recording

    i = 1

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

    print("Speak")
    sd.wait(5)  # Wait until recording is finished
    a=str(i)+".wav"
    write(str(a), fs, myrecording)  # Save as WAV file
    print("Recorded")

    num = predict(str(a))
    print(num)
    return num

if __name__ == "__main__":
    voice_run()












