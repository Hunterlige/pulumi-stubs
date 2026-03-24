

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListConnectionKeysResult', 'AwaitableListConnectionKeysResult', 'list_connection_keys', 'list_connection_keys_output']
@pulumi.output_type
class ListConnectionKeysResult:
    def __init__(__self__, connection_key=..., parameter_values=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionKey")
    def connection_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValues")
    def parameter_values(self) -> Optional[Mapping[str, Any]]:
        
        ...
    


class AwaitableListConnectionKeysResult(ListConnectionKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListConnectionKeysResult]:
        ...
    


def list_connection_keys(connection_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., kind: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., type: Optional[_builtins.str] = ..., validity_time_span: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListConnectionKeysResult:
    
    ...

def list_connection_keys_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., kind: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., validity_time_span: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListConnectionKeysResult]:
    
    ...

