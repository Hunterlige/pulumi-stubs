

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMetadataSchemaResult', 'AwaitableGetMetadataSchemaResult', 'get_metadata_schema', 'get_metadata_schema_output']
@pulumi.output_type
class GetMetadataSchemaResult:
    
    def __init__(__self__, assigned_to=..., azure_api_version=..., id=..., name=..., schema=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedTo")
    def assigned_to(self) -> Optional[Sequence[outputs.MetadataAssignmentResponse]]:
        
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
    @pulumi.getter
    def schema(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetMetadataSchemaResult(GetMetadataSchemaResult):
    def __await__(self): # -> Generator[Never, Any, GetMetadataSchemaResult]:
        ...
    


def get_metadata_schema(metadata_schema_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMetadataSchemaResult:
    
    ...

def get_metadata_schema_output(metadata_schema_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMetadataSchemaResult]:
    
    ...

