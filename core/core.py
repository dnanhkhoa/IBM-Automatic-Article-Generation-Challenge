#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils import *


def suggest_paragraph_images(paragraph):
    assert isinstance(paragraph, str), 'Paragraph is invalid!'
    keywords, entities = watson_analyse_text(paragraph)
    debug(keywords)
    keywords = sorted(filter(lambda x: x[1] >= 0.8, keywords), key=lambda x: x[1], reverse=True)[:3]
    debug(keywords)
    keywords = list(set([w for x in keywords for w in x[0].lower().split(' ') if len(w) > 3]))
    # keywords = [x[0].lower() for x in keywords]
    debug(keywords)
    debug(bing_search_images(keywords))



def suggest_article_images(article):
    assert isinstance(article, str), 'Article is invalid!'
    article = normalize_text(article)
    assert len(article) > 0, 'Article is invalid!'

    lang = detect_language(article)

    suggest_paragraph_images(article)
    return None

    # valid_paragraphs = []
    #
    # paragraphs = split_paragraphs(article)
    # for paragraph in paragraphs:
    #     if len(paragraph.split('.')) >= 5:
    #         valid_paragraphs.append(paragraph)
    #
    # debug(valid_paragraphs)
    return article
