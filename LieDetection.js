/********************* 
 * Liedetection Test *
 *********************/

import { PsychoJS } from './lib/core-2021.1.4.js';
import * as core from './lib/core-2021.1.4.js';
import { TrialHandler } from './lib/data-2021.1.4.js';
import { Scheduler } from './lib/util-2021.1.4.js';
import * as visual from './lib/visual-2021.1.4.js';
import * as sound from './lib/sound-2021.1.4.js';
import * as util from './lib/util-2021.1.4.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'LieDetection';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
/* Syntax Error: Fix Python code */
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(StartRoutineBegin());
flowScheduler.add(StartRoutineEachFrame());
flowScheduler.add(StartRoutineEnd());
const trials_instruct_numLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_instruct_numLoopBegin, trials_instruct_numLoopScheduler);
flowScheduler.add(trials_instruct_numLoopScheduler);
flowScheduler.add(trials_instruct_numLoopEnd);
const trials_instruct_questLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_instruct_questLoopBegin, trials_instruct_questLoopScheduler);
flowScheduler.add(trials_instruct_questLoopScheduler);
flowScheduler.add(trials_instruct_questLoopEnd);
const trials_instruct_num2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_instruct_num2LoopBegin, trials_instruct_num2LoopScheduler);
flowScheduler.add(trials_instruct_num2LoopScheduler);
flowScheduler.add(trials_instruct_num2LoopEnd);
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "Start"
  StartClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: "Welcome!\n\nThis is an experiment about lie detection.\n\nPress 'space' to continue",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  reihenfolge = false;
  
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: "In the following, you will be asked if the number in the middle is greater than 10.\n\nPlease always lie!\n\nPress 'space' to start",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instructions_space = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  order = [2, 1, 0];
  function gen_rand_list() {
      var randomlist_1, randomlist_2;
      randomlist_1 = random.sample(util.range(11, 19), 5);
      randomlist_1.extend(random.sample(util.range(11, 19), 5));
      randomlist_2 = random.sample(util.range(1, 9), 5);
      randomlist_2.extend(random.sample(util.range(1, 9), 5));
      randomlist_1.extend(randomlist_2);
      return randomlist_1;
  }
  
  // Initialize components for Routine "Baseline"
  BaselineClock = new util.Clock();
  fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_cross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "NumberTest"
  NumberTestClock = new util.Clock();
  question_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_1',
    text: 'Is the displayed number greater than 10?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  press_key_r = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_key_r',
    text: '                    Yes "→" ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  press_key_l = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_key_l',
    text: '"←" No',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.12), (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  num_test = new visual.TextStim({
    win: psychoJS.window,
    name: 'num_test',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  import * as random from 'random';
  
  timer_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'timer_line', 
    vertices: [[-[1, 0.02][0]/2.0, 0], [+[1, 0.02][0]/2.0, 0]],
    ori: 0.0, pos: [0, (- 0.35)],
    lineWidth: 10.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  import * as time from 'time';
  import {event} from 'psychopy';
  
  arrow_response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Save_Data"
  Save_DataClock = new util.Clock();
  // Initialize components for Routine "Instructions_Quest"
  Instructions_QuestClock = new util.Clock();
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instructions_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  order = [2, 1, 0];
  questions = [];
  questions_emo = read_csv("Question_emotional.csv", ",");
  questions_neu = read_csv("Question_neutral.csv", ";");
  random.shuffle(questions_emo);
  random.shuffle(questions_neu);
  questions_lie = questions_emo.slice(0, 10);
  questions_lie.extend(questions_neu.slice(0, 10));
  questions_truth = questions_emo.slice(10, 20);
  questions_truth.extend(questions_neu.slice(10, 20));
  questions_choice = questions_emo.copy();
  questions_choice.extend(questions_neu.slice(0));
  console.log("lie");
  console.log(questions_lie.length);
  console.log("truth");
  console.log(questions_truth.length);
  console.log("chioce");
  console.log(questions_choice.length);
  
  // Initialize components for Routine "Baseline"
  BaselineClock = new util.Clock();
  fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_cross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "QuestionsTest"
  QuestionsTestClock = new util.Clock();
  press_key_l2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_key_l2',
    text: '"←" No',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.12), (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  press_key_r2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_key_r2',
    text: '                    Yes "→" ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  question = new visual.TextStim({
    win: psychoJS.window,
    name: 'question',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  question_response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  timer_line2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'timer_line2', 
    vertices: [[-[1, 0.02][0]/2.0, 0], [+[1, 0.02][0]/2.0, 0]],
    ori: 0.0, pos: [0, (- 0.35)],
    lineWidth: 10.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "Save_Data"
  Save_DataClock = new util.Clock();
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: "In the following, you will be asked if the number in the middle is greater than 10.\n\nPlease always lie!\n\nPress 'space' to start",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instructions_space = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  order = [2, 1, 0];
  function gen_rand_list() {
      var randomlist_1, randomlist_2;
      randomlist_1 = random.sample(util.range(11, 19), 5);
      randomlist_1.extend(random.sample(util.range(11, 19), 5));
      randomlist_2 = random.sample(util.range(1, 9), 5);
      randomlist_2.extend(random.sample(util.range(1, 9), 5));
      randomlist_1.extend(randomlist_2);
      return randomlist_1;
  }
  
  // Initialize components for Routine "Baseline"
  BaselineClock = new util.Clock();
  fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_cross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "NumberTest"
  NumberTestClock = new util.Clock();
  question_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_1',
    text: 'Is the displayed number greater than 10?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  press_key_r = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_key_r',
    text: '                    Yes "→" ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  press_key_l = new visual.TextStim({
    win: psychoJS.window,
    name: 'press_key_l',
    text: '"←" No',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.12), (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  num_test = new visual.TextStim({
    win: psychoJS.window,
    name: 'num_test',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  import * as random from 'random';
  
  timer_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'timer_line', 
    vertices: [[-[1, 0.02][0]/2.0, 0], [+[1, 0.02][0]/2.0, 0]],
    ori: 0.0, pos: [0, (- 0.35)],
    lineWidth: 10.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  import * as time from 'time';
  import {event} from 'psychopy';
  
  arrow_response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Save_Data"
  Save_DataClock = new util.Clock();
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  end = new visual.TextStim({
    win: psychoJS.window,
    name: 'end',
    text: 'Thank you for participating!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function StartRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Start'-------
    t = 0;
    StartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    StartComponents = [];
    StartComponents.push(text);
    StartComponents.push(key_resp);
    
    for (const thisComponent of StartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function StartRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Start'-------
    // get current time
    t = StartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp.clock.reset();
      key_resp.start();
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StartComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function StartRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Start'-------
    for (const thisComponent of StartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function trials_instruct_numLoopBegin(trials_instruct_numLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_instruct_num = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_instruct_num'
  });
  psychoJS.experiment.addLoop(trials_instruct_num); // add the loop to the experiment
  currentLoop = trials_instruct_num;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials_instruct_num of trials_instruct_num) {
    const snapshot = trials_instruct_num.getSnapshot();
    trials_instruct_numLoopScheduler.add(importConditions(snapshot));
    trials_instruct_numLoopScheduler.add(InstructionsRoutineBegin(snapshot));
    trials_instruct_numLoopScheduler.add(InstructionsRoutineEachFrame(snapshot));
    trials_instruct_numLoopScheduler.add(InstructionsRoutineEnd(snapshot));
    const trials_numLoopScheduler = new Scheduler(psychoJS);
    trials_instruct_numLoopScheduler.add(trials_numLoopBegin, trials_numLoopScheduler);
    trials_instruct_numLoopScheduler.add(trials_numLoopScheduler);
    trials_instruct_numLoopScheduler.add(trials_numLoopEnd);
    trials_instruct_numLoopScheduler.add(Save_DataRoutineBegin(snapshot));
    trials_instruct_numLoopScheduler.add(Save_DataRoutineEachFrame(snapshot));
    trials_instruct_numLoopScheduler.add(Save_DataRoutineEnd(snapshot));
    trials_instruct_numLoopScheduler.add(endLoopIteration(trials_instruct_numLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function trials_numLoopBegin(trials_numLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_num = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_num'
  });
  psychoJS.experiment.addLoop(trials_num); // add the loop to the experiment
  currentLoop = trials_num;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials_num of trials_num) {
    const snapshot = trials_num.getSnapshot();
    trials_numLoopScheduler.add(importConditions(snapshot));
    trials_numLoopScheduler.add(BaselineRoutineBegin(snapshot));
    trials_numLoopScheduler.add(BaselineRoutineEachFrame(snapshot));
    trials_numLoopScheduler.add(BaselineRoutineEnd(snapshot));
    trials_numLoopScheduler.add(NumberTestRoutineBegin(snapshot));
    trials_numLoopScheduler.add(NumberTestRoutineEachFrame(snapshot));
    trials_numLoopScheduler.add(NumberTestRoutineEnd(snapshot));
    trials_numLoopScheduler.add(endLoopIteration(trials_numLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function trials_numLoopEnd() {
  psychoJS.experiment.removeLoop(trials_num);

  return Scheduler.Event.NEXT;
}

function trials_instruct_numLoopEnd() {
  psychoJS.experiment.removeLoop(trials_instruct_num);

  return Scheduler.Event.NEXT;
}

function trials_instruct_questLoopBegin(trials_instruct_questLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_instruct_quest = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_instruct_quest'
  });
  psychoJS.experiment.addLoop(trials_instruct_quest); // add the loop to the experiment
  currentLoop = trials_instruct_quest;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials_instruct_quest of trials_instruct_quest) {
    const snapshot = trials_instruct_quest.getSnapshot();
    trials_instruct_questLoopScheduler.add(importConditions(snapshot));
    trials_instruct_questLoopScheduler.add(Instructions_QuestRoutineBegin(snapshot));
    trials_instruct_questLoopScheduler.add(Instructions_QuestRoutineEachFrame(snapshot));
    trials_instruct_questLoopScheduler.add(Instructions_QuestRoutineEnd(snapshot));
    const trials_questLoopScheduler = new Scheduler(psychoJS);
    trials_instruct_questLoopScheduler.add(trials_questLoopBegin, trials_questLoopScheduler);
    trials_instruct_questLoopScheduler.add(trials_questLoopScheduler);
    trials_instruct_questLoopScheduler.add(trials_questLoopEnd);
    trials_instruct_questLoopScheduler.add(Save_DataRoutineBegin(snapshot));
    trials_instruct_questLoopScheduler.add(Save_DataRoutineEachFrame(snapshot));
    trials_instruct_questLoopScheduler.add(Save_DataRoutineEnd(snapshot));
    trials_instruct_questLoopScheduler.add(endLoopIteration(trials_instruct_questLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function trials_questLoopBegin(trials_questLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_quest = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_quest'
  });
  psychoJS.experiment.addLoop(trials_quest); // add the loop to the experiment
  currentLoop = trials_quest;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials_quest of trials_quest) {
    const snapshot = trials_quest.getSnapshot();
    trials_questLoopScheduler.add(importConditions(snapshot));
    trials_questLoopScheduler.add(BaselineRoutineBegin(snapshot));
    trials_questLoopScheduler.add(BaselineRoutineEachFrame(snapshot));
    trials_questLoopScheduler.add(BaselineRoutineEnd(snapshot));
    trials_questLoopScheduler.add(QuestionsTestRoutineBegin(snapshot));
    trials_questLoopScheduler.add(QuestionsTestRoutineEachFrame(snapshot));
    trials_questLoopScheduler.add(QuestionsTestRoutineEnd(snapshot));
    trials_questLoopScheduler.add(endLoopIteration(trials_questLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function trials_questLoopEnd() {
  psychoJS.experiment.removeLoop(trials_quest);

  return Scheduler.Event.NEXT;
}

function trials_instruct_questLoopEnd() {
  psychoJS.experiment.removeLoop(trials_instruct_quest);

  return Scheduler.Event.NEXT;
}

function trials_instruct_num2LoopBegin(trials_instruct_num2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_instruct_num2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_instruct_num2'
  });
  psychoJS.experiment.addLoop(trials_instruct_num2); // add the loop to the experiment
  currentLoop = trials_instruct_num2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials_instruct_num2 of trials_instruct_num2) {
    const snapshot = trials_instruct_num2.getSnapshot();
    trials_instruct_num2LoopScheduler.add(importConditions(snapshot));
    trials_instruct_num2LoopScheduler.add(InstructionsRoutineBegin(snapshot));
    trials_instruct_num2LoopScheduler.add(InstructionsRoutineEachFrame(snapshot));
    trials_instruct_num2LoopScheduler.add(InstructionsRoutineEnd(snapshot));
    const trials_num2LoopScheduler = new Scheduler(psychoJS);
    trials_instruct_num2LoopScheduler.add(trials_num2LoopBegin, trials_num2LoopScheduler);
    trials_instruct_num2LoopScheduler.add(trials_num2LoopScheduler);
    trials_instruct_num2LoopScheduler.add(trials_num2LoopEnd);
    trials_instruct_num2LoopScheduler.add(Save_DataRoutineBegin(snapshot));
    trials_instruct_num2LoopScheduler.add(Save_DataRoutineEachFrame(snapshot));
    trials_instruct_num2LoopScheduler.add(Save_DataRoutineEnd(snapshot));
    trials_instruct_num2LoopScheduler.add(endLoopIteration(trials_instruct_num2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function trials_num2LoopBegin(trials_num2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_num2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_num2'
  });
  psychoJS.experiment.addLoop(trials_num2); // add the loop to the experiment
  currentLoop = trials_num2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials_num2 of trials_num2) {
    const snapshot = trials_num2.getSnapshot();
    trials_num2LoopScheduler.add(importConditions(snapshot));
    trials_num2LoopScheduler.add(BaselineRoutineBegin(snapshot));
    trials_num2LoopScheduler.add(BaselineRoutineEachFrame(snapshot));
    trials_num2LoopScheduler.add(BaselineRoutineEnd(snapshot));
    trials_num2LoopScheduler.add(NumberTestRoutineBegin(snapshot));
    trials_num2LoopScheduler.add(NumberTestRoutineEachFrame(snapshot));
    trials_num2LoopScheduler.add(NumberTestRoutineEnd(snapshot));
    trials_num2LoopScheduler.add(endLoopIteration(trials_num2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function trials_num2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_num2);

  return Scheduler.Event.NEXT;
}

function trials_instruct_num2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_instruct_num2);

  return Scheduler.Event.NEXT;
}

function InstructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instructions'-------
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructions_space.keys = undefined;
    instructions_space.rt = undefined;
    _instructions_space_allKeys = [];
    numbers_rand = [];
    trials_limit = 20;
    option = "number";
    number_r = 0;
    if (reihenfolge) {
        number_r = trials_instruct_num.thisN;
    } else {
        number_r = trials_instruct_num2.thisN;
    }
    if ((order[number_r] === 0)) {
        instructions_text.text = "In the following, you will be asked if the number in the middle is greater than 10.\n \nPlease always lie! \n \nPress 'space' to start";
        psychoJS.experiment.addData("numbers.instructions", "lie");
        mode = "lie";
        numbers_rand = gen_rand_list();
    }
    if ((order[number_r] === 1)) {
        instructions_text.text = "In the following, you will be asked if the number in the middle is greater than 10.\n \nPlease always tell the truth! \n \nPress 'space' to start";
        psychoJS.experiment.addData("numbers.instructions", "truth");
        numbers_rand = gen_rand_list();
        mode = "truth";
    }
    if ((order[number_r] === 2)) {
        instructions_text.text = "In the following, you will be asked if the number in the middle is greater than 10.\n \nYou can choose to lie or tell the truth! \n \nPress 'space' to start";
        psychoJS.experiment.addData("numbers.instructions", "choice");
        numbers_rand = gen_rand_list();
        numbers_rand.extend(gen_rand_list());
        trials_limit = 40;
        mode = "choice";
    }
    random.shuffle(numbers_rand);
    console.log(numbers_rand);
    
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(instructions_text);
    InstructionsComponents.push(instructions_space);
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function InstructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instructions'-------
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_text* updates
    if (t >= 0.0 && instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_text.tStart = t;  // (not accounting for frame time here)
      instructions_text.frameNStart = frameN;  // exact frame index
      
      instructions_text.setAutoDraw(true);
    }

    
    // *instructions_space* updates
    if (t >= 0.0 && instructions_space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_space.tStart = t;  // (not accounting for frame time here)
      instructions_space.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      instructions_space.clock.reset();
      instructions_space.start();
    }

    if (instructions_space.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_space.getKeys({keyList: ['space'], waitRelease: false});
      _instructions_space_allKeys = _instructions_space_allKeys.concat(theseKeys);
      if (_instructions_space_allKeys.length > 0) {
        instructions_space.keys = _instructions_space_allKeys[_instructions_space_allKeys.length - 1].name;  // just the last key pressed
        instructions_space.rt = _instructions_space_allKeys[_instructions_space_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function InstructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instructions'-------
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instructions_space.keys', instructions_space.keys);
    if (typeof instructions_space.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructions_space.rt', instructions_space.rt);
        routineTimer.reset();
        }
    
    instructions_space.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function BaselineRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Baseline'-------
    t = 0;
    BaselineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    loopClock = new core.Clock();
    routine_time = util.randint(2, 5);
    loopClock.add(routine_time);
    
    // keep track of which components have finished
    BaselineComponents = [];
    BaselineComponents.push(fixation_cross);
    
    for (const thisComponent of BaselineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function BaselineRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Baseline'-------
    // get current time
    t = BaselineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_cross* updates
    if (t >= 0.0 && fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_cross.tStart = t;  // (not accounting for frame time here)
      fixation_cross.frameNStart = frameN;  // exact frame index
      
      fixation_cross.setAutoDraw(true);
    }

    if ((loopClock.getTime() > 0)) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BaselineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function BaselineRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Baseline'-------
    for (const thisComponent of BaselineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    loopClock.reset();
    psychoJS.experiment.addData("basline.time", routine_time);
    
    // the Routine "Baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function NumberTestRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'NumberTest'-------
    t = 0;
    NumberTestClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    corResp = "";
    press_key_l.height = 0.05;
    press_key_l.pos = [(- 0.12), (- 0.3)];
    press_key_r.height = 0.05;
    press_key_r.pos = [0, (- 0.3)];
    ind = 0;
    if (reihenfolge) {
        ind = trials_num.thisN;
    } else {
        ind = trials_num2.thisN;
    }
    num = numbers_rand[ind];
    thisExp.addData("num_test.value", num);
    if ((num > 10)) {
        corResp = "right";
    } else {
        corResp = "left";
    }
    num_test.text = num.toString();
    timer_set = false;
    
    t = 5;
    timer_line.size = [1, 0.02];
    width = timer_line.size[0];
    dist = (width / (30 * t));
    timer_line.autoDraw = false;
    
    arrow_response.keys = undefined;
    arrow_response.rt = undefined;
    _arrow_response_allKeys = [];
    // keep track of which components have finished
    NumberTestComponents = [];
    NumberTestComponents.push(question_1);
    NumberTestComponents.push(press_key_r);
    NumberTestComponents.push(press_key_l);
    NumberTestComponents.push(num_test);
    NumberTestComponents.push(timer_line);
    NumberTestComponents.push(arrow_response);
    
    for (const thisComponent of NumberTestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function NumberTestRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'NumberTest'-------
    // get current time
    t = NumberTestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_1* updates
    if (t >= 0.0 && question_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_1.tStart = t;  // (not accounting for frame time here)
      question_1.frameNStart = frameN;  // exact frame index
      
      question_1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (question_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      question_1.setAutoDraw(false);
    }
    
    // *press_key_r* updates
    if (t >= 0.0 && press_key_r.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_key_r.tStart = t;  // (not accounting for frame time here)
      press_key_r.frameNStart = frameN;  // exact frame index
      
      press_key_r.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (press_key_r.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      press_key_r.setAutoDraw(false);
    }
    
    // *press_key_l* updates
    if (t >= 0.0 && press_key_l.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_key_l.tStart = t;  // (not accounting for frame time here)
      press_key_l.frameNStart = frameN;  // exact frame index
      
      press_key_l.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (press_key_l.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      press_key_l.setAutoDraw(false);
    }
    
    // *num_test* updates
    if (t >= 0.0 && num_test.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      num_test.tStart = t;  // (not accounting for frame time here)
      num_test.frameNStart = frameN;  // exact frame index
      
      num_test.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (num_test.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      num_test.setAutoDraw(false);
    }
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if ((arrow_response.keys && (! timer_set))) {
        if (_pj.in_es6("right", arrow_response.keys)) {
            press_key_r.height = 0.08;
            press_key_r.pos = [0, (- 0.29)];
        }
        if (_pj.in_es6("left", arrow_response.keys)) {
            press_key_l.height = 0.08;
            press_key_l.pos = [(- 0.12), (- 0.29)];
        }
        text_clock = new core.Clock();
        text_clock.add(1);
        timer_set = true;
    }
    if (timer_set) {
        if ((text_clock.getTime() < 0)) {
        } else {
            continueRoutine = false;
        }
    }
    
    
    // *timer_line* updates
    if (t >= 0.0 && timer_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timer_line.tStart = t;  // (not accounting for frame time here)
      timer_line.frameNStart = frameN;  // exact frame index
      
      timer_line.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (timer_line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      timer_line.setAutoDraw(false);
    }
    width -= dist;
    timer_line.size = [width, 0.02];
    timer_line.draw();
    win.flip();
    /*
    keys = event.getKeys()
    if keys:
    if 'right' in keys:
    rt = arrow_response.rt
    print(rt)
    continueRoutine = False
    if 'left' in keys:
    rt = arrow_response.rt
    print(rt)
    continueRoutine = False*/
    
    
    // *arrow_response* updates
    if (t >= 0.0 && arrow_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arrow_response.tStart = t;  // (not accounting for frame time here)
      arrow_response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      arrow_response.clock.reset();
      arrow_response.start();
      arrow_response.clearEvents();
    }

    frameRemains = 5.0  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((arrow_response.status === PsychoJS.Status.STARTED || arrow_response.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      arrow_response.status = PsychoJS.Status.FINISHED;
  }

    if (arrow_response.status === PsychoJS.Status.STARTED) {
      let theseKeys = arrow_response.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _arrow_response_allKeys = _arrow_response_allKeys.concat(theseKeys);
      if (_arrow_response_allKeys.length > 0) {
        arrow_response.keys = _arrow_response_allKeys[_arrow_response_allKeys.length - 1].name;  // just the last key pressed
        arrow_response.rt = _arrow_response_allKeys[_arrow_response_allKeys.length - 1].rt;
        // was this correct?
        if (arrow_response.keys == corResp) {
            arrow_response.corr = 1;
        } else {
            arrow_response.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NumberTestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function NumberTestRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'NumberTest'-------
    for (const thisComponent of NumberTestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    text_clock.reset();
    if (reihenfolge) {
        if ((trials_num.thisN >= (trials_limit - 1))) {
            trials_num.finished = true;
        }
    } else {
        if ((trials_num2.thisN >= (trials_limit - 1))) {
            trials_num2.finished = true;
        }
    }
    
    /* Syntax Error: Fix Python code */
    // was no response the correct answer?!
    if (arrow_response.keys === undefined) {
      if (['None','none',undefined].includes(corResp)) {
         arrow_response.corr = 1;  // correct non-response
      } else {
         arrow_response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('arrow_response.keys', arrow_response.keys);
    psychoJS.experiment.addData('arrow_response.corr', arrow_response.corr);
    if (typeof arrow_response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('arrow_response.rt', arrow_response.rt);
        }
    
    arrow_response.stop();
    return Scheduler.Event.NEXT;
  };
}

function Save_DataRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Save_Data'-------
    t = 0;
    Save_DataClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    Save_DataComponents = [];
    
    for (const thisComponent of Save_DataComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Save_DataRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Save_Data'-------
    // get current time
    t = Save_DataClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Save_DataComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Save_DataRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Save_Data'-------
    for (const thisComponent of Save_DataComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Save_Data" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function Instructions_QuestRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instructions_Quest'-------
    t = 0;
    Instructions_QuestClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    option = "questions";
    trials_limit = 20;
    if ((order[trials_instruct_quest.thisN] === 0)) {
        instructions_text2.text = "In the following, you will be asked personal questions.\n \nPlease always lie! \n \nPress 'space' to start";
        psychoJS.experiment.addData("questions.instructions", "lie");
        questions = questions_lie.copy();
        mode = "lie";
    }
    if ((order[trials_instruct_quest.thisN] === 1)) {
        instructions_text2.text = "In the following, you will be asked personal questions.\n \nPlease always tell the truth! \n \nPress 'space' to start";
        psychoJS.experiment.addData("questions.instructions", "truth");
        questions = questions_truth.copy();
        mode = "truth";
    }
    if ((order[trials_instruct_quest.thisN] === 2)) {
        instructions_text2.text = "In the following, you will be asked personal questions.\n \nYou can choose to lie or tell the truth! \n \nPress 'space' to start";
        psychoJS.experiment.addData("questions.instructions", "choice");
        questions = questions_choice.copy();
        trials_limit = 40;
        mode = "choice";
    }
    random.shuffle(questions);
    
    // keep track of which components have finished
    Instructions_QuestComponents = [];
    Instructions_QuestComponents.push(key_resp_2);
    Instructions_QuestComponents.push(instructions_text2);
    
    for (const thisComponent of Instructions_QuestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Instructions_QuestRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instructions_Quest'-------
    // get current time
    t = Instructions_QuestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_2.clock.reset();
      key_resp_2.start();
      key_resp_2.clearEvents();
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instructions_text2* updates
    if (t >= 0.0 && instructions_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_text2.tStart = t;  // (not accounting for frame time here)
      instructions_text2.frameNStart = frameN;  // exact frame index
      
      instructions_text2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instructions_QuestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Instructions_QuestRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instructions_Quest'-------
    for (const thisComponent of Instructions_QuestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "Instructions_Quest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function QuestionsTestRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'QuestionsTest'-------
    t = 0;
    QuestionsTestClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    num_quest = trials_quest.thisN;
    question.text = questions[num_quest][1].toString();
    thisExp.addData("question.id", questions[num_quest][0]);
    press_key_l2.height = 0.05;
    press_key_l2.pos = [(- 0.12), (- 0.3)];
    press_key_r2.height = 0.05;
    press_key_r2.pos = [0, (- 0.3)];
    timer_set = false;
    
    question_response.keys = undefined;
    question_response.rt = undefined;
    _question_response_allKeys = [];
    continueRoutine = true;
    time = 10;
    timer_line2.size = [1, 0.02];
    width = timer_line2.size[0];
    dist = (width / (30 * time));
    timer_line2.autoDraw = false;
    
    // keep track of which components have finished
    QuestionsTestComponents = [];
    QuestionsTestComponents.push(press_key_l2);
    QuestionsTestComponents.push(press_key_r2);
    QuestionsTestComponents.push(question);
    QuestionsTestComponents.push(question_response);
    QuestionsTestComponents.push(timer_line2);
    
    for (const thisComponent of QuestionsTestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function QuestionsTestRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'QuestionsTest'-------
    // get current time
    t = QuestionsTestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *press_key_l2* updates
    if (t >= 0.0 && press_key_l2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_key_l2.tStart = t;  // (not accounting for frame time here)
      press_key_l2.frameNStart = frameN;  // exact frame index
      
      press_key_l2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (press_key_l2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      press_key_l2.setAutoDraw(false);
    }
    
    // *press_key_r2* updates
    if (t >= 0.0 && press_key_r2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      press_key_r2.tStart = t;  // (not accounting for frame time here)
      press_key_r2.frameNStart = frameN;  // exact frame index
      
      press_key_r2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (press_key_r2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      press_key_r2.setAutoDraw(false);
    }
    
    // *question* updates
    if (t >= 0.0 && question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question.tStart = t;  // (not accounting for frame time here)
      question.frameNStart = frameN;  // exact frame index
      
      question.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (question.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      question.setAutoDraw(false);
    }
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if ((quest_response.keys && (! timer_set))) {
        if (_pj.in_es6("right", quest_response.keys)) {
            press_key_r2.height = 0.08;
            press_key_r2.pos = [0, (- 0.29)];
        }
        if (_pj.in_es6("left", quest_response.keys)) {
            press_key_l2.height = 0.08;
            press_key_l2.pos = [(- 0.12), (- 0.29)];
        }
        text_clock = new core.Clock();
        text_clock.add(1);
        timer_set = true;
    }
    if (timer_set) {
        if ((text_clock.getTime() < 0)) {
        } else {
            continueRoutine = false;
        }
    }
    
    
    // *question_response* updates
    if (t >= 0.0 && question_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_response.tStart = t;  // (not accounting for frame time here)
      question_response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      question_response.clock.reset();
      question_response.start();
      question_response.clearEvents();
    }

    frameRemains = 10.0  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((question_response.status === PsychoJS.Status.STARTED || question_response.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      question_response.status = PsychoJS.Status.FINISHED;
  }

    if (question_response.status === PsychoJS.Status.STARTED) {
      let theseKeys = question_response.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _question_response_allKeys = _question_response_allKeys.concat(theseKeys);
      if (_question_response_allKeys.length > 0) {
        question_response.keys = _question_response_allKeys[_question_response_allKeys.length - 1].name;  // just the last key pressed
        question_response.rt = _question_response_allKeys[_question_response_allKeys.length - 1].rt;
      }
    }
    
    
    // *timer_line2* updates
    if (t >= 0.0 && timer_line2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timer_line2.tStart = t;  // (not accounting for frame time here)
      timer_line2.frameNStart = frameN;  // exact frame index
      
      timer_line2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (timer_line2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      timer_line2.setAutoDraw(false);
    }
    width -= dist;
    timer_line2.size = [width, 0.02];
    timer_line2.draw();
    /*
    # check if response was given
    keys = event.getKeys()
    if keys:
    if 'right' in keys:
    continueRoutine = False
    if 'left' in keys:
    continueRoutine = False*/
    psychoJS.window.flip();
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of QuestionsTestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function QuestionsTestRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'QuestionsTest'-------
    for (const thisComponent of QuestionsTestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    text_clock.reset();
    
    psychoJS.experiment.addData('question_response.keys', question_response.keys);
    if (typeof question_response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('question_response.rt', question_response.rt);
        }
    
    question_response.stop();
    if ((trials_quest.thisN >= (trials_limit - 1))) {
        trials_quest.finished = true;
    }
    
    return Scheduler.Event.NEXT;
  };
}

function EndRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(end);
    
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function EndRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'End'-------
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end* updates
    if (t >= 0.0 && end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end.tStart = t;  // (not accounting for frame time here)
      end.frameNStart = frameN;  // exact frame index
      
      end.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EndRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'End'-------
    for (const thisComponent of EndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    eye_tracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, {"as_dictionary": true});
    
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
