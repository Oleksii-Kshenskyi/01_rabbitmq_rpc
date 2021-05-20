#!/bin/bash

set -xe

BASE_DIR=`pwd`
SOFUNC_BUILD="${BASE_DIR}/so_functions/build"
DISTRO_DIR="${BASE_DIR}/bin"

# clean the previous distribution

rm -rf $DISTRO_DIR
rm -rf $SOFUNC_BUILD