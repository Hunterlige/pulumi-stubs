

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBlobInventoryPolicyResult', 'AwaitableGetBlobInventoryPolicyResult', 'get_blob_inventory_policy', 'get_blob_inventory_policy_output']
@pulumi.output_type
class GetBlobInventoryPolicyResult:
    
    def __init__(__self__, azure_api_version=..., id=..., last_modified_time=..., name=..., policy=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> outputs.BlobInventoryPolicySchemaResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBlobInventoryPolicyResult(GetBlobInventoryPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetBlobInventoryPolicyResult]:
        ...
    


def get_blob_inventory_policy(account_name: Optional[_builtins.str] = ..., blob_inventory_policy_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBlobInventoryPolicyResult:
    
    ...

def get_blob_inventory_policy_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., blob_inventory_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBlobInventoryPolicyResult]:
    
    ...

