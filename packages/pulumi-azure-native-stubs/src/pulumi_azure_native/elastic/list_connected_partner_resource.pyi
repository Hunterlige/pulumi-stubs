import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListConnectedPartnerResourceResult",
    "AwaitableListConnectedPartnerResourceResult",
    "list_connected_partner_resource",
    "list_connected_partner_resource_output",
]

@pulumi.output_type
class ListConnectedPartnerResourceResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[Sequence[outputs.ConnectedPartnerResourcesListFormatResponse]]: ...

class AwaitableListConnectedPartnerResourceResult(ListConnectedPartnerResourceResult):
    def __await__(self): ...

def list_connected_partner_resource(
    monitor_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListConnectedPartnerResourceResult: ...
def list_connected_partner_resource_output(
    monitor_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListConnectedPartnerResourceResult]: ...
