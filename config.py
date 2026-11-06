#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8697438916:AAFIvCw-MsZX9Klbo81excf6fjLhzR0MxZU")
    API_ID = int(os.environ.get("API_ID", "30247401"))
    API_HASH = os.environ.get("API_HASH", "15672484ee3efb90c52f8fcc0339f525")
    AUTH_USERS = os.environ.get("AUTH_USERS", "8817209259")
