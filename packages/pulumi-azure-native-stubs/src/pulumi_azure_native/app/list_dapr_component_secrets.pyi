

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListDaprComponentSecretsResult', 'AwaitableListDaprComponentSecretsResult', 'list_dapr_component_secrets', 'list_dapr_component_secrets_output']
@pulumi.output_type
class ListDaprComponentSecretsResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.DaprSecretResponse]:
        
        ...
    


class AwaitableListDaprComponentSecretsResult(ListDaprComponentSecretsResult):
    def __await__(self): # -> Generator[Never, Any, ListDaprComponentSecretsResult]:
        ...
    


def list_dapr_component_secrets(component_name: Optional[_builtins.str] = ..., environment_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListDaprComponentSecretsResult:
    
    ...

def list_dapr_component_secrets_output(component_name: Optional[pulumi.Input[_builtins.str]] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListDaprComponentSecretsResult]:
    
    ...

