import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKubernetesRoleResult",
    "AwaitableGetKubernetesRoleResult",
    "get_kubernetes_role",
    "get_kubernetes_role_output",
]

@pulumi.output_type
class GetKubernetesRoleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        host_platform=...,
        host_platform_type=...,
        id=...,
        kind=...,
        kubernetes_cluster_info=...,
        kubernetes_role_resources=...,
        name=...,
        provisioning_state=...,
        role_status=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesClusterInfo")
    def kubernetes_cluster_info(self) -> outputs.KubernetesClusterInfoResponse: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesRoleResources")
    def kubernetes_role_resources(self) -> outputs.KubernetesRoleResourcesResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetKubernetesRoleResult(GetKubernetesRoleResult):
    def __await__(self): ...

def get_kubernetes_role(
    device_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKubernetesRoleResult: ...
def get_kubernetes_role_output(
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKubernetesRoleResult]: ...
