#!/bin/bash

uvicorn src.app.main:app --host 0.0.0.0 --port 8003 --reload