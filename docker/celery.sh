#!/bin/bash

if [ "$1" == "celery" ]; then
  celery --app=app.tasks.conf_cel:celery_app worker -l INFO
elif [ "$1" == "flower" ]; then
  celery --app=app.tasks.conf_cel:celery_app flower
fi
      