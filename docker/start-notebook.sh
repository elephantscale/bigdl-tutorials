#!/bin/bash
set -e

# run Jupyter
#. /usr/local/bin/start.sh  ~/run_jupyter.sh
/usr/local/bin/start.sh  ~/run_jupyter.sh

# And run bash shell, so the container doesn't exit when Jupyter exits
# This way we can re-run ./run_jupyter.sh if needed to
/bin/bash
