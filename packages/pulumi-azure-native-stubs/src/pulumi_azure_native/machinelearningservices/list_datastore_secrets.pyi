import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListDatastoreSecretsResult",
    "AwaitableListDatastoreSecretsResult",
    "list_datastore_secrets",
    "list_datastore_secrets_output",
]

@pulumi.output_type
class ListDatastoreSecretsResult:
    def __init__(__self__, secrets_type=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretsType")
    def secrets_type(self) -> _builtins.str: ...

class AwaitableListDatastoreSecretsResult(ListDatastoreSecretsResult):
    def __await__(self): ...

def list_datastore_secrets(
    expirable_secret: Optional[_builtins.bool] = ...,
    expire_after_hours: Optional[_builtins.int] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListDatastoreSecretsResult: ...
def list_datastore_secrets_output(
    expirable_secret: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    expire_after_hours: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListDatastoreSecretsResult]: ...
