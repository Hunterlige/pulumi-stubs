import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListShareSynchronizationsResult",
    "AwaitableListShareSynchronizationsResult",
    "list_share_synchronizations",
    "list_share_synchronizations_output",
]

@pulumi.output_type
class ListShareSynchronizationsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.ShareSynchronizationResponse]: ...

class AwaitableListShareSynchronizationsResult(ListShareSynchronizationsResult):
    def __await__(self): ...

def list_share_synchronizations(
    account_name: Optional[_builtins.str] = ...,
    filter: Optional[_builtins.str] = ...,
    orderby: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    share_name: Optional[_builtins.str] = ...,
    skip_token: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListShareSynchronizationsResult: ...
def list_share_synchronizations_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    orderby: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    share_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListShareSynchronizationsResult]: ...
