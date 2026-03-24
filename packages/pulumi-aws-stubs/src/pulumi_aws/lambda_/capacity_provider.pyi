import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
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
        permissions_config: pulumi.Input[CapacityProviderPermissionsConfigArgs],
        vpc_config: pulumi.Input[CapacityProviderVpcConfigArgs],
        capacity_provider_scaling_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CapacityProviderCapacityProviderScalingConfigArgs]
                ]
            ]
        ] = ...,
        instance_requirements: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CapacityProviderInstanceRequirementArgs]]
            ]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[CapacityProviderTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="permissionsConfig")
    def permissions_config(
        self,
    ) -> pulumi.Input[CapacityProviderPermissionsConfigArgs]: ...
    @permissions_config.setter
    def permissions_config(
        self, value: pulumi.Input[CapacityProviderPermissionsConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Input[CapacityProviderVpcConfigArgs]: ...
    @vpc_config.setter
    def vpc_config(self, value: pulumi.Input[CapacityProviderVpcConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderScalingConfigs")
    def capacity_provider_scaling_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CapacityProviderCapacityProviderScalingConfigArgs]]
        ]
    ]: ...
    @capacity_provider_scaling_configs.setter
    def capacity_provider_scaling_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CapacityProviderCapacityProviderScalingConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CapacityProviderInstanceRequirementArgs]]]
    ]: ...
    @instance_requirements.setter
    def instance_requirements(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CapacityProviderInstanceRequirementArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CapacityProviderTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CapacityProviderTimeoutsArgs]]): ...

@pulumi.input_type
class _CapacityProviderState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_provider_scaling_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CapacityProviderCapacityProviderScalingConfigArgs]
                ]
            ]
        ] = ...,
        instance_requirements: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CapacityProviderInstanceRequirementArgs]]
            ]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_config: Optional[
            pulumi.Input[CapacityProviderPermissionsConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[CapacityProviderTimeoutsArgs]] = ...,
        vpc_config: Optional[pulumi.Input[CapacityProviderVpcConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderScalingConfigs")
    def capacity_provider_scaling_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CapacityProviderCapacityProviderScalingConfigArgs]]
        ]
    ]: ...
    @capacity_provider_scaling_configs.setter
    def capacity_provider_scaling_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CapacityProviderCapacityProviderScalingConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CapacityProviderInstanceRequirementArgs]]]
    ]: ...
    @instance_requirements.setter
    def instance_requirements(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CapacityProviderInstanceRequirementArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="permissionsConfig")
    def permissions_config(
        self,
    ) -> Optional[pulumi.Input[CapacityProviderPermissionsConfigArgs]]: ...
    @permissions_config.setter
    def permissions_config(
        self, value: Optional[pulumi.Input[CapacityProviderPermissionsConfigArgs]]
    ): ...
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
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CapacityProviderTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CapacityProviderTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[CapacityProviderVpcConfigArgs]]: ...
    @vpc_config.setter
    def vpc_config(
        self, value: Optional[pulumi.Input[CapacityProviderVpcConfigArgs]]
    ): ...

@pulumi.type_token("aws:lambda/capacityProvider:CapacityProvider")
class CapacityProvider(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        capacity_provider_scaling_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CapacityProviderCapacityProviderScalingConfigArgs,
                            CapacityProviderCapacityProviderScalingConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        instance_requirements: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CapacityProviderInstanceRequirementArgs,
                            CapacityProviderInstanceRequirementArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_config: Optional[
            pulumi.Input[
                Union[
                    CapacityProviderPermissionsConfigArgs,
                    CapacityProviderPermissionsConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[CapacityProviderTimeoutsArgs, CapacityProviderTimeoutsArgsDict]
            ]
        ] = ...,
        vpc_config: Optional[
            pulumi.Input[
                Union[CapacityProviderVpcConfigArgs, CapacityProviderVpcConfigArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CapacityProviderArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_provider_scaling_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CapacityProviderCapacityProviderScalingConfigArgs,
                            CapacityProviderCapacityProviderScalingConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        instance_requirements: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CapacityProviderInstanceRequirementArgs,
                            CapacityProviderInstanceRequirementArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_config: Optional[
            pulumi.Input[
                Union[
                    CapacityProviderPermissionsConfigArgs,
                    CapacityProviderPermissionsConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[CapacityProviderTimeoutsArgs, CapacityProviderTimeoutsArgsDict]
            ]
        ] = ...,
        vpc_config: Optional[
            pulumi.Input[
                Union[CapacityProviderVpcConfigArgs, CapacityProviderVpcConfigArgsDict]
            ]
        ] = ...,
    ) -> CapacityProvider: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderScalingConfigs")
    def capacity_provider_scaling_configs(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.CapacityProviderCapacityProviderScalingConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(
        self,
    ) -> pulumi.Output[Sequence[outputs.CapacityProviderInstanceRequirement]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permissionsConfig")
    def permissions_config(
        self,
    ) -> pulumi.Output[outputs.CapacityProviderPermissionsConfig]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.CapacityProviderTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[outputs.CapacityProviderVpcConfig]: ...
