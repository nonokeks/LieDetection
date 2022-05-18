#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Mai 18, 2022, at 13:44
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
    size=(1024, 768), fullscr=True, screen=0, 
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
    text="Wellcome!\n\nThis is an experiement about lie detection.\n\nPress 'space' to continue",
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text="In the following, you will be asked if the number in the middle is greater than 10.\n\nPlease always lie!\n\nPress 'space' to start",
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_space = keyboard.Keyboard()
# here you can change the order in 
# which they should lie, tell truth or choose

# lie = 0, truth = 1, choorse = 2

order = [2, 1, 0]

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
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
press_key = visual.TextStim(win=win, name='press_key',
    text='"←" No         Yes "→" ',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);
num_test = visual.TextStim(win=win, name='num_test',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
import random 
timer_line = visual.Line(
    win=win, name='timer_line',
    start=(-(1,0.02)[0]/2.0, 0), end=(+(1,0.02)[0]/2.0, 0),
    ori=0.0, pos=(0, -0.45),
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
import time
import sys
from psychopy import event
arrow_response = keyboard.Keyboard()

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
trials_instruct = data.TrialHandler(nReps=3.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_instruct')
thisExp.addLoop(trials_instruct)  # add the loop to the experiment
thisTrials_instruct = trials_instruct.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_instruct.rgb)
if thisTrials_instruct != None:
    for paramName in thisTrials_instruct:
        exec('{} = thisTrials_instruct[paramName]'.format(paramName))

for thisTrials_instruct in trials_instruct:
    currentLoop = trials_instruct
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_instruct.rgb)
    if thisTrials_instruct != None:
        for paramName in thisTrials_instruct:
            exec('{} = thisTrials_instruct[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructions_space.keys = []
    instructions_space.rt = []
    _instructions_space_allKeys = []
    if order[trials_instruct.thisN] == 0:
        instructions_text.text  = "In the following, you will be asked if the number in the middle is greater than 10.\n \nPlease always lie! \n \nPress 'space' to start"
        
    if order[trials_instruct.thisN] == 1:
        instructions_text.text  = "In the following, you will be asked if the number in the middle is greater than 10.\n \nPlease always tell the truth! \n \nPress 'space' to start"
        
    if order[trials_instruct.thisN] == 2:
        instructions_text.text  = "In the following, you will be asked if the number in the middle is greater than 10.\n \nYou can choose to lie or tell the truth! \n \nPress 'space' to start"
        
    #instruct = visual.TextBox2(win, text=instructions_text1, font='Open Sans', letterHeight=50, color="white", alignment='center', pos=(0,0), size=[None, None], units='pix',bold=True)
    #instruct.autoDraw = True
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
    trials_instruct.addData('instructions_space.keys',instructions_space.keys)
    if instructions_space.keys != None:  # we had a response
        trials_instruct.addData('instructions_space.rt', instructions_space.rt)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Baseline"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
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
        while continueRoutine and routineTimer.getTime() > 0:
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
            if fixation_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross.tStop = t  # not accounting for scr refresh
                    fixation_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
                    fixation_cross.setAutoDraw(False)
            
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
        
        # ------Prepare to start Routine "NumberTest"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        # generate a random number to be displayed which is not 10
        num = 10
        corResp = ''
        while num == 10:
            num = random.randint(0,20)
            
        # write generated number to data
        thisExp.addData('num_test.value', num)
        
        # generate correct response (always truth)
        if num > 10:
            corResp = 'right'
        else:
            corResp = 'left'
        
        num_test.text = str(num)
        
        # configure visual timer
        time = 5
        timer = core.CountdownTimer(time)
        
        # size of line
        timer_line.size = [1,0.02]
        width = timer_line.size[0]
        
        # how much the line shrinks each frame
        dist = width/(60.5*time)
        timer_line.autoDraw= False
        arrow_response.keys = []
        arrow_response.rt = []
        _arrow_response_allKeys = []
        # keep track of which components have finished
        NumberTestComponents = [question_1, press_key, num_test, timer_line, arrow_response]
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
            
            # *press_key* updates
            if press_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_key.frameNStart = frameN  # exact frame index
                press_key.tStart = t  # local t and not account for scr refresh
                press_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_key, 'tStartRefresh')  # time at next scr refresh
                press_key.setAutoDraw(True)
            if press_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > press_key.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    press_key.tStop = t  # not accounting for scr refresh
                    press_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(press_key, 'tStopRefresh')  # time at next scr refresh
                    press_key.setAutoDraw(False)
            
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
            while timer.getTime() > 0 and continueRoutine:
                # adjust line size to visualize time
                width -= dist
                timer_line.size = [width,0.02]
                timer_line.draw()
                    
                # check if response was given
                keys = event.getKeys()
                if keys: 
                    if 'right' in keys: 
                        continueRoutine = False
                    if 'left' in keys: 
                        continueRoutine = False
                        
                win.flip()
            
            
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
                    # a response ends the routine
                    continueRoutine = False
            
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
        # check responses
        if arrow_response.keys in ['', [], None]:  # No response was made
            arrow_response.keys = None
            # was no response the correct answer?!
            if str(corResp).lower() == 'none':
               arrow_response.corr = 1;  # correct non-response
            else:
               arrow_response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('arrow_response.keys',arrow_response.keys)
        trials.addData('arrow_response.corr', arrow_response.corr)
        if arrow_response.keys != None:  # we had a response
            trials.addData('arrow_response.rt', arrow_response.rt)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials_instruct'


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
