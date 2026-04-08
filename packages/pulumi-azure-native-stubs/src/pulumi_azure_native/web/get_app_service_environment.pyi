import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAppServiceEnvironmentResult",
    "AwaitableGetAppServiceEnvironmentResult",
    "get_app_service_environment",
    "get_app_service_environment_output",
]

@pulumi.output_type
class GetAppServiceEnvironmentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        cluster_settings=...,
        custom_dns_suffix_configuration=...,
        dedicated_host_count=...,
        dns_suffix=...,
        front_end_scale_factor=...,
        has_linux_workers=...,
        id=...,
        internal_load_balancing_mode=...,
        ipssl_address_count=...,
        kind=...,
        location=...,
        maximum_number_of_machines=...,
        multi_role_count=...,
        multi_size=...,
        name=...,
        networking_configuration=...,
        provisioning_state=...,
        status=...,
        suspended=...,
        tags=...,
        type=...,
        upgrade_availability=...,
        upgrade_preference=...,
        user_whitelisted_ip_ranges=...,
        virtual_network=...,
        zone_redundant=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterSettings")
    def cluster_settings(self) -> Optional[Sequence[outputs.NameValuePairResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="customDnsSuffixConfiguration")
    def custom_dns_suffix_configuration(
        self,
    ) -> Optional[outputs.CustomDnsSuffixConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedHostCount")
    def dedicated_host_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="frontEndScaleFactor")
    def front_end_scale_factor(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="hasLinuxWorkers")
    def has_linux_workers(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="internalLoadBalancingMode")
    def internal_load_balancing_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipsslAddressCount")
    def ipssl_address_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maximumNumberOfMachines")
    def maximum_number_of_machines(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="multiRoleCount")
    def multi_role_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="multiSize")
    def multi_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkingConfiguration")
    def networking_configuration(
        self,
    ) -> Optional[outputs.AseV3NetworkingConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def suspended(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upgradeAvailability")
    def upgrade_availability(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upgradePreference")
    def upgrade_preference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userWhitelistedIpRanges")
    def user_whitelisted_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> outputs.VirtualNetworkProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[_builtins.bool]: ...

class AwaitableGetAppServiceEnvironmentResult(GetAppServiceEnvironmentResult):
    def __await__(self): ...

def get_app_service_environment(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAppServiceEnvironmentResult: ...
def get_app_service_environment_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAppServiceEnvironmentResult]: ...
