# Remitly-Tasks

This Python script validates AWS IAM policy JSON files, checking for overly permissive wildcard permissions indicated by a single asterisk ("*") in policy statements.

## Getting Started

### Prerequisites
- Ensure you have Git and Python 3.x installed on your machine.

### Installation
Clone the repository and set up a virtual environment:
```bash
git clone https://github.com/sit3kk/Remitly-Tasks.git
cd Remitly-Tasks
# Linux/Mac
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
# Windows
python -m venv venv && .\venv\Scripts\activate && pip install -r requirements.txt
```

## Usage

Run the script by specifying the path to your IAM policy JSON file. Replace /path/to/policy.json with the actual file path.

# Linux/Mac
```bash
python3 json_validator.py /path/to/policy.json
```
# Windows
```bash
python json_validator.py C:\path\to\policy.json
```
This will validate the specified IAM policy file and print the result to the console, indicating whether the policy contains any overly permissive wildcard permissions.


## Example
```bash
python3 json_validator.py example.json
```

## Running the Tests

Ensure `pytest` is installed for running unit tests:
```bash
cd tests
pytest
```

## Logs
- If something went wrong, check logs.log in log directory
![image](https://github.com/sit3kk/Remitly-Tasks/assets/69002597/ccf62b4b-618a-4924-92bd-b3401a8f9665)


