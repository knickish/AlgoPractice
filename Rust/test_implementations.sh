#!/bin/bash

#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

# this script will compile all rust projects in the same folder as the script together
# with the required sorting tester, then runs them.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
TEST_DIRS=("${DIR}/sort_evaluator/" "${DIR}/test_sort_evaluator/" "${DIR}/")

echo "test_sort_evaluator"
cargo run -q --manifest-path ${DIR}/test_sort_evaluator/Cargo.toml

for f in ${DIR}/*/
do
    
    if [[ ! " ${TEST_DIRS[@]} " =~ " ${f} " ]]; then
        dirname="${f%"${f##*[!/]}"}"
        dirname="${dirname##*/}"
        echo ""
        echo "${dirname}"
        TOML_PATH="${f}Cargo.toml"
        cargo run -q --release --manifest-path ${TOML_PATH}
    fi
done