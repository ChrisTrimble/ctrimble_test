#!/usr/bin/env python

import imp
import sys
import os
from os.path import abspath, dirname

from django.core.management import execute_manager, setup_environ
from django.template.defaultfilters import striptags
from djblets.util.filesystem import is_exe_in_path


sys.path.insert(0, dirname(dirname(abspath(__file__))))

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    if settings.DEBUG:
        if len(sys.argv) > 1 and \
           (sys.argv[1] == 'runserver' or sys.argv[1] == 'test'):
            # If DJANGO_SETTINGS_MODULE is in our environment, we're in
            # execute_manager's sub-process.  It doesn't make sense to do this
            # check twice, so just return.
            if 'DJANGO_SETTINGS_MODULE' not in os.environ:
                sys.stderr.write('Running dependency checks (set DEBUG=False to turn this off)...\n')
                check_dependencies()

    fix_django_evolution_issues(settings)

    execute_manager(settings)
