# Whisper Facial Animations Backend
This is the backend to several plugins and applications I've built that allow for real time facial animations across various platforms.

# Requirements
## Whisper-timestamped
### Via pip
```
pip install whisper-timestamped
```
### Manually
https://github.com/linto-ai/whisper-timestamped

## Eng-To-Ipa
### Via pip
```
pip install eng-to-ipa
```
### Manually
https://pypi.org/project/eng-to-ipa/

#Installation

Simply clone the repository and run the batch file to start the server.

# Tutorial / Example Request
The server will take any .txt file located in /Requests/ with proper json structure and process it.
The proper json structure is:
```
{
  "PathToAudio":"The path to the audio to be transcribed"
}
```

Example Request:
```
{"PathToAudio":"F:\\ai-voice-cloning-3.0\\results\\output.wav"}
```

# Output
The output is a .txt file containing the following json Structure:
```
{
  "AudioPath":"The path to the audio we requested earlier",
  "Phonemes": [ #Array of object with the following structure:
    {
      "IPA Symbol":foat time in seconds the phoneme was detected
    }
  ]
}
```
Example Output:
```
{"AudioPath":"F:\\ai-voice-cloning-3.0\\results\\output.wav","Phonemes":"j:0.22,ʊ:0.3,r:0.38,l:0.46,ʊ:0.548,k:0.636,ɪ:0.724,ŋ:0.812,k:1.32,j:1.4266666666666667,t:1.5333333333333332,"}
```