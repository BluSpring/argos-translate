from argostranslate import cli, argospm
import os

if os.getenv('argospm', 'false') == 'true':
    argospm.main()
else:
    cli.main()