import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListWorkflowAccessKeySecretKeysResult",
    "AwaitableListWorkflowAccessKeySecretKeysResult",
    "list_workflow_access_key_secret_keys",
    "list_workflow_access_key_secret_keys_output",
]

@pulumi.output_type
class ListWorkflowAccessKeySecretKeysResult:
    def __init__(
        __self__, primary_secret_key=..., secondary_secret_key=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primarySecretKey")
    def primary_secret_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondarySecretKey")
    def secondary_secret_key(self) -> _builtins.str: ...

class AwaitableListWorkflowAccessKeySecretKeysResult(
    ListWorkflowAccessKeySecretKeysResult
):
    def __await__(self): ...

def list_workflow_access_key_secret_keys(
    access_key_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workflow_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListWorkflowAccessKeySecretKeysResult: ...
def list_workflow_access_key_secret_keys_output(
    access_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListWorkflowAccessKeySecretKeysResult]: ...
