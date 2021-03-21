#!/bin/bash

#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

# this script will compile all c files in the same folder as the script together
# with the required sorting tester, then runs them.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
TEST_FILES=("${DIR}/sort_evaluator.cpp" "${DIR}/test_sort_evaluator.cpp")

g++ sort_evaluator.hpp sort_evaluator.cpp  test_sort_evaluator.cpp  -o ${DIR}/known_good
echo ${DIR}/known_good
${DIR}/known_good
rm ${DIR}/known_good

for f in ${DIR}/*.cpp
do
    if [[ ! " ${TEST_FILES[@]} " =~ " ${f} " ]]; then
        echo "\n${f}"  
        g++ sort_evaluator.hpp sort_evaluator.cpp  ${f}  -o ${DIR}/sort_test
        ${DIR}/sort_test
        rm ${DIR}/sort_test
    fi
done

