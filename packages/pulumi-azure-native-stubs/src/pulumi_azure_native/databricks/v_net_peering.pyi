import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VNetPeeringArgs", "VNetPeering"]

@pulumi.input_type
class VNetPeeringArgs:
    def __init__(
        __self__,
        *,
        remote_virtual_network: pulumi.Input[
            VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        allow_forwarded_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_gateway_transit: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_virtual_network_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        databricks_address_space: Optional[pulumi.Input[AddressSpaceArgs]] = ...,
        databricks_virtual_network: Optional[
            pulumi.Input[
                VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs
            ]
        ] = ...,
        peering_name: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_address_space: Optional[pulumi.Input[AddressSpaceArgs]] = ...,
        use_remote_gateways: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(
        self,
    ) -> pulumi.Input[
        VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs
    ]: ...
    @remote_virtual_network.setter
    def remote_virtual_network(
        self,
        value: pulumi.Input[
            VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_forwarded_traffic.setter
    def allow_forwarded_traffic(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_gateway_transit.setter
    def allow_gateway_transit(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_virtual_network_access.setter
    def allow_virtual_network_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databricksAddressSpace")
    def databricks_address_space(self) -> Optional[pulumi.Input[AddressSpaceArgs]]: ...
    @databricks_address_space.setter
    def databricks_address_space(
        self, value: Optional[pulumi.Input[AddressSpaceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databricksVirtualNetwork")
    def databricks_virtual_network(
        self,
    ) -> Optional[
        pulumi.Input[VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs]
    ]: ...
    @databricks_virtual_network.setter
    def databricks_virtual_network(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peering_name.setter
    def peering_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteAddressSpace")
    def remote_address_space(self) -> Optional[pulumi.Input[AddressSpaceArgs]]: ...
    @remote_address_space.setter
    def remote_address_space(self, value: Optional[pulumi.Input[AddressSpaceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_remote_gateways.setter
    def use_remote_gateways(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("azure-native:databricks:VNetPeering")
class VNetPeering(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_forwarded_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_gateway_transit: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_virtual_network_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        databricks_address_space: Optional[
            pulumi.Input[Union[AddressSpaceArgs, AddressSpaceArgsDict]]
        ] = ...,
        databricks_virtual_network: Optional[
            pulumi.Input[
                Union[
                    VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs,
                    VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgsDict,
                ]
            ]
        ] = ...,
        peering_name: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_address_space: Optional[
            pulumi.Input[Union[AddressSpaceArgs, AddressSpaceArgsDict]]
        ] = ...,
        remote_virtual_network: Optional[
            pulumi.Input[
                Union[
                    VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs,
                    VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        use_remote_gateways: Optional[pulumi.Input[_builtins.bool]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VNetPeeringArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VNetPeering: ...
    @_builtins.property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databricksAddressSpace")
    def databricks_address_space(
        self,
    ) -> pulumi.Output[Optional[outputs.AddressSpaceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="databricksVirtualNetwork")
    def databricks_virtual_network(
        self,
    ) -> pulumi.Output[
        Optional[
            outputs.VirtualNetworkPeeringPropertiesFormatResponseDatabricksVirtualNetwork
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peeringState")
    def peering_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteAddressSpace")
    def remote_address_space(
        self,
    ) -> pulumi.Output[Optional[outputs.AddressSpaceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(
        self,
    ) -> pulumi.Output[
        outputs.VirtualNetworkPeeringPropertiesFormatResponseRemoteVirtualNetwork
    ]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
