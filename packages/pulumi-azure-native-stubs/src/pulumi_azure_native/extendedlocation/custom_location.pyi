import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CustomLocationArgs", "CustomLocation"]

@pulumi.input_type
class CustomLocationArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        authentication: Optional[
            pulumi.Input[CustomLocationPropertiesAuthenticationArgs]
        ] = ...,
        cluster_extension_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        host_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        host_type: Optional[pulumi.Input[Union[_builtins.str, HostType]]] = ...,
        identity: Optional[pulumi.Input[IdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_state: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def authentication(
        self,
    ) -> Optional[pulumi.Input[CustomLocationPropertiesAuthenticationArgs]]: ...
    @authentication.setter
    def authentication(
        self, value: Optional[pulumi.Input[CustomLocationPropertiesAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterExtensionIds")
    def cluster_extension_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cluster_extension_ids.setter
    def cluster_extension_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostResourceId")
    def host_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_resource_id.setter
    def host_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> Optional[pulumi.Input[Union[_builtins.str, HostType]]]: ...
    @host_type.setter
    def host_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HostType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:extendedlocation:CustomLocation")
class CustomLocation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authentication: Optional[
            pulumi.Input[
                Union[
                    CustomLocationPropertiesAuthenticationArgs,
                    CustomLocationPropertiesAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        cluster_extension_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        host_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        host_type: Optional[pulumi.Input[Union[_builtins.str, HostType]]] = ...,
        identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_state: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CustomLocationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CustomLocation: ...
    @_builtins.property
    @pulumi.getter
    def authentication(
        self,
    ) -> pulumi.Output[
        Optional[outputs.CustomLocationPropertiesResponseAuthentication]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterExtensionIds")
    def cluster_extension_ids(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostResourceId")
    def host_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
