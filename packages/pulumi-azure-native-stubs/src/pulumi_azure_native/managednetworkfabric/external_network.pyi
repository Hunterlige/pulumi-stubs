import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ExternalNetworkArgs", "ExternalNetwork"]

@pulumi.input_type
class ExternalNetworkArgs:
    def __init__(
        __self__,
        *,
        l3_isolation_domain_name: pulumi.Input[_builtins.str],
        peering_option: pulumi.Input[Union[_builtins.str, PeeringOption]],
        resource_group_name: pulumi.Input[_builtins.str],
        annotation: Optional[pulumi.Input[_builtins.str]] = ...,
        export_route_policy: Optional[pulumi.Input[ExportRoutePolicyArgs]] = ...,
        export_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        external_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
        import_route_policy: Optional[pulumi.Input[ImportRoutePolicyArgs]] = ...,
        import_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_to_network_interconnect_id: Optional[pulumi.Input[_builtins.str]] = ...,
        option_a_properties: Optional[
            pulumi.Input[ExternalNetworkPropertiesOptionAPropertiesArgs]
        ] = ...,
        option_b_properties: Optional[pulumi.Input[L3OptionBPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="l3IsolationDomainName")
    def l3_isolation_domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @l3_isolation_domain_name.setter
    def l3_isolation_domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="peeringOption")
    def peering_option(self) -> pulumi.Input[Union[_builtins.str, PeeringOption]]: ...
    @peering_option.setter
    def peering_option(
        self, value: pulumi.Input[Union[_builtins.str, PeeringOption]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicy")
    def export_route_policy(self) -> Optional[pulumi.Input[ExportRoutePolicyArgs]]: ...
    @export_route_policy.setter
    def export_route_policy(
        self, value: Optional[pulumi.Input[ExportRoutePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_route_policy_id.setter
    def export_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalNetworkName")
    def external_network_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_network_name.setter
    def external_network_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="importRoutePolicy")
    def import_route_policy(self) -> Optional[pulumi.Input[ImportRoutePolicyArgs]]: ...
    @import_route_policy.setter
    def import_route_policy(
        self, value: Optional[pulumi.Input[ImportRoutePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importRoutePolicyId")
    def import_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @import_route_policy_id.setter
    def import_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkToNetworkInterconnectId")
    def network_to_network_interconnect_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_to_network_interconnect_id.setter
    def network_to_network_interconnect_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="optionAProperties")
    def option_a_properties(
        self,
    ) -> Optional[pulumi.Input[ExternalNetworkPropertiesOptionAPropertiesArgs]]: ...
    @option_a_properties.setter
    def option_a_properties(
        self,
        value: Optional[pulumi.Input[ExternalNetworkPropertiesOptionAPropertiesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="optionBProperties")
    def option_b_properties(
        self,
    ) -> Optional[pulumi.Input[L3OptionBPropertiesArgs]]: ...
    @option_b_properties.setter
    def option_b_properties(
        self, value: Optional[pulumi.Input[L3OptionBPropertiesArgs]]
    ): ...

@pulumi.type_token("azure-native:managednetworkfabric:ExternalNetwork")
class ExternalNetwork(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotation: Optional[pulumi.Input[_builtins.str]] = ...,
        export_route_policy: Optional[
            pulumi.Input[Union[ExportRoutePolicyArgs, ExportRoutePolicyArgsDict]]
        ] = ...,
        export_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        external_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
        import_route_policy: Optional[
            pulumi.Input[Union[ImportRoutePolicyArgs, ImportRoutePolicyArgsDict]]
        ] = ...,
        import_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        l3_isolation_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_to_network_interconnect_id: Optional[pulumi.Input[_builtins.str]] = ...,
        option_a_properties: Optional[
            pulumi.Input[
                Union[
                    ExternalNetworkPropertiesOptionAPropertiesArgs,
                    ExternalNetworkPropertiesOptionAPropertiesArgsDict,
                ]
            ]
        ] = ...,
        option_b_properties: Optional[
            pulumi.Input[Union[L3OptionBPropertiesArgs, L3OptionBPropertiesArgsDict]]
        ] = ...,
        peering_option: Optional[
            pulumi.Input[Union[_builtins.str, PeeringOption]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ExternalNetworkArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ExternalNetwork: ...
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicy")
    def export_route_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ExportRoutePolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="importRoutePolicy")
    def import_route_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ImportRoutePolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="importRoutePolicyId")
    def import_route_policy_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkToNetworkInterconnectId")
    def network_to_network_interconnect_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="optionAProperties")
    def option_a_properties(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ExternalNetworkPropertiesResponseOptionAProperties]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="optionBProperties")
    def option_b_properties(
        self,
    ) -> pulumi.Output[Optional[outputs.L3OptionBPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="peeringOption")
    def peering_option(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
