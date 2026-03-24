

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBundleResult', 'AwaitableGetBundleResult', 'get_bundle', 'get_bundle_output']
@pulumi.output_type
class GetBundleResult:
    
    def __init__(__self__, bundle_id=..., compute_types=..., description=..., id=..., name=..., owner=..., region=..., root_storages=..., user_storages=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeTypes")
    def compute_types(self) -> Sequence[outputs.GetBundleComputeTypeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootStorages")
    def root_storages(self) -> Sequence[outputs.GetBundleRootStorageResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userStorages")
    def user_storages(self) -> Sequence[outputs.GetBundleUserStorageResult]:
        
        ...
    


class AwaitableGetBundleResult(GetBundleResult):
    def __await__(self): # -> Generator[Never, Any, GetBundleResult]:
        ...
    


def get_bundle(bundle_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., owner: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBundleResult:
    
    ...

def get_bundle_output(bundle_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., owner: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBundleResult]:
    
    ...

