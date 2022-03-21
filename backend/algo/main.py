import itertools
from datetime import datetime as dt
import pandas as pd
import numpy as np

def common_element(list1, list2):
    #Converts both lists to sets, which cannot have duplicates.
    #If the intersection of the two sets is greater than 0, then the two lists have a common element.
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.intersection(set2)) > 0

def compare_times(time1, time2):
    #Convert both of the times into datetime objects, which filters AM/PM among other things.
    #Return whether the first time is greater (after) the second.
    dt1 = dt.strptime(time1, "%I:%M%p")
    dt2 = dt.strptime(time2, "%I:%M%p")
    return dt1 >= dt2

def is_overlap(slot1, slot2):
    # Find what days each of the class's time slots fall upon
    days1 = slot1[2].split("-")
    days2 = slot2[2].split("-")
    # If the two classes never meet on the same day, we automatically know they can't overlap.
    if not common_element(days1, days2):
        return False
    
    #First, check if second class's start time is after the first one's
    if compare_times(slot2[0], slot1[0]):
        #Check if the second class starts after the first one ends to determine overlap
        if compare_times(slot2[0], slot1[1]):
            return False
        else:
            return True
    # If first class's start time is after the second one's.
    else:
        #Check whether the first class's start time is after the second one's end time.
        if compare_times(slot1[0], slot2[1]):
            return False
        else:
            return True

def all_schedules(timetable):
    all_slots = list(timetable.values())
    possible = list(itertools.product(*all_slots))
    return possible

def find_class_names(timetable):
    return list(timetable.keys())

def build_schedules(possible):
    schedules = []
    #For every possible schedule involving all of the desired classes,
    for schedule in possible:
        ignore_schedule = 0
        for combination in itertools.combinations(schedule, 2):
            #Go through every pair of classes in the schedule, ignore a schedule if  pair of classes overlap in it.
            if is_overlap(combination[0], combination[1]):
                ignore_schedule = 1
                break
        if ignore_schedule == 0:
            schedules.append(schedule)
    return schedules

def rank_morningtime(schedule):
    sched_array = np.asarray(schedule)
    startTimes = sched_array[:, 0]
    numMorningClasses = np.count_nonzero(startTimes=="8:30AM")
    return numMorningClasses


class_times = {"biol_121": [("10:15AM", "11:45AM", "M-W-F", "101")], 
               "cis_120": [("10:30AM", "11:30AM", "M-W-F", "101"), ("12:00PM", "1:00PM", "M-W-F", "101")],
               "cis_160": [("8:30AM", "10:00AM", "T-R", "101"), ("10:15AM", "11:45AM", "T-R", "101")],
               "biol_123": [("12:00PM", "3:00PM", "R", "101"), ("8:30AM", "11:30AM", "R", "102")],
               "stat_430": [("3:30PM", "5:00PM", "T-R", "101"), ("5:15PM", "6:45PM", "T-R", "101")],
               "writ_020": [("3:30PM", "5:00PM", "M-W", "101")],
               "cis_120_r": [("5:15PM", "6:15PM", "W", "101")],
               "biol_123_r": [("8:30AM", "9:30AM", "F", "101")],
               "cis_160_r": [("3:30PM", "4:30PM", "F", "101")],
               }

class_names = find_class_names(class_times)

all = all_schedules(class_times)

schedules = build_schedules(all)

num_schedules = len(schedules)

print (f"You have {num_schedules} different options for schedules.\n")
for printed_sched in schedules:
    numMorning = rank_morningtime(printed_sched)
    print (f"This schedule features {numMorning} 8:30 classes.")
    for class_slot in range(len(printed_sched)):
        class_name = class_names[class_slot]
        timing = f"{printed_sched[class_slot][0]}-{printed_sched[class_slot][1]}"
        days = printed_sched[class_slot][2]
        section = printed_sched[class_slot][3]
        print (f"{class_name} Section {section}: {timing} on {days}")
    print ("\n")
