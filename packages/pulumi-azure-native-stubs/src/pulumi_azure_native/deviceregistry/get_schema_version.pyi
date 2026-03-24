

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSchemaVersionResult', 'AwaitableGetSchemaVersionResult', 'get_schema_version', 'get_schema_version_output']
@pulumi.output_type
class GetSchemaVersionResult:
    
    def __init__(__self__, azure_api_version=..., description=..., hash=..., id=..., name=..., provisioning_state=..., schema_content=..., system_data=..., type=..., uuid=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hash(self) -> _builtins.str:
        
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
    @pulumi.getter(name="schemaContent")
    def schema_content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSchemaVersionResult(GetSchemaVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetSchemaVersionResult]:
        ...
    


def get_schema_version(resource_group_name: Optional[_builtins.str] = ..., schema_name: Optional[_builtins.str] = ..., schema_registry_name: Optional[_builtins.str] = ..., schema_version_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSchemaVersionResult:
    
    ...

def get_schema_version_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_registry_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_version_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSchemaVersionResult]:
    
    ...

