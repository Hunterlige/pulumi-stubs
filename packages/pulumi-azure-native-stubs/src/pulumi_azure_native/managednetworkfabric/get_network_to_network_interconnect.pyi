import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkToNetworkInterconnectResult",
    "AwaitableGetNetworkToNetworkInterconnectResult",
    "get_network_to_network_interconnect",
    "get_network_to_network_interconnect_output",
]

@pulumi.output_type
class GetNetworkToNetworkInterconnectResult:
    def __init__(
        __self__,
        administrative_state=...,
        azure_api_version=...,
        configuration_state=...,
        egress_acl_id=...,
        export_route_policy=...,
        id=...,
        import_route_policy=...,
        ingress_acl_id=...,
        is_management_type=...,
        layer2_configuration=...,
        name=...,
        nni_type=...,
        npb_static_route_configuration=...,
        option_b_layer3_configuration=...,
        provisioning_state=...,
        system_data=...,
        type=...,
        use_option_b=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="egressAclId")
    def egress_acl_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicy")
    def export_route_policy(
        self,
    ) -> Optional[outputs.ExportRoutePolicyInformationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="importRoutePolicy")
    def import_route_policy(
        self,
    ) -> Optional[outputs.ImportRoutePolicyInformationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="ingressAclId")
    def ingress_acl_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isManagementType")
    def is_management_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="layer2Configuration")
    def layer2_configuration(self) -> Optional[outputs.Layer2ConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nniType")
    def nni_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="npbStaticRouteConfiguration")
    def npb_static_route_configuration(
        self,
    ) -> Optional[outputs.NpbStaticRouteConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="optionBLayer3Configuration")
    def option_b_layer3_configuration(
        self,
    ) -> Optional[
        outputs.NetworkToNetworkInterconnectPropertiesResponseOptionBLayer3Configuration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useOptionB")
    def use_option_b(self) -> _builtins.str: ...

class AwaitableGetNetworkToNetworkInterconnectResult(
    GetNetworkToNetworkInterconnectResult
):
    def __await__(self): ...

def get_network_to_network_interconnect(
    network_fabric_name: Optional[_builtins.str] = ...,
    network_to_network_interconnect_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkToNetworkInterconnectResult: ...
def get_network_to_network_interconnect_output(
    network_fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
    network_to_network_interconnect_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkToNetworkInterconnectResult]: ...
