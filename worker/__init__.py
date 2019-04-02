import os

from celery import Celery
from worker import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TanTan.settings')

# 创建celery对象
celery_app = Celery('TanTan')

celery_app.config_from_object(config)

# 自动检测
celery_app.autodiscover_tasks()
