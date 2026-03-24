

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerlessLifecyclePolicyResult', 'AwaitableGetServerlessLifecyclePolicyResult', 'get_serverless_lifecycle_policy', 'get_serverless_lifecycle_policy_output']
@pulumi.output_type
class GetServerlessLifecyclePolicyResult:
    
    def __init__(__self__, created_date=..., description=..., id=..., last_modified_date=..., name=..., policy=..., policy_version=..., region=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str:
        
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
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyVersion")
    def policy_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


class AwaitableGetServerlessLifecyclePolicyResult(GetServerlessLifecyclePolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetServerlessLifecyclePolicyResult]:
        ...
    


def get_serverless_lifecycle_policy(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerlessLifecyclePolicyResult:
    
    ...

def get_serverless_lifecycle_policy_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerlessLifecyclePolicyResult]:
    
    ...

