f:
cd craigComp\programming\python
python create.py %1 %2
cd..
cd %1\%2
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/craiglobo1/%2.git
git push -u origin master
code .
TASKKILL /im cmd.exe