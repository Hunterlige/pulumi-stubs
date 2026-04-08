import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RosettaNetProcessConfigurationArgs", "RosettaNetProcessConfiguration"]

@pulumi.input_type
class RosettaNetProcessConfigurationArgs:
    def __init__(
        __self__,
        *,
        activity_settings: pulumi.Input[RosettaNetPipActivitySettingsArgs],
        initiator_role_settings: pulumi.Input[RosettaNetPipRoleSettingsArgs],
        integration_account_name: pulumi.Input[_builtins.str],
        process_code: pulumi.Input[_builtins.str],
        process_name: pulumi.Input[_builtins.str],
        process_version: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        responder_role_settings: pulumi.Input[RosettaNetPipRoleSettingsArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        rosetta_net_process_configuration_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activitySettings")
    def activity_settings(self) -> pulumi.Input[RosettaNetPipActivitySettingsArgs]: ...
    @activity_settings.setter
    def activity_settings(
        self, value: pulumi.Input[RosettaNetPipActivitySettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initiatorRoleSettings")
    def initiator_role_settings(
        self,
    ) -> pulumi.Input[RosettaNetPipRoleSettingsArgs]: ...
    @initiator_role_settings.setter
    def initiator_role_settings(
        self, value: pulumi.Input[RosettaNetPipRoleSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="processCode")
    def process_code(self) -> pulumi.Input[_builtins.str]: ...
    @process_code.setter
    def process_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="processName")
    def process_name(self) -> pulumi.Input[_builtins.str]: ...
    @process_name.setter
    def process_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="processVersion")
    def process_version(self) -> pulumi.Input[_builtins.str]: ...
    @process_version.setter
    def process_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="responderRoleSettings")
    def responder_role_settings(
        self,
    ) -> pulumi.Input[RosettaNetPipRoleSettingsArgs]: ...
    @responder_role_settings.setter
    def responder_role_settings(
        self, value: pulumi.Input[RosettaNetPipRoleSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rosettaNetProcessConfigurationName")
    def rosetta_net_process_configuration_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rosetta_net_process_configuration_name.setter
    def rosetta_net_process_configuration_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:logic:RosettaNetProcessConfiguration")
class RosettaNetProcessConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        activity_settings: Optional[
            pulumi.Input[
                Union[
                    RosettaNetPipActivitySettingsArgs,
                    RosettaNetPipActivitySettingsArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        initiator_role_settings: Optional[
            pulumi.Input[
                Union[RosettaNetPipRoleSettingsArgs, RosettaNetPipRoleSettingsArgsDict]
            ]
        ] = ...,
        integration_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        process_code: Optional[pulumi.Input[_builtins.str]] = ...,
        process_name: Optional[pulumi.Input[_builtins.str]] = ...,
        process_version: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        responder_role_settings: Optional[
            pulumi.Input[
                Union[RosettaNetPipRoleSettingsArgs, RosettaNetPipRoleSettingsArgsDict]
            ]
        ] = ...,
        rosetta_net_process_configuration_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RosettaNetProcessConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RosettaNetProcessConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="activitySettings")
    def activity_settings(
        self,
    ) -> pulumi.Output[outputs.RosettaNetPipActivitySettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="initiatorRoleSettings")
    def initiator_role_settings(
        self,
    ) -> pulumi.Output[outputs.RosettaNetPipRoleSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processCode")
    def process_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processName")
    def process_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processVersion")
    def process_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responderRoleSettings")
    def responder_role_settings(
        self,
    ) -> pulumi.Output[outputs.RosettaNetPipRoleSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
