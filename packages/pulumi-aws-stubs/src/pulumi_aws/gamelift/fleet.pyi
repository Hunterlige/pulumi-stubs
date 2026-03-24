import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FleetArgs", "Fleet"]

@pulumi.input_type
class FleetArgs:
    def __init__(
        __self__,
        *,
        ec2_instance_type: pulumi.Input[_builtins.str],
        build_id: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_configuration: Optional[
            pulumi.Input[FleetCertificateConfigurationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ec2_inbound_permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[FleetEc2InboundPermissionArgs]]]
        ] = ...,
        fleet_type: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        new_game_session_protection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_creation_limit_policy: Optional[
            pulumi.Input[FleetResourceCreationLimitPolicyArgs]
        ] = ...,
        runtime_configuration: Optional[
            pulumi.Input[FleetRuntimeConfigurationArgs]
        ] = ...,
        script_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceType")
    def ec2_instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @ec2_instance_type.setter
    def ec2_instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="buildId")
    def build_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_id.setter
    def build_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateConfiguration")
    def certificate_configuration(
        self,
    ) -> Optional[pulumi.Input[FleetCertificateConfigurationArgs]]: ...
    @certificate_configuration.setter
    def certificate_configuration(
        self, value: Optional[pulumi.Input[FleetCertificateConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ec2InboundPermissions")
    def ec2_inbound_permissions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FleetEc2InboundPermissionArgs]]]
    ]: ...
    @ec2_inbound_permissions.setter
    def ec2_inbound_permissions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FleetEc2InboundPermissionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fleet_type.setter
    def fleet_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceRoleArn")
    def instance_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_role_arn.setter
    def instance_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricGroups")
    def metric_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @metric_groups.setter
    def metric_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="newGameSessionProtectionPolicy")
    def new_game_session_protection_policy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @new_game_session_protection_policy.setter
    def new_game_session_protection_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceCreationLimitPolicy")
    def resource_creation_limit_policy(
        self,
    ) -> Optional[pulumi.Input[FleetResourceCreationLimitPolicyArgs]]: ...
    @resource_creation_limit_policy.setter
    def resource_creation_limit_policy(
        self, value: Optional[pulumi.Input[FleetResourceCreationLimitPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfiguration")
    def runtime_configuration(
        self,
    ) -> Optional[pulumi.Input[FleetRuntimeConfigurationArgs]]: ...
    @runtime_configuration.setter
    def runtime_configuration(
        self, value: Optional[pulumi.Input[FleetRuntimeConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptId")
    def script_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_id.setter
    def script_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _FleetState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        build_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        build_id: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_configuration: Optional[
            pulumi.Input[FleetCertificateConfigurationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ec2_inbound_permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[FleetEc2InboundPermissionArgs]]]
        ] = ...,
        ec2_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        fleet_type: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        log_paths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        metric_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        new_game_session_protection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_creation_limit_policy: Optional[
            pulumi.Input[FleetResourceCreationLimitPolicyArgs]
        ] = ...,
        runtime_configuration: Optional[
            pulumi.Input[FleetRuntimeConfigurationArgs]
        ] = ...,
        script_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        script_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="buildArn")
    def build_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_arn.setter
    def build_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="buildId")
    def build_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_id.setter
    def build_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateConfiguration")
    def certificate_configuration(
        self,
    ) -> Optional[pulumi.Input[FleetCertificateConfigurationArgs]]: ...
    @certificate_configuration.setter
    def certificate_configuration(
        self, value: Optional[pulumi.Input[FleetCertificateConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ec2InboundPermissions")
    def ec2_inbound_permissions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FleetEc2InboundPermissionArgs]]]
    ]: ...
    @ec2_inbound_permissions.setter
    def ec2_inbound_permissions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FleetEc2InboundPermissionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceType")
    def ec2_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ec2_instance_type.setter
    def ec2_instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fleet_type.setter
    def fleet_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceRoleArn")
    def instance_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_role_arn.setter
    def instance_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logPaths")
    def log_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @log_paths.setter
    def log_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricGroups")
    def metric_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @metric_groups.setter
    def metric_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="newGameSessionProtectionPolicy")
    def new_game_session_protection_policy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @new_game_session_protection_policy.setter
    def new_game_session_protection_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceCreationLimitPolicy")
    def resource_creation_limit_policy(
        self,
    ) -> Optional[pulumi.Input[FleetResourceCreationLimitPolicyArgs]]: ...
    @resource_creation_limit_policy.setter
    def resource_creation_limit_policy(
        self, value: Optional[pulumi.Input[FleetResourceCreationLimitPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfiguration")
    def runtime_configuration(
        self,
    ) -> Optional[pulumi.Input[FleetRuntimeConfigurationArgs]]: ...
    @runtime_configuration.setter
    def runtime_configuration(
        self, value: Optional[pulumi.Input[FleetRuntimeConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptArn")
    def script_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_arn.setter
    def script_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptId")
    def script_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_id.setter
    def script_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:gamelift/fleet:Fleet")
class Fleet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        build_id: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_configuration: Optional[
            pulumi.Input[
                Union[
                    FleetCertificateConfigurationArgs,
                    FleetCertificateConfigurationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ec2_inbound_permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FleetEc2InboundPermissionArgs,
                            FleetEc2InboundPermissionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        ec2_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        fleet_type: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        new_game_session_protection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_creation_limit_policy: Optional[
            pulumi.Input[
                Union[
                    FleetResourceCreationLimitPolicyArgs,
                    FleetResourceCreationLimitPolicyArgsDict,
                ]
            ]
        ] = ...,
        runtime_configuration: Optional[
            pulumi.Input[
                Union[FleetRuntimeConfigurationArgs, FleetRuntimeConfigurationArgsDict]
            ]
        ] = ...,
        script_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FleetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        build_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        build_id: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_configuration: Optional[
            pulumi.Input[
                Union[
                    FleetCertificateConfigurationArgs,
                    FleetCertificateConfigurationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ec2_inbound_permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FleetEc2InboundPermissionArgs,
                            FleetEc2InboundPermissionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        ec2_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        fleet_type: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        log_paths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        metric_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        new_game_session_protection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_creation_limit_policy: Optional[
            pulumi.Input[
                Union[
                    FleetResourceCreationLimitPolicyArgs,
                    FleetResourceCreationLimitPolicyArgsDict,
                ]
            ]
        ] = ...,
        runtime_configuration: Optional[
            pulumi.Input[
                Union[FleetRuntimeConfigurationArgs, FleetRuntimeConfigurationArgsDict]
            ]
        ] = ...,
        script_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        script_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Fleet: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="buildArn")
    def build_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="buildId")
    def build_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="certificateConfiguration")
    def certificate_configuration(
        self,
    ) -> pulumi.Output[outputs.FleetCertificateConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ec2InboundPermissions")
    def ec2_inbound_permissions(
        self,
    ) -> pulumi.Output[Sequence[outputs.FleetEc2InboundPermission]]: ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceType")
    def ec2_instance_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceRoleArn")
    def instance_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logPaths")
    def log_paths(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="metricGroups")
    def metric_groups(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="newGameSessionProtectionPolicy")
    def new_game_session_protection_policy(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceCreationLimitPolicy")
    def resource_creation_limit_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.FleetResourceCreationLimitPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfiguration")
    def runtime_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.FleetRuntimeConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="scriptArn")
    def script_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scriptId")
    def script_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
