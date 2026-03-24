import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RuleArgs", "Rule"]

@pulumi.input_type
class RuleArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        retention_period: pulumi.Input[RuleRetentionPeriodArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_resource_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuleExcludeResourceTagArgs]]]
        ] = ...,
        lock_configuration: Optional[pulumi.Input[RuleLockConfigurationArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuleResourceTagArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Input[RuleRetentionPeriodArgs]: ...
    @retention_period.setter
    def retention_period(self, value: pulumi.Input[RuleRetentionPeriodArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludeResourceTags")
    def exclude_resource_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleExcludeResourceTagArgs]]]]: ...
    @exclude_resource_tags.setter
    def exclude_resource_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuleExcludeResourceTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lockConfiguration")
    def lock_configuration(
        self,
    ) -> Optional[pulumi.Input[RuleLockConfigurationArgs]]: ...
    @lock_configuration.setter
    def lock_configuration(
        self, value: Optional[pulumi.Input[RuleLockConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleResourceTagArgs]]]]: ...
    @resource_tags.setter
    def resource_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RuleResourceTagArgs]]]]
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

@pulumi.input_type
class _RuleState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_resource_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuleExcludeResourceTagArgs]]]
        ] = ...,
        lock_configuration: Optional[pulumi.Input[RuleLockConfigurationArgs]] = ...,
        lock_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        lock_state: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuleResourceTagArgs]]]
        ] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[RuleRetentionPeriodArgs]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludeResourceTags")
    def exclude_resource_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleExcludeResourceTagArgs]]]]: ...
    @exclude_resource_tags.setter
    def exclude_resource_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuleExcludeResourceTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lockConfiguration")
    def lock_configuration(
        self,
    ) -> Optional[pulumi.Input[RuleLockConfigurationArgs]]: ...
    @lock_configuration.setter
    def lock_configuration(
        self, value: Optional[pulumi.Input[RuleLockConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lockEndTime")
    def lock_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lock_end_time.setter
    def lock_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lockState")
    def lock_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lock_state.setter
    def lock_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleResourceTagArgs]]]]: ...
    @resource_tags.setter
    def resource_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RuleResourceTagArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[RuleRetentionPeriodArgs]]: ...
    @retention_period.setter
    def retention_period(
        self, value: Optional[pulumi.Input[RuleRetentionPeriodArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:rbin/rule:Rule")
class Rule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_resource_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RuleExcludeResourceTagArgs, RuleExcludeResourceTagArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        lock_configuration: Optional[
            pulumi.Input[
                Union[RuleLockConfigurationArgs, RuleLockConfigurationArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[RuleResourceTagArgs, RuleResourceTagArgsDict]]
                ]
            ]
        ] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[
            pulumi.Input[Union[RuleRetentionPeriodArgs, RuleRetentionPeriodArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_resource_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RuleExcludeResourceTagArgs, RuleExcludeResourceTagArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        lock_configuration: Optional[
            pulumi.Input[
                Union[RuleLockConfigurationArgs, RuleLockConfigurationArgsDict]
            ]
        ] = ...,
        lock_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        lock_state: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[RuleResourceTagArgs, RuleResourceTagArgsDict]]
                ]
            ]
        ] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[
            pulumi.Input[Union[RuleRetentionPeriodArgs, RuleRetentionPeriodArgsDict]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Rule: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludeResourceTags")
    def exclude_resource_tags(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RuleExcludeResourceTag]]]: ...
    @_builtins.property
    @pulumi.getter(name="lockConfiguration")
    def lock_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.RuleLockConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="lockEndTime")
    def lock_end_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lockState")
    def lock_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RuleResourceTag]]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Output[outputs.RuleRetentionPeriod]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
