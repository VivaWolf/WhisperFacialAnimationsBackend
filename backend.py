import eng_to_ipa as p
import os
from os import listdir
from os.path import isfile, join
import time
import whisper_timestamped as whisper
import re
import requests
import json

#Load the whisper model - only happens once
#Default model is tiny as larger models produce marginally better results for disproportionately large computing cost
model = whisper.load_model("tiny", device="cuda")

#Loop through files in the requests folder
while True:
	for d in [e for e in listdir("Requests\\") if isfile(join("Requests\\", e))]:
		if d[-4:] == ".txt":
			#Open the Request
			t = open("Requests\\" + d, "r",  encoding='utf-8')
			
			#Convert text to json
			j = json.load(t)
			ToWriteAudio = j["PathToAudio"]
			
			#Close the file
			t.close()
			
			#Load the audio into whisper
			audio = whisper.load_audio(ToWriteAudio)
			
			#Use whisper to transcribe the audio
			result = whisper.transcribe(model, audio, language="en")
			
			#Break each word down into it's phonemes
			ToWritePhonemes = ""
			for y in range(len(result.get("segments"))):
				for x in result.get("segments")[y].get("words"):
					s = p.convert(x.get("text"))
					beg = x.get("start")
					end = x.get("end")
					if not "*" in s:
						s = re.sub('[^ðθʌæʧʃʒʤlfbmpnŋdtjrwhszgɡkəeaɑɒʊɛɔɪi]', '', s)
						offset = (end - beg) / (len(s))
						for x in range(len(s)):
							ToWritePhonemes += "{\"" + s[x] + "\":" + str(beg + (x * offset)) + "},"
							
			#Print out the results for easy debug viewing
			print(ToWriteAudio)
			print(ToWritePhonemes)
			
			#Save the results
			f = open("Results\\" + d, "w",  encoding='utf-8')
			f.write("{\"AudioPath\":\"" + ToWriteAudio + "\",\"Phonemes\":[" + ToWritePhonemes[:-1] + "]}")
			f.close()
			
			#Relocate the request to the processed folder
			os.rename("Requests\\" + d, "Processed\\" + d)
			
	time.sleep(.1)