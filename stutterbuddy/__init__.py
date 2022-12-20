"""
    Author: Jonas Briguet
    Date: 06.12.2021
    Last Change: 14.08.2022
    version: 0.2.0
    This is a library with functions to interact with the stutterbuddy.ch api 
"""

import requests
from requests_toolbelt import MultipartEncoderMonitor
import urllib.parse

class Stutterbuddy():
    """A class to interact with the stutterbuddy.ch api"""

    def __init__(self, API_KEY, verbose=1):
        self.API_KEY = API_KEY
        self.verbose = verbose

    def upload_file(self, path_to_file, verbose=1, upload_callback=None):
        """A function to upload local files to stutterbuddy using the API. More information on the arguments taken available at https://stutterbuddy.ch/api-doc
        returns a unique identifier to your uploaded file.
        Has 3 verbose levels: 0 for no cmd line output, 1 for basic information on progress and 3 for debugging purposes"""

        # request a upload_url
        r = requests.get('https://api.stutterbuddy.ch/upload/file?api_key=' +
                         urllib.parse.quote(self.API_KEY)).json()

        if verbose >= 2: print(r)

        if 'error' in r:
            raise Exception("Error occured when requesting slot: "+r['error'])

        cdn_url = r['worker_url']

        m = MultipartEncoderMonitor.from_fields(
            fields={
                'file': (path_to_file, open(path_to_file, 'rb'), 'text/plain')
            },
            callback=(upload_callback)
        )

        if verbose >= 1: print('Uploading file to StutterBuddy')

        r = requests.post(cdn_url+'/upload/file?api_key='+urllib.parse.quote(self.API_KEY), data=m,
                          headers={'Content-Type': m.content_type}, timeout=(10, 2000)).json()
        
        if verbose >= 1: print('Upload finished')
        if verbose >= 2: print(r)            

        if 'message' in r and r['message'] == 'success':
            return r['asset_id']

        raise Exception("Error occured when submitting video: "+r['error'])

    # def get_info(self, upload_id):
    #     """
    #         Takes a single upload_id as string and the API_KEY
    #         returns video_name, video_url, status, timesaved corresponding to upload_id
    #     """
    #     result = requests.get('https://stutterbuddy.ch/api/data/request/single?key=' +
    #                           urllib.parse.quote(self.API_KEY)+"&uploadid="+urllib.parse.quote(upload_id)).json()

    #     if 'error' in result:
    #         raise Exception(
    #             "Error occured when requesting info: "+result['error'])
    #     else:
    #         return result['data']
