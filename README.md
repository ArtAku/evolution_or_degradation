# evolution_or_degradation

# Install

From repository root

```
cd game
```

Python init virtual env

```powershell
python -m venv venv
```

Python install reqs

```powershell
pip install -r requirements.txt
```

## Troubleshooting

**Error**: `ERROR: Could not install packages due to an EnvironmentError: [WinError 2] The system cannot find the file specified: 'c:\\python38\\Scripts\\dotenv.exe' -> 'c:\\python38\\Scripts\\dotenv.exe.deleteme'`

**Fix**: use full path to init virtual env:

```
"C:\Python38\python.exe" -m venv venv
```

# Dev

## Scripts

```powershell
# format
autopep8 --in-place --aggressive @(ls -Filter *.py)
# lint
pylint --fail-under=5 @(ls -Filter *.py)
```

# Start

web working on localhost:8080
To set cell size, send get request `localhost:8080/set/size/{number}`

## Run all

```powershell
docker-compose up --build
```

## Debug python

start supply services

```powershell
docker-compose -f docker-compose.web.yaml --build
```

Run python

```powershell
cd ./game
python main.py
```

## Debug web

start supply services

```powershell
docker-compose -f docker-compose.game.yaml --build
```

Run web

```powershell
cd ./view
npm start
```
