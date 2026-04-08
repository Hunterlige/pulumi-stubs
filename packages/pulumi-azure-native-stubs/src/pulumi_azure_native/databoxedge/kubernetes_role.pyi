import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KubernetesRoleArgs", "KubernetesRole"]

@pulumi.input_type
class KubernetesRoleArgs:
    def __init__(
        __self__,
        *,
        device_name: pulumi.Input[_builtins.str],
        host_platform: pulumi.Input[Union[_builtins.str, PlatformType]],
        kind: pulumi.Input[_builtins.str],
        kubernetes_cluster_info: pulumi.Input[KubernetesClusterInfoArgs],
        kubernetes_role_resources: pulumi.Input[KubernetesRoleResourcesArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        role_status: pulumi.Input[Union[_builtins.str, RoleStatus]],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> pulumi.Input[Union[_builtins.str, PlatformType]]: ...
    @host_platform.setter
    def host_platform(
        self, value: pulumi.Input[Union[_builtins.str, PlatformType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesClusterInfo")
    def kubernetes_cluster_info(self) -> pulumi.Input[KubernetesClusterInfoArgs]: ...
    @kubernetes_cluster_info.setter
    def kubernetes_cluster_info(
        self, value: pulumi.Input[KubernetesClusterInfoArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesRoleResources")
    def kubernetes_role_resources(
        self,
    ) -> pulumi.Input[KubernetesRoleResourcesArgs]: ...
    @kubernetes_role_resources.setter
    def kubernetes_role_resources(
        self, value: pulumi.Input[KubernetesRoleResourcesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> pulumi.Input[Union[_builtins.str, RoleStatus]]: ...
    @role_status.setter
    def role_status(self, value: pulumi.Input[Union[_builtins.str, RoleStatus]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:databoxedge:KubernetesRole")
class KubernetesRole(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        host_platform: Optional[pulumi.Input[Union[_builtins.str, PlatformType]]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        kubernetes_cluster_info: Optional[
            pulumi.Input[
                Union[KubernetesClusterInfoArgs, KubernetesClusterInfoArgsDict]
            ]
        ] = ...,
        kubernetes_role_resources: Optional[
            pulumi.Input[
                Union[KubernetesRoleResourcesArgs, KubernetesRoleResourcesArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        role_status: Optional[pulumi.Input[Union[_builtins.str, RoleStatus]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KubernetesRoleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> KubernetesRole: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesClusterInfo")
    def kubernetes_cluster_info(
        self,
    ) -> pulumi.Output[outputs.KubernetesClusterInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesRoleResources")
    def kubernetes_role_resources(
        self,
    ) -> pulumi.Output[outputs.KubernetesRoleResourcesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
