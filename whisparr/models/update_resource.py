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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel
from whisparr.models.update_changes import UpdateChanges

class UpdateResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    version: Optional[str]
    branch: Optional[str]
    release_date: Optional[datetime]
    file_name: Optional[str]
    url: Optional[str]
    installed: Optional[bool]
    installed_on: Optional[datetime]
    installable: Optional[bool]
    latest: Optional[bool]
    changes: Optional[UpdateChanges]
    hash: Optional[str]
    __properties = ["id", "version", "branch", "releaseDate", "fileName", "url", "installed", "installedOn", "installable", "latest", "changes", "hash"]

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
    def from_json(cls, json_str: str) -> UpdateResource:
        """Create an instance of UpdateResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of changes
        if self.changes:
            _dict['changes'] = self.changes.to_dict()
        # set to None if branch (nullable) is None
        if self.branch is None:
            _dict['branch'] = None

        # set to None if file_name (nullable) is None
        if self.file_name is None:
            _dict['fileName'] = None

        # set to None if url (nullable) is None
        if self.url is None:
            _dict['url'] = None

        # set to None if installed_on (nullable) is None
        if self.installed_on is None:
            _dict['installedOn'] = None

        # set to None if hash (nullable) is None
        if self.hash is None:
            _dict['hash'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateResource:
        """Create an instance of UpdateResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UpdateResource.parse_obj(obj)

        _obj = UpdateResource.parse_obj({
            "id": obj.get("id"),
            "version": obj.get("version"),
            "branch": obj.get("branch"),
            "release_date": obj.get("releaseDate"),
            "file_name": obj.get("fileName"),
            "url": obj.get("url"),
            "installed": obj.get("installed"),
            "installed_on": obj.get("installedOn"),
            "installable": obj.get("installable"),
            "latest": obj.get("latest"),
            "changes": UpdateChanges.from_dict(obj.get("changes")) if obj.get("changes") is not None else None,
            "hash": obj.get("hash")
        })
        return _obj

