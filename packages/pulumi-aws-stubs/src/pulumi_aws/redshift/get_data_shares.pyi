

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDataSharesResult', 'AwaitableGetDataSharesResult', 'get_data_shares', 'get_data_shares_output']
@pulumi.output_type
class GetDataSharesResult:
    
    def __init__(__self__, data_shares=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataShares")
    def data_shares(self) -> Sequence[outputs.GetDataSharesDataShareResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetDataSharesResult(GetDataSharesResult):
    def __await__(self): # -> Generator[Never, Any, GetDataSharesResult]:
        ...
    


def get_data_shares(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDataSharesResult:
    
    ...

def get_data_shares_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDataSharesResult]:
    
    ...

