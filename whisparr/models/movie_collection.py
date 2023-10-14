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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from whisparr.models.media_cover import MediaCover
from whisparr.models.movie_metadata import MovieMetadata
from whisparr.models.movie_status_type import MovieStatusType

class MovieCollection(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    title: Optional[str]
    clean_title: Optional[str]
    sort_title: Optional[str]
    tmdb_id: Optional[int]
    overview: Optional[str]
    monitored: Optional[bool]
    quality_profile_id: Optional[int]
    root_folder_path: Optional[str]
    search_on_add: Optional[bool]
    minimum_availability: Optional[MovieStatusType]
    last_info_sync: Optional[datetime]
    images: Optional[List]
    added: Optional[datetime]
    movies: Optional[List]
    tags: Optional[List]
    __properties = ["id", "title", "cleanTitle", "sortTitle", "tmdbId", "overview", "monitored", "qualityProfileId", "rootFolderPath", "searchOnAdd", "minimumAvailability", "lastInfoSync", "images", "added", "movies", "tags"]

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
    def from_json(cls, json_str: str) -> MovieCollection:
        """Create an instance of MovieCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in movies (list)
        _items = []
        if self.movies:
            for _item in self.movies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['movies'] = _items
        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if clean_title (nullable) is None
        if self.clean_title is None:
            _dict['cleanTitle'] = None

        # set to None if sort_title (nullable) is None
        if self.sort_title is None:
            _dict['sortTitle'] = None

        # set to None if overview (nullable) is None
        if self.overview is None:
            _dict['overview'] = None

        # set to None if root_folder_path (nullable) is None
        if self.root_folder_path is None:
            _dict['rootFolderPath'] = None

        # set to None if last_info_sync (nullable) is None
        if self.last_info_sync is None:
            _dict['lastInfoSync'] = None

        # set to None if images (nullable) is None
        if self.images is None:
            _dict['images'] = None

        # set to None if movies (nullable) is None
        if self.movies is None:
            _dict['movies'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MovieCollection:
        """Create an instance of MovieCollection from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MovieCollection.parse_obj(obj)

        _obj = MovieCollection.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "clean_title": obj.get("cleanTitle"),
            "sort_title": obj.get("sortTitle"),
            "tmdb_id": obj.get("tmdbId"),
            "overview": obj.get("overview"),
            "monitored": obj.get("monitored"),
            "quality_profile_id": obj.get("qualityProfileId"),
            "root_folder_path": obj.get("rootFolderPath"),
            "search_on_add": obj.get("searchOnAdd"),
            "minimum_availability": obj.get("minimumAvailability"),
            "last_info_sync": obj.get("lastInfoSync"),
            "images": [MediaCover.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "added": obj.get("added"),
            "movies": [MovieMetadata.from_dict(_item) for _item in obj.get("movies")] if obj.get("movies") is not None else None,
            "tags": obj.get("tags")
        })
        return _obj

