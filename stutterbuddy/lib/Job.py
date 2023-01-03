from dict2xml import dict2xml
import json

class Job:
    """
        A class that represents a job on stutterbuddy
    """
    def __init__(self, job_dict):
        self.id = job_dict['id']
        self.assetId = job_dict['assetId']
        self.job_name = job_dict['job_name']
        self.date_submitted = job_dict['date_submitted']
        self.date_completed = job_dict['date_completed']
        self.status = job_dict['status']
        self.userMessage = job_dict['userMessage']
        self.model_version = job_dict['model_version']
        self.remove_stutter = job_dict['remove_stutter']
        self.remove_silence = job_dict['remove_silence']
        self.remove_music = job_dict['remove_music']
        self.remove_other = job_dict['remove_other']
        self.min_gap = job_dict['min_gap']
        self.renderVideo = job_dict['renderVideo']
        self.renderAudio = job_dict['renderAudio']
        self.resolution = job_dict['resolution']
        self.framerate = job_dict['framerate']
        self.notify = job_dict['notify']
        self.saved_time = job_dict['saved_time']

    def __str__(self):
        return self.job_name

    def __repr__(self):
        return self.job_name

    def to_dict(self):
        return {
            'id': self.id,
            'assetId': self.assetId,
            'job_name': self.job_name,
            'date_submitted': self.date_submitted,
            'date_completed': self.date_completed,
            'status': self.status,
            'userMessage': self.userMessage,
            'model_version': self.model_version,
            'remove_stutter': self.remove_stutter,
            'remove_silence': self.remove_silence,
            'remove_music': self.remove_music,
            'remove_other': self.remove_other,
            'min_gap': self.min_gap,
            'renderVideo': self.renderVideo,
            'renderAudio': self.renderAudio,
            'resolution': self.resolution,
            'framerate': self.framerate,
            'notify': self.notify,
            'saved_time': self.saved_time
        }

    def to_xml(self):
        return dict2xml(self.to_dict())

    def to_json(self):
        return json.dumps(self.to_dict())