## row하게 sql문을 확인하기 => settings.py에 추가

```python
 LOGGING = {
     'version': 1,
     'disable_existing_loggers': False,
     'handlers': {
         'console': {
             'level': 'DEBUG',
             'class': 'logging.StreamHandler',
         }
     },
     'loggers': {
         'django.db.backends': {
             'handlers': ['console'],
             'level': 'DEBUG',
         },
     }
 }
 ```

 ## debug_toolbar 사용하기

 1. pip install django-debug-toolbar

### settings.py 설정 변경

 2. INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'debug_toolbar',
]

 3. ```python 
   if settings.DEBUG:
    import debug_toolbar
    urlpatterns = + [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ]
```
 4. MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

 5. INTERNAL_IPS = ['127.0.0.1']




