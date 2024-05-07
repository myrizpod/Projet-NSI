import winsound
import pyxel
from pydub import AudioSegment

def play_music(vol):
    winsound.PlaySound("sound_folder/"+str(vol)+".wav",winsound.SND_LOOP+winsound.SND_ASYNC)

def update_sound_effects(vol):
    """
    sets the volume of the sound effects to vol [0,7]
    """
    pyxel.sounds[0].set_volumes(str(vol))
    pyxel.sounds[1].set_volumes(str(vol)*2)
    pyxel.sounds[2].set_volumes(str(vol)*2)
    pyxel.sounds[3].set_volumes(str(vol))
    pyxel.sounds[4].set_volumes(str(vol))