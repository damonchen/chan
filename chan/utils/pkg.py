#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os


class Package(object):
    @staticmethod
    def resource_filename(module, path):
        mod = myimport(module)
        p = os.path.dirname(mod.__file__)
        if path:
            return os.path.join(p, path)
        else:
            return p

    @staticmethod
    def resource_listdir(module, path):
        d = Package.resource_filename(module, path)
        return os.listdir(d)

    @staticmethod
    def resource_isdir(module, path):
        d = Package.resource_filename(module, path)
        return os.path.isdir(d)



try:
    import pkg_resources as pkg
except:
    pkg = Package

def _callback(action, src, dst):
    pass

def extract_file(module, path, dist, replace=True, callback=None):
    if callback is None:
        callback = _callback

    src_file = pkg.resource_filename(module, path)
    sfile = os.path.basename(src_file)
    if os.path.isdir(dist):
        dst_file = os.path.join(dist, sfile)
    else:
        dst_file = dist

    f = os.path.exists(dst_file)
    if replace or not f:
        shutil.copy2(src_file, dst_file)
        if callback and callable(callback):
            callback(src_file, dst_file, action='extract_file')

def extract_folder(mod, path, dst, exclude=None, exclude_ext=None, recursion=True, replace=True, callback=None):
    default_exclude = ['.svn', '_svn', '.git', '.hg']
    default_exclude_ext = ['.pyc', '.pyo', '.bak', '.tmp']
    exclude = exclude or []
    exclude_ext = exclude_ext or []

    if callback is None:
        callback = _callback

    if not os.path.exists(dst):
        os.makedirs(dst)
        if callback and callable(callback):
            callback(dst, action='extract_folder')

    for r in pkg.resource_listdir(mod, path):
        if r in exclude or r in default_exclude:
            continue

        fpath = os.path.join(path, r)
        if pkg.resource_isdir(mod, fpath):
            if recursion:
                extract_folder(mod, fpath, os.path.join(dst, r), exclude, exclude_ext, recursion, replace, callback)
        else:
            ext = os.path.splitext(fpath)[1]
            if ext in exclude_ext or ext in default_exclude_ext:
                continue
            extract_file(mod, fpath, dst, replace, callback)
