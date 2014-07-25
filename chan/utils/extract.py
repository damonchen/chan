#!/usr/bin/env python
# -*- coding: utf-8 -*-

def extract(text, start, end):
    if start == 0:
        sindex = 0
    else:
        s = text.find(start)
        sindex = s + len(start)

    if end == -1:
        return text[sindex:]
    else:
        e = text.find(end, sindex)
        return text[sindex:e]


def extract_all(text, start, end):
    results = []
    slen = len(start)
    s = text.find(start)
    while s != -1:
        e = text.find(end, s+slen)
        t = text[s+slen:e]
        s = text.find(start, s+slen)

        results.append(t)

    return results
