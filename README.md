**Voice-Activated Multilingual Translator:**

**Overview:**
Voice-Activated Multilingual Translator is a hands-free application that uses voice commands to translate spoken words across multiple languages. Powered by MarianMT from Hugging Face for translation, it listens for a specific wake word, recognizes the target language, transcribes the spoken input, translates it to the selected language, and provides audio output of the translation. This project is ideal for real-time, multilingual interactions without requiring text input.

**Features:**
Voice Activation: Starts translating based on a customizable wake word.
Language Selection: Recognizes the target language from a spoken command.
Real-Time Translation: Provides instant translations using MarianMT models.
Audio Output: Converts translated text into spoken audio for a seamless multilingual experience.
Supports Multiple Languages: Supports popular languages such as French, Spanish, German, Hindi, Chinese, Russian, Italian, Arabic, and more.

**Requirements:**
Python 3.x
Required libraries:
transformers (Hugging Face Transformers library)
SpeechRecognition
gTTS (Google Text-to-Speech)
playsound
pydub (optional, for enhanced audio control)

**Setup Instructions:**
1. Clone the Repository
git clone https://github.com/your-username/Voice-Activated-Multilingual-Translator.git
cd Voice-Activated-Multilingual-Translator

2. Install Dependencies
Install the required Python libraries:
pip install transformers SpeechRecognition gTTS playsound pydub

3. Run the Translator
To start the voice-activated translator:
python main.py

**Usage**
Activation with Wake Word: The application listens for a wake word (default: "translate"). When it hears the wake word, it activates the translation mode.
Select Target Language by Voice: After activation, the application prompts you to say the target language, which is recognized from predefined language options.
Speak for Translation: Once the target language is set, speak your message in English (or another source language). The app will transcribe the audio, translate it into the selected language, and output the translated text as spoken audio.

**Example Workflow:**
Say the wake word: "translate"
Respond to the prompt by saying your target language (e.g., "Spanish")
Speak a sentence, such as "Hello, how are you?"
The app will translate and speak out the translation in Spanish: "Hola, ¿cómo estás?"
Language Options
The following languages are supported (you may add more by extending the language_codes dictionary):
French
Spanish
German
Marathi
Hindi
Chinese
Russian
Italian
Arabic
![Screenshot 2024-11-03 185423](https://github.com/user-attachments/assets/d339f7fe-22ce-4569-a400-3cf56ebc86c5)


**Code Structure**
main.py: Main script that integrates wake word detection, language selection, voice recognition, translation, and audio output.
load_translation_model: Loads the MarianMT model based on the source and target language pair.
text_to_speech: Converts translated text to audio using gTTS and plays it with playsound.

**Future Enhancements:**
Continuous Translation: Loop the translator to continuously listen for new inputs without requiring a wake word each time.
Extended Language Support: Add more languages and improve model caching for frequently used language pairs.
Offline Capabilities: Integrate offline speech recognition and TTS for use without internet access.
Interactive GUI: Build a user-friendly interface to allow for easier language selection and command visibility.
