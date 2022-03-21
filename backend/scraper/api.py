#Pull data from the Penn Registrar API on course size, timing, etc.


from penn import Registrar
import pandas as pd

username = "UPENN_OD_enLg_1005584"
password = "su1m2vc650cip78bdsqnrtkoar"

r = Registrar("UPENN_OD_enLg_1005584", "su1m2vc650cip78bdsqnrtkoar")

allCourses = []

courses = r.search({'course_level_at_or_below': "800"})

for courseData in courses:
    description = courseData["course_description"]
    department = courseData["course_department"]
    courseNumber = courseData["course_number"]
    instructor = courseData["instructors"][0]["name"] if courseData["instructors"] else "NA"
    section = courseData["section_id_normalized"].split("-")[-1]
    meetingDays = courseData["meetings"][0]["meeting_days"] if courseData["meetings"] else "NA"
    startTime = courseData["meetings"][0]["start_time"] if courseData["meetings"] else "NA"
    endTime = courseData["meetings"][0]["end_time"] if courseData["meetings"] else "NA"
    recitations = " ".join([department + "-" + courseNumber + "-" + rec["section_id"] for rec in courseData["recitations"]])
    labs = " ".join([department + "-" + lab["course_id"] + "-" + lab["section_id"] for lab in courseData["labs"]])
    allCourses.append([department, courseNumber, instructor, section, meetingDays, startTime, endTime, recitations, labs])

df = pd.DataFrame(allCourses, columns=["Dept", "Number", "Instructor", "Section", "Days", "Start", "End", "Recitations", "Labs"])
df.to_csv("test.csv", index=False)
