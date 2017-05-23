set HOME = E:\keys

cd E:\pengwk_project\bug2butterfly
python.exe setup.py sdist
twine upload dist/*

pause