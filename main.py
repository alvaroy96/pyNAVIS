from pyNAVIS_functions.screens_plot import *
from pyNAVIS_functions.loadAERDATA import *
from pyNAVIS_functions.utils import *
from pyNAVIS_functions.raw_audio_functions import *
from pyNAVIS_settings.main_settings import *


#path = 'D:\\Repositorios\\GitHub\\pyNAVIS\\1khz_test_pdm_mono_30att2.aedat'
#path = 'D:\\Repositorios\\GitHub\\pyNAVIS\\c120e80e_nohash_8.wav.aedat'
path = 'D:\\Repositorios\\GitHub\\pyNAVIS\\train_cut.aedat'

settings = MainSettings(p_num_channels=64, p_mono_stereo=1, p_address_size=4, p_ts_tick=0.1, p_bin_size=2000)
#settings = MainSettings(p_num_channels=32, p_mono_stereo=0, p_address_size=2, p_ts_tick=0.2, p_bin_size=20000)

add, ts = loadAERDATA(path, settings)
ts = adaptAERDATA(ts, settings)
checkAERDATA(add, ts, settings)

print "The file contains", len(add), "spikes"
print "The audio has", max(ts), '$\mu$s'

#print execution_time(loadAERDATA, [path])
"""
print execution_time(spikegram, (add, ts, settings))
"""

print execution_time(sonogram, (add, ts, settings))
"""
print execution_time(histogram, (add, settings.num_channels, settings.mono_stereo, settings.bar_line))
print execution_time(average_activity,(ts, settings.bin_size))
"""



"""
wav_data, wav_fs = wav_loadWAV('D:\\Repositorios\\GitHub\\pyNAVIS\\c120e80e_nohash_8.wav')
wav_plot(wav_data, wav_fs)
wav_spectrogram(wav_data, wav_fs)
"""


raw_input()