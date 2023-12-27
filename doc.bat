powershell -Command "Remove-Item -Path doc -Recurse -Force"
pdoc --html xingyun --output-dir doc --force
powershell -Command "move doc/xingyun/* doc"
powershell -Command "Remove-Item -Path doc/xingyun -Recurse -Force"
