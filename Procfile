web: uvicorn src.app:app --host "0.0.0.0" --port ${PORT:-8000}
celery: celery src.tasks beat --loglevel=INFO
celery: celery src.tasks worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo