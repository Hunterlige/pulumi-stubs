

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., 'list_connected_environments_dapr_component_secrets', ...]
@pulumi.output_type
class ListConnectedEnvironmentsDaprComponentSecretsResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.DaprSecretResponse]:
        
        ...
    


class AwaitableListConnectedEnvironmentsDaprComponentSecretsResult(ListConnectedEnvironmentsDaprComponentSecretsResult):
    def __await__(self): # -> Generator[Never, Any, ListConnectedEnvironmentsDaprComponentSecretsResult]:
        ...
    


def list_connected_environments_dapr_component_secrets(component_name: Optional[_builtins.str] = ..., connected_environment_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListConnectedEnvironmentsDaprComponentSecretsResult:
    
    ...

def list_connected_environments_dapr_component_secrets_output(component_name: Optional[pulumi.Input[_builtins.str]] = ..., connected_environment_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListConnectedEnvironmentsDaprComponentSecretsResult]:
    
    ...

