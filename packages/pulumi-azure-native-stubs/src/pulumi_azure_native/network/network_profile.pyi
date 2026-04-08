import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkProfileArgs", "NetworkProfile"]

@pulumi.input_type
class NetworkProfileArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        container_network_interface_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContainerNetworkInterfaceConfigurationArgs]]
            ]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerNetworkInterfaceConfigurations")
    def container_network_interface_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ContainerNetworkInterfaceConfigurationArgs]]]
    ]: ...
    @container_network_interface_configurations.setter
    def container_network_interface_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContainerNetworkInterfaceConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfileName")
    def network_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_profile_name.setter
    def network_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:network:NetworkProfile")
class NetworkProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        container_network_interface_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ContainerNetworkInterfaceConfigurationArgs,
                            ContainerNetworkInterfaceConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NetworkProfile: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerNetworkInterfaceConfigurations")
    def container_network_interface_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ContainerNetworkInterfaceConfigurationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="containerNetworkInterfaces")
    def container_network_interfaces(
        self,
    ) -> pulumi.Output[Sequence[outputs.ContainerNetworkInterfaceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
