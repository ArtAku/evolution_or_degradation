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

web working on localhost:8080
to change cell's size open localhost:8080/:size

## run all

```powershell
docker-compose up --build
```

## debug python

start supply services
```powershell
docker-compose -f docker-compose.web.yaml --build
```

Run python
```powershell
cd ./game
python main.py
```

## debug web

start supply services
```powershell
docker-compose -f docker-compose.game.yaml --build
```

Run web
```powershell
cd ./view
npm start
```
