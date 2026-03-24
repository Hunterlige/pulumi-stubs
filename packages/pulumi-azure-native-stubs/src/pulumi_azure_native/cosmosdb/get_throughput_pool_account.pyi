

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetThroughputPoolAccountResult', 'AwaitableGetThroughputPoolAccountResult', 'get_throughput_pool_account', 'get_throughput_pool_account_output']
@pulumi.output_type
class GetThroughputPoolAccountResult:
    
    def __init__(__self__, account_instance_id=..., account_location=..., account_resource_identifier=..., azure_api_version=..., id=..., name=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountInstanceId")
    def account_instance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountLocation")
    def account_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountResourceIdentifier")
    def account_resource_identifier(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetThroughputPoolAccountResult(GetThroughputPoolAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetThroughputPoolAccountResult]:
        ...
    


def get_throughput_pool_account(resource_group_name: Optional[_builtins.str] = ..., throughput_pool_account_name: Optional[_builtins.str] = ..., throughput_pool_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetThroughputPoolAccountResult:
    
    ...

def get_throughput_pool_account_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., throughput_pool_account_name: Optional[pulumi.Input[_builtins.str]] = ..., throughput_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetThroughputPoolAccountResult]:
    
    ...

