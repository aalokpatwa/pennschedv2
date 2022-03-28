# pennschedv2

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