import matplotlib.pyplot as plt
from pyNAVIS import *


def run(path, settings):    
    stereo_file = Loaders.loadAEDAT(path, settings)
    stereo_file.timestamps = Functions.adapt_timestamps(stereo_file.timestamps, settings)
    Functions.check_SpikesFile(stereo_file, settings)
    
    Plots.spikegram(stereo_file, settings)
    Plots.sonogram(stereo_file, settings)
    Plots.histogram(stereo_file, settings)
    Plots.average_activity(stereo_file, settings)
    Plots.difference_between_LR(stereo_file, settings)
    plt.show()