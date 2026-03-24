

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListIotDpsResourceKeysForKeyNameResult', 'AwaitableListIotDpsResourceKeysForKeyNameResult', 'list_iot_dps_resource_keys_for_key_name', 'list_iot_dps_resource_keys_for_key_name_output']
@pulumi.output_type
class ListIotDpsResourceKeysForKeyNameResult:
    
    def __init__(__self__, key_name=..., primary_key=..., rights=..., secondary_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rights(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListIotDpsResourceKeysForKeyNameResult(ListIotDpsResourceKeysForKeyNameResult):
    def __await__(self): # -> Generator[Never, Any, ListIotDpsResourceKeysForKeyNameResult]:
        ...
    


def list_iot_dps_resource_keys_for_key_name(key_name: Optional[_builtins.str] = ..., provisioning_service_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListIotDpsResourceKeysForKeyNameResult:
    
    ...

def list_iot_dps_resource_keys_for_key_name_output(key_name: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_service_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListIotDpsResourceKeysForKeyNameResult]:
    
    ...

