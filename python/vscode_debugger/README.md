test using click vscode debugger launch.json
pdb works

test using command in args:[] and debug open file
${worspaceFolder}/y train
and 
${workspaceFolder}/y
args:['train']

do these really work in vscode? I cant get them to work in pytext. 
this works with this launch.json

   {
      "name": "Python: Current File (Integrated Terminal)",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/subcommands/y.py",
      "console": "integratedTerminal"
    },

set breakpoint in main() of y.py

