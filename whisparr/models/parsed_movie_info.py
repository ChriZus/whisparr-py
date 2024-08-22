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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from whisparr.models.language import Language
from whisparr.models.quality_model import QualityModel
from typing import Optional, Set
from typing_extensions import Self

class ParsedMovieInfo(BaseModel):
    """
    ParsedMovieInfo
    """ # noqa: E501
    movie_titles: Optional[List[StrictStr]] = Field(default=None, alias="movieTitles")
    original_title: Optional[StrictStr] = Field(default=None, alias="originalTitle")
    release_title: Optional[StrictStr] = Field(default=None, alias="releaseTitle")
    simple_release_title: Optional[StrictStr] = Field(default=None, alias="simpleReleaseTitle")
    quality: Optional[QualityModel] = None
    languages: Optional[List[Language]] = None
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    release_hash: Optional[StrictStr] = Field(default=None, alias="releaseHash")
    edition: Optional[StrictStr] = None
    year: Optional[StrictInt] = None
    imdb_id: Optional[StrictStr] = Field(default=None, alias="imdbId")
    tmdb_id: Optional[StrictInt] = Field(default=None, alias="tmdbId")
    hardcoded_subs: Optional[StrictStr] = Field(default=None, alias="hardcodedSubs")
    movie_title: Optional[StrictStr] = Field(default=None, alias="movieTitle")
    primary_movie_title: Optional[StrictStr] = Field(default=None, alias="primaryMovieTitle")
    __properties: ClassVar[List[str]] = ["movieTitles", "originalTitle", "releaseTitle", "simpleReleaseTitle", "quality", "languages", "releaseGroup", "releaseHash", "edition", "year", "imdbId", "tmdbId", "hardcodedSubs", "movieTitle", "primaryMovieTitle"]

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
        """Create an instance of ParsedMovieInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "movie_title",
            "primary_movie_title",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item_languages in self.languages:
                if _item_languages:
                    _items.append(_item_languages.to_dict())
            _dict['languages'] = _items
        # set to None if movie_titles (nullable) is None
        # and model_fields_set contains the field
        if self.movie_titles is None and "movie_titles" in self.model_fields_set:
            _dict['movieTitles'] = None

        # set to None if original_title (nullable) is None
        # and model_fields_set contains the field
        if self.original_title is None and "original_title" in self.model_fields_set:
            _dict['originalTitle'] = None

        # set to None if release_title (nullable) is None
        # and model_fields_set contains the field
        if self.release_title is None and "release_title" in self.model_fields_set:
            _dict['releaseTitle'] = None

        # set to None if simple_release_title (nullable) is None
        # and model_fields_set contains the field
        if self.simple_release_title is None and "simple_release_title" in self.model_fields_set:
            _dict['simpleReleaseTitle'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if release_hash (nullable) is None
        # and model_fields_set contains the field
        if self.release_hash is None and "release_hash" in self.model_fields_set:
            _dict['releaseHash'] = None

        # set to None if edition (nullable) is None
        # and model_fields_set contains the field
        if self.edition is None and "edition" in self.model_fields_set:
            _dict['edition'] = None

        # set to None if imdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.imdb_id is None and "imdb_id" in self.model_fields_set:
            _dict['imdbId'] = None

        # set to None if hardcoded_subs (nullable) is None
        # and model_fields_set contains the field
        if self.hardcoded_subs is None and "hardcoded_subs" in self.model_fields_set:
            _dict['hardcodedSubs'] = None

        # set to None if movie_title (nullable) is None
        # and model_fields_set contains the field
        if self.movie_title is None and "movie_title" in self.model_fields_set:
            _dict['movieTitle'] = None

        # set to None if primary_movie_title (nullable) is None
        # and model_fields_set contains the field
        if self.primary_movie_title is None and "primary_movie_title" in self.model_fields_set:
            _dict['primaryMovieTitle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParsedMovieInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "movieTitles": obj.get("movieTitles"),
            "originalTitle": obj.get("originalTitle"),
            "releaseTitle": obj.get("releaseTitle"),
            "simpleReleaseTitle": obj.get("simpleReleaseTitle"),
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "languages": [Language.from_dict(_item) for _item in obj["languages"]] if obj.get("languages") is not None else None,
            "releaseGroup": obj.get("releaseGroup"),
            "releaseHash": obj.get("releaseHash"),
            "edition": obj.get("edition"),
            "year": obj.get("year"),
            "imdbId": obj.get("imdbId"),
            "tmdbId": obj.get("tmdbId"),
            "hardcodedSubs": obj.get("hardcodedSubs"),
            "movieTitle": obj.get("movieTitle"),
            "primaryMovieTitle": obj.get("primaryMovieTitle")
        })
        return _obj


