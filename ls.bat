@echo off
IF [%1]==[] (python ls.py 0 %~dp0) ELSE (python ls.py 1 %1)