import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListOpenShiftClusterCredentialsResult",
    "AwaitableListOpenShiftClusterCredentialsResult",
    "list_open_shift_cluster_credentials",
    "list_open_shift_cluster_credentials_output",
]

@pulumi.output_type
class ListOpenShiftClusterCredentialsResult:
    def __init__(__self__, kubeadmin_password=..., kubeadmin_username=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kubeadminPassword")
    def kubeadmin_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kubeadminUsername")
    def kubeadmin_username(self) -> Optional[_builtins.str]: ...

class AwaitableListOpenShiftClusterCredentialsResult(
    ListOpenShiftClusterCredentialsResult
):
    def __await__(self): ...

def list_open_shift_cluster_credentials(
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListOpenShiftClusterCredentialsResult: ...
def list_open_shift_cluster_credentials_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListOpenShiftClusterCredentialsResult]: ...
