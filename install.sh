#!/bin/sh

# install file for plugin

EOC_DOTDIR=~/.enemies-of-carlotta
PLUGIN_DIR=$EOC_DOTDIR/plugins

REPO_DIR=$PWD
cd $PLUGIN_DIR && find $REPO_DIR -name \*.py -exec ln -s {} \; && cd $REPO_DIR