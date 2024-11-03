import speech_recognition as sr
from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
import playsound

# Initialize Speech Recognizer
recognizer = sr.Recognizer()

# Language codes for MarianMT and gTTS
language_codes = {
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Marathi": "mr",
    "Hindi": "hi",
    "Chinese": "zh",
    "Russian": "ru",
    "Italian": "it",
    "Arabic": "ar"
}

# Initialize MarianMT Model and Tokenizer
def load_translation_model(src_lang="en", tgt_lang="fr"):
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

# Translation function using MarianMT
def translate_text(text, model, tokenizer):
    # Tokenize and translate text
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translation = model.generate(**tokens)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    print(f"Translated Text: {translated_text}")
    return translated_text

# Text-to-Speech (TTS) Function
def text_to_speech(text, language_code):
    tts = gTTS(text=text, lang=language_code)
    audio_file = "translated_audio.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)

# Listen and Translate function
def listen_and_translate(model, tokenizer, target_language_code='fr'):
    print("Listening for speech...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        # Recognize speech
        print("Processing...")
        text = recognizer.recognize_google(audio, language='en')
        print(f"Recognized Text: {text}")
        
        # Translate text
        translated_text = translate_text(text, model, tokenizer)

        # Convert translation to speech
        text_to_speech(translated_text, language_code=target_language_code)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

# Listen for target language
def listen_for_language():
    print("Listening for the target language...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        # Recognize speech for target language
        print("Processing language selection...")
        language_text = recognizer.recognize_google(audio).capitalize()
        print(f"Recognized Language: {language_text}")
        
        tgt_lang_code = language_codes.get(language_text, None)
        if tgt_lang_code is None:
            print("Sorry, this language is not supported.")
        return tgt_lang_code

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

# Activation function to detect the wake word
def activate_bot(wake_word="translate"):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say the wake word to start translation.")
        while True:
            audio = recognizer.listen(source)
            try:
                # Recognize wake word
                trigger_word = recognizer.recognize_google(audio).lower()
                print(f"Heard: {trigger_word}")
                
                # Check if wake word matches
                if wake_word in trigger_word:
                    print("Wake word detected! Activating translation mode.")
                    
                    # Listen for target language
                    tgt_lang_code = listen_for_language()

                    if tgt_lang_code:
                        model, tokenizer = load_translation_model("en", tgt_lang_code)
                        listen_and_translate(model, tokenizer, tgt_lang_code)
                    break  # Stop after one translation; modify as needed

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

# Run the bot
activate_bot("translate")  # Wake word is "translate"
