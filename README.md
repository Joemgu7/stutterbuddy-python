# StutterBuddy

Set of tools to interact with the API of StutterBuddy.

## Installation
```
pip install stutterbuddy
```

## Usage
```
from stutterbuddy import Worker

api_key = ''

sb = Worker(api_key)

response, job_id = sb.submit_file('test.mp4')

status = sb.get_info(job_id)

print(status)
```

## Features

* Bulk processing and automatized upload of files to stutterbuddy.ch
* submit videos or audio both as links or as files
* retrieve status of jobs

## Dependencies
* requests-toolbelt

## Known Bugs
* None atm