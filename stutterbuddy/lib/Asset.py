from dict2xml import dict2xml
import json

class Asset:
    """
    A class representing an asset.
    """
    def __init__(self, asset_dict):
        self.id = asset_dict['id']
        self.userId = asset_dict['userId']
        self.fileId = asset_dict['fileId']
        self.asset_name = asset_dict['asset_name']
        self.status = asset_dict['status']
        self.date_requested = asset_dict['date_requested']
        self.date_uploaded = asset_dict['date_uploaded']
        self.file = asset_dict['file']

    def __str__(self):
        return self.asset_name

    def __repr__(self):
        return self.asset_name

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'fileId': self.fileId,
            'asset_name': self.asset_name,
            'status': self.status,
            'date_requested': self.date_requested,
            'date_uploaded': self.date_uploaded,
            'file': self.file
        }

    def to_xml(self):
        return dict2xml(self.to_dict())

    def to_json(self):
        return json.dumps(self.to_dict())