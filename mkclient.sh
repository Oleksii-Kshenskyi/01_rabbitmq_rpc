#!/bin/bash

set -xe

BASE_DIR=`pwd`
DISTRO_DIR="${BASE_DIR}/bin"
CREDS_FILE="${BASE_DIR}/creds.json"

# clean the previous distribution

rm -rf $DISTRO_DIR

# Creating the distribution

mkdir $DISTRO_DIR
cp rpc_src/client.py $DISTRO_DIR
cp $CREDS_FILE $DISTRO_DIR