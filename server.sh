#!/bin/sh
exec pipenv run hypercorn example.asgi:application --reload