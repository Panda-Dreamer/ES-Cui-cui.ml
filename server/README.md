New server build

Celery worker start:
celery -A tasks worker -l info

Server start:
python3 wgsi.py --host 0.0.0.0 --port 3000 --debug True