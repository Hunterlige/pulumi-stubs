

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApiSchemaResult', 'AwaitableGetApiSchemaResult', 'get_api_schema', 'get_api_schema_output']
@pulumi.output_type
class GetApiSchemaResult:
    
    def __init__(__self__, azure_api_version=..., components=..., content_type=..., definitions=..., id=..., name=..., provisioning_state=..., type=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> Optional[Any]:
        
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
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetApiSchemaResult(GetApiSchemaResult):
    def __await__(self): # -> Generator[Never, Any, GetApiSchemaResult]:
        ...
    


def get_api_schema(api_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., schema_id: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApiSchemaResult:
    
    ...

def get_api_schema_output(api_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_id: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApiSchemaResult]:
    
    ...

