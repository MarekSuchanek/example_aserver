#!/bin/bash
if [ -f env/bin/activate ]; then
    source env/bin/activate
else
    source env/Scripts/activate
fi
example_aserver $1
