

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWebPubSubKeysResult', 'AwaitableListWebPubSubKeysResult', 'list_web_pub_sub_keys', 'list_web_pub_sub_keys_output']
@pulumi.output_type
class ListWebPubSubKeysResult:
    
    def __init__(__self__, primary_connection_string=..., primary_key=..., secondary_connection_string=..., secondary_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListWebPubSubKeysResult(ListWebPubSubKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListWebPubSubKeysResult]:
        ...
    


def list_web_pub_sub_keys(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWebPubSubKeysResult:
    
    ...

def list_web_pub_sub_keys_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWebPubSubKeysResult]:
    
    ...

