import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ComputeEnvironmentArgs", "ComputeEnvironment"]

@pulumi.input_type
class ComputeEnvironmentArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        compute_resources: Optional[
            pulumi.Input[ComputeEnvironmentComputeResourcesArgs]
        ] = ...,
        eks_configuration: Optional[
            pulumi.Input[ComputeEnvironmentEksConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        update_policy: Optional[pulumi.Input[ComputeEnvironmentUpdatePolicyArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeResources")
    def compute_resources(
        self,
    ) -> Optional[pulumi.Input[ComputeEnvironmentComputeResourcesArgs]]: ...
    @compute_resources.setter
    def compute_resources(
        self, value: Optional[pulumi.Input[ComputeEnvironmentComputeResourcesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eksConfiguration")
    def eks_configuration(
        self,
    ) -> Optional[pulumi.Input[ComputeEnvironmentEksConfigurationArgs]]: ...
    @eks_configuration.setter
    def eks_configuration(
        self, value: Optional[pulumi.Input[ComputeEnvironmentEksConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_role.setter
    def service_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="updatePolicy")
    def update_policy(
        self,
    ) -> Optional[pulumi.Input[ComputeEnvironmentUpdatePolicyArgs]]: ...
    @update_policy.setter
    def update_policy(
        self, value: Optional[pulumi.Input[ComputeEnvironmentUpdatePolicyArgs]]
    ): ...

@pulumi.input_type
class _ComputeEnvironmentState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_resources: Optional[
            pulumi.Input[ComputeEnvironmentComputeResourcesArgs]
        ] = ...,
        ecs_cluster_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        eks_configuration: Optional[
            pulumi.Input[ComputeEnvironmentEksConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_policy: Optional[pulumi.Input[ComputeEnvironmentUpdatePolicyArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeResources")
    def compute_resources(
        self,
    ) -> Optional[pulumi.Input[ComputeEnvironmentComputeResourcesArgs]]: ...
    @compute_resources.setter
    def compute_resources(
        self, value: Optional[pulumi.Input[ComputeEnvironmentComputeResourcesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecsClusterArn")
    def ecs_cluster_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ecs_cluster_arn.setter
    def ecs_cluster_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eksConfiguration")
    def eks_configuration(
        self,
    ) -> Optional[pulumi.Input[ComputeEnvironmentEksConfigurationArgs]]: ...
    @eks_configuration.setter
    def eks_configuration(
        self, value: Optional[pulumi.Input[ComputeEnvironmentEksConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_role.setter
    def service_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status_reason.setter
    def status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updatePolicy")
    def update_policy(
        self,
    ) -> Optional[pulumi.Input[ComputeEnvironmentUpdatePolicyArgs]]: ...
    @update_policy.setter
    def update_policy(
        self, value: Optional[pulumi.Input[ComputeEnvironmentUpdatePolicyArgs]]
    ): ...

@pulumi.type_token("aws:batch/computeEnvironment:ComputeEnvironment")
class ComputeEnvironment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        compute_resources: Optional[
            pulumi.Input[
                Union[
                    ComputeEnvironmentComputeResourcesArgs,
                    ComputeEnvironmentComputeResourcesArgsDict,
                ]
            ]
        ] = ...,
        eks_configuration: Optional[
            pulumi.Input[
                Union[
                    ComputeEnvironmentEksConfigurationArgs,
                    ComputeEnvironmentEksConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_policy: Optional[
            pulumi.Input[
                Union[
                    ComputeEnvironmentUpdatePolicyArgs,
                    ComputeEnvironmentUpdatePolicyArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ComputeEnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_resources: Optional[
            pulumi.Input[
                Union[
                    ComputeEnvironmentComputeResourcesArgs,
                    ComputeEnvironmentComputeResourcesArgsDict,
                ]
            ]
        ] = ...,
        ecs_cluster_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        eks_configuration: Optional[
            pulumi.Input[
                Union[
                    ComputeEnvironmentEksConfigurationArgs,
                    ComputeEnvironmentEksConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_policy: Optional[
            pulumi.Input[
                Union[
                    ComputeEnvironmentUpdatePolicyArgs,
                    ComputeEnvironmentUpdatePolicyArgsDict,
                ]
            ]
        ] = ...,
    ) -> ComputeEnvironment: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeResources")
    def compute_resources(
        self,
    ) -> pulumi.Output[outputs.ComputeEnvironmentComputeResources]: ...
    @_builtins.property
    @pulumi.getter(name="ecsClusterArn")
    def ecs_cluster_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eksConfiguration")
    def eks_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ComputeEnvironmentEksConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatePolicy")
    def update_policy(
        self,
    ) -> pulumi.Output[outputs.ComputeEnvironmentUpdatePolicy]: ...
