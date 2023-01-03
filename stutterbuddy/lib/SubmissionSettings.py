from dict2xml import dict2xml
import json

class SubmissionSettings:
    """
        A class to store the settings for a job.
    """

    def __init__(self, 
        settings_dict={
            'model_version': 'stable',
            'remove_stutter': 95,
            'remove_silence': 95,
            'remove_music': 95,
            'remove_other': 95,
            'min_gap': 0,
            'renderVideo': True,
            'renderAudio': False,
            'resolution': 480,
            'framerate': 30
        }):

        self.model_version = settings_dict['model_version']
        self.remove_stutter = settings_dict['remove_stutter']
        self.remove_silence = settings_dict['remove_silence']
        self.remove_music = settings_dict['remove_music']
        self.remove_other = settings_dict['remove_other']
        self.min_gap = settings_dict['min_gap']
        self.renderVideo = settings_dict['renderVideo']
        self.renderAudio = settings_dict['renderAudio']
        self.resolution = settings_dict['resolution']
        self.framerate = settings_dict['framerate']

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            'model_version': self.model_version,
            'remove_stutter': self.remove_stutter,
            'remove_silence': self.remove_silence,
            'remove_music': self.remove_music,
            'remove_other': self.remove_other,
            'min_gap': self.min_gap,
            'renderVideo': self.renderVideo,
            'renderAudio': self.renderAudio,
            'resolution': self.resolution,
            'framerate': self.framerate
        }

    def to_xml(self):
        return dict2xml(self.to_dict())

    def to_json(self):
        return json.dumps(self.to_dict())