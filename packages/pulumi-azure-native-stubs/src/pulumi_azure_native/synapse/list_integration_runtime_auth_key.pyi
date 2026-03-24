

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListIntegrationRuntimeAuthKeyResult', 'AwaitableListIntegrationRuntimeAuthKeyResult', 'list_integration_runtime_auth_key', 'list_integration_runtime_auth_key_output']
@pulumi.output_type
class ListIntegrationRuntimeAuthKeyResult:
    
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
    


class AwaitableListIntegrationRuntimeAuthKeyResult(ListIntegrationRuntimeAuthKeyResult):
    def __await__(self): # -> Generator[Never, Any, ListIntegrationRuntimeAuthKeyResult]:
        ...
    


def list_integration_runtime_auth_key(integration_runtime_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListIntegrationRuntimeAuthKeyResult:
    
    ...

def list_integration_runtime_auth_key_output(integration_runtime_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListIntegrationRuntimeAuthKeyResult]:
    
    ...

