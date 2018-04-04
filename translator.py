# -*- coding: utf-8 -*-

import time
import logging
import requests
import json
import string
import os
from os import path
import time
from senpy.plugins import SentimentPlugin, AnalysisPlugin
from senpy.models import Results, Entry, Sentiment, Error
from mstranslator import Translator

logger = logging.getLogger(__name__)


class TranslatorPlugin(AnalysisPlugin):
    '''Plugin for translation.'''

    def analyse_entry(self, entry, params):
        txt = entry['nif:isString']
        lang = params.get("lang")
        lang_to = params.get("lang_to")
        key = params.get("key")
        print(params)
        translator = Translator(key)
        txttranslated = translator.translate(txt, lang_from=lang, lang_to=lang_to)
        entry['output'] = {"nif:isString":txttranslated}

        yield entry
