

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSuppressionResult', 'AwaitableGetSuppressionResult', 'get_suppression', 'get_suppression_output']
@pulumi.output_type
class GetSuppressionResult:
    
    def __init__(__self__, azure_api_version=..., expiration_time_stamp=..., id=..., name=..., suppression_id=..., system_data=..., ttl=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTimeStamp")
    def expiration_time_stamp(self) -> _builtins.str:
        
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
    @pulumi.getter(name="suppressionId")
    def suppression_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSuppressionResult(GetSuppressionResult):
    def __await__(self): # -> Generator[Never, Any, GetSuppressionResult]:
        ...
    


def get_suppression(name: Optional[_builtins.str] = ..., recommendation_id: Optional[_builtins.str] = ..., resource_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSuppressionResult:
    
    ...

def get_suppression_output(name: Optional[pulumi.Input[_builtins.str]] = ..., recommendation_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSuppressionResult]:
    
    ...

