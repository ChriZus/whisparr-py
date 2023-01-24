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


from typing import Optional
from pydantic import BaseModel

class TimeSpan(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    ticks: Optional[int]
    days: Optional[int]
    hours: Optional[int]
    milliseconds: Optional[int]
    minutes: Optional[int]
    seconds: Optional[int]
    total_days: Optional[float]
    total_hours: Optional[float]
    total_milliseconds: Optional[float]
    total_minutes: Optional[float]
    total_seconds: Optional[float]
    __properties = ["ticks", "days", "hours", "milliseconds", "minutes", "seconds", "totalDays", "totalHours", "totalMilliseconds", "totalMinutes", "totalSeconds"]

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
    def from_json(cls, json_str: str) -> TimeSpan:
        """Create an instance of TimeSpan from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "days",
                            "hours",
                            "milliseconds",
                            "minutes",
                            "seconds",
                            "total_days",
                            "total_hours",
                            "total_milliseconds",
                            "total_minutes",
                            "total_seconds",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimeSpan:
        """Create an instance of TimeSpan from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TimeSpan.parse_obj(obj)

        _obj = TimeSpan.parse_obj({
            "ticks": obj.get("ticks"),
            "days": obj.get("days"),
            "hours": obj.get("hours"),
            "milliseconds": obj.get("milliseconds"),
            "minutes": obj.get("minutes"),
            "seconds": obj.get("seconds"),
            "total_days": obj.get("totalDays"),
            "total_hours": obj.get("totalHours"),
            "total_milliseconds": obj.get("totalMilliseconds"),
            "total_minutes": obj.get("totalMinutes"),
            "total_seconds": obj.get("totalSeconds")
        })
        return _obj

