import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FirewallArgs", "Firewall"]

@pulumi.input_type
class FirewallArgs:
    def __init__(
        __self__,
        *,
        dns_settings: pulumi.Input[DNSSettingsArgs],
        marketplace_details: pulumi.Input[MarketplaceDetailsArgs],
        network_profile: pulumi.Input[NetworkProfileArgs],
        plan_data: pulumi.Input[PlanDataArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        associated_rulestack: Optional[pulumi.Input[RulestackDetailsArgs]] = ...,
        firewall_name: Optional[pulumi.Input[_builtins.str]] = ...,
        front_end_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[FrontendSettingArgs]]]
        ] = ...,
        identity: Optional[
            pulumi.Input[AzureResourceManagerManagedIdentityPropertiesArgs]
        ] = ...,
        is_panorama_managed: Optional[
            pulumi.Input[Union[_builtins.str, BooleanEnum]]
        ] = ...,
        is_strata_cloud_managed: Optional[
            pulumi.Input[Union[_builtins.str, BooleanEnum]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        pan_etag: Optional[pulumi.Input[_builtins.str]] = ...,
        panorama_config: Optional[pulumi.Input[PanoramaConfigArgs]] = ...,
        strata_cloud_manager_config: Optional[
            pulumi.Input[StrataCloudManagerConfigArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Input[DNSSettingsArgs]: ...
    @dns_settings.setter
    def dns_settings(self, value: pulumi.Input[DNSSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="marketplaceDetails")
    def marketplace_details(self) -> pulumi.Input[MarketplaceDetailsArgs]: ...
    @marketplace_details.setter
    def marketplace_details(self, value: pulumi.Input[MarketplaceDetailsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Input[NetworkProfileArgs]: ...
    @network_profile.setter
    def network_profile(self, value: pulumi.Input[NetworkProfileArgs]): ...
    @_builtins.property
    @pulumi.getter(name="planData")
    def plan_data(self) -> pulumi.Input[PlanDataArgs]: ...
    @plan_data.setter
    def plan_data(self, value: pulumi.Input[PlanDataArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="associatedRulestack")
    def associated_rulestack(self) -> Optional[pulumi.Input[RulestackDetailsArgs]]: ...
    @associated_rulestack.setter
    def associated_rulestack(
        self, value: Optional[pulumi.Input[RulestackDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="firewallName")
    def firewall_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_name.setter
    def firewall_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="frontEndSettings")
    def front_end_settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FrontendSettingArgs]]]]: ...
    @front_end_settings.setter
    def front_end_settings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FrontendSettingArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[pulumi.Input[AzureResourceManagerManagedIdentityPropertiesArgs]]: ...
    @identity.setter
    def identity(
        self,
        value: Optional[
            pulumi.Input[AzureResourceManagerManagedIdentityPropertiesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isPanoramaManaged")
    def is_panorama_managed(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BooleanEnum]]]: ...
    @is_panorama_managed.setter
    def is_panorama_managed(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BooleanEnum]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isStrataCloudManaged")
    def is_strata_cloud_managed(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BooleanEnum]]]: ...
    @is_strata_cloud_managed.setter
    def is_strata_cloud_managed(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BooleanEnum]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pan_etag.setter
    def pan_etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="panoramaConfig")
    def panorama_config(self) -> Optional[pulumi.Input[PanoramaConfigArgs]]: ...
    @panorama_config.setter
    def panorama_config(self, value: Optional[pulumi.Input[PanoramaConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="strataCloudManagerConfig")
    def strata_cloud_manager_config(
        self,
    ) -> Optional[pulumi.Input[StrataCloudManagerConfigArgs]]: ...
    @strata_cloud_manager_config.setter
    def strata_cloud_manager_config(
        self, value: Optional[pulumi.Input[StrataCloudManagerConfigArgs]]
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

@pulumi.type_token("azure-native:cloudngfw:Firewall")
class Firewall(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        associated_rulestack: Optional[
            pulumi.Input[Union[RulestackDetailsArgs, RulestackDetailsArgsDict]]
        ] = ...,
        dns_settings: Optional[
            pulumi.Input[Union[DNSSettingsArgs, DNSSettingsArgsDict]]
        ] = ...,
        firewall_name: Optional[pulumi.Input[_builtins.str]] = ...,
        front_end_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[FrontendSettingArgs, FrontendSettingArgsDict]]
                ]
            ]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[
                    AzureResourceManagerManagedIdentityPropertiesArgs,
                    AzureResourceManagerManagedIdentityPropertiesArgsDict,
                ]
            ]
        ] = ...,
        is_panorama_managed: Optional[
            pulumi.Input[Union[_builtins.str, BooleanEnum]]
        ] = ...,
        is_strata_cloud_managed: Optional[
            pulumi.Input[Union[_builtins.str, BooleanEnum]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        marketplace_details: Optional[
            pulumi.Input[Union[MarketplaceDetailsArgs, MarketplaceDetailsArgsDict]]
        ] = ...,
        network_profile: Optional[
            pulumi.Input[Union[NetworkProfileArgs, NetworkProfileArgsDict]]
        ] = ...,
        pan_etag: Optional[pulumi.Input[_builtins.str]] = ...,
        panorama_config: Optional[
            pulumi.Input[Union[PanoramaConfigArgs, PanoramaConfigArgsDict]]
        ] = ...,
        plan_data: Optional[pulumi.Input[Union[PlanDataArgs, PlanDataArgsDict]]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        strata_cloud_manager_config: Optional[
            pulumi.Input[
                Union[StrataCloudManagerConfigArgs, StrataCloudManagerConfigArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FirewallArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Firewall: ...
    @_builtins.property
    @pulumi.getter(name="associatedRulestack")
    def associated_rulestack(
        self,
    ) -> pulumi.Output[Optional[outputs.RulestackDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output[outputs.DNSSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="frontEndSettings")
    def front_end_settings(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.FrontendSettingResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AzureResourceManagerManagedIdentityPropertiesResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="isPanoramaManaged")
    def is_panorama_managed(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isStrataCloudManaged")
    def is_strata_cloud_managed(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceDetails")
    def marketplace_details(
        self,
    ) -> pulumi.Output[outputs.MarketplaceDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="panoramaConfig")
    def panorama_config(
        self,
    ) -> pulumi.Output[Optional[outputs.PanoramaConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="planData")
    def plan_data(self) -> pulumi.Output[outputs.PlanDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="strataCloudManagerConfig")
    def strata_cloud_manager_config(
        self,
    ) -> pulumi.Output[Optional[outputs.StrataCloudManagerConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
