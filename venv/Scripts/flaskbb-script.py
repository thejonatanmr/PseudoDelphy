#!c:\users\3075\pycharmprojects\flaskbb\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'FlaskBB','console_scripts','flaskbb'
__requires__ = 'FlaskBB'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('FlaskBB', 'console_scripts', 'flaskbb')()
    )
