#!/usr/bin/env python

import os
import sys
import signal
import optparse

try:
  import whisper
except ImportError:
  raise SystemExit('[ERROR] Please make sure whisper is installed properly')

# Ignore SIGPIPE
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

option_parser = optparse.OptionParser(
    usage='''%prog [options] to_path from_path1 from_path2 ...''')

(options, args) = option_parser.parse_args()

if len(args) < 2:
  option_parser.print_help()
  sys.exit(1)

path_to = args[0]
paths_from = args[1:]

for filename in paths_from:
  if not os.path.exists(filename):
    raise SystemExit('[ERROR] File "%s" does not exist!' % filename)

if os.path.exists(path_to):
  raise SystemExit('[ERROR] File "%s" exists already!' % path_to)

whisper.merge_sum(paths_from, path_to)
