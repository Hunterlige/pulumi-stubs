import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListEffectiveVirtualNetworkByNetworkGroupResult",
    ...,
    "list_effective_virtual_network_by_network_group",
    ...,
]

@pulumi.output_type
class ListEffectiveVirtualNetworkByNetworkGroupResult:
    def __init__(__self__, skip_token=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.EffectiveVirtualNetworkResponse]]: ...

class AwaitableListEffectiveVirtualNetworkByNetworkGroupResult(
    ListEffectiveVirtualNetworkByNetworkGroupResult
):
    def __await__(self): ...

def list_effective_virtual_network_by_network_group(
    network_group_name: Optional[_builtins.str] = ...,
    network_manager_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    skip_token: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListEffectiveVirtualNetworkByNetworkGroupResult: ...
def list_effective_virtual_network_by_network_group_output(
    network_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    network_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListEffectiveVirtualNetworkByNetworkGroupResult]: ...
