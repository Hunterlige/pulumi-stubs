import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListApplianceClusterCustomerUserCredentialResult",
    ...,
    "list_appliance_cluster_customer_user_credential",
    ...,
]

@pulumi.output_type
class ListApplianceClusterCustomerUserCredentialResult:
    def __init__(__self__, kubeconfigs=..., ssh_keys=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(
        self,
    ) -> Sequence[outputs.ApplianceCredentialKubeconfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sshKeys")
    def ssh_keys(self) -> Mapping[str, outputs.SSHKeyResponse]: ...

class AwaitableListApplianceClusterCustomerUserCredentialResult(
    ListApplianceClusterCustomerUserCredentialResult
):
    def __await__(self): ...

def list_appliance_cluster_customer_user_credential(
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListApplianceClusterCustomerUserCredentialResult: ...
def list_appliance_cluster_customer_user_credential_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListApplianceClusterCustomerUserCredentialResult]: ...
