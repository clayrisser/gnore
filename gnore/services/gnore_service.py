from shutil import rmtree
import glob
from os import getcwd, path, listdir, remove
import os
import re

_gnore_paths = list()

def clean(verbose=True):
    for rule in get_gitignore_rules():
        for root, dirs, files in os.walk(getcwd()):
            matches = re.findall(r'\.git(?![^\/])', root)
            if len(matches) > 0:
                continue
            rimraf(root, rule, verbose)

def get_gitignore_rules():
    gitignore = list()
    with open(get_path(r'\.gitignore$')) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or len(line) <= 0 or line[0] == '#':
                continue
            gitignore.append(line)
    return gitignore

def get_gnore_rules():
    gitignore = list()
    with open(get_path(r'\.gnore$')) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or len(line) <= 0 or line[0] == '#':
                continue
            gitignore.append(line)
    return gitignore

def get_gnore_paths():
    if len(_gnore_paths) > 0:
        return _gnore_paths
    for rule in get_gnore_rules():
        for root, dirs, files in os.walk(getcwd()):
            matches = re.findall(r'\.git(?![^\/])', root)
            if len(matches) > 0:
                continue
            for p in glob.glob(path.join(root, rule)):
                _gnore_paths.append(p)
    return _gnore_paths

def rimraf(root, rule, verbose):
    gnore_paths = get_gnore_paths()
    for p in glob.glob(path.join(root, rule)):
        should_continue = False
        for gnore_path in gnore_paths:
            if gnore_path in p:
                should_continue = True
        if should_continue:
            continue
        if verbose:
            print('R ' + p)
        if path.exists(p):
            if path.isdir(p):
                rmtree(p)
            else:
                remove(p)

def get_path(regex, cwd=None):
    if not cwd:
        cwd = getcwd()
    for p in listdir(cwd):
        if len(re.findall(regex, p)) > 0:
            return path.abspath(path.join(cwd, p))
    return get_path(regex, path.abspath(path.join(cwd, '../')))
