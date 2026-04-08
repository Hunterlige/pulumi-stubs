import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListBotSecretsResult",
    "AwaitableListBotSecretsResult",
    "list_bot_secrets",
    "list_bot_secrets_output",
]

@pulumi.output_type
class ListBotSecretsResult:
    def __init__(__self__, secrets=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.HealthBotKeyResponse]]: ...

class AwaitableListBotSecretsResult(ListBotSecretsResult):
    def __await__(self): ...

def list_bot_secrets(
    bot_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListBotSecretsResult: ...
def list_bot_secrets_output(
    bot_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListBotSecretsResult]: ...
