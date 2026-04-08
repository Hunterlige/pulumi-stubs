import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListActiveConnectivityConfigurationsResult",
    ...,
    "list_active_connectivity_configurations",
    "list_active_connectivity_configurations_output",
]

@pulumi.output_type
class ListActiveConnectivityConfigurationsResult:
    def __init__(__self__, skip_token=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[Sequence[outputs.ActiveConnectivityConfigurationResponseV1]]: ...

class AwaitableListActiveConnectivityConfigurationsResult(
    ListActiveConnectivityConfigurationsResult
):
    def __await__(self): ...

def list_active_connectivity_configurations(
    network_manager_name: Optional[_builtins.str] = ...,
    regions: Optional[Sequence[_builtins.str]] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    skip_token: Optional[_builtins.str] = ...,
    top: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListActiveConnectivityConfigurationsResult: ...
def list_active_connectivity_configurations_output(
    network_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
    regions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    top: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListActiveConnectivityConfigurationsResult]: ...
