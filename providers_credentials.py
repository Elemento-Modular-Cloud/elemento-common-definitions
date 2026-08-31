# Copyright(c) 2019-2026, Elemento srl, All rights reserved                    #
# Author: Elemento srl
# The code in this repo is licnesed under Business Source License 1.1
# See full License text in LICENSE file.
# fmt: off
from os.path import join, dirname, basename
from json import load

data = open(join(dirname(__file__), basename(__file__).replace('.py', '.json').replace('.jsonc', '.json')))
data_json = load(data)
globals().update(data_json)
del data_json
del data
