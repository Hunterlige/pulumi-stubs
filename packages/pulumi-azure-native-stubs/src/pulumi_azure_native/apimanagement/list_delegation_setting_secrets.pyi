

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListDelegationSettingSecretsResult', 'AwaitableListDelegationSettingSecretsResult', 'list_delegation_setting_secrets', 'list_delegation_setting_secrets_output']
@pulumi.output_type
class ListDelegationSettingSecretsResult:
    
    def __init__(__self__, validation_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationKey")
    def validation_key(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListDelegationSettingSecretsResult(ListDelegationSettingSecretsResult):
    def __await__(self): # -> Generator[Never, Any, ListDelegationSettingSecretsResult]:
        ...
    


def list_delegation_setting_secrets(resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListDelegationSettingSecretsResult:
    
    ...

def list_delegation_setting_secrets_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListDelegationSettingSecretsResult]:
    
    ...

