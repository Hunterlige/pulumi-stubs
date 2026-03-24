

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIntegrationRuntimeObjectMetadatumResult', ..., 'get_integration_runtime_object_metadatum', 'get_integration_runtime_object_metadatum_output']
@pulumi.output_type
class GetIntegrationRuntimeObjectMetadatumResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]:
        
        ...
    


class AwaitableGetIntegrationRuntimeObjectMetadatumResult(GetIntegrationRuntimeObjectMetadatumResult):
    def __await__(self): # -> Generator[Never, Any, GetIntegrationRuntimeObjectMetadatumResult]:
        ...
    


def get_integration_runtime_object_metadatum(integration_runtime_name: Optional[_builtins.str] = ..., metadata_path: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIntegrationRuntimeObjectMetadatumResult:
    
    ...

def get_integration_runtime_object_metadatum_output(integration_runtime_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata_path: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIntegrationRuntimeObjectMetadatumResult]:
    
    ...

