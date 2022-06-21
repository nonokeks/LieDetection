#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Juni 21, 2022, at 12:04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import csv
# function to read in csv files
def read_csv(filename, delim):
    questions = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delim)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                questions.append([int(row[0]),str(row[1])])
                line_count += 1
    return questions



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'LieDetection'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='Z:\\Dokumente\\Uni\\Hiwi\\HannahBA\\LieDetection\\LieDetection_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Start"
StartClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Welcome!\n\nThis is an experiment about lie detection.\n\nPress 'space' to continue",
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
#True = number, False = questions
reihenfolge = False

text_clock = core.Clock()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text="In the following, you will be asked if the number in the middle is greater than 10.\n\nPlease always lie!\n\nPress 'space' to start",
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_space = keyboard.Keyboard()
# here you can change the order in 
# which they should lie, tell truth or choose

# lie = 0, truth = 1, choorse = 2

order = [2, 1, 0]

# generates list with len 20, 10 ints < 10, 10 ints > 10
def gen_rand_list():
    # list len 10, random num from 11 to 19
    randomlist_1 = random.sample(range(11, 19), 5)
    randomlist_1.extend(random.sample(range(11, 19), 5))
    #list len 10, random num from 1 to 9
    randomlist_2 = random.sample(range(1, 9), 5)
    randomlist_2.extend(random.sample(range(1, 9), 5))
    
    randomlist_1.extend(randomlist_2)
    return randomlist_1

# Initialize components for Routine "Baseline"
BaselineClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "NumberTest"
NumberTestClock = core.Clock()
question_1 = visual.TextStim(win=win, name='question_1',
    text='Is the displayed number greater than 10?',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
press_key_r = visual.TextStim(win=win, name='press_key_r',
    text='                    Yes "→" ',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
press_key_l = visual.TextStim(win=win, name='press_key_l',
    text='"←" No',
    font='Open Sans',
    pos=(-0.12, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-2.0);
num_test = visual.TextStim(win=win, name='num_test',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
import random 
timer_line = visual.Line(
    win=win, name='timer_line',
    start=(-(1,0.02)[0]/2.0, 0), end=(+(1,0.02)[0]/2.0, 0),
    ori=0.0, pos=(0, -0.35),
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
import time
#import sys
from psychopy import event
arrow_response = keyboard.Keyboard()

# Initialize components for Routine "Save_Data"
Save_DataClock = core.Clock()

# Initialize components for Routine "Instructions_Quest"
Instructions_QuestClock = core.Clock()
key_resp_2 = keyboard.Keyboard()
instructions_text2 = visual.TextStim(win=win, name='instructions_text2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
# here you can change the order in 
# which they should lie, tell truth or choose

# lie = 0, truth = 1, choice = 2

order = [2, 1, 0]

# read in the csv for questions and randomize order of questions
questions = []

questions_emo = read_csv('Question_emotional.csv', ',')
questions_neu = read_csv('Question_neutral.csv', ';')

# pick questions for lie and truth
#pick_emo = pick_quest()
#pick_neu = pick_quest()
# shuffle questions and then pick first 10 from each for lie 
# and last 10 for truth
random.shuffle(questions_emo)
random.shuffle(questions_neu)

questions_lie = questions_emo[0:10]
questions_lie.extend(questions_neu[0:10])

questions_truth = questions_emo[10:20]
questions_truth.extend(questions_neu[10:20])

questions_choice = questions_emo.copy()
questions_choice.extend(questions_neu[:])

print('lie')
print(len(questions_lie))
print('truth')
print(len(questions_truth))
print('chioce')
print(len(questions_choice))

# Initialize components for Routine "Baseline"
BaselineClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "QuestionsTest"
QuestionsTestClock = core.Clock()
press_key_l2 = visual.TextStim(win=win, name='press_key_l2',
    text='"←" No',
    font='Open Sans',
    pos=(-0.12, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
press_key_r2 = visual.TextStim(win=win, name='press_key_r2',
    text='                    Yes "→" ',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
question = visual.TextStim(win=win, name='question',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
question_response = keyboard.Keyboard()
timer_line2 = visual.Line(
    win=win, name='timer_line2',
    start=(-(1,0.02)[0]/2.0, 0), end=(+(1,0.02)[0]/2.0, 0),
    ori=0.0, pos=(0, -0.35),
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# Initialize components for Routine "Save_Data"
Save_DataClock = core.Clock()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text="In the following, you will be asked if the number in the middle is greater than 10.\n\nPlease always lie!\n\nPress 'space' to start",
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_space = keyboard.Keyboard()
# here you can change the order in 
# which they should lie, tell truth or choose

# lie = 0, truth = 1, choorse = 2

order = [2, 1, 0]

# generates list with len 20, 10 ints < 10, 10 ints > 10
def gen_rand_list():
    # list len 10, random num from 11 to 19
    randomlist_1 = random.sample(range(11, 19), 5)
    randomlist_1.extend(random.sample(range(11, 19), 5))
    #list len 10, random num from 1 to 9
    randomlist_2 = random.sample(range(1, 9), 5)
    randomlist_2.extend(random.sample(range(1, 9), 5))
    
    randomlist_1.extend(randomlist_2)
    return randomlist_1

# Initialize components for Routine "Baseline"
BaselineClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "NumberTest"
NumberTestClock = core.Clock()
question_1 = visual.TextStim(win=win, name='question_1',
    text='Is the displayed number greater than 10?',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
press_key_r = visual.TextStim(win=win, name='press_key_r',
    text='                    Yes "→" ',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
press_key_l = visual.TextStim(win=win, name='press_key_l',
    text='"←" No',
    font='Open Sans',
    pos=(-0.12, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-2.0);
num_test = visual.TextStim(win=win, name='num_test',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
import random 
timer_line = visual.Line(
    win=win, name='timer_line',
    start=(-(1,0.02)[0]/2.0, 0), end=(+(1,0.02)[0]/2.0, 0),
    ori=0.0, pos=(0, -0.35),
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
import time
#import sys
from psychopy import event
arrow_response = keyboard.Keyboard()

# Initialize components for Routine "Save_Data"
Save_DataClock = core.Clock()

# Initialize components for Routine "End"
EndClock = core.Clock()
end = visual.TextStim(win=win, name='end',
    text='Thank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
StartComponents = [text, key_resp]
for thisComponent in StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start"-------
while continueRoutine:
    # get current time
    t = StartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_instruct_num = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_instruct_num')
thisExp.addLoop(trials_instruct_num)  # add the loop to the experiment
thisTrials_instruct_num = trials_instruct_num.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_instruct_num.rgb)
if thisTrials_instruct_num != None:
    for paramName in thisTrials_instruct_num:
        exec('{} = thisTrials_instruct_num[paramName]'.format(paramName))

for thisTrials_instruct_num in trials_instruct_num:
    currentLoop = trials_instruct_num
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_instruct_num.rgb)
    if thisTrials_instruct_num != None:
        for paramName in thisTrials_instruct_num:
            exec('{} = thisTrials_instruct_num[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructions_space.keys = []
    instructions_space.rt = []
    _instructions_space_allKeys = []
    # depending on the oder decided in the beginning
    # edit the displayed text and write to output file
    numbers_rand =[]
    trials_limit = 20
    option = 'number'
    number_r = 0
    if reihenfolge:
        number_r = trials_instruct_num.thisN
    else:
        number_r = trials_instruct_num2.thisN
    
    if order[number_r] == 0:
        instructions_text.text  = "In the following, you will be asked if the number in the middle is greater than 10.\n \nPlease always lie! \n \nPress 'space' to start"
        thisExp.addData('numbers.instructions', 'lie')
        mode = 'lie'
        numbers_rand = gen_rand_list()
    if order[number_r] == 1:
        instructions_text.text  = "In the following, you will be asked if the number in the middle is greater than 10.\n \nPlease always tell the truth! \n \nPress 'space' to start"
        thisExp.addData('numbers.instructions', 'truth')
        numbers_rand = gen_rand_list()
        mode = 'truth'
    if order[number_r] == 2:
        instructions_text.text  = "In the following, you will be asked if the number in the middle is greater than 10.\n \nYou can choose to lie or tell the truth! \n \nPress 'space' to start"
        thisExp.addData('numbers.instructions', 'choice')
        numbers_rand = gen_rand_list()
        numbers_rand. extend(gen_rand_list())
        trials_limit = 40
        mode = 'choice'
    
    # randomize numbers
    random.shuffle(numbers_rand)
    print(numbers_rand)
    
    # keep track of which components have finished
    InstructionsComponents = [instructions_text, instructions_space]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_text.frameNStart = frameN  # exact frame index
            instructions_text.tStart = t  # local t and not account for scr refresh
            instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            instructions_text.setAutoDraw(True)
        
        # *instructions_space* updates
        if instructions_space.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_space.frameNStart = frameN  # exact frame index
            instructions_space.tStart = t  # local t and not account for scr refresh
            instructions_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_space, 'tStartRefresh')  # time at next scr refresh
            instructions_space.status = STARTED
            # keyboard checking is just starting
            instructions_space.clock.reset()  # now t=0
        if instructions_space.status == STARTED:
            theseKeys = instructions_space.getKeys(keyList=['space'], waitRelease=False)
            _instructions_space_allKeys.extend(theseKeys)
            if len(_instructions_space_allKeys):
                instructions_space.keys = _instructions_space_allKeys[-1].name  # just the last key pressed
                instructions_space.rt = _instructions_space_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if instructions_space.keys in ['', [], None]:  # No response was made
        instructions_space.keys = None
    trials_instruct_num.addData('instructions_space.keys',instructions_space.keys)
    if instructions_space.keys != None:  # we had a response
        trials_instruct_num.addData('instructions_space.rt', instructions_space.rt)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_num = data.TrialHandler(nReps=3.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_num')
    thisExp.addLoop(trials_num)  # add the loop to the experiment
    thisTrials_num = trials_num.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_num.rgb)
    if thisTrials_num != None:
        for paramName in thisTrials_num:
            exec('{} = thisTrials_num[paramName]'.format(paramName))
    
    for thisTrials_num in trials_num:
        currentLoop = trials_num
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_num.rgb)
        if thisTrials_num != None:
            for paramName in thisTrials_num:
                exec('{} = thisTrials_num[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Baseline"-------
        continueRoutine = True
        # update component parameters for each repeat
        # timer to randomise time of routine
        loopClock = core.Clock()
        routine_time = randint(2,5)
        loopClock.add(routine_time)
        
        # keep track of which components have finished
        BaselineComponents = [fixation_cross]
        for thisComponent in BaselineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BaselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Baseline"-------
        while continueRoutine:
            # get current time
            t = BaselineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BaselineClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross* updates
            if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.tStart = t  # local t and not account for scr refresh
                fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                fixation_cross.setAutoDraw(True)
            # check if timer is over
            if (loopClock.getTime() >0):
                continueRoutine = False 
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BaselineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Baseline"-------
        for thisComponent in BaselineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # reset Clock
        loopClock.reset()
        thisExp.addData('basline.time', routine_time)
        # the Routine "Baseline" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "NumberTest"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        corResp = ''
        press_key_l.height = 0.05
        press_key_l.pos = (-0.12, -0.3)
        press_key_r.height = 0.05
        press_key_r.pos = (0, -0.3)
        
        # select number from list generated in the introduction
        ind = 0
        if reihenfolge:
            ind = trials_num.thisN
        else: 
            ind = trials_num2.thisN
        num = numbers_rand[ind]
           
        # write generated number to data
        thisExp.addData('num_test.value', num)
        
        # generate correct response (always truth)
        if num > 10:
            corResp = 'right'
        else:
            corResp = 'left'
        
        num_test.text = str(num)
        
        # set arrow timer
        timer_set = False
        # configure visual timer
        t = 5
        
        #timer = core.Clock()
        #timer.add(t)
        
        #timer = core.CountdownTimer(t)
        
        # size of line
        timer_line.size = [1,0.02]
        width = timer_line.size[0]
        
        # how much the line shrinks each frame
        dist = width/(30*t)
        timer_line.autoDraw= False
        arrow_response.keys = []
        arrow_response.rt = []
        _arrow_response_allKeys = []
        # keep track of which components have finished
        NumberTestComponents = [question_1, press_key_r, press_key_l, num_test, timer_line, arrow_response]
        for thisComponent in NumberTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        NumberTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "NumberTest"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = NumberTestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=NumberTestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_1* updates
            if question_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_1.frameNStart = frameN  # exact frame index
                question_1.tStart = t  # local t and not account for scr refresh
                question_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_1, 'tStartRefresh')  # time at next scr refresh
                question_1.setAutoDraw(True)
            if question_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > question_1.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    question_1.tStop = t  # not accounting for scr refresh
                    question_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(question_1, 'tStopRefresh')  # time at next scr refresh
                    question_1.setAutoDraw(False)
            
            # *press_key_r* updates
            if press_key_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_key_r.frameNStart = frameN  # exact frame index
                press_key_r.tStart = t  # local t and not account for scr refresh
                press_key_r.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_key_r, 'tStartRefresh')  # time at next scr refresh
                press_key_r.setAutoDraw(True)
            if press_key_r.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > press_key_r.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    press_key_r.tStop = t  # not accounting for scr refresh
                    press_key_r.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(press_key_r, 'tStopRefresh')  # time at next scr refresh
                    press_key_r.setAutoDraw(False)
            
            # *press_key_l* updates
            if press_key_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_key_l.frameNStart = frameN  # exact frame index
                press_key_l.tStart = t  # local t and not account for scr refresh
                press_key_l.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_key_l, 'tStartRefresh')  # time at next scr refresh
                press_key_l.setAutoDraw(True)
            if press_key_l.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > press_key_l.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    press_key_l.tStop = t  # not accounting for scr refresh
                    press_key_l.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(press_key_l, 'tStopRefresh')  # time at next scr refresh
                    press_key_l.setAutoDraw(False)
            
            # *num_test* updates
            if num_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                num_test.frameNStart = frameN  # exact frame index
                num_test.tStart = t  # local t and not account for scr refresh
                num_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num_test, 'tStartRefresh')  # time at next scr refresh
                num_test.setAutoDraw(True)
            if num_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > num_test.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    num_test.tStop = t  # not accounting for scr refresh
                    num_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(num_test, 'tStopRefresh')  # time at next scr refresh
                    num_test.setAutoDraw(False)
            if arrow_response.keys and not timer_set:
                # right key
                if 'right' in arrow_response.keys:
                    press_key_r.height = 0.08
                    press_key_r.pos = (0, -0.29)
                # left key
                if 'left' in arrow_response.keys:
                    press_key_l.height = 0.08
                    press_key_l.pos = (-0.12, -0.29)
                # set timer
                text_clock = core.Clock()
                text_clock.add(1)
                timer_set = True
                
            if timer_set:
                if text_clock.getTime()<0:
                    pass
                else:
                    continueRoutine = False
            
            # *timer_line* updates
            if timer_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer_line.frameNStart = frameN  # exact frame index
                timer_line.tStart = t  # local t and not account for scr refresh
                timer_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer_line, 'tStartRefresh')  # time at next scr refresh
                timer_line.setAutoDraw(True)
            if timer_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timer_line.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    timer_line.tStop = t  # not accounting for scr refresh
                    timer_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(timer_line, 'tStopRefresh')  # time at next scr refresh
                    timer_line.setAutoDraw(False)
            #if timer.getTime() > 0 and continueRoutine:
            # adjust line size to visualize time
            width -= dist
            timer_line.size = [width,0.02]
            timer_line.draw()
            win.flip()
                    
            # check if response was given 
            """
                keys = event.getKeys()
                if keys: 
                    if 'right' in keys: 
                        rt = arrow_response.rt
                        print(rt)
                        continueRoutine = False
                    if 'left' in keys: 
                        rt = arrow_response.rt
                        print(rt)
                        continueRoutine = False
            """      
                        
            
                
            
            
            
            # *arrow_response* updates
            if arrow_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow_response.frameNStart = frameN  # exact frame index
                arrow_response.tStart = t  # local t and not account for scr refresh
                arrow_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_response, 'tStartRefresh')  # time at next scr refresh
                arrow_response.status = STARTED
                # keyboard checking is just starting
                arrow_response.clock.reset()  # now t=0
                arrow_response.clearEvents(eventType='keyboard')
            if arrow_response.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow_response.tStop = t  # not accounting for scr refresh
                    arrow_response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(arrow_response, 'tStopRefresh')  # time at next scr refresh
                    arrow_response.status = FINISHED
            if arrow_response.status == STARTED:
                theseKeys = arrow_response.getKeys(keyList=['left', 'right'], waitRelease=False)
                _arrow_response_allKeys.extend(theseKeys)
                if len(_arrow_response_allKeys):
                    arrow_response.keys = _arrow_response_allKeys[-1].name  # just the last key pressed
                    arrow_response.rt = _arrow_response_allKeys[-1].rt
                    # was this correct?
                    if (arrow_response.keys == str(corResp)) or (arrow_response.keys == corResp):
                        arrow_response.corr = 1
                    else:
                        arrow_response.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NumberTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "NumberTest"-------
        for thisComponent in NumberTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_num.addData('press_key_r.started', press_key_r.tStartRefresh)
        trials_num.addData('press_key_r.stopped', press_key_r.tStopRefresh)
        text_clock.reset()
        #if trials max is 20 end early 
        if reihenfolge:
            if trials_num.thisN >= (trials_limit-1):
                trials_num.finished = True
        else: 
            if trials_num2.thisN >= (trials_limit-1):
                trials_num2.finished = True
        
        
        #rt = arrow_response.rt
        #print(rt)
        #event.clearEvents()
        # check responses
        if arrow_response.keys in ['', [], None]:  # No response was made
            arrow_response.keys = None
            # was no response the correct answer?!
            if str(corResp).lower() == 'none':
               arrow_response.corr = 1;  # correct non-response
            else:
               arrow_response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_num (TrialHandler)
        trials_num.addData('arrow_response.keys',arrow_response.keys)
        trials_num.addData('arrow_response.corr', arrow_response.corr)
        if arrow_response.keys != None:  # we had a response
            trials_num.addData('arrow_response.rt', arrow_response.rt)
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'trials_num'
    
    
    # ------Prepare to start Routine "Save_Data"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Save_DataComponents = []
    for thisComponent in Save_DataComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Save_DataClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Save_Data"-------
    while continueRoutine:
        # get current time
        t = Save_DataClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Save_DataClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Save_DataComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Save_Data"-------
    for thisComponent in Save_DataComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Save_Data" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'trials_instruct_num'


# set up handler to look after randomisation of conditions etc
trials_instruct_quest = data.TrialHandler(nReps=3.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_instruct_quest')
thisExp.addLoop(trials_instruct_quest)  # add the loop to the experiment
thisTrials_instruct_quest = trials_instruct_quest.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_instruct_quest.rgb)
if thisTrials_instruct_quest != None:
    for paramName in thisTrials_instruct_quest:
        exec('{} = thisTrials_instruct_quest[paramName]'.format(paramName))

for thisTrials_instruct_quest in trials_instruct_quest:
    currentLoop = trials_instruct_quest
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_instruct_quest.rgb)
    if thisTrials_instruct_quest != None:
        for paramName in thisTrials_instruct_quest:
            exec('{} = thisTrials_instruct_quest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions_Quest"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # depending on the oder decided in the beginning
    # edit the displayed text and write to output file
    
    option = 'questions'
    trials_limit = 20
    if order[trials_instruct_quest.thisN] == 0:
        instructions_text2.text  = "In the following, you will be asked personal questions.\n \nPlease always lie! \n \nPress 'space' to start"
        thisExp.addData('questions.instructions', 'lie')
        questions = questions_lie.copy()
        mode = 'lie'
    if order[trials_instruct_quest.thisN] == 1:
        instructions_text2.text  = "In the following, you will be asked personal questions.\n \nPlease always tell the truth! \n \nPress 'space' to start"
        thisExp.addData('questions.instructions', 'truth')
        questions = questions_truth.copy()
        mode = 'truth'
    if order[trials_instruct_quest.thisN] == 2:
        instructions_text2.text  = "In the following, you will be asked personal questions.\n \nYou can choose to lie or tell the truth! \n \nPress 'space' to start"
        thisExp.addData('questions.instructions', 'choice')
        questions = questions_choice.copy()
        trials_limit = 40
        mode = 'choice'
    
    random.shuffle(questions)
    #print(questions)
    # some datastorages
    
    baseline_s = []
    eye_measures = []
    key_s = []
    id_s = []
    correct_s = []
    # keep track of which components have finished
    Instructions_QuestComponents = [key_resp_2, instructions_text2]
    for thisComponent in Instructions_QuestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instructions_QuestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions_Quest"-------
    while continueRoutine:
        # get current time
        t = Instructions_QuestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instructions_QuestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *instructions_text2* updates
        if instructions_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_text2.frameNStart = frameN  # exact frame index
            instructions_text2.tStart = t  # local t and not account for scr refresh
            instructions_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text2, 'tStartRefresh')  # time at next scr refresh
            instructions_text2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_QuestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions_Quest"-------
    for thisComponent in Instructions_QuestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials_instruct_quest.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_instruct_quest.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "Instructions_Quest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_quest = data.TrialHandler(nReps=4.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_quest')
    thisExp.addLoop(trials_quest)  # add the loop to the experiment
    thisTrials_quest = trials_quest.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_quest.rgb)
    if thisTrials_quest != None:
        for paramName in thisTrials_quest:
            exec('{} = thisTrials_quest[paramName]'.format(paramName))
    
    for thisTrials_quest in trials_quest:
        currentLoop = trials_quest
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_quest.rgb)
        if thisTrials_quest != None:
            for paramName in thisTrials_quest:
                exec('{} = thisTrials_quest[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Baseline"-------
        continueRoutine = True
        # update component parameters for each repeat
        # timer to randomise time of routine
        loopClock = core.Clock()
        routine_time = randint(2,5)
        loopClock.add(routine_time)
        
        # keep track of which components have finished
        BaselineComponents = [fixation_cross]
        for thisComponent in BaselineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BaselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Baseline"-------
        while continueRoutine:
            # get current time
            t = BaselineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BaselineClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross* updates
            if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.tStart = t  # local t and not account for scr refresh
                fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                fixation_cross.setAutoDraw(True)
            # check if timer is over
            if (loopClock.getTime() >0):
                continueRoutine = False 
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BaselineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Baseline"-------
        for thisComponent in BaselineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # reset Clock
        loopClock.reset()
        thisExp.addData('basline.time', routine_time)
        # the Routine "Baseline" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "QuestionsTest"-------
        continueRoutine = True
        routineTimer.add(15.000000)
        # update component parameters for each repeat
        # get question to display on screen
        num_quest = trials_quest.thisN
        question.text = str(questions[num_quest][1])
        
        # write selected question to data
        thisExp.addData('question.id', questions[num_quest][0])
        
        press_key_l2.height = 0.05
        press_key_l2.pos = (-0.12, -0.3)
        press_key_r2.height = 0.05
        press_key_r2.pos = (0, -0.3)
        
        timer_set = False
        question_response.keys = []
        question_response.rt = []
        _question_response_allKeys = []
        continueRoutine = True
        # configure visual timer
        time = 15
        #timer = core.CountdownTimer(time)
        
        # size of line
        timer_line2.size = [1,0.02]
        width = timer_line2.size[0]
        
        # how much the line shrinks each frame
        dist = width/(30*time)
        timer_line2.autoDraw= False
        # keep track of which components have finished
        QuestionsTestComponents = [press_key_l2, press_key_r2, question, question_response, timer_line2]
        for thisComponent in QuestionsTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        QuestionsTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "QuestionsTest"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = QuestionsTestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=QuestionsTestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *press_key_l2* updates
            if press_key_l2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_key_l2.frameNStart = frameN  # exact frame index
                press_key_l2.tStart = t  # local t and not account for scr refresh
                press_key_l2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_key_l2, 'tStartRefresh')  # time at next scr refresh
                press_key_l2.setAutoDraw(True)
            if press_key_l2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > press_key_l2.tStartRefresh + 15.0-frameTolerance:
                    # keep track of stop time/frame for later
                    press_key_l2.tStop = t  # not accounting for scr refresh
                    press_key_l2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(press_key_l2, 'tStopRefresh')  # time at next scr refresh
                    press_key_l2.setAutoDraw(False)
            
            # *press_key_r2* updates
            if press_key_r2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_key_r2.frameNStart = frameN  # exact frame index
                press_key_r2.tStart = t  # local t and not account for scr refresh
                press_key_r2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_key_r2, 'tStartRefresh')  # time at next scr refresh
                press_key_r2.setAutoDraw(True)
            if press_key_r2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > press_key_r2.tStartRefresh + 15.0-frameTolerance:
                    # keep track of stop time/frame for later
                    press_key_r2.tStop = t  # not accounting for scr refresh
                    press_key_r2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(press_key_r2, 'tStopRefresh')  # time at next scr refresh
                    press_key_r2.setAutoDraw(False)
            
            # *question* updates
            if question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question.frameNStart = frameN  # exact frame index
                question.tStart = t  # local t and not account for scr refresh
                question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
                question.setAutoDraw(True)
            if question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > question.tStartRefresh + 15.0-frameTolerance:
                    # keep track of stop time/frame for later
                    question.tStop = t  # not accounting for scr refresh
                    question.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(question, 'tStopRefresh')  # time at next scr refresh
                    question.setAutoDraw(False)
            if question_response.keys and not timer_set:
                # right key
                if 'right' in question_response.keys:
                    press_key_r2.height = 0.08
                    press_key_r2.pos = (0, -0.29)
                # left key
                if 'left' in question_response.keys:
                    press_key_l2.height = 0.08
                    press_key_l2.pos = (-0.12, -0.29)
                # set timer
                text_clock = core.Clock()
                text_clock.add(1)
                timer_set = True
                
            if timer_set:
                if text_clock.getTime()<0:
                    pass
                else:
                    continueRoutine = False
            
            # *question_response* updates
            if question_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_response.frameNStart = frameN  # exact frame index
                question_response.tStart = t  # local t and not account for scr refresh
                question_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_response, 'tStartRefresh')  # time at next scr refresh
                question_response.status = STARTED
                # keyboard checking is just starting
                question_response.clock.reset()  # now t=0
                question_response.clearEvents(eventType='keyboard')
            if question_response.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 15.0-frameTolerance:
                    # keep track of stop time/frame for later
                    question_response.tStop = t  # not accounting for scr refresh
                    question_response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(question_response, 'tStopRefresh')  # time at next scr refresh
                    question_response.status = FINISHED
            if question_response.status == STARTED:
                theseKeys = question_response.getKeys(keyList=['left', 'right'], waitRelease=False)
                _question_response_allKeys.extend(theseKeys)
                if len(_question_response_allKeys):
                    question_response.keys = _question_response_allKeys[-1].name  # just the last key pressed
                    question_response.rt = _question_response_allKeys[-1].rt
            
            # *timer_line2* updates
            if timer_line2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer_line2.frameNStart = frameN  # exact frame index
                timer_line2.tStart = t  # local t and not account for scr refresh
                timer_line2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer_line2, 'tStartRefresh')  # time at next scr refresh
                timer_line2.setAutoDraw(True)
            if timer_line2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timer_line2.tStartRefresh + 15.0-frameTolerance:
                    # keep track of stop time/frame for later
                    timer_line2.tStop = t  # not accounting for scr refresh
                    timer_line2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(timer_line2, 'tStopRefresh')  # time at next scr refresh
                    timer_line2.setAutoDraw(False)
            #while timer.getTime() > 0 and continueRoutine:
                # adjust line size to visualize time
            width -= dist
            timer_line2.size = [width,0.02]
            timer_line2.draw()
                
            """
            # check if response was given
            keys = event.getKeys()
            if keys: 
                if 'right' in keys: 
                    continueRoutine = False
                if 'left' in keys: 
                    continueRoutine = False
            """        
            win.flip()
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in QuestionsTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "QuestionsTest"-------
        for thisComponent in QuestionsTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_quest.addData('press_key_l2.started', press_key_l2.tStartRefresh)
        trials_quest.addData('press_key_l2.stopped', press_key_l2.tStopRefresh)
        text_clock.reset()
        # check responses
        if question_response.keys in ['', [], None]:  # No response was made
            question_response.keys = None
        trials_quest.addData('question_response.keys',question_response.keys)
        if question_response.keys != None:  # we had a response
            trials_quest.addData('question_response.rt', question_response.rt)
        # check if question limit is reached
        if trials_quest.thisN >= (trials_limit-1):
            trials_quest.finished = True
        thisExp.nextEntry()
        
    # completed 4.0 repeats of 'trials_quest'
    
    
    # ------Prepare to start Routine "Save_Data"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Save_DataComponents = []
    for thisComponent in Save_DataComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Save_DataClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Save_Data"-------
    while continueRoutine:
        # get current time
        t = Save_DataClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Save_DataClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Save_DataComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Save_Data"-------
    for thisComponent in Save_DataComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Save_Data" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials_instruct_quest'


# set up handler to look after randomisation of conditions etc
trials_instruct_num2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_instruct_num2')
thisExp.addLoop(trials_instruct_num2)  # add the loop to the experiment
thisTrials_instruct_num2 = trials_instruct_num2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_instruct_num2.rgb)
if thisTrials_instruct_num2 != None:
    for paramName in thisTrials_instruct_num2:
        exec('{} = thisTrials_instruct_num2[paramName]'.format(paramName))

for thisTrials_instruct_num2 in trials_instruct_num2:
    currentLoop = trials_instruct_num2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_instruct_num2.rgb)
    if thisTrials_instruct_num2 != None:
        for paramName in thisTrials_instruct_num2:
            exec('{} = thisTrials_instruct_num2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructions_space.keys = []
    instructions_space.rt = []
    _instructions_space_allKeys = []
    # depending on the oder decided in the beginning
    # edit the displayed text and write to output file
    numbers_rand =[]
    trials_limit = 20
    option = 'number'
    number_r = 0
    if reihenfolge:
        number_r = trials_instruct_num.thisN
    else:
        number_r = trials_instruct_num2.thisN
    
    if order[number_r] == 0:
        instructions_text.text  = "In the following, you will be asked if the number in the middle is greater than 10.\n \nPlease always lie! \n \nPress 'space' to start"
        thisExp.addData('numbers.instructions', 'lie')
        mode = 'lie'
        numbers_rand = gen_rand_list()
    if order[number_r] == 1:
        instructions_text.text  = "In the following, you will be asked if the number in the middle is greater than 10.\n \nPlease always tell the truth! \n \nPress 'space' to start"
        thisExp.addData('numbers.instructions', 'truth')
        numbers_rand = gen_rand_list()
        mode = 'truth'
    if order[number_r] == 2:
        instructions_text.text  = "In the following, you will be asked if the number in the middle is greater than 10.\n \nYou can choose to lie or tell the truth! \n \nPress 'space' to start"
        thisExp.addData('numbers.instructions', 'choice')
        numbers_rand = gen_rand_list()
        numbers_rand. extend(gen_rand_list())
        trials_limit = 40
        mode = 'choice'
    
    # randomize numbers
    random.shuffle(numbers_rand)
    print(numbers_rand)
    
    # keep track of which components have finished
    InstructionsComponents = [instructions_text, instructions_space]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_text.frameNStart = frameN  # exact frame index
            instructions_text.tStart = t  # local t and not account for scr refresh
            instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            instructions_text.setAutoDraw(True)
        
        # *instructions_space* updates
        if instructions_space.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_space.frameNStart = frameN  # exact frame index
            instructions_space.tStart = t  # local t and not account for scr refresh
            instructions_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_space, 'tStartRefresh')  # time at next scr refresh
            instructions_space.status = STARTED
            # keyboard checking is just starting
            instructions_space.clock.reset()  # now t=0
        if instructions_space.status == STARTED:
            theseKeys = instructions_space.getKeys(keyList=['space'], waitRelease=False)
            _instructions_space_allKeys.extend(theseKeys)
            if len(_instructions_space_allKeys):
                instructions_space.keys = _instructions_space_allKeys[-1].name  # just the last key pressed
                instructions_space.rt = _instructions_space_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if instructions_space.keys in ['', [], None]:  # No response was made
        instructions_space.keys = None
    trials_instruct_num2.addData('instructions_space.keys',instructions_space.keys)
    if instructions_space.keys != None:  # we had a response
        trials_instruct_num2.addData('instructions_space.rt', instructions_space.rt)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_num2 = data.TrialHandler(nReps=4.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_num2')
    thisExp.addLoop(trials_num2)  # add the loop to the experiment
    thisTrials_num2 = trials_num2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_num2.rgb)
    if thisTrials_num2 != None:
        for paramName in thisTrials_num2:
            exec('{} = thisTrials_num2[paramName]'.format(paramName))
    
    for thisTrials_num2 in trials_num2:
        currentLoop = trials_num2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_num2.rgb)
        if thisTrials_num2 != None:
            for paramName in thisTrials_num2:
                exec('{} = thisTrials_num2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Baseline"-------
        continueRoutine = True
        # update component parameters for each repeat
        # timer to randomise time of routine
        loopClock = core.Clock()
        routine_time = randint(2,5)
        loopClock.add(routine_time)
        
        # keep track of which components have finished
        BaselineComponents = [fixation_cross]
        for thisComponent in BaselineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BaselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Baseline"-------
        while continueRoutine:
            # get current time
            t = BaselineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BaselineClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross* updates
            if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.tStart = t  # local t and not account for scr refresh
                fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                fixation_cross.setAutoDraw(True)
            # check if timer is over
            if (loopClock.getTime() >0):
                continueRoutine = False 
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BaselineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Baseline"-------
        for thisComponent in BaselineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # reset Clock
        loopClock.reset()
        thisExp.addData('basline.time', routine_time)
        # the Routine "Baseline" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "NumberTest"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        corResp = ''
        press_key_l.height = 0.05
        press_key_l.pos = (-0.12, -0.3)
        press_key_r.height = 0.05
        press_key_r.pos = (0, -0.3)
        
        # select number from list generated in the introduction
        ind = 0
        if reihenfolge:
            ind = trials_num.thisN
        else: 
            ind = trials_num2.thisN
        num = numbers_rand[ind]
           
        # write generated number to data
        thisExp.addData('num_test.value', num)
        
        # generate correct response (always truth)
        if num > 10:
            corResp = 'right'
        else:
            corResp = 'left'
        
        num_test.text = str(num)
        
        # set arrow timer
        timer_set = False
        # configure visual timer
        t = 5
        
        #timer = core.Clock()
        #timer.add(t)
        
        #timer = core.CountdownTimer(t)
        
        # size of line
        timer_line.size = [1,0.02]
        width = timer_line.size[0]
        
        # how much the line shrinks each frame
        dist = width/(30*t)
        timer_line.autoDraw= False
        arrow_response.keys = []
        arrow_response.rt = []
        _arrow_response_allKeys = []
        # keep track of which components have finished
        NumberTestComponents = [question_1, press_key_r, press_key_l, num_test, timer_line, arrow_response]
        for thisComponent in NumberTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        NumberTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "NumberTest"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = NumberTestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=NumberTestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_1* updates
            if question_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_1.frameNStart = frameN  # exact frame index
                question_1.tStart = t  # local t and not account for scr refresh
                question_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_1, 'tStartRefresh')  # time at next scr refresh
                question_1.setAutoDraw(True)
            if question_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > question_1.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    question_1.tStop = t  # not accounting for scr refresh
                    question_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(question_1, 'tStopRefresh')  # time at next scr refresh
                    question_1.setAutoDraw(False)
            
            # *press_key_r* updates
            if press_key_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_key_r.frameNStart = frameN  # exact frame index
                press_key_r.tStart = t  # local t and not account for scr refresh
                press_key_r.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_key_r, 'tStartRefresh')  # time at next scr refresh
                press_key_r.setAutoDraw(True)
            if press_key_r.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > press_key_r.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    press_key_r.tStop = t  # not accounting for scr refresh
                    press_key_r.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(press_key_r, 'tStopRefresh')  # time at next scr refresh
                    press_key_r.setAutoDraw(False)
            
            # *press_key_l* updates
            if press_key_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_key_l.frameNStart = frameN  # exact frame index
                press_key_l.tStart = t  # local t and not account for scr refresh
                press_key_l.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_key_l, 'tStartRefresh')  # time at next scr refresh
                press_key_l.setAutoDraw(True)
            if press_key_l.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > press_key_l.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    press_key_l.tStop = t  # not accounting for scr refresh
                    press_key_l.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(press_key_l, 'tStopRefresh')  # time at next scr refresh
                    press_key_l.setAutoDraw(False)
            
            # *num_test* updates
            if num_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                num_test.frameNStart = frameN  # exact frame index
                num_test.tStart = t  # local t and not account for scr refresh
                num_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num_test, 'tStartRefresh')  # time at next scr refresh
                num_test.setAutoDraw(True)
            if num_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > num_test.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    num_test.tStop = t  # not accounting for scr refresh
                    num_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(num_test, 'tStopRefresh')  # time at next scr refresh
                    num_test.setAutoDraw(False)
            if arrow_response.keys and not timer_set:
                # right key
                if 'right' in arrow_response.keys:
                    press_key_r.height = 0.08
                    press_key_r.pos = (0, -0.29)
                # left key
                if 'left' in arrow_response.keys:
                    press_key_l.height = 0.08
                    press_key_l.pos = (-0.12, -0.29)
                # set timer
                text_clock = core.Clock()
                text_clock.add(1)
                timer_set = True
                
            if timer_set:
                if text_clock.getTime()<0:
                    pass
                else:
                    continueRoutine = False
            
            # *timer_line* updates
            if timer_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer_line.frameNStart = frameN  # exact frame index
                timer_line.tStart = t  # local t and not account for scr refresh
                timer_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer_line, 'tStartRefresh')  # time at next scr refresh
                timer_line.setAutoDraw(True)
            if timer_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timer_line.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    timer_line.tStop = t  # not accounting for scr refresh
                    timer_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(timer_line, 'tStopRefresh')  # time at next scr refresh
                    timer_line.setAutoDraw(False)
            #if timer.getTime() > 0 and continueRoutine:
            # adjust line size to visualize time
            width -= dist
            timer_line.size = [width,0.02]
            timer_line.draw()
            win.flip()
                    
            # check if response was given 
            """
                keys = event.getKeys()
                if keys: 
                    if 'right' in keys: 
                        rt = arrow_response.rt
                        print(rt)
                        continueRoutine = False
                    if 'left' in keys: 
                        rt = arrow_response.rt
                        print(rt)
                        continueRoutine = False
            """      
                        
            
                
            
            
            
            # *arrow_response* updates
            if arrow_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow_response.frameNStart = frameN  # exact frame index
                arrow_response.tStart = t  # local t and not account for scr refresh
                arrow_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_response, 'tStartRefresh')  # time at next scr refresh
                arrow_response.status = STARTED
                # keyboard checking is just starting
                arrow_response.clock.reset()  # now t=0
                arrow_response.clearEvents(eventType='keyboard')
            if arrow_response.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow_response.tStop = t  # not accounting for scr refresh
                    arrow_response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(arrow_response, 'tStopRefresh')  # time at next scr refresh
                    arrow_response.status = FINISHED
            if arrow_response.status == STARTED:
                theseKeys = arrow_response.getKeys(keyList=['left', 'right'], waitRelease=False)
                _arrow_response_allKeys.extend(theseKeys)
                if len(_arrow_response_allKeys):
                    arrow_response.keys = _arrow_response_allKeys[-1].name  # just the last key pressed
                    arrow_response.rt = _arrow_response_allKeys[-1].rt
                    # was this correct?
                    if (arrow_response.keys == str(corResp)) or (arrow_response.keys == corResp):
                        arrow_response.corr = 1
                    else:
                        arrow_response.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NumberTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "NumberTest"-------
        for thisComponent in NumberTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_num2.addData('press_key_r.started', press_key_r.tStartRefresh)
        trials_num2.addData('press_key_r.stopped', press_key_r.tStopRefresh)
        text_clock.reset()
        #if trials max is 20 end early 
        if reihenfolge:
            if trials_num.thisN >= (trials_limit-1):
                trials_num.finished = True
        else: 
            if trials_num2.thisN >= (trials_limit-1):
                trials_num2.finished = True
        
        
        #rt = arrow_response.rt
        #print(rt)
        #event.clearEvents()
        # check responses
        if arrow_response.keys in ['', [], None]:  # No response was made
            arrow_response.keys = None
            # was no response the correct answer?!
            if str(corResp).lower() == 'none':
               arrow_response.corr = 1;  # correct non-response
            else:
               arrow_response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_num2 (TrialHandler)
        trials_num2.addData('arrow_response.keys',arrow_response.keys)
        trials_num2.addData('arrow_response.corr', arrow_response.corr)
        if arrow_response.keys != None:  # we had a response
            trials_num2.addData('arrow_response.rt', arrow_response.rt)
        thisExp.nextEntry()
        
    # completed 4.0 repeats of 'trials_num2'
    
    
    # ------Prepare to start Routine "Save_Data"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Save_DataComponents = []
    for thisComponent in Save_DataComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Save_DataClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Save_Data"-------
    while continueRoutine:
        # get current time
        t = Save_DataClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Save_DataClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Save_DataComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Save_Data"-------
    for thisComponent in Save_DataComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Save_Data" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_instruct_num2'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [end]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end* updates
    if end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end.frameNStart = frameN  # exact frame index
        end.tStart = t  # local t and not account for scr refresh
        end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end, 'tStartRefresh')  # time at next scr refresh
        end.setAutoDraw(True)
    if end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            end.tStop = t  # not accounting for scr refresh
            end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end, 'tStopRefresh')  # time at next scr refresh
            end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
