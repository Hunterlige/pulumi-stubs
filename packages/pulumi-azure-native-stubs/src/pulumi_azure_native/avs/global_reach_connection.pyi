import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GlobalReachConnectionArgs", "GlobalReachConnection"]

@pulumi.input_type
class GlobalReachConnectionArgs:
    def __init__(
        __self__,
        *,
        private_cloud_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        authorization_key: Optional[pulumi.Input[_builtins.str]] = ...,
        express_route_id: Optional[pulumi.Input[_builtins.str]] = ...,
        global_reach_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_express_route_circuit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[_builtins.str]: ...
    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expressRouteId")
    def express_route_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @express_route_id.setter
    def express_route_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="globalReachConnectionName")
    def global_reach_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_reach_connection_name.setter
    def global_reach_connection_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peerExpressRouteCircuit")
    def peer_express_route_circuit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_express_route_circuit.setter
    def peer_express_route_circuit(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:avs:GlobalReachConnection")
class GlobalReachConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authorization_key: Optional[pulumi.Input[_builtins.str]] = ...,
        express_route_id: Optional[pulumi.Input[_builtins.str]] = ...,
        global_reach_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_express_route_circuit: Optional[pulumi.Input[_builtins.str]] = ...,
        private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GlobalReachConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> GlobalReachConnection: ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="circuitConnectionStatus")
    def circuit_connection_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expressRouteId")
    def express_route_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerExpressRouteCircuit")
    def peer_express_route_circuit(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
