import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LabArgs", "Lab"]

@pulumi.input_type
class LabArgs:
    def __init__(
        __self__,
        *,
        auto_shutdown_profile: pulumi.Input[AutoShutdownProfileArgs],
        connection_profile: pulumi.Input[ConnectionProfileArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        security_profile: pulumi.Input[SecurityProfileArgs],
        virtual_machine_profile: pulumi.Input[VirtualMachineProfileArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lab_plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile: Optional[pulumi.Input[LabNetworkProfileArgs]] = ...,
        roster_profile: Optional[pulumi.Input[RosterProfileArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoShutdownProfile")
    def auto_shutdown_profile(self) -> pulumi.Input[AutoShutdownProfileArgs]: ...
    @auto_shutdown_profile.setter
    def auto_shutdown_profile(self, value: pulumi.Input[AutoShutdownProfileArgs]): ...
    @_builtins.property
    @pulumi.getter(name="connectionProfile")
    def connection_profile(self) -> pulumi.Input[ConnectionProfileArgs]: ...
    @connection_profile.setter
    def connection_profile(self, value: pulumi.Input[ConnectionProfileArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Input[SecurityProfileArgs]: ...
    @security_profile.setter
    def security_profile(self, value: pulumi.Input[SecurityProfileArgs]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> pulumi.Input[VirtualMachineProfileArgs]: ...
    @virtual_machine_profile.setter
    def virtual_machine_profile(
        self, value: pulumi.Input[VirtualMachineProfileArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labName")
    def lab_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lab_name.setter
    def lab_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labPlanId")
    def lab_plan_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lab_plan_id.setter
    def lab_plan_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[LabNetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[LabNetworkProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="rosterProfile")
    def roster_profile(self) -> Optional[pulumi.Input[RosterProfileArgs]]: ...
    @roster_profile.setter
    def roster_profile(self, value: Optional[pulumi.Input[RosterProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:labservices:Lab")
class Lab(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_shutdown_profile: Optional[
            pulumi.Input[Union[AutoShutdownProfileArgs, AutoShutdownProfileArgsDict]]
        ] = ...,
        connection_profile: Optional[
            pulumi.Input[Union[ConnectionProfileArgs, ConnectionProfileArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lab_plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile: Optional[
            pulumi.Input[Union[LabNetworkProfileArgs, LabNetworkProfileArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        roster_profile: Optional[
            pulumi.Input[Union[RosterProfileArgs, RosterProfileArgsDict]]
        ] = ...,
        security_profile: Optional[
            pulumi.Input[Union[SecurityProfileArgs, SecurityProfileArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine_profile: Optional[
            pulumi.Input[
                Union[VirtualMachineProfileArgs, VirtualMachineProfileArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LabArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Lab: ...
    @_builtins.property
    @pulumi.getter(name="autoShutdownProfile")
    def auto_shutdown_profile(
        self,
    ) -> pulumi.Output[outputs.AutoShutdownProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionProfile")
    def connection_profile(
        self,
    ) -> pulumi.Output[outputs.ConnectionProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="labPlanId")
    def lab_plan_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.LabNetworkProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceOperationError")
    def resource_operation_error(
        self,
    ) -> pulumi.Output[outputs.ResourceOperationErrorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="rosterProfile")
    def roster_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.RosterProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Output[outputs.SecurityProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(
        self,
    ) -> pulumi.Output[outputs.VirtualMachineProfileResponse]: ...
