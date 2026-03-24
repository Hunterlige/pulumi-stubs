

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetComponentLinkedStorageAccountResult', 'AwaitableGetComponentLinkedStorageAccountResult', 'get_component_linked_storage_account', 'get_component_linked_storage_account_output']
@pulumi.output_type
class GetComponentLinkedStorageAccountResult:
    
    def __init__(__self__, azure_api_version=..., id=..., linked_storage_account=..., name=..., type=...) -> None:
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
    @pulumi.getter(name="linkedStorageAccount")
    def linked_storage_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetComponentLinkedStorageAccountResult(GetComponentLinkedStorageAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetComponentLinkedStorageAccountResult]:
        ...
    


def get_component_linked_storage_account(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., storage_type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetComponentLinkedStorageAccountResult:
    
    ...

def get_component_linked_storage_account_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetComponentLinkedStorageAccountResult]:
    
    ...

