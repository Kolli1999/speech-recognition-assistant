**Voice-Controlled YouTube Player**

**Project Description**

This project is a Python-based voice-controlled YouTube player that listens for commands and plays the requested songs or videos on YouTube. The application leverages speech_recognition for capturing and processing voice input, pyttsx3 for text-to-speech output, and pywhatkit for interacting with YouTube.

**Features**

Voice Command Recognition: Captures voice commands through the microphone.

Text-to-Speech: Responds with text-to-speech feedback.

YouTube Integration: Plays requested songs or videos on YouTube.

**Prerequisites**

Before running this project, ensure you have the following installed:

Python 3.x

speech_recognition library

pyttsx3 library

pywhatkit library

Microphone

**Installation**

Clone the repository:

git clone https://github.com/Kolli1999/speech-recognition-assistant

Navigate to the project directory:

cd Voice-Controlled-Youtube-Player

Install the required libraries:

pip install speechrecognition pyttsx3 pywhatkit

**How to Run**

Ensure your microphone is connected.

Run the script:

python main.py

Say "Kolli" followed by "play [song name]" to play a song on YouTube.

**Example Usage**

Command: "Kolli, play Shape of You"

Response: "Playing Shape of You"

**Error Handling**

If the voice command is not recognized, the program will output a message indicating the issue and will wait for another command.

**License**

This project is licensed under the MIT License.
