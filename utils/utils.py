#!/usr/bin/python
# -*- coding: utf-8 -*-
import html
import json
import multiprocessing
import os
import re
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import googletrans
import requests

DEBUG = True

MAX_PROCESSOR = multiprocessing.cpu_count()

APP_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

TRANSLATOR = googletrans.Translator()

IMAGE_SOURCES = ['pexels.com', 'pixabay.com', 'flickr.com', 'unsplash.com', 'pinterest.com', '500px.com']


# Done
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


# Done
def pool_executor(fn, args, executor_mode=0, max_workers=None, timeout=None):
    assert executor_mode in [0, 1, 2], 'Executor mode is invalid!'
    debug('Run %s in %s mode.' % (fn.__name__,
                                  ['sequential', 'multi-threading', 'multi-processing'][executor_mode]))
    if executor_mode == 0:
        return list(map(fn, *args))
    else:
        executor_class = ThreadPoolExecutor if executor_mode == 1 else ProcessPoolExecutor
        with executor_class(max_workers=max_workers) as executor:
            return list(executor.map(fn, *args, timeout=timeout))


# Done
def detect_language(text):
    result = TRANSLATOR.detect(text)
    return result.lang, googletrans.constants.LANGUAGES.get(result.lang), result.confidence


# Done
def translate_text(text):
    result = TRANSLATOR.translate(text)
    return result.src, googletrans.constants.LANGUAGES.get(result.src), result.text


# Done
def normalize_text(text):
    assert isinstance(text, str), 'Text is invalid!'
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'(?:^\s+)|(?:\s+$)', '', text, flags=re.MULTILINE)
    text = re.sub(r'(?:\r?\n)+', '\n', text)
    return text.strip()


# Done
def split_paragraphs(text):
    assert isinstance(text, str), 'Text is invalid!'
    return re.split(r'(?:\r?\n)+', text)


# Done
def bing_search_images(keywords, timeout=60):
    assert isinstance(keywords, list) and len(keywords) > 0, 'Keywords is invalid!'
    try:
        with requests.Session() as session:
            response = session.get(
                url='https://azure.microsoft.com/en-gb/services/cognitive-services/bing-image-search-api/',
                timeout=timeout)
            if response.status_code == requests.codes.ok:
                matcher = re.search(r'name="__RequestVerificationToken" type="hidden" value="([^"]+)"',
                                    response.content.decode(), re.IGNORECASE)
                if matcher is not None:
                    # payload = {
                    #     'Query': '(%s) (%s)' % (
                    #         ' | '.join(map(lambda s: 'site:' + s, IMAGE_SOURCES)), ' '.join(keywords)),
                    #     'ImageType': 'Photo',
                    #     '__RequestVerificationToken': matcher.group(1)
                    # }
                    payload = {
                        'Query': ' '.join(keywords),
                        'ImageType': 'Photo',
                        '__RequestVerificationToken': matcher.group(1)
                    }
                    response = session.post(
                        url='https://azure.microsoft.com/en-gb/cognitive-services/demo/imagesearchapi/',
                        data=payload, timeout=timeout)
                    if response.status_code == requests.codes.ok:
                        matcher = re.search(r'<code>(.+?)</code>', response.content.decode(), re.IGNORECASE | re.DOTALL)
                        if matcher is not None:
                            images = []

                            value = json.loads(html.unescape(matcher.group(1))).get('value')
                            for item in value:
                                images.append((item.get('thumbnailUrl'), item.get('contentUrl')))

                            return images
    except Exception as e:
        debug(e)
    return None


# Done
def watson_analyse_image(image_url, timeout=60):
    assert isinstance(image_url, str) and len(image_url) > 0, 'Image URL is invalid!'
    try:
        payload = {'url': image_url}
        response = requests.post(url='https://visual-recognition-demo.mybluemix.net/api/classify', data=payload,
                                 timeout=timeout)
        if response.status_code == requests.codes.ok:
            images = json.loads(response.content.decode()).get('images')

            classes = []
            for image in images:
                for classifier in image.get('classifiers'):
                    for item in classifier.get('classes'):
                        classes.append((item.get('class'), item.get('score')))

            return classes
    except Exception as e:
        debug(e)
    return None


# Done
def azure_analyse_image(image_url, timeout=60):
    assert isinstance(image_url, str) and len(image_url) > 0, 'Image URL is invalid!'
    try:
        with requests.Session() as session:
            response = session.get(
                url='https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/', timeout=timeout)
            if response.status_code == requests.codes.ok:
                matcher = re.search(r'name="__RequestVerificationToken" type="hidden" value="([^"]+)"',
                                    response.content.decode(), re.IGNORECASE)
                if matcher is not None:
                    payload = {
                        '__RequestVerificationToken': (None, matcher.group(1)),
                        'Image.Url': (None, image_url)
                    }
                    response = session.post(
                        url='https://azure.microsoft.com/en-us/cognitive-services/demo/visionanalysisapi/',
                        files=payload, timeout=timeout)
                    if response.status_code == requests.codes.ok:
                        keywords = []
                        tags = []

                        content = response.content.decode()
                        matcher = re.search(r'<td id="imgDescription">(.+?)</td>', content, re.IGNORECASE | re.DOTALL)
                        if matcher is not None:
                            keywords = json.loads(html.unescape(matcher.group(1))).get('tags')

                        matcher = re.search(r'<td>Tags </td>.+?<td>(.+?)</td>', content, re.IGNORECASE | re.DOTALL)
                        if matcher is not None:
                            value = json.loads(html.unescape(matcher.group(1)))
                            for item in value:
                                tags.append((item.get('name'), item.get('confidence')))

                        return keywords, tags
    except Exception as e:
        debug(e)
    return None


# Done
def watson_analyse_text(text, timeout=60):
    assert isinstance(text, str) and len(text) > 0, 'Text is invalid!'
    try:
        payload = {
            'features': {
                'entities': {},
                'keywords': {}
            },
            'text': text
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url='https://natural-language-understanding-demo.mybluemix.net/api/analyze',
                                 headers=headers, data=json.dumps(payload), timeout=timeout)
        if response.status_code == requests.codes.ok:
            keywords = []
            entities = []

            value = json.loads(response.content.decode()).get('results')

            for item in value.get('keywords'):
                keywords.append((item.get('text'), item.get('relevance')))

            for item in value.get('entities'):
                entities.append((item.get('type'), item.get('text'), item.get('relevance'), item.get('count')))

            return keywords, entities
    except Exception as e:
        debug(e)
    return None
