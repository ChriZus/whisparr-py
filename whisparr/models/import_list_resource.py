# coding: utf-8

"""
    Whisparr

    Whisparr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel
from whisparr.models.field import Field
from whisparr.models.import_list_type import ImportListType
from whisparr.models.movie_status_type import MovieStatusType
from whisparr.models.provider_message import ProviderMessage

class ImportListResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    fields: Optional[List]
    implementation_name: Optional[str]
    implementation: Optional[str]
    config_contract: Optional[str]
    info_link: Optional[str]
    message: Optional[ProviderMessage]
    tags: Optional[List]
    presets: Optional[List]
    enabled: Optional[bool]
    enable_auto: Optional[bool]
    should_monitor: Optional[bool]
    root_folder_path: Optional[str]
    quality_profile_id: Optional[int]
    search_on_add: Optional[bool]
    minimum_availability: Optional[MovieStatusType]
    list_type: Optional[ImportListType]
    list_order: Optional[int]
    __properties = ["id", "name", "fields", "implementationName", "implementation", "configContract", "infoLink", "message", "tags", "presets", "enabled", "enableAuto", "shouldMonitor", "rootFolderPath", "qualityProfileId", "searchOnAdd", "minimumAvailability", "listType", "listOrder"]

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
    def from_json(cls, json_str: str) -> ImportListResource:
        """Create an instance of ImportListResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in presets (list)
        _items = []
        if self.presets:
            for _item in self.presets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['presets'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if fields (nullable) is None
        if self.fields is None:
            _dict['fields'] = None

        # set to None if implementation_name (nullable) is None
        if self.implementation_name is None:
            _dict['implementationName'] = None

        # set to None if implementation (nullable) is None
        if self.implementation is None:
            _dict['implementation'] = None

        # set to None if config_contract (nullable) is None
        if self.config_contract is None:
            _dict['configContract'] = None

        # set to None if info_link (nullable) is None
        if self.info_link is None:
            _dict['infoLink'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        # set to None if presets (nullable) is None
        if self.presets is None:
            _dict['presets'] = None

        # set to None if root_folder_path (nullable) is None
        if self.root_folder_path is None:
            _dict['rootFolderPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImportListResource:
        """Create an instance of ImportListResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ImportListResource.parse_obj(obj)

        _obj = ImportListResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "fields": [Field.from_dict(_item) for _item in obj.get("fields")] if obj.get("fields") is not None else None,
            "implementation_name": obj.get("implementationName"),
            "implementation": obj.get("implementation"),
            "config_contract": obj.get("configContract"),
            "info_link": obj.get("infoLink"),
            "message": ProviderMessage.from_dict(obj.get("message")) if obj.get("message") is not None else None,
            "tags": obj.get("tags"),
            "presets": [ImportListResource.from_dict(_item) for _item in obj.get("presets")] if obj.get("presets") is not None else None,
            "enabled": obj.get("enabled"),
            "enable_auto": obj.get("enableAuto"),
            "should_monitor": obj.get("shouldMonitor"),
            "root_folder_path": obj.get("rootFolderPath"),
            "quality_profile_id": obj.get("qualityProfileId"),
            "search_on_add": obj.get("searchOnAdd"),
            "minimum_availability": obj.get("minimumAvailability"),
            "list_type": obj.get("listType"),
            "list_order": obj.get("listOrder")
        })
        return _obj

