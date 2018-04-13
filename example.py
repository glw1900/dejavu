import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("music.config") as f:
    config = json.load(f)

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)

    path = "/Users/liangweg/Workplace/fingerprint/src/PryonFingerprinter/data/audio/reference"
    # Fingerprint all the mp3's in the directory we give it
    # djv.fingerprint_directory(path, [".wav"])

    # print "Finish fingerprinting the files. \n"
    # Recognize audio from a file
    # song = djv.recognize(FileRecognizer, "mp3/Brad-Sucks--Total-Breakdown.mp3")
    # print "From file we recognized: %s\n" % song

    # Or recognize audio from your microphone for `secs` seconds
    secs = 5
    songs = djv.recognize(MicrophoneRecognizer, seconds=secs)
    if songs is None:
        print "Nothing recognized -- did you play the song out loud so your mic could hear it? :)"
    else:
        print "From mic with %d seconds we recognized:\n" % (secs)
        for song in songs:
            print song

    # Or use a recognizer without the shortcut, in anyway you would like
    # recognizer = FileRecognizer(djv)
    # songs, match_time = recognizer.recognize_file(path + "/TBD_Kindle_17-07-07_140209.wav")
    # print "we recognized: \n"
    # for song in songs:
    #     print song