# AlternativeTitleResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**source_type** | [**SourceType**](SourceType.md) |  | [optional] 
**movie_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**clean_title** | **str** |  | [optional] 
**source_id** | **int** |  | [optional] 
**votes** | **int** |  | [optional] 
**vote_count** | **int** |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 

## Example

```python
from whisparr.models.alternative_title_resource import AlternativeTitleResource

# TODO update the JSON string below
json = "{}"
# create an instance of AlternativeTitleResource from a JSON string
alternative_title_resource_instance = AlternativeTitleResource.from_json(json)
# print the JSON string representation of the object
print AlternativeTitleResource.to_json()

# convert the object into a dict
alternative_title_resource_dict = alternative_title_resource_instance.to_dict()
# create an instance of AlternativeTitleResource from a dict
alternative_title_resource_form_dict = alternative_title_resource.from_dict(alternative_title_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


