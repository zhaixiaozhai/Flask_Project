#SECRET_KEY='24个字符的字符串'
import os
from datetime import timedelta

SECRET_KEY = os.urandom(24)

# PERMANENT_SESSTION_LIFETIME = timedelta(days=7)