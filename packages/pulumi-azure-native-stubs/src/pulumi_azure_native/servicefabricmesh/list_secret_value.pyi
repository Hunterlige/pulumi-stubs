import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListSecretValueResult",
    "AwaitableListSecretValueResult",
    "list_secret_value",
    "list_secret_value_output",
]

@pulumi.output_type
class ListSecretValueResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

class AwaitableListSecretValueResult(ListSecretValueResult):
    def __await__(self): ...

def list_secret_value(
    resource_group_name: Optional[_builtins.str] = ...,
    secret_resource_name: Optional[_builtins.str] = ...,
    secret_value_resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListSecretValueResult: ...
def list_secret_value_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    secret_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    secret_value_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListSecretValueResult]: ...
