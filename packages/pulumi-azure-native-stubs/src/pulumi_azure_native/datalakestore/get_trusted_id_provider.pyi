

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTrustedIdProviderResult', 'AwaitableGetTrustedIdProviderResult', 'get_trusted_id_provider', 'get_trusted_id_provider_output']
@pulumi.output_type
class GetTrustedIdProviderResult:
    
    def __init__(__self__, azure_api_version=..., id=..., id_provider=..., name=..., type=...) -> None:
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
    @pulumi.getter(name="idProvider")
    def id_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTrustedIdProviderResult(GetTrustedIdProviderResult):
    def __await__(self): # -> Generator[Never, Any, GetTrustedIdProviderResult]:
        ...
    


def get_trusted_id_provider(account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., trusted_id_provider_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTrustedIdProviderResult:
    
    ...

def get_trusted_id_provider_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., trusted_id_provider_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTrustedIdProviderResult]:
    
    ...

