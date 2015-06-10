#!/bin/sh

# install file for plugin

EOC_DOTDIR=~/.enemies-of-carlotta
PLUGIN_DIR=$EOC_DOTDIR/plugins

REPO_DIR=$PWD
cd $PLUGIN_DIR 
SRC_FILES=$(find $REPO_DIR -name \*.py)
for file in $SRC_FILES; do
    if [ ! -h $file ]; then
        ln -s $file
    fi
done
cd $REPO_DIR

# init logfile
LOGFILE="$PLUGIN_DIR/eoc_plugin.log"
if [ ! -e $LOGFILE ]; then
    touch $LOGFILE
fi