

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSupportedDatabaseFlagsResult', 'AwaitableGetSupportedDatabaseFlagsResult', 'get_supported_database_flags', 'get_supported_database_flags_output']
@pulumi.output_type
class GetSupportedDatabaseFlagsResult:
    
    def __init__(__self__, id=..., location=..., project=..., supported_database_flags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedDatabaseFlags")
    def supported_database_flags(self) -> Sequence[outputs.GetSupportedDatabaseFlagsSupportedDatabaseFlagResult]:
        
        ...
    


class AwaitableGetSupportedDatabaseFlagsResult(GetSupportedDatabaseFlagsResult):
    def __await__(self): # -> Generator[Never, Any, GetSupportedDatabaseFlagsResult]:
        ...
    


def get_supported_database_flags(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSupportedDatabaseFlagsResult:
    
    ...

def get_supported_database_flags_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSupportedDatabaseFlagsResult]:
    
    ...

