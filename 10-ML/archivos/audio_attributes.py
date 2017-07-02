import os
# import sys
# import math
# from shutil import copyfile
# from shutil import rmtree


def obtainPitch(audioFileName):
    # Extract Pitch Track
    completePath = os.getcwd() + audioFileName[:-4]
    os.system('praat extract-pitch-track.praat ' + completePath + '.wav ' + completePath + '.PitchTier 50 300')

    originalPitchTier = fileName + '.PitchTier'
    xmin, xmax, points = parsePitchTier(originalPitchTier)
    return (xmin, xmax)
