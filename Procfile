web: uvicorn src.app:app --host "0.0.0.0" --port ${PORT:-8000} --workers 4
worker: celery -A src.tasks worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
beat: celery -A src.tasks beat --loglevel=INFO