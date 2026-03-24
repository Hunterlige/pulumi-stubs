

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPureStoragePolicyResult', 'AwaitableGetPureStoragePolicyResult', 'get_pure_storage_policy', 'get_pure_storage_policy_output']
@pulumi.output_type
class GetPureStoragePolicyResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., provisioning_state=..., storage_policy_definition=..., storage_pool_id=..., system_data=..., type=...) -> None:
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
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePolicyDefinition")
    def storage_policy_definition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePoolId")
    def storage_pool_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPureStoragePolicyResult(GetPureStoragePolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetPureStoragePolicyResult]:
        ...
    


def get_pure_storage_policy(private_cloud_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., storage_policy_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPureStoragePolicyResult:
    
    ...

def get_pure_storage_policy_output(private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPureStoragePolicyResult]:
    
    ...

