

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccessPointsResult', 'AwaitableGetAccessPointsResult', 'get_access_points', 'get_access_points_output']
@pulumi.output_type
class GetAccessPointsResult:
    
    def __init__(__self__, access_points=..., account_id=..., bucket=..., data_source_id=..., data_source_type=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPoints")
    def access_points(self) -> Sequence[outputs.GetAccessPointsAccessPointResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetAccessPointsResult(GetAccessPointsResult):
    def __await__(self): # -> Generator[Never, Any, GetAccessPointsResult]:
        ...
    


def get_access_points(account_id: Optional[_builtins.str] = ..., bucket: Optional[_builtins.str] = ..., data_source_id: Optional[_builtins.str] = ..., data_source_type: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccessPointsResult:
    
    ...

def get_access_points_output(account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., bucket: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., data_source_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., data_source_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccessPointsResult]:
    
    ...

