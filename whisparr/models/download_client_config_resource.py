# coding: utf-8

"""
    Radarr

    Radarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel

class DownloadClientConfigResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    download_client_working_folders: Optional[str]
    enable_completed_download_handling: Optional[bool]
    check_for_finished_download_interval: Optional[int]
    auto_redownload_failed: Optional[bool]
    auto_redownload_failed_from_interactive_search: Optional[bool]
    __properties = ["id", "downloadClientWorkingFolders", "enableCompletedDownloadHandling", "checkForFinishedDownloadInterval", "autoRedownloadFailed", "autoRedownloadFailedFromInteractiveSearch"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DownloadClientConfigResource:
        """Create an instance of DownloadClientConfigResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if download_client_working_folders (nullable) is None
        if self.download_client_working_folders is None:
            _dict['downloadClientWorkingFolders'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DownloadClientConfigResource:
        """Create an instance of DownloadClientConfigResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DownloadClientConfigResource.parse_obj(obj)

        _obj = DownloadClientConfigResource.parse_obj({
            "id": obj.get("id"),
            "download_client_working_folders": obj.get("downloadClientWorkingFolders"),
            "enable_completed_download_handling": obj.get("enableCompletedDownloadHandling"),
            "check_for_finished_download_interval": obj.get("checkForFinishedDownloadInterval"),
            "auto_redownload_failed": obj.get("autoRedownloadFailed"),
            "auto_redownload_failed_from_interactive_search": obj.get("autoRedownloadFailedFromInteractiveSearch")
        })
        return _obj

