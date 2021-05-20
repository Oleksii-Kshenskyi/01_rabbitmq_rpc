#!/bin/bash

set -xe

BASE_DIR=`pwd`
SOFUNC_BUILD="${BASE_DIR}/so_functions/build"
SOFUNC_LIB="libsofuncs.so"
DISTRO_DIR="${BASE_DIR}/bin"

# clean the previous distribution

rm -rf $DISTRO_DIR
rm -rf $SOFUNC_BUILD

# The .so functions stage

mkdir $SOFUNC_BUILD && cd $SOFUNC_BUILD
cmake .. -DCMAKE_BUILD_TYPE=Release
make
cd $BASE_DIR

# Creating the distribution

mkdir $DISTRO_DIR
cp $SOFUNC_BUILD/$SOFUNC_LIB $DISTRO_DIR