import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListSiteIdentifiersAssignedToHostNameResult",
    ...,
    "list_site_identifiers_assigned_to_host_name",
    "list_site_identifiers_assigned_to_host_name_output",
]

@pulumi.output_type
class ListSiteIdentifiersAssignedToHostNameResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.IdentifierResponse]: ...

class AwaitableListSiteIdentifiersAssignedToHostNameResult(
    ListSiteIdentifiersAssignedToHostNameResult
):
    def __await__(self): ...

def list_site_identifiers_assigned_to_host_name(
    name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableListSiteIdentifiersAssignedToHostNameResult: ...
def list_site_identifiers_assigned_to_host_name_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListSiteIdentifiersAssignedToHostNameResult]: ...
