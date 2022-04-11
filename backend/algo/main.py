import itertools
from datetime import datetime as dt
import pandas as pd
import numpy as np
import json
from django.forms.models import model_to_dict
from schedv2.models import Meeting, Section, Course

def common_element(list1, list2):
    #Converts both lists to sets, which cannot have duplicates.
    #If the intersection of the two sets is greater than 0, then the two lists have a common element.
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.intersection(set2)) > 0

def compare_times(time1, time2):
    return time1 >= time2

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

def rank_endtime(schedule):
    sched_array = np.asarray(schedule)
    endTimes = sched_array[:, 1]
    numLateClasses = np.count_nonzero(pd.to_datetime(endTimes) > pd.to_datetime("5:00PM"))
    return numLateClasses

def parseDjango(courseSet):
    class_times = {}
    for course in courseSet.iterator():
        className = course.full_code
        if (not className in class_times):
            class_times[className] = []
        sectionNumber = list(Section.objects.filter(course=course).values_list('code'))
        meetingInfo = list(Meeting.objects.filter(section__course=course).values_list('start', 'end', 'days'))
        class_times[className] = [meet + (num,) for num, meet in zip(sectionNumber, meetingInfo)]
    return class_times

def addUserSlots(inputDict, userJson):
    inputDict.update(json.load(userJson))
    return inputDict

def main(courseSet, rankingScheme, inputJson):
    """
    Inputs: courseList: the list of Courses that the student wants to build a schedule for, rankingScheme: a string representing how they would like to rank schedules.
    """

    class_times = parseDjango(courseSet)
    # addUserSlots(class_times, inputJson)

    class_names = find_class_names(class_times)

    # Create all of the possible schedules given the timeslots for each course provided
    all = all_schedules(class_times)

    # Return only the schedules that do not have overlaps
    schedules = build_schedules(all)
    num_schedules = len(schedules)

    schedules.sort(key=rankingScheme)    
    print (f"You have {num_schedules} different options for schedules.\n")

    jsonList = []

    for printed_sched in schedules:
        classesList = []
        for class_slot in range(len(printed_sched)):
            class_name = class_names[class_slot]
            classDict["className"] = class_name

            section = printed_sched[class_slot][3]
            classDict["classSection"] = section

            timing = f"{printed_sched[class_slot][0]}-{printed_sched[class_slot][1]}"
            classDict["classTime"] = timing
            
            days = printed_sched[class_slot][2]
            classDict["classDays"] = days

            summary = f"{class_name} Section {section}: {timing} on {days}"
            classDict["className"]
            classDict["classSummary"] = summary
            classesList.append(classDict)
        jsonList.append(classesList)
    
    return json.dumps(jsonList)

# class_times = {"biol_121": [("10:15AM", "11:45AM", "M-W-F", "101")], 
#                "cis_120": [("10:30AM", "11:30AM", "M-W-F", "101"), ("12:00PM", "1:00PM", "M-W-F", "101")],
#                "cis_160": [("8:30AM", "10:00AM", "T-R", "101"), ("10:15AM", "11:45AM", "T-R", "101")],
#                "biol_123": [("12:00PM", "3:00PM", "R", "101"), ("8:30AM", "11:30AM", "R", "102")],
#                "stat_430": [("3:30PM", "5:00PM", "T-R", "101"), ("5:15PM", "6:45PM", "T-R", "101")],
#                "writ_020": [("3:30PM", "5:00PM", "M-W", "101")],
#                "cis_120_r": [("5:15PM", "6:15PM", "W", "101")],
#                "biol_123_r": [("8:30AM", "9:30AM", "F", "101")],
#                "cis_160_r": [("3:30PM", "4:30PM", "F", "101")],
#                }
# print (main(class_times, rank_morningtime))