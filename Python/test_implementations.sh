#!/bin/bash

#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

# this script will compile all c files in the same folder as the script together
# with the required sorting tester, then runs them.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
TEST_FILES=("${DIR}/scratchpad.py" "${DIR}/sortEvaluator.py" "${DIR}/test_sort_evaluator.py")

python3 ${DIR}/test_sort_evaluator.py

for f in ${DIR}/*.py
do
    if [[ ! " ${TEST_FILES[@]} " =~ " ${f} " ]]; then
        echo ""
        echo "${f}"  
        time python3 ${f}
        wait $!
    fi
done