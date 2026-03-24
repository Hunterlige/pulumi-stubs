

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCloudExadataInfrastructuresResult', 'AwaitableGetCloudExadataInfrastructuresResult', 'get_cloud_exadata_infrastructures', 'get_cloud_exadata_infrastructures_output']
@pulumi.output_type
class GetCloudExadataInfrastructuresResult:
    
    def __init__(__self__, cloud_exadata_infrastructures=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructures")
    def cloud_exadata_infrastructures(self) -> Sequence[outputs.GetCloudExadataInfrastructuresCloudExadataInfrastructureResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetCloudExadataInfrastructuresResult(GetCloudExadataInfrastructuresResult):
    def __await__(self): # -> Generator[Never, Any, GetCloudExadataInfrastructuresResult]:
        ...
    


def get_cloud_exadata_infrastructures(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCloudExadataInfrastructuresResult:
    
    ...

def get_cloud_exadata_infrastructures_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCloudExadataInfrastructuresResult]:
    
    ...

