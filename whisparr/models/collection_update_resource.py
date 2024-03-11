# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: b08981dee068e1ed23e4f45a0d8fe70ef7bf7703
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from whisparr.models.movie_status_type import MovieStatusType
from typing import Optional, Set
from typing_extensions import Self

class CollectionUpdateResource(BaseModel):
    """
    CollectionUpdateResource
    """ # noqa: E501
    collection_ids: Optional[List[StrictInt]] = Field(default=None, alias="collectionIds")
    monitored: Optional[StrictBool] = None
    monitor_movies: Optional[StrictBool] = Field(default=None, alias="monitorMovies")
    search_on_add: Optional[StrictBool] = Field(default=None, alias="searchOnAdd")
    quality_profile_id: Optional[StrictInt] = Field(default=None, alias="qualityProfileId")
    root_folder_path: Optional[StrictStr] = Field(default=None, alias="rootFolderPath")
    minimum_availability: Optional[MovieStatusType] = Field(default=None, alias="minimumAvailability")
    __properties: ClassVar[List[str]] = ["collectionIds", "monitored", "monitorMovies", "searchOnAdd", "qualityProfileId", "rootFolderPath", "minimumAvailability"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CollectionUpdateResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if collection_ids (nullable) is None
        # and model_fields_set contains the field
        if self.collection_ids is None and "collection_ids" in self.model_fields_set:
            _dict['collectionIds'] = None

        # set to None if monitored (nullable) is None
        # and model_fields_set contains the field
        if self.monitored is None and "monitored" in self.model_fields_set:
            _dict['monitored'] = None

        # set to None if monitor_movies (nullable) is None
        # and model_fields_set contains the field
        if self.monitor_movies is None and "monitor_movies" in self.model_fields_set:
            _dict['monitorMovies'] = None

        # set to None if search_on_add (nullable) is None
        # and model_fields_set contains the field
        if self.search_on_add is None and "search_on_add" in self.model_fields_set:
            _dict['searchOnAdd'] = None

        # set to None if quality_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.quality_profile_id is None and "quality_profile_id" in self.model_fields_set:
            _dict['qualityProfileId'] = None

        # set to None if root_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.root_folder_path is None and "root_folder_path" in self.model_fields_set:
            _dict['rootFolderPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CollectionUpdateResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "collectionIds": obj.get("collectionIds"),
            "monitored": obj.get("monitored"),
            "monitorMovies": obj.get("monitorMovies"),
            "searchOnAdd": obj.get("searchOnAdd"),
            "qualityProfileId": obj.get("qualityProfileId"),
            "rootFolderPath": obj.get("rootFolderPath"),
            "minimumAvailability": obj.get("minimumAvailability")
        })
        return _obj


