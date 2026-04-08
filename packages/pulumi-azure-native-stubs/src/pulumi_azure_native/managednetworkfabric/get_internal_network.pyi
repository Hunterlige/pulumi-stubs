import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInternalNetworkResult",
    "AwaitableGetInternalNetworkResult",
    "get_internal_network",
    "get_internal_network_output",
]

@pulumi.output_type
class GetInternalNetworkResult:
    def __init__(
        __self__,
        administrative_state=...,
        annotation=...,
        azure_api_version=...,
        bgp_configuration=...,
        configuration_state=...,
        connected_i_pv4_subnets=...,
        connected_i_pv6_subnets=...,
        egress_acl_id=...,
        export_route_policy=...,
        export_route_policy_id=...,
        extension=...,
        id=...,
        import_route_policy=...,
        import_route_policy_id=...,
        ingress_acl_id=...,
        is_monitoring_enabled=...,
        mtu=...,
        name=...,
        provisioning_state=...,
        static_route_configuration=...,
        system_data=...,
        type=...,
        vlan_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bgpConfiguration")
    def bgp_configuration(
        self,
    ) -> Optional[outputs.InternalNetworkPropertiesResponseBgpConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectedIPv4Subnets")
    def connected_i_pv4_subnets(
        self,
    ) -> Optional[Sequence[outputs.ConnectedSubnetResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="connectedIPv6Subnets")
    def connected_i_pv6_subnets(
        self,
    ) -> Optional[Sequence[outputs.ConnectedSubnetResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="egressAclId")
    def egress_acl_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicy")
    def export_route_policy(self) -> Optional[outputs.ExportRoutePolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def extension(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="importRoutePolicy")
    def import_route_policy(self) -> Optional[outputs.ImportRoutePolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="importRoutePolicyId")
    def import_route_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ingressAclId")
    def ingress_acl_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isMonitoringEnabled")
    def is_monitoring_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="staticRouteConfiguration")
    def static_route_configuration(
        self,
    ) -> Optional[
        outputs.InternalNetworkPropertiesResponseStaticRouteConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> _builtins.int: ...

class AwaitableGetInternalNetworkResult(GetInternalNetworkResult):
    def __await__(self): ...

def get_internal_network(
    internal_network_name: Optional[_builtins.str] = ...,
    l3_isolation_domain_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInternalNetworkResult: ...
def get_internal_network_output(
    internal_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
    l3_isolation_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInternalNetworkResult]: ...
