import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BastionHostArgs", "BastionHost"]

@pulumi.input_type
class BastionHostArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        bastion_host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_copy_paste: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_file_copy: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_ip_connect: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_kerberos: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_private_only_bastion: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_session_recording: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_shareable_link: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_tunneling: Optional[pulumi.Input[_builtins.bool]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[BastionHostIPConfigurationArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_acls: Optional[
            pulumi.Input[BastionHostPropertiesFormatNetworkAclsArgs]
        ] = ...,
        scale_units: Optional[pulumi.Input[_builtins.int]] = ...,
        sku: Optional[pulumi.Input[SkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_network: Optional[pulumi.Input[SubResourceArgs]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bastionHostName")
    def bastion_host_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bastion_host_name.setter
    def bastion_host_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableCopyPaste")
    def disable_copy_paste(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_copy_paste.setter
    def disable_copy_paste(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableFileCopy")
    def enable_file_copy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_file_copy.setter
    def enable_file_copy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableIpConnect")
    def enable_ip_connect(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ip_connect.setter
    def enable_ip_connect(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableKerberos")
    def enable_kerberos(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_kerberos.setter
    def enable_kerberos(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateOnlyBastion")
    def enable_private_only_bastion(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_private_only_bastion.setter
    def enable_private_only_bastion(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSessionRecording")
    def enable_session_recording(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_session_recording.setter
    def enable_session_recording(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableShareableLink")
    def enable_shareable_link(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_shareable_link.setter
    def enable_shareable_link(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableTunneling")
    def enable_tunneling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_tunneling.setter
    def enable_tunneling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BastionHostIPConfigurationArgs]]]
    ]: ...
    @ip_configurations.setter
    def ip_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BastionHostIPConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(
        self,
    ) -> Optional[pulumi.Input[BastionHostPropertiesFormatNetworkAclsArgs]]: ...
    @network_acls.setter
    def network_acls(
        self, value: Optional[pulumi.Input[BastionHostPropertiesFormatNetworkAclsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleUnits")
    def scale_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale_units.setter
    def scale_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @virtual_network.setter
    def virtual_network(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:network:BastionHost")
class BastionHost(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bastion_host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_copy_paste: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_file_copy: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_ip_connect: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_kerberos: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_private_only_bastion: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_session_recording: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_shareable_link: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_tunneling: Optional[pulumi.Input[_builtins.bool]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BastionHostIPConfigurationArgs,
                            BastionHostIPConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_acls: Optional[
            pulumi.Input[
                Union[
                    BastionHostPropertiesFormatNetworkAclsArgs,
                    BastionHostPropertiesFormatNetworkAclsArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scale_units: Optional[pulumi.Input[_builtins.int]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_network: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BastionHostArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> BastionHost: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableCopyPaste")
    def disable_copy_paste(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableFileCopy")
    def enable_file_copy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableIpConnect")
    def enable_ip_connect(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableKerberos")
    def enable_kerberos(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateOnlyBastion")
    def enable_private_only_bastion(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableSessionRecording")
    def enable_session_recording(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableShareableLink")
    def enable_shareable_link(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableTunneling")
    def enable_tunneling(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.BastionHostIPConfigurationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(
        self,
    ) -> pulumi.Output[
        Optional[outputs.BastionHostPropertiesFormatResponseNetworkAcls]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scaleUnits")
    def scale_units(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
