

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
__all__ = ['GetLicenseGrantsResult', 'AwaitableGetLicenseGrantsResult', 'get_license_grants', 'get_license_grants_output']
@pulumi.output_type
class GetLicenseGrantsResult:
    
    def __init__(__self__, arns=..., filters=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetLicenseGrantsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetLicenseGrantsResult(GetLicenseGrantsResult):
    def __await__(self): # -> Generator[Never, Any, GetLicenseGrantsResult]:
        ...
    


def get_license_grants(filters: Optional[Sequence[Union[GetLicenseGrantsFilterArgs, GetLicenseGrantsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLicenseGrantsResult:
    
    ...

def get_license_grants_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetLicenseGrantsFilterArgs, GetLicenseGrantsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLicenseGrantsResult]:
    
    ...

