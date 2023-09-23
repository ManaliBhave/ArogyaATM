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
    
@app.route("/question/<string:quest>/<string:lang>/<string:ans>", methods=['GET', 'POST'])    
def question(quest, lang, ans):
    if quest == 'flu':
            return render_template("flu.html", lang = lang)
    elif quest == 'resp':
        answers.append(int(ans))
        return render_template("resp.html", lang = lang)
    
    # ------------------------------------------------------------
    elif quest == 'skin':
        answers.append(int(ans))
        return render_template("skin.html", lang = lang)
    elif quest == 'itch':
        answers.append(int(ans))
        return render_template("skin/1_skin_itch.html", lang = lang)
    elif quest == 'rash':
        answers.append(int(ans))
        return render_template("skin/2_skin_rash.html", lang = lang)
    elif quest == 'erupt':
        answers.append(int(ans))
        return render_template("skin/3_skin_erupt.html", lang = lang)
    elif quest == 'spots':
        answers.append(int(ans))
        return render_template("skin/4_skin_spots.html", lang = lang)
    
    # ------------------------------------------------------------
    elif quest == 'digest':
        if len(ans) > 1:
            for i in range(0, len(str(ans))):
                answers.append(0)
        else:
            answers.append(int(ans))
        return render_template("digest.html", lang = lang)
    elif quest == 'kidney':
        answers.append(int(ans))
        return render_template("kidney.html", lang = lang)
    elif quest == 'bone':
        answers.append(int(ans))
        return render_template("bone.html", lang = lang)
    elif quest == 'weight':
        answers.append(int(ans))
        return render_template("weight.html", lang = lang)
    elif quest == 'mental':
        answers.append(int(ans))
        return render_template("mental.html", lang = lang)
    elif quest == 'heart':
        answers.append(int(ans))
        return render_template("heart.html", lang = lang)
    elif quest == 'eyes':
        answers.append(int(ans))
        return render_template("eyes.html", lang = lang)

@app.route("/question/audio/<string:quest>/<string:lang>", methods=['POST'])
def question_lang(quest, lang):
    if lang == 'eng_audio':
        if quest == 'flu':
            wlcm_sound_eng = "./static/audio/flu_like/english/flu_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'resp':
            wlcm_sound_eng = "./static/audio/resp_like/english/resp_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
            
        # ---------------------------------------------------------------------------
        elif quest == 'skin':
            wlcm_sound_eng = "./static/audio/skin_like/english/skin_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'itch':
            wlcm_sound_eng = "./static/audio/skin_like/english/itch_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'rash':
            wlcm_sound_eng = "./static/audio/skin_like/english/rash_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'erupt':
            wlcm_sound_eng = "./static/audio/skin_like/english/erupt_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'spots':
            wlcm_sound_eng = "./static/audio/skin_like/english/spots_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
            
        # ---------------------------------------------------------------------------
        elif quest == 'digest':
            wlcm_sound_eng = "./static/audio/digest_like/english/digest_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'kidney':
            wlcm_sound_eng = "./static/audio/kidney_like/english/kidney_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'bone':
            wlcm_sound_eng = "./static/audio/bone_like/english/bone_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'weight':
            wlcm_sound_eng = "./static/audio/weight_like/english/weight_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'mental':
            wlcm_sound_eng = "./static/audio/mental_like/english/mental_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'heart':
            wlcm_sound_eng = "./static/audio/heart_like/english/heart_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'eyes':
            wlcm_sound_eng = "./static/audio/eyes_like/english/eyes_eng.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        else:
            pass
    else:
        if quest == 'flu':
            wlcm_sound_hin = "./static/audio/flu_like/hindi/flu_hin.wav"
            wave_obj_wlcm_sound_hin = sa.WaveObject.from_wave_file(wlcm_sound_hin)
            play_obj_wlcm_sound_hin = wave_obj_wlcm_sound_hin.play()
            play_obj_wlcm_sound_hin.wait_done()
        elif quest == 'resp':
            wlcm_sound_hin = "./static/audio/resp_like/hindi/resp_hin.wav"
            wave_obj_wlcm_sound_hin = sa.WaveObject.from_wave_file(wlcm_sound_hin)
            play_obj_wlcm_sound_hin = wave_obj_wlcm_sound_hin.play()
            play_obj_wlcm_sound_hin.wait_done()
            
        # ----------------------------------------------------------------------------
        elif quest == 'skin':
            wlcm_sound_eng = "./static/audio/skin_like/hindi/skin_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'itch':
            wlcm_sound_eng = "./static/audio/skin_like/hindi/itch_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'rash':
            wlcm_sound_eng = "./static/audio/skin_like/hindi/rash_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'erupt':
            wlcm_sound_eng = "./static/audio/skin_like/hindi/erupt_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'spots':
            wlcm_sound_eng = "./static/audio/skin_like/hindi/spots_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        
        # ----------------------------------------------------------------------------
        elif quest == 'digest':
            wlcm_sound_eng = "./static/audio/digest_like/hindi/digest_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'kidney':
            wlcm_sound_eng = "./static/audio/kidney_like/hindi/kidney_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'bone':
            wlcm_sound_eng = "./static/audio/bone_like/hindi/bone_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'weight':
            wlcm_sound_eng = "./static/audio/weight_like/hindi/weight_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'mental':
            wlcm_sound_eng = "./static/audio/mental_like/hindi/mental_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'heart':
            wlcm_sound_eng = "./static/audio/heart_like/hindi/heart_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        elif quest == 'eyes':
            wlcm_sound_eng = "./static/audio/eyes_like/hindi/eyes_hin.wav"
            wave_obj_wlcm_sound_eng = sa.WaveObject.from_wave_file(wlcm_sound_eng)
            play_obj_wlcm_sound_eng = wave_obj_wlcm_sound_eng.play()
            play_obj_wlcm_sound_eng.wait_done()
        else:
            pass
    
    return redirect("/question/language")

if __name__ == '__main__':  
   app.run(debug = True)