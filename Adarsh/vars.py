# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '21958939'))
    API_HASH = str(getenv('API_HASH', '85e28186197c9bc2dc04165b9c7216dd'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '7919974613:AAGuBzEjR8M6OIDF2idMepnR99jjoe3O0dk'))
    name = str(getenv('name', 'cacacaya_log'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '3'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002508415743'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6965075891").split())
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'dud4rus'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', APP_NAME + '.herokuapp.com' if ON_HEROKU else '0.0.0.0'))
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://kteh393:Manado2020@cluster0.srxx6g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'cacacayacha').replace('https://t.me/', ''))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))      
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'onepagelink.in')
    SHORTLINK_API = getenv('SHORTLINK_API', 'c47e1c4469c0a66e74af7153cb8f4d3b304d010')
    TUTORIAL_URL = getenv('TUTORIAL_URL', 'https://t.me/rk_back_up/18')
