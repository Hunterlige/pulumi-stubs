import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListServerlessEndpointKeysResult",
    "AwaitableListServerlessEndpointKeysResult",
    "list_serverless_endpoint_keys",
    "list_serverless_endpoint_keys_output",
]

@pulumi.output_type
class ListServerlessEndpointKeysResult:
    def __init__(__self__, primary_key=..., secondary_key=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]: ...

class AwaitableListServerlessEndpointKeysResult(ListServerlessEndpointKeysResult):
    def __await__(self): ...

def list_serverless_endpoint_keys(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListServerlessEndpointKeysResult: ...
def list_serverless_endpoint_keys_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListServerlessEndpointKeysResult]: ...
