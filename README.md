# Participant Signup

**Participant Signup** is a simple Django app for rendering form that sends participant entry on events/contest.

![Sample](screenshot.png)

## Quick start

### 1. Add "apps.participant_signup" to your `INSTALLED_APPS` setting like this:
	
```
#!python
INSTALLED_APPS = (
	...
	'apps.participant_signup',
)
```

### 2. To test locally, open a new terminal then run this command (Python built-in SMTP server listening on port 1025 of localhost), or if you are using other SMTP server just skip this part:

```
#!python
    python -m smtpd -n -c DebuggingServer localhost:1025
```

### 3. For meta-world testing, set Email configuration on settings.py:

```
#!python
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
```

### 4. For real-world testing, set Email configuration on settings.py (in this example i'm using GMail SMTP server):

```
#!python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'youremailpassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

### 5. Include the participant_signup URLconf in your project `urls.py` like this:

```
#!python
    url(r'^participant-signup/', include('apps.participant_signup.urls')),
```

and also add static file dir for user-uploaded files, it should look something like this:

```
#!python
    urlpatterns = patterns('',
    	url(r'^admin/', include(admin.site.urls)),
    	url(r'^media/(.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
    	(r'^participant-signup/', include('apps.participant_signup.urls')),
	) + static(settings.MEDIA_URL, PROJECT_ROOT=settings.MEDIA_ROOT)
```

### 6. Also include file upload restrictions on settings.py:

```
#!python
	# Limit file uploads
	# 2.5MB - 2621440
	# 5MB - 5242880
	# 10MB - 10485760
	# 20MB - 20971520
	# 50MB - 52428800
	# 100MB 104857600
	# 250MB - 214958080
	# 500MB - 429916160
	FILE_UPLOAD_TYPES = ['image/jpeg', 'image/png']
	FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880
```

### 7. Add extra customization on admin view (CSS & JS for Admin media viewer):

```
#!python
    STATIC_URL = '/theme/'

	STATICFILES_DIRS = (
	    PROJECT_ROOT.child('apps').child('participant_signup').child('theme'),
	)
```

### 8. Run `python manage.py syncdb` to create the participant_signup models.

### 9. Run `python manage.py runserver` then Visit `http://127.0.0.1:8000/participant-signup/` to view the Participant Signup form.

### 10. To check Participant(s), visit Admin `http://127.0.0.1:8000/participant-signup/admin/`