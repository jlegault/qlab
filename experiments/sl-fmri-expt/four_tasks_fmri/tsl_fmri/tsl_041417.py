#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Thu May 26 18:30:18 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'asl'  # from the Builder filename that created this script
expInfo = {u'language': u'', u'target': u'', u'PartID': u'', u'block': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' %(expInfo['PartID'], expName, expInfo['block'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "start"
startClock = core.Clock()
startText = visual.TextStim(win=win, ori=0, name='startText',
    text='Press the spacebar to begin.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_24 = sound.Sound('instr_1.wav', secs=-1)
sound_24.setVolume(1)

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text="Hi! We're going to listen to some alien folk music today.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_25 = sound.Sound('instr_2.wav', secs=-1)
sound_25.setVolume(1)

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instr2Text = visual.TextStim(win=win, ori=0, name='instr2Text',
    text='This is Klaptoo!',    font='Arial',
    pos=[-.3, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_10 = visual.ImageStim(win=win, name='image_10',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_26 = sound.Sound('instr_3.wav', secs=-1)
sound_26.setVolume(1)

# Initialize components for Routine "instr3_2"
instr3_2Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text="Klaptoo is from Planet A.\nWe're going to listen to some\nfolk music from Klaptoo's \nplanet!",    font='Arial',
    pos=[-.4, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_11 = visual.ImageStim(win=win, name='image_11',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_27 = sound.Sound('instr_4.wav', secs=-1)
sound_27.setVolume(1)

# Initialize components for Routine "instr3_3"
instr3_3Clock = core.Clock()
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='Klaptoo is going to play\nhis favorite note for you \nnow. Listen carefully!',    font='Arial',
    pos=[-.4, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_13 = visual.ImageStim(win=win, name='image_13',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_28 = sound.Sound('instr_5.wav', secs=-1)
sound_28.setVolume(1)

# Initialize components for Routine "target_tone"
target_toneClock = core.Clock()
sound_12 = sound.Sound(u'%s.wav' % str(expInfo['target']), secs=-1)
sound_12.setVolume(1)
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='Press space to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instr3_4"
instr3_4Clock = core.Clock()
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text="When you hear Klaptoo play\nhis favorite note, press\nthe space bar as soon as you\ncan. Let's practice!",    font='Arial',
    pos=[-.4, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_14 = visual.ImageStim(win=win, name='image_14',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_29 = sound.Sound('instr_6.wav', secs=-1)
sound_29.setVolume(1)

# Initialize components for Routine "target_tone_2"
target_tone_2Clock = core.Clock()
sound_13 = sound.Sound(u'%s.wav' % str(expInfo['target']), secs=-1)
sound_13.setVolume(1)
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='Press space!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instr3_6"
instr3_6Clock = core.Clock()
text_41 = visual.TextStim(win=win, ori=0, name='text_41',
    text='Good job! Now Klaptoo is \ngoing to play six notes in\na row. Press space when you\nhear his favorite note!',    font='Arial',
    pos=[-.4,.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_31 = visual.ImageStim(win=win, name='image_31',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_45 = sound.Sound('instr_24.wav', secs=-1)
sound_45.setVolume(1)

# Initialize components for Routine "six_tones_1"
six_tones_1Clock = core.Clock()
sound_43 = sound.Sound('A', secs=-1)
sound_43.setVolume(1)
image_32 = visual.ImageStim(win=win, name='image_32',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr3_7"
instr3_7Clock = core.Clock()
text_42 = visual.TextStim(win=win, ori=0, name='text_42',
    text="Did you hear it? The fourth\nnote was Klaptoo's favorite\nnote! Let's listen again...",    font='Arial',
    pos=[-.4,.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_33 = visual.ImageStim(win=win, name='image_33',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_46 = sound.Sound('instr_25.wav', secs=-1)
sound_46.setVolume(1)

# Initialize components for Routine "six_tones_1"
six_tones_1Clock = core.Clock()
sound_43 = sound.Sound('A', secs=-1)
sound_43.setVolume(1)
image_32 = visual.ImageStim(win=win, name='image_32',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr3_5"
instr3_5Clock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text="Now just relax and enjoy Klaptoo's\nmusic! You don't have to watch the\nscreen. Remember to press the \nspacebar whenever you hear Klaptoo's\nfavorite note. Let's start!",    font='Arial',
    pos=[-.4, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_15 = visual.ImageStim(win=win, name='image_15',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_30 = sound.Sound('new_instr_7.wav', secs=-1)
sound_30.setVolume(1)

# Initialize components for Routine "trial"
trialClock = core.Clock()
tone = sound.Sound('A', secs=-1)
tone.setVolume(1)
alien = visual.ImageStim(win=win, name='alien',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Great, you did it!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_31 = sound.Sound('instr_8.wav', secs=-1)
sound_31.setVolume(1)

# Initialize components for Routine "instr5"
instr5Clock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='Now look at these two aliens:',    font='Arial',
    pos=[0, .8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_12 = visual.ImageStim(win=win, name='image_12',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_32 = sound.Sound('instr_9.wav', secs=-1)
sound_32.setVolume(1)

# Initialize components for Routine "instr6"
instr6Clock = core.Clock()
text_12 = visual.TextStim(win=win, ori=0, name='text_12',
    text="Each of these aliens will play \na very short piece of music in \neach trial. Please try your best \nto identify which piece sounds \nmore like Klaptoo's music. If you \ndon't know the answer, just give \nyour best guess! \n\nPress the left arrow if the first \npiece of music sounds more like the \nmusic Klaptoo made, and press the right \narrow if the second piece of music \nsounds more like the music \nKlaptoo made.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_33 = sound.Sound('new_test.wav', secs=-1)
sound_33.setVolume(1)

# Initialize components for Routine "start"
startClock = core.Clock()
startText = visual.TextStim(win=win, ori=0, name='startText',
    text='Press the spacebar to begin.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_24 = sound.Sound('instr_1.wav', secs=-1)
sound_24.setVolume(1)

# Initialize components for Routine "test"
testClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1)
image_2 = visual.ImageStim(win=win, name='image_2',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_13 = visual.TextStim(win=win, ori=0, name='text_13',
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test2"
test2Clock = core.Clock()
sound_7 = sound.Sound('A', secs=-1)
sound_7.setVolume(1)
image_3 = visual.ImageStim(win=win, name='image_3',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_14 = visual.TextStim(win=win, ori=0, name='text_14',
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test3"
test3Clock = core.Clock()
sound_8 = sound.Sound('A', secs=-1)
sound_8.setVolume(1)
image_4 = visual.ImageStim(win=win, name='image_4',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_15 = visual.TextStim(win=win, ori=0, name='text_15',
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "triplet_pause"
triplet_pauseClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
image_5 = visual.ImageStim(win=win, name='image_5',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_16 = visual.TextStim(win=win, ori=0, name='text_16',
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test4"
test4Clock = core.Clock()
sound_9 = sound.Sound('A', secs=-1)
sound_9.setVolume(1)
image_6 = visual.ImageStim(win=win, name='image_6',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_17 = visual.TextStim(win=win, ori=0, name='text_17',
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test5"
test5Clock = core.Clock()
sound_10 = sound.Sound('A', secs=-1)
sound_10.setVolume(1)
image_7 = visual.ImageStim(win=win, name='image_7',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_18 = visual.TextStim(win=win, ori=0, name='text_18',
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test6"
test6Clock = core.Clock()
sound_11 = sound.Sound('A', secs=-1)
sound_11.setVolume(1)
image_8 = visual.ImageStim(win=win, name='image_8',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_19 = visual.TextStim(win=win, ori=0, name='text_19',
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "question"
questionClock = core.Clock()
image_9 = visual.ImageStim(win=win, name='image_9',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_20 = visual.TextStim(win=win, ori=0, name='text_20',
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "five_s_gap"
five_s_gapClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='Please wait...',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text="Great, you're all done! Thank you :)\nPress any key to exit.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_42 = sound.Sound('instr_22.wav', secs=-1)
sound_42.setVolume(1)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
startKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
startKey.status = NOT_STARTED
# keep track of which components have finished
startComponents = []
startComponents.append(startText)
startComponents.append(startKey)
startComponents.append(sound_24)
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "start"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startText* updates
    if t >= 0.0 and startText.status == NOT_STARTED:
        # keep track of start time/frame for later
        startText.tStart = t  # underestimates by a little under one frame
        startText.frameNStart = frameN  # exact frame index
        startText.setAutoDraw(True)
    
    # *startKey* updates
    if t >= 0.0 and startKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        startKey.tStart = t  # underestimates by a little under one frame
        startKey.frameNStart = frameN  # exact frame index
        startKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if startKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_24
    if t >= 0.0 and sound_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_24.tStart = t  # underestimates by a little under one frame
        sound_24.frameNStart = frameN  # exact frame index
        sound_24.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_24.stop() #ensure sound has stopped at end of routine
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instr1Components = []
instr1Components.append(instrText)
instr1Components.append(key_resp_2)
instr1Components.append(sound_25)
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_25
    if t >= 0.0 and sound_25.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_25.tStart = t  # underestimates by a little under one frame
        sound_25.frameNStart = frameN  # exact frame index
        sound_25.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_25.stop() #ensure sound has stopped at end of routine
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr2"-------
t = 0
instr2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr2Key = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr2Key.status = NOT_STARTED
# keep track of which components have finished
instr2Components = []
instr2Components.append(instr2Text)
instr2Components.append(instr2Key)
instr2Components.append(image_10)
instr2Components.append(sound_26)
for thisComponent in instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2Text* updates
    if t >= 0.0 and instr2Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2Text.tStart = t  # underestimates by a little under one frame
        instr2Text.frameNStart = frameN  # exact frame index
        instr2Text.setAutoDraw(True)
    
    # *instr2Key* updates
    if t >= 0.0 and instr2Key.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2Key.tStart = t  # underestimates by a little under one frame
        instr2Key.frameNStart = frameN  # exact frame index
        instr2Key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instr2Key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_10* updates
    if t >= 0.0 and image_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_10.tStart = t  # underestimates by a little under one frame
        image_10.frameNStart = frameN  # exact frame index
        image_10.setAutoDraw(True)
    # start/stop sound_26
    if t >= 0.0 and sound_26.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_26.tStart = t  # underestimates by a little under one frame
        sound_26.frameNStart = frameN  # exact frame index
        sound_26.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_26.stop() #ensure sound has stopped at end of routine
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr3_2"-------
t = 0
instr3_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
instr3_2Components = []
instr3_2Components.append(text)
instr3_2Components.append(key_resp_3)
instr3_2Components.append(image_11)
instr3_2Components.append(sound_27)
for thisComponent in instr3_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_11* updates
    if t >= 0.0 and image_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_11.tStart = t  # underestimates by a little under one frame
        image_11.frameNStart = frameN  # exact frame index
        image_11.setAutoDraw(True)
    # start/stop sound_27
    if t >= 0.0 and sound_27.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_27.tStart = t  # underestimates by a little under one frame
        sound_27.frameNStart = frameN  # exact frame index
        sound_27.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_2"-------
for thisComponent in instr3_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_27.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr3_3"-------
t = 0
instr3_3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_9.status = NOT_STARTED
# keep track of which components have finished
instr3_3Components = []
instr3_3Components.append(text_7)
instr3_3Components.append(key_resp_9)
instr3_3Components.append(image_13)
instr3_3Components.append(sound_28)
for thisComponent in instr3_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # underestimates by a little under one frame
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # underestimates by a little under one frame
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_13* updates
    if t >= 0.0 and image_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_13.tStart = t  # underestimates by a little under one frame
        image_13.frameNStart = frameN  # exact frame index
        image_13.setAutoDraw(True)
    # start/stop sound_28
    if t >= 0.0 and sound_28.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_28.tStart = t  # underestimates by a little under one frame
        sound_28.frameNStart = frameN  # exact frame index
        sound_28.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_3"-------
for thisComponent in instr3_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_28.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "target_tone"-------
t = 0
target_toneClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_12.status = NOT_STARTED
# keep track of which components have finished
target_toneComponents = []
target_toneComponents.append(sound_12)
target_toneComponents.append(key_resp_12)
target_toneComponents.append(text_10)
for thisComponent in target_toneComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "target_tone"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = target_toneClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_12
    if t >= 0.0 and sound_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_12.tStart = t  # underestimates by a little under one frame
        sound_12.frameNStart = frameN  # exact frame index
        sound_12.play()  # start the sound (it finishes automatically)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # underestimates by a little under one frame
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # underestimates by a little under one frame
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in target_toneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "target_tone"-------
for thisComponent in target_toneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_12.stop() #ensure sound has stopped at end of routine
# the Routine "target_tone" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr3_4"-------
t = 0
instr3_4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_10.status = NOT_STARTED
# keep track of which components have finished
instr3_4Components = []
instr3_4Components.append(text_8)
instr3_4Components.append(image_14)
instr3_4Components.append(key_resp_10)
instr3_4Components.append(sound_29)
for thisComponent in instr3_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # underestimates by a little under one frame
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    
    # *image_14* updates
    if t >= 0.0 and image_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_14.tStart = t  # underestimates by a little under one frame
        image_14.frameNStart = frameN  # exact frame index
        image_14.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t  # underestimates by a little under one frame
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_29
    if t >= 0.0 and sound_29.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_29.tStart = t  # underestimates by a little under one frame
        sound_29.frameNStart = frameN  # exact frame index
        sound_29.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_4"-------
for thisComponent in instr3_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_29.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "target_tone_2"-------
t = 0
target_tone_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_11.status = NOT_STARTED
# keep track of which components have finished
target_tone_2Components = []
target_tone_2Components.append(sound_13)
target_tone_2Components.append(key_resp_11)
target_tone_2Components.append(text_9)
for thisComponent in target_tone_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "target_tone_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = target_tone_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_13
    if t >= 0.0 and sound_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_13.tStart = t  # underestimates by a little under one frame
        sound_13.frameNStart = frameN  # exact frame index
        sound_13.play()  # start the sound (it finishes automatically)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t  # underestimates by a little under one frame
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # underestimates by a little under one frame
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in target_tone_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "target_tone_2"-------
for thisComponent in target_tone_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_13.stop() #ensure sound has stopped at end of routine
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
   key_resp_11.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "target_tone_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr3_6"-------
t = 0
instr3_6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_27 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_27.status = NOT_STARTED
# keep track of which components have finished
instr3_6Components = []
instr3_6Components.append(text_41)
instr3_6Components.append(image_31)
instr3_6Components.append(key_resp_27)
instr3_6Components.append(sound_45)
for thisComponent in instr3_6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_41* updates
    if t >= 0.0 and text_41.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_41.tStart = t  # underestimates by a little under one frame
        text_41.frameNStart = frameN  # exact frame index
        text_41.setAutoDraw(True)
    
    # *image_31* updates
    if t >= 0.0 and image_31.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_31.tStart = t  # underestimates by a little under one frame
        image_31.frameNStart = frameN  # exact frame index
        image_31.setAutoDraw(True)
    
    # *key_resp_27* updates
    if t >= 0.0 and key_resp_27.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_27.tStart = t  # underestimates by a little under one frame
        key_resp_27.frameNStart = frameN  # exact frame index
        key_resp_27.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_27.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_45
    if t >= 0.0 and sound_45.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_45.tStart = t  # underestimates by a little under one frame
        sound_45.frameNStart = frameN  # exact frame index
        sound_45.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_6"-------
for thisComponent in instr3_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_45.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials_1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'six_tones_%s.xlsx' % str(expInfo['target'])),
    seed=None, name='practice_trials_1')
thisExp.addLoop(practice_trials_1)  # add the loop to the experiment
thisPractice_trial_1 = practice_trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_trial_1.rgb)
if thisPractice_trial_1 != None:
    for paramName in thisPractice_trial_1.keys():
        exec(paramName + '= thisPractice_trial_1.' + paramName)

for thisPractice_trial_1 in practice_trials_1:
    currentLoop = practice_trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial_1.rgb)
    if thisPractice_trial_1 != None:
        for paramName in thisPractice_trial_1.keys():
            exec(paramName + '= thisPractice_trial_1.' + paramName)
    
    #------Prepare to start Routine "six_tones_1"-------
    t = 0
    six_tones_1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_43.setSound(soundFile, secs=0.46)
    practice_trial_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    practice_trial_1.status = NOT_STARTED
    # keep track of which components have finished
    six_tones_1Components = []
    six_tones_1Components.append(sound_43)
    six_tones_1Components.append(image_32)
    six_tones_1Components.append(practice_trial_1)
    for thisComponent in six_tones_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "six_tones_1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = six_tones_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_43
        if t >= 0.0 and sound_43.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_43.tStart = t  # underestimates by a little under one frame
            sound_43.frameNStart = frameN  # exact frame index
            sound_43.play()  # start the sound (it finishes automatically)
        if sound_43.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_43.stop()  # stop the sound (if longer than duration)
        
        # *image_32* updates
        if t >= 0.0 and image_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_32.tStart = t  # underestimates by a little under one frame
            image_32.frameNStart = frameN  # exact frame index
            image_32.setAutoDraw(True)
        if image_32.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_32.setAutoDraw(False)
        
        # *practice_trial_1* updates
        if t >= 0.0 and practice_trial_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_trial_1.tStart = t  # underestimates by a little under one frame
            practice_trial_1.frameNStart = frameN  # exact frame index
            practice_trial_1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(practice_trial_1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if practice_trial_1.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_trial_1.status = STOPPED
        if practice_trial_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                practice_trial_1.keys = theseKeys[-1]  # just the last key pressed
                practice_trial_1.rt = practice_trial_1.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in six_tones_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "six_tones_1"-------
    for thisComponent in six_tones_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_43.stop() #ensure sound has stopped at end of routine
    # check responses
    if practice_trial_1.keys in ['', [], None]:  # No response was made
       practice_trial_1.keys=None
    # store data for practice_trials_1 (TrialHandler)
    practice_trials_1.addData('practice_trial_1.keys',practice_trial_1.keys)
    if practice_trial_1.keys != None:  # we had a response
        practice_trials_1.addData('practice_trial_1.rt', practice_trial_1.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trials_1'


#------Prepare to start Routine "instr3_7"-------
t = 0
instr3_7Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_28 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_28.status = NOT_STARTED
# keep track of which components have finished
instr3_7Components = []
instr3_7Components.append(text_42)
instr3_7Components.append(image_33)
instr3_7Components.append(key_resp_28)
instr3_7Components.append(sound_46)
for thisComponent in instr3_7Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_7"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_42* updates
    if t >= 0.0 and text_42.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_42.tStart = t  # underestimates by a little under one frame
        text_42.frameNStart = frameN  # exact frame index
        text_42.setAutoDraw(True)
    
    # *image_33* updates
    if t >= 0.0 and image_33.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_33.tStart = t  # underestimates by a little under one frame
        image_33.frameNStart = frameN  # exact frame index
        image_33.setAutoDraw(True)
    
    # *key_resp_28* updates
    if t >= 0.0 and key_resp_28.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_28.tStart = t  # underestimates by a little under one frame
        key_resp_28.frameNStart = frameN  # exact frame index
        key_resp_28.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_28.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_46
    if t >= 0.0 and sound_46.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_46.tStart = t  # underestimates by a little under one frame
        sound_46.frameNStart = frameN  # exact frame index
        sound_46.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_7"-------
for thisComponent in instr3_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_46.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'six_tones_%s.xlsx' % str(expInfo['target'])),
    seed=None, name='practice_trials_2')
thisExp.addLoop(practice_trials_2)  # add the loop to the experiment
thisPractice_trial_2 = practice_trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_trial_2.rgb)
if thisPractice_trial_2 != None:
    for paramName in thisPractice_trial_2.keys():
        exec(paramName + '= thisPractice_trial_2.' + paramName)

for thisPractice_trial_2 in practice_trials_2:
    currentLoop = practice_trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial_2.rgb)
    if thisPractice_trial_2 != None:
        for paramName in thisPractice_trial_2.keys():
            exec(paramName + '= thisPractice_trial_2.' + paramName)
    
    #------Prepare to start Routine "six_tones_1"-------
    t = 0
    six_tones_1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_43.setSound(soundFile, secs=0.46)
    practice_trial_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    practice_trial_1.status = NOT_STARTED
    # keep track of which components have finished
    six_tones_1Components = []
    six_tones_1Components.append(sound_43)
    six_tones_1Components.append(image_32)
    six_tones_1Components.append(practice_trial_1)
    for thisComponent in six_tones_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "six_tones_1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = six_tones_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_43
        if t >= 0.0 and sound_43.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_43.tStart = t  # underestimates by a little under one frame
            sound_43.frameNStart = frameN  # exact frame index
            sound_43.play()  # start the sound (it finishes automatically)
        if sound_43.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_43.stop()  # stop the sound (if longer than duration)
        
        # *image_32* updates
        if t >= 0.0 and image_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_32.tStart = t  # underestimates by a little under one frame
            image_32.frameNStart = frameN  # exact frame index
            image_32.setAutoDraw(True)
        if image_32.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_32.setAutoDraw(False)
        
        # *practice_trial_1* updates
        if t >= 0.0 and practice_trial_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_trial_1.tStart = t  # underestimates by a little under one frame
            practice_trial_1.frameNStart = frameN  # exact frame index
            practice_trial_1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(practice_trial_1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if practice_trial_1.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_trial_1.status = STOPPED
        if practice_trial_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                practice_trial_1.keys = theseKeys[-1]  # just the last key pressed
                practice_trial_1.rt = practice_trial_1.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in six_tones_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "six_tones_1"-------
    for thisComponent in six_tones_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_43.stop() #ensure sound has stopped at end of routine
    # check responses
    if practice_trial_1.keys in ['', [], None]:  # No response was made
       practice_trial_1.keys=None
    # store data for practice_trials_2 (TrialHandler)
    practice_trials_2.addData('practice_trial_1.keys',practice_trial_1.keys)
    if practice_trial_1.keys != None:  # we had a response
        practice_trials_2.addData('practice_trial_1.rt', practice_trial_1.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trials_2'


#------Prepare to start Routine "instr3_5"-------
t = 0
instr3_5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_13.status = NOT_STARTED
# keep track of which components have finished
instr3_5Components = []
instr3_5Components.append(text_11)
instr3_5Components.append(key_resp_13)
instr3_5Components.append(image_15)
instr3_5Components.append(sound_30)
for thisComponent in instr3_5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # underestimates by a little under one frame
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t  # underestimates by a little under one frame
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_15* updates
    if t >= 0.0 and image_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_15.tStart = t  # underestimates by a little under one frame
        image_15.frameNStart = frameN  # exact frame index
        image_15.setAutoDraw(True)
    # start/stop sound_30
    if t >= 0.0 and sound_30.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_30.tStart = t  # underestimates by a little under one frame
        sound_30.frameNStart = frameN  # exact frame index
        sound_30.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_5"-------
for thisComponent in instr3_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_30.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'%s_fam_seq_%s.xlsx' % (str(expInfo['block']), str(expInfo['language']))),
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1.keys():
        exec(paramName + '= thisTrial_1.' + paramName)

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1.keys():
            exec(paramName + '= thisTrial_1.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    tone.setSound(soundFile, secs=0.46)
    target_tone_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    target_tone_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(tone)
    trialComponents.append(alien)
    trialComponents.append(target_tone_key_resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop tone
        if t >= 0.0 and tone.status == NOT_STARTED:
            # keep track of start time/frame for later
            tone.tStart = t  # underestimates by a little under one frame
            tone.frameNStart = frameN  # exact frame index
            tone.play()  # start the sound (it finishes automatically)
        if tone.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            tone.stop()  # stop the sound (if longer than duration)
        
        # *alien* updates
        if t >= 0.0 and alien.status == NOT_STARTED:
            # keep track of start time/frame for later
            alien.tStart = t  # underestimates by a little under one frame
            alien.frameNStart = frameN  # exact frame index
            alien.setAutoDraw(True)
        if alien.status == STARTED and t >= (0.0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            alien.setAutoDraw(False)
        
        # *target_tone_key_resp* updates
        if t >= 0.0 and target_tone_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            target_tone_key_resp.tStart = t  # underestimates by a little under one frame
            target_tone_key_resp.frameNStart = frameN  # exact frame index
            target_tone_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(target_tone_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if target_tone_key_resp.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            target_tone_key_resp.status = STOPPED
        if target_tone_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                target_tone_key_resp.keys = theseKeys[-1]  # just the last key pressed
                target_tone_key_resp.rt = target_tone_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tone.stop() #ensure sound has stopped at end of routine
    # check responses
    if target_tone_key_resp.keys in ['', [], None]:  # No response was made
       target_tone_key_resp.keys=None
    # store data for trials_1 (TrialHandler)
    trials_1.addData('target_tone_key_resp.keys',target_tone_key_resp.keys)
    if target_tone_key_resp.keys != None:  # we had a response
        trials_1.addData('target_tone_key_resp.rt', target_tone_key_resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_1'


#------Prepare to start Routine "instr4"-------
t = 0
instr4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
instr4Components = []
instr4Components.append(text_2)
instr4Components.append(key_resp_4)
instr4Components.append(sound_31)
for thisComponent in instr4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_31
    if t >= 0.0 and sound_31.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_31.tStart = t  # underestimates by a little under one frame
        sound_31.frameNStart = frameN  # exact frame index
        sound_31.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr4"-------
for thisComponent in instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_31.stop() #ensure sound has stopped at end of routine
# the Routine "instr4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr5"-------
t = 0
instr5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_8.status = NOT_STARTED
# keep track of which components have finished
instr5Components = []
instr5Components.append(text_6)
instr5Components.append(key_resp_8)
instr5Components.append(image_12)
instr5Components.append(sound_32)
for thisComponent in instr5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t  # underestimates by a little under one frame
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_12* updates
    if t >= 0.0 and image_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_12.tStart = t  # underestimates by a little under one frame
        image_12.frameNStart = frameN  # exact frame index
        image_12.setAutoDraw(True)
    # start/stop sound_32
    if t >= 0.0 and sound_32.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_32.tStart = t  # underestimates by a little under one frame
        sound_32.frameNStart = frameN  # exact frame index
        sound_32.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr5"-------
for thisComponent in instr5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_32.stop() #ensure sound has stopped at end of routine
# the Routine "instr5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr6"-------
t = 0
instr6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_15 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_15.status = NOT_STARTED
# keep track of which components have finished
instr6Components = []
instr6Components.append(text_12)
instr6Components.append(key_resp_15)
instr6Components.append(sound_33)
for thisComponent in instr6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t  # underestimates by a little under one frame
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)
    
    # *key_resp_15* updates
    if t >= 0.0 and key_resp_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_15.tStart = t  # underestimates by a little under one frame
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_15.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_33
    if t >= 0.0 and sound_33.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_33.tStart = t  # underestimates by a little under one frame
        sound_33.frameNStart = frameN  # exact frame index
        sound_33.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr6"-------
for thisComponent in instr6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_33.stop() #ensure sound has stopped at end of routine
# the Routine "instr6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
startKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
startKey.status = NOT_STARTED
# keep track of which components have finished
startComponents = []
startComponents.append(startText)
startComponents.append(startKey)
startComponents.append(sound_24)
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "start"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startText* updates
    if t >= 0.0 and startText.status == NOT_STARTED:
        # keep track of start time/frame for later
        startText.tStart = t  # underestimates by a little under one frame
        startText.frameNStart = frameN  # exact frame index
        startText.setAutoDraw(True)
    
    # *startKey* updates
    if t >= 0.0 and startKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        startKey.tStart = t  # underestimates by a little under one frame
        startKey.frameNStart = frameN  # exact frame index
        startKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if startKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_24
    if t >= 0.0 and sound_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_24.tStart = t  # underestimates by a little under one frame
        sound_24.frameNStart = frameN  # exact frame index
        sound_24.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_24.stop() #ensure sound has stopped at end of routine
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
twoAFC_1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'%s_forced_test_%s.xlsx' % (str(expInfo['block']), str(expInfo['language']))),
    seed=None, name='twoAFC_1')
thisExp.addLoop(twoAFC_1)  # add the loop to the experiment
thisTwoAFC_1 = twoAFC_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTwoAFC_1.rgb)
if thisTwoAFC_1 != None:
    for paramName in thisTwoAFC_1.keys():
        exec(paramName + '= thisTwoAFC_1.' + paramName)

for thisTwoAFC_1 in twoAFC_1:
    currentLoop = twoAFC_1
    # abbreviate parameter names if possible (e.g. rgb = thisTwoAFC_1.rgb)
    if thisTwoAFC_1 != None:
        for paramName in thisTwoAFC_1.keys():
            exec(paramName + '= thisTwoAFC_1.' + paramName)
    
    #------Prepare to start Routine "test"-------
    t = 0
    testClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_1.setSound(soundFile1, secs=.46)
    # keep track of which components have finished
    testComponents = []
    testComponents.append(sound_1)
    testComponents.append(image_2)
    testComponents.append(text_13)
    for thisComponent in testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if t >= 0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        if image_2.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_2.setAutoDraw(False)
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t  # underestimates by a little under one frame
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        if text_13.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_13.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test2"-------
    t = 0
    test2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_7.setSound(soundFile2, secs=0.46)
    # keep track of which components have finished
    test2Components = []
    test2Components.append(sound_7)
    test2Components.append(image_3)
    test2Components.append(text_14)
    for thisComponent in test2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_7
        if t >= 0 and sound_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_7.tStart = t  # underestimates by a little under one frame
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.play()  # start the sound (it finishes automatically)
        if sound_7.status == STARTED and t >= (0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_7.stop()  # stop the sound (if longer than duration)
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        if image_3.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_3.setAutoDraw(False)
        
        # *text_14* updates
        if t >= 0.0 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t  # underestimates by a little under one frame
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        if text_14.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_14.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test2"-------
    for thisComponent in test2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_7.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test3"-------
    t = 0
    test3Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_8.setSound(soundFile3, secs=.46)
    # keep track of which components have finished
    test3Components = []
    test3Components.append(sound_8)
    test3Components.append(image_4)
    test3Components.append(text_15)
    for thisComponent in test3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test3"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_8
        if t >= 0 and sound_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_8.tStart = t  # underestimates by a little under one frame
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.play()  # start the sound (it finishes automatically)
        if sound_8.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_8.stop()  # stop the sound (if longer than duration)
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t  # underestimates by a little under one frame
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        if image_4.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_4.setAutoDraw(False)
        
        # *text_15* updates
        if t >= 0.0 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t  # underestimates by a little under one frame
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        if text_15.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_15.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test3"-------
    for thisComponent in test3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_8.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "triplet_pause"-------
    t = 0
    triplet_pauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.480000)
    # update component parameters for each repeat
    # keep track of which components have finished
    triplet_pauseComponents = []
    triplet_pauseComponents.append(ISI)
    triplet_pauseComponents.append(image_5)
    triplet_pauseComponents.append(text_16)
    for thisComponent in triplet_pauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "triplet_pause"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = triplet_pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t  # underestimates by a little under one frame
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        if image_5.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_5.setAutoDraw(False)
        
        # *text_16* updates
        if t >= 0.0 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t  # underestimates by a little under one frame
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        if text_16.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_16.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.48)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in triplet_pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "triplet_pause"-------
    for thisComponent in triplet_pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "test4"-------
    t = 0
    test4Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_9.setSound(soundFile4, secs=.46)
    # keep track of which components have finished
    test4Components = []
    test4Components.append(sound_9)
    test4Components.append(image_6)
    test4Components.append(text_17)
    for thisComponent in test4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test4"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_9
        if t >= 0 and sound_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_9.tStart = t  # underestimates by a little under one frame
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.play()  # start the sound (it finishes automatically)
        if sound_9.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_9.stop()  # stop the sound (if longer than duration)
        
        # *image_6* updates
        if t >= 0.0 and image_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_6.tStart = t  # underestimates by a little under one frame
            image_6.frameNStart = frameN  # exact frame index
            image_6.setAutoDraw(True)
        if image_6.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_6.setAutoDraw(False)
        
        # *text_17* updates
        if t >= 0.0 and text_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_17.tStart = t  # underestimates by a little under one frame
            text_17.frameNStart = frameN  # exact frame index
            text_17.setAutoDraw(True)
        if text_17.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_17.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test4"-------
    for thisComponent in test4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_9.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test5"-------
    t = 0
    test5Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_10.setSound(soundFile5, secs=.46)
    # keep track of which components have finished
    test5Components = []
    test5Components.append(sound_10)
    test5Components.append(image_7)
    test5Components.append(text_18)
    for thisComponent in test5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test5"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_10
        if t >= 0 and sound_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_10.tStart = t  # underestimates by a little under one frame
            sound_10.frameNStart = frameN  # exact frame index
            sound_10.play()  # start the sound (it finishes automatically)
        if sound_10.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_10.stop()  # stop the sound (if longer than duration)
        
        # *image_7* updates
        if t >= 0.0 and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t  # underestimates by a little under one frame
            image_7.frameNStart = frameN  # exact frame index
            image_7.setAutoDraw(True)
        if image_7.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_7.setAutoDraw(False)
        
        # *text_18* updates
        if t >= 0.0 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t  # underestimates by a little under one frame
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        if text_18.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_18.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test5"-------
    for thisComponent in test5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_10.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test6"-------
    t = 0
    test6Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_11.setSound(soundFile6, secs=.46)
    # keep track of which components have finished
    test6Components = []
    test6Components.append(sound_11)
    test6Components.append(image_8)
    test6Components.append(text_19)
    for thisComponent in test6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test6"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_11
        if t >= 0 and sound_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_11.tStart = t  # underestimates by a little under one frame
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.play()  # start the sound (it finishes automatically)
        if sound_11.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_11.stop()  # stop the sound (if longer than duration)
        
        # *image_8* updates
        if t >= 0.0 and image_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_8.tStart = t  # underestimates by a little under one frame
            image_8.frameNStart = frameN  # exact frame index
            image_8.setAutoDraw(True)
        if image_8.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_8.setAutoDraw(False)
        
        # *text_19* updates
        if t >= 0.0 and text_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_19.tStart = t  # underestimates by a little under one frame
            text_19.frameNStart = frameN  # exact frame index
            text_19.setAutoDraw(True)
        if text_19.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_19.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test6"-------
    for thisComponent in test6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_11.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "question"-------
    t = 0
    questionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_6.status = NOT_STARTED
    # keep track of which components have finished
    questionComponents = []
    questionComponents.append(key_resp_6)
    questionComponents.append(image_9)
    questionComponents.append(text_20)
    for thisComponent in questionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "question"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = questionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t  # underestimates by a little under one frame
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # was this 'correct'?
                if (key_resp_6.keys == str(corrAns)) or (key_resp_6.keys == corrAns):
                    key_resp_6.corr = 1
                else:
                    key_resp_6.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image_9* updates
        if t >= 0.0 and image_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_9.tStart = t  # underestimates by a little under one frame
            image_9.frameNStart = frameN  # exact frame index
            image_9.setAutoDraw(True)
        
        # *text_20* updates
        if t >= 0.0 and text_20.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_20.tStart = t  # underestimates by a little under one frame
            text_20.frameNStart = frameN  # exact frame index
            text_20.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "question"-------
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
       key_resp_6.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_6.corr = 1  # correct non-response
       else: key_resp_6.corr = 0  # failed to respond (incorrectly)
    # store data for twoAFC_1 (TrialHandler)
    twoAFC_1.addData('key_resp_6.keys',key_resp_6.keys)
    twoAFC_1.addData('key_resp_6.corr', key_resp_6.corr)
    if key_resp_6.keys != None:  # we had a response
        twoAFC_1.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "five_s_gap"-------
    t = 0
    five_s_gapClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    five_s_gapComponents = []
    five_s_gapComponents.append(text_4)
    for thisComponent in five_s_gapComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "five_s_gap"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = five_s_gapClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        if text_4.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in five_s_gapComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "five_s_gap"-------
    for thisComponent in five_s_gapComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'twoAFC_1'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(text_5)
endComponents.append(key_resp_7)
endComponents.append(sound_42)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_42
    if t >= 0.0 and sound_42.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_42.tStart = t  # underestimates by a little under one frame
        sound_42.frameNStart = frameN  # exact frame index
        sound_42.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_42.stop() #ensure sound has stopped at end of routine
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
