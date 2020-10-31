import os
from pathlib import Path

dir = r'./dependencias'
pasta = Path(dir)

if pasta.is_dir() == False:
    os.mkdir(dir)
else:
    print('ja existe')