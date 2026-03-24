import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CapacityProviderArgs", "CapacityProvider"]

@pulumi.input_type
class CapacityProviderArgs:
    def __init__(
        __self__,
        *,
        auto_scaling_group_provider: Optional[
            pulumi.Input[CapacityProviderAutoScalingGroupProviderArgs]
        ] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_instances_provider: Optional[
            pulumi.Input[CapacityProviderManagedInstancesProviderArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingGroupProvider")
    def auto_scaling_group_provider(
        self,
    ) -> Optional[pulumi.Input[CapacityProviderAutoScalingGroupProviderArgs]]: ...
    @auto_scaling_group_provider.setter
    def auto_scaling_group_provider(
        self,
        value: Optional[pulumi.Input[CapacityProviderAutoScalingGroupProviderArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedInstancesProvider")
    def managed_instances_provider(
        self,
    ) -> Optional[pulumi.Input[CapacityProviderManagedInstancesProviderArgs]]: ...
    @managed_instances_provider.setter
    def managed_instances_provider(
        self,
        value: Optional[pulumi.Input[CapacityProviderManagedInstancesProviderArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _CapacityProviderState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_scaling_group_provider: Optional[
            pulumi.Input[CapacityProviderAutoScalingGroupProviderArgs]
        ] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_instances_provider: Optional[
            pulumi.Input[CapacityProviderManagedInstancesProviderArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="autoScalingGroupProvider")
    def auto_scaling_group_provider(
        self,
    ) -> Optional[pulumi.Input[CapacityProviderAutoScalingGroupProviderArgs]]: ...
    @auto_scaling_group_provider.setter
    def auto_scaling_group_provider(
        self,
        value: Optional[pulumi.Input[CapacityProviderAutoScalingGroupProviderArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedInstancesProvider")
    def managed_instances_provider(
        self,
    ) -> Optional[pulumi.Input[CapacityProviderManagedInstancesProviderArgs]]: ...
    @managed_instances_provider.setter
    def managed_instances_provider(
        self,
        value: Optional[pulumi.Input[CapacityProviderManagedInstancesProviderArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:ecs/capacityProvider:CapacityProvider")
class CapacityProvider(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_scaling_group_provider: Optional[
            pulumi.Input[
                Union[
                    CapacityProviderAutoScalingGroupProviderArgs,
                    CapacityProviderAutoScalingGroupProviderArgsDict,
                ]
            ]
        ] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_instances_provider: Optional[
            pulumi.Input[
                Union[
                    CapacityProviderManagedInstancesProviderArgs,
                    CapacityProviderManagedInstancesProviderArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[CapacityProviderArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_scaling_group_provider: Optional[
            pulumi.Input[
                Union[
                    CapacityProviderAutoScalingGroupProviderArgs,
                    CapacityProviderAutoScalingGroupProviderArgsDict,
                ]
            ]
        ] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_instances_provider: Optional[
            pulumi.Input[
                Union[
                    CapacityProviderManagedInstancesProviderArgs,
                    CapacityProviderManagedInstancesProviderArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> CapacityProvider: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingGroupProvider")
    def auto_scaling_group_provider(
        self,
    ) -> pulumi.Output[Optional[outputs.CapacityProviderAutoScalingGroupProvider]]: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managedInstancesProvider")
    def managed_instances_provider(
        self,
    ) -> pulumi.Output[Optional[outputs.CapacityProviderManagedInstancesProvider]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
