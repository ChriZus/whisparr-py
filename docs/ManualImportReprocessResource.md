# ManualImportReprocessResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**series_id** | **int** |  | [optional] 
**season_number** | **int** |  | [optional] 
**episodes** | [**List[EpisodeResource]**](EpisodeResource.md) |  | [optional] 
**episode_ids** | **List[int]** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**release_group** | **str** |  | [optional] 
**download_id** | **str** |  | [optional] 
**rejections** | [**List[Rejection]**](Rejection.md) |  | [optional] 

## Example

```python
from whisparr.models.manual_import_reprocess_resource import ManualImportReprocessResource

# TODO update the JSON string below
json = "{}"
# create an instance of ManualImportReprocessResource from a JSON string
manual_import_reprocess_resource_instance = ManualImportReprocessResource.from_json(json)
# print the JSON string representation of the object
print ManualImportReprocessResource.to_json()

# convert the object into a dict
manual_import_reprocess_resource_dict = manual_import_reprocess_resource_instance.to_dict()
# create an instance of ManualImportReprocessResource from a dict
manual_import_reprocess_resource_form_dict = manual_import_reprocess_resource.from_dict(manual_import_reprocess_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


