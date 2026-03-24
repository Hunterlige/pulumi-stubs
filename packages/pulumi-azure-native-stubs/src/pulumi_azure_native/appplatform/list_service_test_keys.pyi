

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListServiceTestKeysResult', 'AwaitableListServiceTestKeysResult', 'list_service_test_keys', 'list_service_test_keys_output']
@pulumi.output_type
class ListServiceTestKeysResult:
    
    def __init__(__self__, enabled=..., primary_key=..., primary_test_endpoint=..., secondary_key=..., secondary_test_endpoint=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryTestEndpoint")
    def primary_test_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryTestEndpoint")
    def secondary_test_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListServiceTestKeysResult(ListServiceTestKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListServiceTestKeysResult]:
        ...
    


def list_service_test_keys(resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListServiceTestKeysResult:
    
    ...

def list_service_test_keys_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListServiceTestKeysResult]:
    
    ...

