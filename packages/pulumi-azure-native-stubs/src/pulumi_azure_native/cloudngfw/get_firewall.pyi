import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFirewallResult",
    "AwaitableGetFirewallResult",
    "get_firewall",
    "get_firewall_output",
]

@pulumi.output_type
class GetFirewallResult:
    def __init__(
        __self__,
        associated_rulestack=...,
        azure_api_version=...,
        dns_settings=...,
        front_end_settings=...,
        id=...,
        identity=...,
        is_panorama_managed=...,
        is_strata_cloud_managed=...,
        location=...,
        marketplace_details=...,
        name=...,
        network_profile=...,
        pan_etag=...,
        panorama_config=...,
        plan_data=...,
        provisioning_state=...,
        strata_cloud_manager_config=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedRulestack")
    def associated_rulestack(self) -> Optional[outputs.RulestackDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> outputs.DNSSettingsResponse: ...
    @_builtins.property
    @pulumi.getter(name="frontEndSettings")
    def front_end_settings(
        self,
    ) -> Optional[Sequence[outputs.FrontendSettingResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[outputs.AzureResourceManagerManagedIdentityPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="isPanoramaManaged")
    def is_panorama_managed(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isStrataCloudManaged")
    def is_strata_cloud_managed(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceDetails")
    def marketplace_details(self) -> outputs.MarketplaceDetailsResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> outputs.NetworkProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="panoramaConfig")
    def panorama_config(self) -> Optional[outputs.PanoramaConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="planData")
    def plan_data(self) -> outputs.PlanDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="strataCloudManagerConfig")
    def strata_cloud_manager_config(
        self,
    ) -> Optional[outputs.StrataCloudManagerConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFirewallResult(GetFirewallResult):
    def __await__(self): ...

def get_firewall(
    firewall_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFirewallResult: ...
def get_firewall_output(
    firewall_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFirewallResult]: ...
