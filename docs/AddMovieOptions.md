# AddMovieOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_episodes_with_files** | **bool** |  | [optional] 
**ignore_episodes_without_files** | **bool** |  | [optional] 
**search_for_movie** | **bool** |  | [optional] 

## Example

```python
from whisparr.models.add_movie_options import AddMovieOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AddMovieOptions from a JSON string
add_movie_options_instance = AddMovieOptions.from_json(json)
# print the JSON string representation of the object
print AddMovieOptions.to_json()

# convert the object into a dict
add_movie_options_dict = add_movie_options_instance.to_dict()
# create an instance of AddMovieOptions from a dict
add_movie_options_form_dict = add_movie_options.from_dict(add_movie_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


