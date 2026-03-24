

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAddonVersionResult', 'AwaitableGetAddonVersionResult', 'get_addon_version', 'get_addon_version_output']
@pulumi.output_type
class GetAddonVersionResult:
    
    def __init__(__self__, addon_name=..., id=..., kubernetes_version=..., most_recent=..., region=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAddonVersionResult(GetAddonVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetAddonVersionResult]:
        ...
    


def get_addon_version(addon_name: Optional[_builtins.str] = ..., kubernetes_version: Optional[_builtins.str] = ..., most_recent: Optional[_builtins.bool] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAddonVersionResult:
    
    ...

def get_addon_version_output(addon_name: Optional[pulumi.Input[_builtins.str]] = ..., kubernetes_version: Optional[pulumi.Input[_builtins.str]] = ..., most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAddonVersionResult]:
    
    ...

