from celery import Celery

celery_app = Celery('tasks', borker='redis://localhost:6379', backend='redis://localhost:6379')

celery_app.autodiscover_tasks(['tasks'])  # Replace 'your_module' with the actual module name containing your tasks
