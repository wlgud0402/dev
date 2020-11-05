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

0.  pip install django-debug-toolbar

### settings.py 설정 변경

```python
1.  INSTALLED_APPS = [
    'debug_toolbar',
    ]

2. MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

3. INTERNAL_IPS = ('127.0.0.1',) 추가하기
```

### 프로젝트의 urls.py 설정 변경

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings => 추가
from django.conf.urls import url => 필요

if settings.DEBUG:
import debug_toolbar
urlpatterns += [
url(r'^__debug__/', include(debug_toolbar.urls)),
]
```
