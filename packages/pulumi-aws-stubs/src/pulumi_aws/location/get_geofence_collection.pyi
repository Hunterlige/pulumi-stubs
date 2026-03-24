

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGeofenceCollectionResult', 'AwaitableGetGeofenceCollectionResult', 'get_geofence_collection', 'get_geofence_collection_output']
@pulumi.output_type
class GetGeofenceCollectionResult:
    
    def __init__(__self__, collection_arn=..., collection_name=..., create_time=..., description=..., id=..., kms_key_id=..., region=..., tags=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionArn")
    def collection_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


class AwaitableGetGeofenceCollectionResult(GetGeofenceCollectionResult):
    def __await__(self): # -> Generator[Never, Any, GetGeofenceCollectionResult]:
        ...
    


def get_geofence_collection(collection_name: Optional[_builtins.str] = ..., kms_key_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGeofenceCollectionResult:
    
    ...

def get_geofence_collection_output(collection_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGeofenceCollectionResult]:
    
    ...

