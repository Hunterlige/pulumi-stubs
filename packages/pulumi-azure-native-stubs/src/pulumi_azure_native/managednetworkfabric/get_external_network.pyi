import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetExternalNetworkResult",
    "AwaitableGetExternalNetworkResult",
    "get_external_network",
    "get_external_network_output",
]

@pulumi.output_type
class GetExternalNetworkResult:
    def __init__(
        __self__,
        administrative_state=...,
        annotation=...,
        azure_api_version=...,
        configuration_state=...,
        export_route_policy=...,
        export_route_policy_id=...,
        id=...,
        import_route_policy=...,
        import_route_policy_id=...,
        name=...,
        network_to_network_interconnect_id=...,
        option_a_properties=...,
        option_b_properties=...,
        peering_option=...,
        provisioning_state=...,
        system_data=...,
        type=...,
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
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicy")
    def export_route_policy(self) -> Optional[outputs.ExportRoutePolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> Optional[_builtins.str]: ...
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
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkToNetworkInterconnectId")
    def network_to_network_interconnect_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="optionAProperties")
    def option_a_properties(
        self,
    ) -> Optional[outputs.ExternalNetworkPropertiesResponseOptionAProperties]: ...
    @_builtins.property
    @pulumi.getter(name="optionBProperties")
    def option_b_properties(self) -> Optional[outputs.L3OptionBPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="peeringOption")
    def peering_option(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetExternalNetworkResult(GetExternalNetworkResult):
    def __await__(self): ...

def get_external_network(
    external_network_name: Optional[_builtins.str] = ...,
    l3_isolation_domain_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetExternalNetworkResult: ...
def get_external_network_output(
    external_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
    l3_isolation_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetExternalNetworkResult]: ...
