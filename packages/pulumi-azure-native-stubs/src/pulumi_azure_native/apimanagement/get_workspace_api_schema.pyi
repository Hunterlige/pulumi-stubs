

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkspaceApiSchemaResult', 'AwaitableGetWorkspaceApiSchemaResult', 'get_workspace_api_schema', 'get_workspace_api_schema_output']
@pulumi.output_type
class GetWorkspaceApiSchemaResult:
    
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
    


class AwaitableGetWorkspaceApiSchemaResult(GetWorkspaceApiSchemaResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkspaceApiSchemaResult]:
        ...
    


def get_workspace_api_schema(api_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., schema_id: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., workspace_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkspaceApiSchemaResult:
    
    ...

def get_workspace_api_schema_output(api_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_id: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkspaceApiSchemaResult]:
    
    ...

