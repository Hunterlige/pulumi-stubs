import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListShareSynchronizationDetailsResult",
    "AwaitableListShareSynchronizationDetailsResult",
    "list_share_synchronization_details",
    "list_share_synchronization_details_output",
]

@pulumi.output_type
class ListShareSynchronizationDetailsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.SynchronizationDetailsResponse]: ...

class AwaitableListShareSynchronizationDetailsResult(
    ListShareSynchronizationDetailsResult
):
    def __await__(self): ...

def list_share_synchronization_details(
    account_name: Optional[_builtins.str] = ...,
    consumer_email: Optional[_builtins.str] = ...,
    consumer_name: Optional[_builtins.str] = ...,
    consumer_tenant_name: Optional[_builtins.str] = ...,
    duration_ms: Optional[_builtins.int] = ...,
    end_time: Optional[_builtins.str] = ...,
    filter: Optional[_builtins.str] = ...,
    message: Optional[_builtins.str] = ...,
    orderby: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    share_name: Optional[_builtins.str] = ...,
    skip_token: Optional[_builtins.str] = ...,
    start_time: Optional[_builtins.str] = ...,
    status: Optional[_builtins.str] = ...,
    synchronization_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListShareSynchronizationDetailsResult: ...
def list_share_synchronization_details_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    consumer_email: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    consumer_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    consumer_tenant_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    duration_ms: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    end_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    message: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    orderby: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    share_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    start_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    status: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    synchronization_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListShareSynchronizationDetailsResult]: ...
