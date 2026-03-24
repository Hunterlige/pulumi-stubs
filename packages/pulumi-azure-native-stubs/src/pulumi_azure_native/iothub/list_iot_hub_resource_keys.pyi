

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListIotHubResourceKeysResult', 'AwaitableListIotHubResourceKeysResult', 'list_iot_hub_resource_keys', 'list_iot_hub_resource_keys_output']
@pulumi.output_type
class ListIotHubResourceKeysResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.SharedAccessSignatureAuthorizationRuleResponse]]:
        
        ...
    


class AwaitableListIotHubResourceKeysResult(ListIotHubResourceKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListIotHubResourceKeysResult]:
        ...
    


def list_iot_hub_resource_keys(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListIotHubResourceKeysResult:
    
    ...

def list_iot_hub_resource_keys_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListIotHubResourceKeysResult]:
    
    ...

