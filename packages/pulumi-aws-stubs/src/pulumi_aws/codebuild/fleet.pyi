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
        base_capacity: pulumi.Input[_builtins.int],
        compute_type: pulumi.Input[_builtins.str],
        environment_type: pulumi.Input[_builtins.str],
        compute_configuration: Optional[
            pulumi.Input[FleetComputeConfigurationArgs]
        ] = ...,
        fleet_service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        overflow_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_configuration: Optional[
            pulumi.Input[FleetScalingConfigurationArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[FleetVpcConfigArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseCapacity")
    def base_capacity(self) -> pulumi.Input[_builtins.int]: ...
    @base_capacity.setter
    def base_capacity(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> pulumi.Input[_builtins.str]: ...
    @environment_type.setter
    def environment_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeConfiguration")
    def compute_configuration(
        self,
    ) -> Optional[pulumi.Input[FleetComputeConfigurationArgs]]: ...
    @compute_configuration.setter
    def compute_configuration(
        self, value: Optional[pulumi.Input[FleetComputeConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fleetServiceRole")
    def fleet_service_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fleet_service_role.setter
    def fleet_service_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overflowBehavior")
    def overflow_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @overflow_behavior.setter
    def overflow_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingConfiguration")
    def scaling_configuration(
        self,
    ) -> Optional[pulumi.Input[FleetScalingConfigurationArgs]]: ...
    @scaling_configuration.setter
    def scaling_configuration(
        self, value: Optional[pulumi.Input[FleetScalingConfigurationArgs]]
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
    @_builtins.property
    @pulumi.getter(name="vpcConfigs")
    def vpc_configs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FleetVpcConfigArgs]]]]: ...
    @vpc_configs.setter
    def vpc_configs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FleetVpcConfigArgs]]]]
    ): ...

@pulumi.input_type
class _FleetState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        base_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        compute_configuration: Optional[
            pulumi.Input[FleetComputeConfigurationArgs]
        ] = ...,
        compute_type: Optional[pulumi.Input[_builtins.str]] = ...,
        created: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        fleet_service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_modified: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        overflow_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_configuration: Optional[
            pulumi.Input[FleetScalingConfigurationArgs]
        ] = ...,
        statuses: Optional[pulumi.Input[Sequence[pulumi.Input[FleetStatusArgs]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[FleetVpcConfigArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="baseCapacity")
    def base_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @base_capacity.setter
    def base_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="computeConfiguration")
    def compute_configuration(
        self,
    ) -> Optional[pulumi.Input[FleetComputeConfigurationArgs]]: ...
    @compute_configuration.setter
    def compute_configuration(
        self, value: Optional[pulumi.Input[FleetComputeConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_type.setter
    def compute_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created.setter
    def created(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_type.setter
    def environment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fleetServiceRole")
    def fleet_service_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fleet_service_role.setter
    def fleet_service_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overflowBehavior")
    def overflow_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @overflow_behavior.setter
    def overflow_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingConfiguration")
    def scaling_configuration(
        self,
    ) -> Optional[pulumi.Input[FleetScalingConfigurationArgs]]: ...
    @scaling_configuration.setter
    def scaling_configuration(
        self, value: Optional[pulumi.Input[FleetScalingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FleetStatusArgs]]]]: ...
    @statuses.setter
    def statuses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FleetStatusArgs]]]]
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
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfigs")
    def vpc_configs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FleetVpcConfigArgs]]]]: ...
    @vpc_configs.setter
    def vpc_configs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FleetVpcConfigArgs]]]]
    ): ...

@pulumi.type_token("aws:codebuild/fleet:Fleet")
class Fleet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        base_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        compute_configuration: Optional[
            pulumi.Input[
                Union[FleetComputeConfigurationArgs, FleetComputeConfigurationArgsDict]
            ]
        ] = ...,
        compute_type: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        fleet_service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        overflow_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_configuration: Optional[
            pulumi.Input[
                Union[FleetScalingConfigurationArgs, FleetScalingConfigurationArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[FleetVpcConfigArgs, FleetVpcConfigArgsDict]]
                ]
            ]
        ] = ...,
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
        base_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        compute_configuration: Optional[
            pulumi.Input[
                Union[FleetComputeConfigurationArgs, FleetComputeConfigurationArgsDict]
            ]
        ] = ...,
        compute_type: Optional[pulumi.Input[_builtins.str]] = ...,
        created: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        fleet_service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_modified: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        overflow_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_configuration: Optional[
            pulumi.Input[
                Union[FleetScalingConfigurationArgs, FleetScalingConfigurationArgsDict]
            ]
        ] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[FleetStatusArgs, FleetStatusArgsDict]]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[FleetVpcConfigArgs, FleetVpcConfigArgsDict]]
                ]
            ]
        ] = ...,
    ) -> Fleet: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="baseCapacity")
    def base_capacity(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="computeConfiguration")
    def compute_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.FleetComputeConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fleetServiceRole")
    def fleet_service_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overflowBehavior")
    def overflow_behavior(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalingConfiguration")
    def scaling_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.FleetScalingConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.FleetStatus]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfigs")
    def vpc_configs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.FleetVpcConfig]]]: ...
