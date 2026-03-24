

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAzureVersionsResult', 'AwaitableGetAzureVersionsResult', 'get_azure_versions', 'get_azure_versions_output']
@pulumi.output_type
class GetAzureVersionsResult:
    
    def __init__(__self__, id=..., location=..., project=..., supported_regions=..., valid_versions=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedRegions")
    def supported_regions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validVersions")
    def valid_versions(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetAzureVersionsResult(GetAzureVersionsResult):
    def __await__(self): # -> Generator[Never, Any, GetAzureVersionsResult]:
        ...
    


def get_azure_versions(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAzureVersionsResult:
    
    ...

def get_azure_versions_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAzureVersionsResult]:
    
    ...

