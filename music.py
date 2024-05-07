import winsound
import pyxel
from pydub import AudioSegment

def play_music():
    winsound.PlaySound("loop.wav",winsound.SND_LOOP+winsound.SND_ASYNC)

def update_sound_effects(vol):
    """
    sets the volume of the sound effects to vol [0,7]
    """
    pyxel.sound[0].set_volumes(str(vol))
    pyxel.sound[1].set_volumes(str(vol)*2)
    pyxel.sound[2].set_volumes(str(vol)*2)
    pyxel.sound[3].set_volumes(str(vol))
    pyxel.sound[4].set_volumes(str(vol))

def update_music(vol):
    """
    sets the volume of the music depending on vol [0,7]
    """
    music=  AudioSegment.from_wav("original.wav")
    result=music+(vol-7)*3
    music.export("loop.wav",format="wav")
    