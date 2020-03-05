@echo off
IF [%1]==[] (python F:\craigComp\Programming\python\git\ls.py 0 %cd%) ELSE (python F:\craigComp\Programming\python\git\ls.py 1 %1)