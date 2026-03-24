

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReceivedLicensesResult', 'AwaitableGetReceivedLicensesResult', 'get_received_licenses', 'get_received_licenses_output']
@pulumi.output_type
class GetReceivedLicensesResult:
    
    def __init__(__self__, arns=..., filters=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetReceivedLicensesFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetReceivedLicensesResult(GetReceivedLicensesResult):
    def __await__(self): # -> Generator[Never, Any, GetReceivedLicensesResult]:
        ...
    


def get_received_licenses(filters: Optional[Sequence[Union[GetReceivedLicensesFilterArgs, GetReceivedLicensesFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReceivedLicensesResult:
    
    ...

def get_received_licenses_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetReceivedLicensesFilterArgs, GetReceivedLicensesFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReceivedLicensesResult]:
    
    ...

