@echo off
IF [%1]==[] (
    echo You forgot to specify your path.
) ELSE IF [%2]==[] (
    f:
    cd craigComp\programming\%1
    code .
) ELSE (
    f:
    cd craigComp\programming\%1\%2
    code .
)
EXIT
