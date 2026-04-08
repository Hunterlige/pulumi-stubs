import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MasterSitesControllerArgs", "MasterSitesController"]

@pulumi.input_type
class MasterSitesControllerArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        allow_multiple_sites: Optional[pulumi.Input[_builtins.bool]] = ...,
        customer_storage_account_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, MasterSitePropertiesPublicNetworkAccess]]
        ] = ...,
        site_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sites: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowMultipleSites")
    def allow_multiple_sites(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_multiple_sites.setter
    def allow_multiple_sites(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="customerStorageAccountArmId")
    def customer_storage_account_arm_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_storage_account_arm_id.setter
    def customer_storage_account_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, MasterSitePropertiesPublicNetworkAccess]]
    ]: ...
    @public_network_access.setter
    def public_network_access(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, MasterSitePropertiesPublicNetworkAccess]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @site_name.setter
    def site_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sites(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @sites.setter
    def sites(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:offazure:MasterSitesController")
class MasterSitesController(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_multiple_sites: Optional[pulumi.Input[_builtins.bool]] = ...,
        customer_storage_account_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, MasterSitePropertiesPublicNetworkAccess]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        site_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sites: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MasterSitesControllerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> MasterSitesController: ...
    @_builtins.property
    @pulumi.getter(name="allowMultipleSites")
    def allow_multiple_sites(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerStorageAccountArmId")
    def customer_storage_account_arm_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nestedSites")
    def nested_sites(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sites(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
