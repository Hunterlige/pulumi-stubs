import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListOpenShiftClusterAdminCredentialsResult",
    ...,
    "list_open_shift_cluster_admin_credentials",
    "list_open_shift_cluster_admin_credentials_output",
]

@pulumi.output_type
class ListOpenShiftClusterAdminCredentialsResult:
    def __init__(__self__, kubeconfig=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kubeconfig(self) -> Optional[_builtins.str]: ...

class AwaitableListOpenShiftClusterAdminCredentialsResult(
    ListOpenShiftClusterAdminCredentialsResult
):
    def __await__(self): ...

def list_open_shift_cluster_admin_credentials(
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListOpenShiftClusterAdminCredentialsResult: ...
def list_open_shift_cluster_admin_credentials_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListOpenShiftClusterAdminCredentialsResult]: ...
