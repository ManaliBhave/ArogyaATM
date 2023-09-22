from flask import Flask ,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import json
import simpleaudio as sa
import time


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)

answers = []

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/wlcm_audio", methods=['POST'])
def audio_wlcm():
    wlcm_sound_eng = "./static/audio/wlcm_eng.wav"
    wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
    play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
    play_obj_wlcm_sound_eng.wait_done()
    
    wlcm_sound_hin = "./static/audio/wlcm_hin.wav"
    wave_obj_wlcm_sound_hin = sa.WaveObject.from_wave_file(wlcm_sound_hin)
    play_obj_wlcm_sound_hin = wave_obj_wlcm_sound_hin.play()
    play_obj_wlcm_sound_hin.wait_done()
    
    wlcm_sound_eng_start = "./static/audio/wlcm_eng_start.wav"
    wave_obj_wlcm_sound_eng_start = sa.WaveObject.from_wave_file(wlcm_sound_eng_start)
    play_obj_wlcm_sound_eng_start = wave_obj_wlcm_sound_eng_start.play()
    play_obj_wlcm_sound_eng_start.wait_done()
    
    wlcm_sound_hin_start = "./static/audio/wlcm_hin_start.wav"
    wave_obj_wlcm_sound_hin_start = sa.WaveObject.from_wave_file(wlcm_sound_hin_start)
    play_obj_wlcm_sound_hin_start = wave_obj_wlcm_sound_hin_start.play()
    play_obj_wlcm_sound_hin_start.wait_done()

    return redirect("/")

@app.route("/question/phone", methods=['POST', 'GET'])
def phone():
    return render_template('phone.html')

@app.route("/contact_audio", methods=['POST'])
def audio_phone():
    wlcm_sound_eng = "./static/audio/contact_eng.wav"
    wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
    play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
    play_obj_wlcm_sound_eng.wait_done()
    
    wlcm_sound_hin = "./static/audio/contact_hin.wav"
    wave_obj_wlcm_sound_hin = sa.WaveObject.from_wave_file(wlcm_sound_hin)
    play_obj_wlcm_sound_hin = wave_obj_wlcm_sound_hin.play()
    play_obj_wlcm_sound_hin.wait_done()
    
    return redirect("/question/phone")

@app.route("/question/language", methods=['POST', 'GET'])
def language():
    if request.method == 'POST':
        user_phone = request.form.get("user_phone")
        answers.append(user_phone)
    print(answers)
    return render_template('language.html')

@app.route("/lang_audio", methods=['POST'])
def audio_lang():
    wlcm_sound_eng = "./static/audio/lang_eng.wav"
    wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
    play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
    play_obj_wlcm_sound_eng.wait_done()
    
    wlcm_sound_hin = "./static/audio/lang_hin.wav"
    wave_obj_wlcm_sound_hin = sa.WaveObject.from_wave_file(wlcm_sound_hin)
    play_obj_wlcm_sound_hin = wave_obj_wlcm_sound_hin.play()
    play_obj_wlcm_sound_hin.wait_done()
    
    return redirect("/question/language")
    
@app.route("/question/<string:quest>/<string:lang>/<int:ans>", methods=['GET', 'POST'])    
def question(quest, lang, ans):
    if lang == 'english':
        if quest == 'fever':
            return render_template("fever_eng.html")
        elif quest == 'cold':
            answers.append(ans)
            print(answers)
            return render_template("cold_eng.html")
        else:
            pass
    else:
        if quest == 'fever':
            return render_template("fever_hin.html")
        elif quest == 'cold':
            answers.append(ans)
            print(answers)
            return render_template("cold_hin.html")
        else:
            pass

@app.route("/question/audio/<string:quest>/<string:lang>", methods=['POST'])
def question_lang(quest, lang):
    if lang == 'eng_audio':
        if quest == 'fever':
            wlcm_sound_eng = "./static/audio/fever_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'cold':
            wlcm_sound_eng = "./static/audio/cold_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        else:
            pass
    else:
        if quest == 'fever':
            wlcm_sound_hin = "./static/audio/fever_hin.wav"
            wave_obj_wlcm_sound_hin = sa.WaveObject.from_wave_file(wlcm_sound_hin)
            play_obj_wlcm_sound_hin = wave_obj_wlcm_sound_hin.play()
            play_obj_wlcm_sound_hin.wait_done()
        elif quest == 'cold':
            wlcm_sound_hin = "./static/audio/cold_hin.wav"
            wave_obj_wlcm_sound_hin = sa.WaveObject.from_wave_file(wlcm_sound_hin)
            play_obj_wlcm_sound_hin = wave_obj_wlcm_sound_hin.play()
            play_obj_wlcm_sound_hin.wait_done()
        else:
            pass
    
    return redirect("/question/language")

if __name__ == '__main__':  
   app.run(debug = True)