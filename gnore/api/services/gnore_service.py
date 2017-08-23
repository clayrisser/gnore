from shutil import rmtree
import glob
from os import getcwd, path, listdir, remove
import os
import re

def clean(nuke=False, verbose=False):
    for rule in get_rules(nuke=nuke)[0]:
        for root, dirs, files in os.walk(getcwd()):
            matches = re.findall(r'\.git(?![^\/])', root)
            if len(matches) > 0:
                continue
            if nuke or not is_gnored(root):
                rimraf(root, rule, verbose=verbose)

def get_rules(nuke=None):
    rules = (list(), list())
    with open(get_gitignore_path()) as f:
        ignore = False
        for line in f.readlines():
            line = line.strip()
            if not line or len(line) <= 0 or line[0] == '#':
                if not nuke and line[:7] == '#:gnore':
                    ignore = True
                else:
                    ignore = False
                continue
            if not ignore:
                ignore = False
                rules[0].append(line)
            else:
                rules[1].append(line)
    return rules

def get_gitignore_path(cwd=None):
    if not cwd:
        cwd = getcwd()
    for p in listdir(cwd):
        if len(re.findall(r'\.gitignore(?![^\/])', p)) > 0:
            return path.abspath(path.join(cwd, p))
    return get_gitignore_path(path.abspath(path.join(cwd, '../')))

def is_gnored(root):
    relative_path = root[len(getcwd()):]
    if len(relative_path) <= 0:
        return False
    for rule in get_rules()[1]:
        rule = trim_path(rule)
        if rule == trim_path(relative_path)[:len(rule)]:
            return True
    return False

def trim_path(p):
    if len(p) <= 0:
        return ''
    if p[:2] == './':
        p = p[2:]
    elif p[0] == '/':
        p = p[1:]
    if p[len(p) - 1] == '/':
        p = p[:len(p) - 1]
    return p

def rimraf(root, rule, verbose=None):
    for p in glob.glob(path.join(root, rule)):
        if verbose:
            print('R ' + p)
        if path.exists(p):
            if path.isdir(p):
                rmtree(p)
            else:
                remove(p)
