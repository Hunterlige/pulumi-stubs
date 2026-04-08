import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListFleetCredentialsResult",
    "AwaitableListFleetCredentialsResult",
    "list_fleet_credentials",
    "list_fleet_credentials_output",
]

@pulumi.output_type
class ListFleetCredentialsResult:
    def __init__(__self__, kubeconfigs=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence[outputs.FleetCredentialResultResponse]: ...

class AwaitableListFleetCredentialsResult(ListFleetCredentialsResult):
    def __await__(self): ...

def list_fleet_credentials(
    fleet_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListFleetCredentialsResult: ...
def list_fleet_credentials_output(
    fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListFleetCredentialsResult]: ...
