# evolution_or_degradation


# Dev
## Scripts
```powershell
# format
autopep8 --in-place --aggressive @(ls -Filter *.py)
# lint
pylint --fail-under=5 @(ls -Filter *.py)
```