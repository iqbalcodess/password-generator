# Python Password Generator

A simple, secure CLI password generator using Python's `secrets` module.

## Features
- Secure random generation (`secrets`, not `random`)
- Guarantees lowercase + uppercase + digits (+ symbols by default)
- Custom length via CLI
- Option to exclude symbols
- Zero dependencies (stdlib only)

## Usage

```bash
python3 main.py
python3 main.py -l 20
python3 main.py -l 12 --no-symbols
python3 main.py --help
```

Example:
```
$ python3 main.py -l 16
/Wk]XGOr~DO<cMO3
```

## Project Structure
```
.
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Requirements
- Python 3.8+

No install needed:
```bash
# optional
pip install -r requirements.txt
```

## License
MIT
