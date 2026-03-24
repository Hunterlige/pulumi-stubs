

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApiPolicyResult', 'AwaitableGetApiPolicyResult', 'get_api_policy', 'get_api_policy_output']
@pulumi.output_type
class GetApiPolicyResult:
    
    def __init__(__self__, azure_api_version=..., format=..., id=..., name=..., type=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


class AwaitableGetApiPolicyResult(GetApiPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetApiPolicyResult]:
        ...
    


def get_api_policy(api_id: Optional[_builtins.str] = ..., format: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApiPolicyResult:
    
    ...

def get_api_policy_output(api_id: Optional[pulumi.Input[_builtins.str]] = ..., format: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApiPolicyResult]:
    
    ...

