

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListApmSecretKeysResult', 'AwaitableListApmSecretKeysResult', 'list_apm_secret_keys', 'list_apm_secret_keys_output']
@pulumi.output_type
class ListApmSecretKeysResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableListApmSecretKeysResult(ListApmSecretKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListApmSecretKeysResult]:
        ...
    


def list_apm_secret_keys(apm_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListApmSecretKeysResult:
    
    ...

def list_apm_secret_keys_output(apm_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListApmSecretKeysResult]:
    
    ...

