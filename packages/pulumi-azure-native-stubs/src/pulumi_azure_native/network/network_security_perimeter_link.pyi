import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkSecurityPerimeterLinkArgs", "NetworkSecurityPerimeterLink"]

@pulumi.input_type
class NetworkSecurityPerimeterLinkArgs:
    def __init__(
        __self__,
        *,
        network_security_perimeter_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        auto_approved_remote_perimeter_resource_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        link_name: Optional[pulumi.Input[_builtins.str]] = ...,
        local_inbound_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        remote_inbound_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityPerimeterName")
    def network_security_perimeter_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_security_perimeter_name.setter
    def network_security_perimeter_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoApprovedRemotePerimeterResourceId")
    def auto_approved_remote_perimeter_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_approved_remote_perimeter_resource_id.setter
    def auto_approved_remote_perimeter_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkName")
    def link_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @link_name.setter
    def link_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localInboundProfiles")
    def local_inbound_profiles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @local_inbound_profiles.setter
    def local_inbound_profiles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="remoteInboundProfiles")
    def remote_inbound_profiles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @remote_inbound_profiles.setter
    def remote_inbound_profiles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:network:NetworkSecurityPerimeterLink")
class NetworkSecurityPerimeterLink(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_approved_remote_perimeter_resource_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        link_name: Optional[pulumi.Input[_builtins.str]] = ...,
        local_inbound_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        network_security_perimeter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_inbound_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkSecurityPerimeterLinkArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NetworkSecurityPerimeterLink: ...
    @_builtins.property
    @pulumi.getter(name="autoApprovedRemotePerimeterResourceId")
    def auto_approved_remote_perimeter_resource_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localInboundProfiles")
    def local_inbound_profiles(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="localOutboundProfiles")
    def local_outbound_profiles(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteInboundProfiles")
    def remote_inbound_profiles(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="remoteOutboundProfiles")
    def remote_outbound_profiles(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="remotePerimeterGuid")
    def remote_perimeter_guid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remotePerimeterLocation")
    def remote_perimeter_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
