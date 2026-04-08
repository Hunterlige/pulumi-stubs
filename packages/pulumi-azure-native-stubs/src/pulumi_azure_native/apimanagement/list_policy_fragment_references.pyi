import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListPolicyFragmentReferencesResult",
    "AwaitableListPolicyFragmentReferencesResult",
    "list_policy_fragment_references",
    "list_policy_fragment_references_output",
]

@pulumi.output_type
class ListPolicyFragmentReferencesResult:
    def __init__(__self__, count=..., next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.ResourceCollectionResponseValue]]: ...

class AwaitableListPolicyFragmentReferencesResult(ListPolicyFragmentReferencesResult):
    def __await__(self): ...

def list_policy_fragment_references(
    id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    skip: Optional[_builtins.int] = ...,
    top: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListPolicyFragmentReferencesResult: ...
def list_policy_fragment_references_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    top: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListPolicyFragmentReferencesResult]: ...
