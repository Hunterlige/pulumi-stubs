import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListWebAppFunctionSecretsResult",
    "AwaitableListWebAppFunctionSecretsResult",
    "list_web_app_function_secrets",
    "list_web_app_function_secrets_output",
]

@pulumi.output_type
class ListWebAppFunctionSecretsResult:
    def __init__(__self__, key=..., trigger_url=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerUrl")
    def trigger_url(self) -> Optional[_builtins.str]: ...

class AwaitableListWebAppFunctionSecretsResult(ListWebAppFunctionSecretsResult):
    def __await__(self): ...

def list_web_app_function_secrets(
    function_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListWebAppFunctionSecretsResult: ...
def list_web_app_function_secrets_output(
    function_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListWebAppFunctionSecretsResult]: ...
