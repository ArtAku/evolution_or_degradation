# evolution_or_degradation

# install

Python init virtual env
```powershell
python -m venv venv
```

Python install reqs
```powershell
pip install -r requrments.txt
```
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
