

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListIntegrationRuntimeAuthKeysResult', 'AwaitableListIntegrationRuntimeAuthKeysResult', 'list_integration_runtime_auth_keys', 'list_integration_runtime_auth_keys_output']
@pulumi.output_type
class ListIntegrationRuntimeAuthKeysResult:
    
    def __init__(__self__, auth_key1=..., auth_key2=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authKey1")
    def auth_key1(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authKey2")
    def auth_key2(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListIntegrationRuntimeAuthKeysResult(ListIntegrationRuntimeAuthKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListIntegrationRuntimeAuthKeysResult]:
        ...
    


def list_integration_runtime_auth_keys(factory_name: Optional[_builtins.str] = ..., integration_runtime_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListIntegrationRuntimeAuthKeysResult:
    
    ...

def list_integration_runtime_auth_keys_output(factory_name: Optional[pulumi.Input[_builtins.str]] = ..., integration_runtime_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListIntegrationRuntimeAuthKeysResult]:
    
    ...

