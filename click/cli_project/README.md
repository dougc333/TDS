1) modify setup.py to include the right file to run
type hello at the command line
function cli in h2.py is run. not main.  
entry_point:['hello:h2:cli']

to install: pip install editable .
then >hello
