#!/bin/bash

declare -A WINDOWS=()

#### Page list ####
WINDOWS[main]='main'
WINDOWS[about]='about'
WINDOWS[settings]='settings'

#### Print red text to the terminal ####
function redPrint {
    if [[ "$1" != "" ]]
    then
        STRING=$1
        RED='\033[0;31m'
        NC='\033[0m' # No Color
        echo -e "${RED}${STRING}${NC}"
    fi
}

### Print green text to the terminal ####
function greenPrint {
    if [[ "$1" != "" ]]
    then
        STRING=$1
        GREEN='\033[0;32m'
        NC='\033[0m' # No Color
        echo -e "${GREEN}${STRING}${NC}"
    fi
}

#### Print usage ####
function printUsage {
    echo "Usage: $0 [-w <about|main|settings|runner>] [-r] [-a] [-h]"
    echo "  -w: Specify the window to compile."
    echo "  -r: Compile the resources."
    echo "  -a: Compile everything."
    echo "  -h: Print this message."
}

#### Exit with error ####
function exitError {
    ERR_MSG=$1
    redPrint "${ERR_MSG}"
    printUsage
    exit 1
}

#### Split product name ####
function splitProductName {
    IFS='_'
    read -a splittedName <<< $1
    IFS=' '
}

#### Compile a window ####
function compileWindow {
    if [[ "$1" != "" ]]
    then
        greenPrint "---- Compiling $1 window ----"
        name=$(echo $1 | tr '[:upper:]' '[:lower:]')
        pyside2-uic -o src/pkgs/${name}Window/${name}Window_auto.py src/pkgs/${name}Window/${name}Window.ui
        if [ $? -ne 0 ]
        then
            exitError "Failed to compile $1 window!!!"
        fi
        sed -i 's/import resources_rc/from ..assets import resources/' src/pkgs/${name}Window/${name}Window_auto.py
        if [ $? -ne 0 ]
        then
            exitError "Failed to compile $1 window!!!"
        fi
        greenPrint "DONE"
    else
        exitError "Unspecified window!!!"
    fi
}

#### Compile resources ####
function compileResources {
    greenPrint "---- Compiling resources ----"
    pyside2-rcc -o src/pkgs/assets/resources.py src/pkgs/assets/resources.qrc
    if [ $? -ne 0 ]
    then
        exitError "Failed to compile $1 window!!!"
    fi
    greenPrint "DONE"
}

while getopts ":p:w:rah" options
do
    case "${options}" in
        w)
            windowIdx="${OPTARG}"
            compileWindow "${WINDOWS[$windowIdx]}"
            ;;
        r)
            compileResources
            ;;
        a)
            for page in "${PAGES[@]}"
            do
                compilePage "${page}"
            done
            compileResources
            ;;
        h)
            printUsage
            ;;
        :)
            exitError "Missing page name argument!!!"
            ;;
        *)
            exitError "Unsupported option!!!"
            ;;
    esac
done
