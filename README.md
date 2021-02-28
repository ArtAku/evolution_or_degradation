# evolution_or_degradation


# Dev
## Scripts
```powershell
# format
autopep8 --in-place --aggressive @(ls -Filter *.py)
# lint
pylint --fail-under=5 @(ls -Filter *.py)
```
# start
## run all

```powershell
docker-compose up
```

## debug python

start supply services
```powershell
docker-compose -f docker-compose.dev.yaml
```

Run python
