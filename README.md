# StutterBuddy

This package allows you to interact with the stutterbuddy.ch API and perform a variety of tasks such as uploading files, submitting jobs, and retrieving information about assets and jobs.

To use this package, you will need to have an API key which you can obtain by creating an account on stutterbuddy.ch.

## Installation

```
pip install stutterbuddy
```

## Usage

The main object in the package is the `Stutterbuddy` class, which you can initialize by passing in your API key. This class has several methods that you can use to perform different actions:

- `upload_file(path_to_file, verbose=1, upload_callback=None)`: This method allows you to upload a local file to stutterbuddy. It returns a unique identifier for your uploaded file.
- `submit_job(asset_id, settings=SubmissionSettings(), verbose=1)`: This method allows you to submit a job to the API. You will need to provide the asset id of the file you want to process and can also specify job settings using a `SubmissionSettings` object. It returns a list of job ids.
- `get_all_jobs(verbose=1)`: This method allows you to retrieve a list of all jobs belonging to the user.
- `get_job(job_id, verbose=1)`: This method allows you to retrieve information about a specific job using the job id.
- `get_asset(asset_id, verbose=1)`: This method allows you to retrieve information about a specific asset using the asset id.

For more information and a complete list of available methods, please refer to the documentation on the stutterbuddy.ch website or the inline documentation in the code.

## Features

- Bulk processing and automatized upload of files to stutterbuddy.ch
- submit videos or audio both as links or as files
- retrieve status of jobs
- coming soon: use as CLI tool
