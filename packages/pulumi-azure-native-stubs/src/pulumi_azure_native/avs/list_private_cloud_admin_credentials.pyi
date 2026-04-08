import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListPrivateCloudAdminCredentialsResult",
    "AwaitableListPrivateCloudAdminCredentialsResult",
    "list_private_cloud_admin_credentials",
    "list_private_cloud_admin_credentials_output",
]

@pulumi.output_type
class ListPrivateCloudAdminCredentialsResult:
    def __init__(
        __self__,
        nsxt_password=...,
        nsxt_username=...,
        vcenter_password=...,
        vcenter_username=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nsxtPassword")
    def nsxt_password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nsxtUsername")
    def nsxt_username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vcenterPassword")
    def vcenter_password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vcenterUsername")
    def vcenter_username(self) -> _builtins.str: ...

class AwaitableListPrivateCloudAdminCredentialsResult(
    ListPrivateCloudAdminCredentialsResult
):
    def __await__(self): ...

def list_private_cloud_admin_credentials(
    private_cloud_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListPrivateCloudAdminCredentialsResult: ...
def list_private_cloud_admin_credentials_output(
    private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListPrivateCloudAdminCredentialsResult]: ...
