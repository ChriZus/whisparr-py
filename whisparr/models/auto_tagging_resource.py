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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from whisparr.models.auto_tagging_specification_schema import AutoTaggingSpecificationSchema

class AutoTaggingResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    remove_tags_automatically: Optional[bool]
    tags: Optional[List]
    specifications: Optional[List]
    __properties = ["id", "name", "removeTagsAutomatically", "tags", "specifications"]

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
    def from_json(cls, json_str: str) -> AutoTaggingResource:
        """Create an instance of AutoTaggingResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in specifications (list)
        _items = []
        if self.specifications:
            for _item in self.specifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specifications'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        # set to None if specifications (nullable) is None
        if self.specifications is None:
            _dict['specifications'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AutoTaggingResource:
        """Create an instance of AutoTaggingResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AutoTaggingResource.parse_obj(obj)

        _obj = AutoTaggingResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "remove_tags_automatically": obj.get("removeTagsAutomatically"),
            "tags": obj.get("tags"),
            "specifications": [AutoTaggingSpecificationSchema.from_dict(_item) for _item in obj.get("specifications")] if obj.get("specifications") is not None else None
        })
        return _obj

