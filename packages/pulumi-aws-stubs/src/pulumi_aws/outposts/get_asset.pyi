

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAssetResult', 'AwaitableGetAssetResult', 'get_asset', 'get_asset_output']
@pulumi.output_type
class GetAssetResult:
    
    def __init__(__self__, arn=..., asset_id=..., asset_type=..., host_id=..., id=..., rack_elevation=..., rack_id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assetId")
    def asset_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assetType")
    def asset_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rackElevation")
    def rack_elevation(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rackId")
    def rack_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetAssetResult(GetAssetResult):
    def __await__(self): # -> Generator[Never, Any, GetAssetResult]:
        ...
    


def get_asset(arn: Optional[_builtins.str] = ..., asset_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAssetResult:
    
    ...

def get_asset_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., asset_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAssetResult]:
    
    ...

