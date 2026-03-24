

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBlobServicePropertiesResult', 'AwaitableGetBlobServicePropertiesResult', 'get_blob_service_properties', 'get_blob_service_properties_output']
@pulumi.output_type
class GetBlobServicePropertiesResult:
    
    def __init__(__self__, automatic_snapshot_policy_enabled=..., azure_api_version=..., change_feed=..., container_delete_retention_policy=..., cors=..., default_service_version=..., delete_retention_policy=..., id=..., is_versioning_enabled=..., last_access_time_tracking_policy=..., name=..., restore_policy=..., sku=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticSnapshotPolicyEnabled")
    def automatic_snapshot_policy_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeFeed")
    def change_feed(self) -> Optional[outputs.ChangeFeedResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerDeleteRetentionPolicy")
    def container_delete_retention_policy(self) -> Optional[outputs.DeleteRetentionPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[outputs.CorsRulesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultServiceVersion")
    def default_service_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteRetentionPolicy")
    def delete_retention_policy(self) -> Optional[outputs.DeleteRetentionPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isVersioningEnabled")
    def is_versioning_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAccessTimeTrackingPolicy")
    def last_access_time_tracking_policy(self) -> Optional[outputs.LastAccessTimeTrackingPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicy")
    def restore_policy(self) -> Optional[outputs.RestorePolicyPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBlobServicePropertiesResult(GetBlobServicePropertiesResult):
    def __await__(self): # -> Generator[Never, Any, GetBlobServicePropertiesResult]:
        ...
    


def get_blob_service_properties(account_name: Optional[_builtins.str] = ..., blob_services_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBlobServicePropertiesResult:
    
    ...

def get_blob_service_properties_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., blob_services_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBlobServicePropertiesResult]:
    
    ...

