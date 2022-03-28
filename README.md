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