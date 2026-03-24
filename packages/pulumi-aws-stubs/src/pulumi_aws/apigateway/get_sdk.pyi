

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSdkResult', 'AwaitableGetSdkResult', 'get_sdk', 'get_sdk_output']
@pulumi.output_type
class GetSdkResult:
    
    def __init__(__self__, body=..., content_disposition=..., content_type=..., id=..., parameters=..., region=..., rest_api_id=..., sdk_type=..., stage_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sdkType")
    def sdk_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> _builtins.str:
        ...
    


class AwaitableGetSdkResult(GetSdkResult):
    def __await__(self): # -> Generator[Never, Any, GetSdkResult]:
        ...
    


def get_sdk(parameters: Optional[Mapping[str, _builtins.str]] = ..., region: Optional[_builtins.str] = ..., rest_api_id: Optional[_builtins.str] = ..., sdk_type: Optional[_builtins.str] = ..., stage_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSdkResult:
    
    ...

def get_sdk_output(parameters: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., rest_api_id: Optional[pulumi.Input[_builtins.str]] = ..., sdk_type: Optional[pulumi.Input[_builtins.str]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSdkResult]:
    
    ...

