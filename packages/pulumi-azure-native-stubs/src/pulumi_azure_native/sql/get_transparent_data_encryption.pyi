

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTransparentDataEncryptionResult', 'AwaitableGetTransparentDataEncryptionResult', 'get_transparent_data_encryption', 'get_transparent_data_encryption_output']
@pulumi.output_type
class GetTransparentDataEncryptionResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., state=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTransparentDataEncryptionResult(GetTransparentDataEncryptionResult):
    def __await__(self): # -> Generator[Never, Any, GetTransparentDataEncryptionResult]:
        ...
    


def get_transparent_data_encryption(database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., tde_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTransparentDataEncryptionResult:
    
    ...

def get_transparent_data_encryption_output(database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., tde_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTransparentDataEncryptionResult]:
    
    ...

