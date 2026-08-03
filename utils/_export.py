# cleans quicksave file and forces debug file to be used
# usage: py _export.py [file(s)]

import sys, json
from collections import OrderedDict

for filepath in sys.argv[1:]:
    with open(filepath, "r") as f:
        file = json.load(f, object_pairs_hook=OrderedDict)

    file.pop("saveUid", None)
    file.pop("modSessions", None)

    with open(filepath, "w") as f:
        json.dump(file, f, indent=2)