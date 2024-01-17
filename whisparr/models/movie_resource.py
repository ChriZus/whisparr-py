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
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel
from whisparr.models.add_movie_options import AddMovieOptions
from whisparr.models.alternative_title_resource import AlternativeTitleResource
from whisparr.models.language import Language
from whisparr.models.media_cover import MediaCover
from whisparr.models.movie_collection_resource import MovieCollectionResource
from whisparr.models.movie_file_resource import MovieFileResource
from whisparr.models.movie_statistics_resource import MovieStatisticsResource
from whisparr.models.movie_status_type import MovieStatusType
from whisparr.models.ratings import Ratings

class MovieResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    title: Optional[str]
    original_title: Optional[str]
    original_language: Optional[Language]
    alternate_titles: Optional[List]
    secondary_year: Optional[int]
    secondary_year_source_id: Optional[int]
    sort_title: Optional[str]
    size_on_disk: Optional[int]
    status: Optional[MovieStatusType]
    overview: Optional[str]
    in_cinemas: Optional[datetime]
    physical_release: Optional[datetime]
    digital_release: Optional[datetime]
    physical_release_note: Optional[str]
    images: Optional[List]
    website: Optional[str]
    remote_poster: Optional[str]
    year: Optional[int]
    you_tube_trailer_id: Optional[str]
    studio: Optional[str]
    path: Optional[str]
    quality_profile_id: Optional[int]
    has_file: Optional[bool]
    monitored: Optional[bool]
    minimum_availability: Optional[MovieStatusType]
    is_available: Optional[bool]
    folder_name: Optional[str]
    runtime: Optional[int]
    clean_title: Optional[str]
    imdb_id: Optional[str]
    tmdb_id: Optional[int]
    title_slug: Optional[str]
    root_folder_path: Optional[str]
    folder: Optional[str]
    certification: Optional[str]
    genres: Optional[List]
    tags: Optional[List]
    added: Optional[datetime]
    add_options: Optional[AddMovieOptions]
    ratings: Optional[Ratings]
    movie_file: Optional[MovieFileResource]
    collection: Optional[MovieCollectionResource]
    popularity: Optional[float]
    statistics: Optional[MovieStatisticsResource]
    __properties = ["id", "title", "originalTitle", "originalLanguage", "alternateTitles", "secondaryYear", "secondaryYearSourceId", "sortTitle", "sizeOnDisk", "status", "overview", "inCinemas", "physicalRelease", "digitalRelease", "physicalReleaseNote", "images", "website", "remotePoster", "year", "youTubeTrailerId", "studio", "path", "qualityProfileId", "hasFile", "monitored", "minimumAvailability", "isAvailable", "folderName", "runtime", "cleanTitle", "imdbId", "tmdbId", "titleSlug", "rootFolderPath", "folder", "certification", "genres", "tags", "added", "addOptions", "ratings", "movieFile", "collection", "popularity", "statistics"]

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
    def from_json(cls, json_str: str) -> MovieResource:
        """Create an instance of MovieResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of original_language
        if self.original_language:
            _dict['originalLanguage'] = self.original_language.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in alternate_titles (list)
        _items = []
        if self.alternate_titles:
            for _item in self.alternate_titles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alternateTitles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of add_options
        if self.add_options:
            _dict['addOptions'] = self.add_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of movie_file
        if self.movie_file:
            _dict['movieFile'] = self.movie_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of collection
        if self.collection:
            _dict['collection'] = self.collection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if original_title (nullable) is None
        if self.original_title is None:
            _dict['originalTitle'] = None

        # set to None if alternate_titles (nullable) is None
        if self.alternate_titles is None:
            _dict['alternateTitles'] = None

        # set to None if secondary_year (nullable) is None
        if self.secondary_year is None:
            _dict['secondaryYear'] = None

        # set to None if sort_title (nullable) is None
        if self.sort_title is None:
            _dict['sortTitle'] = None

        # set to None if size_on_disk (nullable) is None
        if self.size_on_disk is None:
            _dict['sizeOnDisk'] = None

        # set to None if overview (nullable) is None
        if self.overview is None:
            _dict['overview'] = None

        # set to None if in_cinemas (nullable) is None
        if self.in_cinemas is None:
            _dict['inCinemas'] = None

        # set to None if physical_release (nullable) is None
        if self.physical_release is None:
            _dict['physicalRelease'] = None

        # set to None if digital_release (nullable) is None
        if self.digital_release is None:
            _dict['digitalRelease'] = None

        # set to None if physical_release_note (nullable) is None
        if self.physical_release_note is None:
            _dict['physicalReleaseNote'] = None

        # set to None if images (nullable) is None
        if self.images is None:
            _dict['images'] = None

        # set to None if website (nullable) is None
        if self.website is None:
            _dict['website'] = None

        # set to None if remote_poster (nullable) is None
        if self.remote_poster is None:
            _dict['remotePoster'] = None

        # set to None if you_tube_trailer_id (nullable) is None
        if self.you_tube_trailer_id is None:
            _dict['youTubeTrailerId'] = None

        # set to None if studio (nullable) is None
        if self.studio is None:
            _dict['studio'] = None

        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if folder_name (nullable) is None
        if self.folder_name is None:
            _dict['folderName'] = None

        # set to None if clean_title (nullable) is None
        if self.clean_title is None:
            _dict['cleanTitle'] = None

        # set to None if imdb_id (nullable) is None
        if self.imdb_id is None:
            _dict['imdbId'] = None

        # set to None if title_slug (nullable) is None
        if self.title_slug is None:
            _dict['titleSlug'] = None

        # set to None if root_folder_path (nullable) is None
        if self.root_folder_path is None:
            _dict['rootFolderPath'] = None

        # set to None if folder (nullable) is None
        if self.folder is None:
            _dict['folder'] = None

        # set to None if certification (nullable) is None
        if self.certification is None:
            _dict['certification'] = None

        # set to None if genres (nullable) is None
        if self.genres is None:
            _dict['genres'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MovieResource:
        """Create an instance of MovieResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MovieResource.parse_obj(obj)

        _obj = MovieResource.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "original_title": obj.get("originalTitle"),
            "original_language": Language.from_dict(obj.get("originalLanguage")) if obj.get("originalLanguage") is not None else None,
            "alternate_titles": [AlternativeTitleResource.from_dict(_item) for _item in obj.get("alternateTitles")] if obj.get("alternateTitles") is not None else None,
            "secondary_year": obj.get("secondaryYear"),
            "secondary_year_source_id": obj.get("secondaryYearSourceId"),
            "sort_title": obj.get("sortTitle"),
            "size_on_disk": obj.get("sizeOnDisk"),
            "status": obj.get("status"),
            "overview": obj.get("overview"),
            "in_cinemas": obj.get("inCinemas"),
            "physical_release": obj.get("physicalRelease"),
            "digital_release": obj.get("digitalRelease"),
            "physical_release_note": obj.get("physicalReleaseNote"),
            "images": [MediaCover.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "website": obj.get("website"),
            "remote_poster": obj.get("remotePoster"),
            "year": obj.get("year"),
            "you_tube_trailer_id": obj.get("youTubeTrailerId"),
            "studio": obj.get("studio"),
            "path": obj.get("path"),
            "quality_profile_id": obj.get("qualityProfileId"),
            "has_file": obj.get("hasFile"),
            "monitored": obj.get("monitored"),
            "minimum_availability": obj.get("minimumAvailability"),
            "is_available": obj.get("isAvailable"),
            "folder_name": obj.get("folderName"),
            "runtime": obj.get("runtime"),
            "clean_title": obj.get("cleanTitle"),
            "imdb_id": obj.get("imdbId"),
            "tmdb_id": obj.get("tmdbId"),
            "title_slug": obj.get("titleSlug"),
            "root_folder_path": obj.get("rootFolderPath"),
            "folder": obj.get("folder"),
            "certification": obj.get("certification"),
            "genres": obj.get("genres"),
            "tags": obj.get("tags"),
            "added": obj.get("added"),
            "add_options": AddMovieOptions.from_dict(obj.get("addOptions")) if obj.get("addOptions") is not None else None,
            "ratings": Ratings.from_dict(obj.get("ratings")) if obj.get("ratings") is not None else None,
            "movie_file": MovieFileResource.from_dict(obj.get("movieFile")) if obj.get("movieFile") is not None else None,
            "collection": MovieCollectionResource.from_dict(obj.get("collection")) if obj.get("collection") is not None else None,
            "popularity": obj.get("popularity"),
            "statistics": MovieStatisticsResource.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None
        })
        return _obj

