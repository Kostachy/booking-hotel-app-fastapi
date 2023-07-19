from celery import Celery

celery_app = Celery(
    'tasks',
    broker='redis://:KBjzRntZsQQbiesQGMQjeVMB1IPXCu+yqMxfpsoor1YcM18MFwyGuH+O8PJjeJhM3mmeM9LGjpcYVK8W@localhost:6379',
    include=['app.tasks.app_tasks']
)
