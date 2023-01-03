import requests
from requests_toolbelt import MultipartEncoderMonitor
import urllib.parse
import mimetypes
from .Jobs import SubmissionSettings

class Stutterbuddy():
    """A class to interact with the stutterbuddy.ch api"""

    def __init__(self, API_KEY : str, verbose = 1):
        self.API_KEY = API_KEY
        self.verbose = verbose

    def upload_file(self, path_to_file, verbose=1, upload_callback=None):
        """A function to upload a local file to stutterbuddy. More information on the arguments taken available at https://stutterbuddy.ch/api-doc
        returns a unique identifier to your uploaded file.
        Has 3 verbose levels: 0 for no cmd line output, 1 for basic information on progress and 3 for debugging purposes"""

        # request a upload_url
        r = requests.get('https://api.stutterbuddy.ch/upload/file?api_key=' + urllib.parse.quote(self.API_KEY))

        if verbose >= 2: print(r.json())

        # check if the request was successful
        if r.status_code != 200:
            raise Exception("Error occured when requesting slot: "+r.json()['message'])

        r = r.json()

        cdn_url = r['worker_url']

        # determine the mime type of the file
        mime_type = mimetypes.guess_type(path_to_file)[0]

        m = MultipartEncoderMonitor.from_fields(
            fields={
                'file': (path_to_file, open(path_to_file, 'rb'), mime_type)
            },
            callback=(upload_callback)
        )

        r = requests.post(cdn_url+'/upload/file?api_key=' + urllib.parse.quote(self.API_KEY), data=m,
                          headers={'Content-Type': m.content_type}, timeout=(10, 2000))
        
        if verbose >= 2: print(r.json())

        # check if the request was successful
        if r.status_code != 200:
            raise Exception("Error occured while uploading file: "+r.json()['message'])

        r = r.json()

        return r['asset_id']
    
    def submit_job(self, asset_id, settings=SubmissionSettings(), verbose=1):
        """
            A function to submit a job to the api.
            
            Args:
                asset_id (str): The asset id of the file to be submitted.
                settings (SubmissionSettings, optional): The settings for the job. Defaults to SubmissionSettings().
            
            Returns:
                list: A list of job ids
        """

        data_dict = settings.to_dict()
        data_dict['asset_ids'] = [asset_id]

        r = requests.post('https://api.stutterbuddy.ch/job/submission?api_key=' + urllib.parse.quote(self.API_KEY), json=data_dict)

        if self.verbose >= 2: print(r.json())

        if r.status_code != 200:
            raise Exception("Error occured when submitting job: "+r.json()['message'])

        r = r.json()

        if 'warning' in r and len(r['warning']) > 0:
            # concat all warnings into one string
            warnings = ""
            for warning in r['warning']:
                warnings += warning + ", "

            print("Warning: "+warnings[:-2])

        return r['job_ids']

    def get_all_jobs(self, verbose=1) -> list:
        """
            A function to get all jobs from the user.
            
            Returns:
                list: A list of all jobs
    
        """
        r = requests.get('https://api.stutterbuddy.ch/user/jobs?api_key=' + urllib.parse.quote(self.API_KEY))

        if verbose >= 2: print(r.json())

        if r.status_code != 200:
            raise Exception("Error occured when fetching jobs: "+r.json()['message'])

        r = r.json()

        return r['jobs']        

    def get_all_assets(self, verbose=1) -> list:
        """
            A function to get all assets from the user.
            
            Returns:
                list: A list of all assets
    
        """
        r = requests.get('https://api.stutterbuddy.ch/user/assets?api_key=' + urllib.parse.quote(self.API_KEY))

        if verbose >= 2: print(r.json())

        if r.status_code != 200:
            raise Exception("Error occured when fetching assets: "+r.json()['message'])

        r = r.json()

        return r['assets']