#!/bin/bash

set -xe

BASE_DIR=`pwd`
DISTRO_DIR="${BASE_DIR}/bin"

# clean the previous distribution

rm -rf $DISTRO_DIR

# Creating the distribution

mkdir $DISTRO_DIR
cp rpc_src/client.py $DISTRO_DIR