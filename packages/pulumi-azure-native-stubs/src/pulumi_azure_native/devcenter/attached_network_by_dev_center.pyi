import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AttachedNetworkByDevCenterArgs", "AttachedNetworkByDevCenter"]

@pulumi.input_type
class AttachedNetworkByDevCenterArgs:
    def __init__(
        __self__,
        *,
        dev_center_name: pulumi.Input[_builtins.str],
        network_connection_id: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        attached_network_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="devCenterName")
    def dev_center_name(self) -> pulumi.Input[_builtins.str]: ...
    @dev_center_name.setter
    def dev_center_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkConnectionId")
    def network_connection_id(self) -> pulumi.Input[_builtins.str]: ...
    @network_connection_id.setter
    def network_connection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="attachedNetworkConnectionName")
    def attached_network_connection_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attached_network_connection_name.setter
    def attached_network_connection_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:devcenter:AttachedNetworkByDevCenter")
class AttachedNetworkByDevCenter(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        attached_network_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dev_center_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AttachedNetworkByDevCenterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AttachedNetworkByDevCenter: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainJoinType")
    def domain_join_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckStatus")
    def health_check_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConnectionId")
    def network_connection_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConnectionLocation")
    def network_connection_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
