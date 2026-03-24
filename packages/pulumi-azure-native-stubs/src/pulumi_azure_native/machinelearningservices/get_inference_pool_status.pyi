

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInferencePoolStatusResult', 'AwaitableGetInferencePoolStatusResult', 'get_inference_pool_status', 'get_inference_pool_status_output']
@pulumi.output_type
class GetInferencePoolStatusResult:
    def __init__(__self__, actual_capacity=..., group_count=..., requested_capacity=..., reserved_capacity=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actualCapacity")
    def actual_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupCount")
    def group_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedCapacity")
    def requested_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedCapacity")
    def reserved_capacity(self) -> Optional[_builtins.int]:
        
        ...
    


class AwaitableGetInferencePoolStatusResult(GetInferencePoolStatusResult):
    def __await__(self): # -> Generator[Never, Any, GetInferencePoolStatusResult]:
        ...
    


def get_inference_pool_status(inference_pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInferencePoolStatusResult:
    
    ...

def get_inference_pool_status_output(inference_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInferencePoolStatusResult]:
    
    ...

