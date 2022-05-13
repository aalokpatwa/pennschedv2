# pennschedv2

# Problem

Course planning is a well-known struggle for Penn students. Deciding what courses to take is the easy part; actually selecting the correct time slots such that all your desired courses fit together is where it gets tough. Every student wants to avoid 8:30 classes, leave time for lunch, and reserve a time slot for their club meetings.  

Existing methods like Penn CoursePlan are excellent for visualizing your course schedule, but don't actually help put it together.  
That's where PennSched comes in: simply select your list of desired courses and the algorithm will show you all of the possible schedules that work, ranked according to latest start time, earliest end time, or whatever metric you personally care about.

Our goal is to cut the time that each Penn student spends putting together their schedule by 10x. Try it out for yourself!

## Basic Setup

### If in production:
1. Make sure you the `DJANGO_SETTINGS_MODULE` environemnt variable to `pennsched.settings.production`
   1. (this is not currently configured)

### If in development:
1. Install from `requirements.txt`
2. Run migrations: 
 ```
 python manage.py migrate  
 python manage.py makemigrations
 ```

## Development
1. When creating viewsets, add them to the router in `schedv2.urls`
2. When creating views directly add them to `schedv2.urls.url_patterns`
3. When importing, treat `backend` as the root folder (configure your IDE!)
   1. `from pennschedv2.backend.schedv2 ...` :x:
   2. `from backend.schedv2 ...` :x:
   3. `from schedv2 ...` :white_check_mark:
4. If there are errors telling you there is no table for a model, even after running `migrate` and `makemigrations`, try the following:
   ```
   manage.py migrate --run-syncdb
   ```
