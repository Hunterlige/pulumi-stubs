import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PlanArgs", "Plan"]

@pulumi.input_type
class PlanArgs:
    def __init__(
        __self__,
        *,
        execution_role: pulumi.Input[_builtins.str],
        recovery_approach: pulumi.Input[_builtins.str],
        regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        associated_alarms: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanAssociatedAlarmArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_region: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_time_objective_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[PlanTimeoutsArgs]] = ...,
        triggers: Optional[pulumi.Input[Sequence[pulumi.Input[PlanTriggerArgs]]]] = ...,
        workflows: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Input[_builtins.str]: ...
    @execution_role.setter
    def execution_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryApproach")
    def recovery_approach(self) -> pulumi.Input[_builtins.str]: ...
    @recovery_approach.setter
    def recovery_approach(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @regions.setter
    def regions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="associatedAlarms")
    def associated_alarms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanAssociatedAlarmArgs]]]]: ...
    @associated_alarms.setter
    def associated_alarms(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanAssociatedAlarmArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryRegion")
    def primary_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_region.setter
    def primary_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryTimeObjectiveMinutes")
    def recovery_time_objective_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_time_objective_minutes.setter
    def recovery_time_objective_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
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
    def timeouts(self) -> Optional[pulumi.Input[PlanTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[PlanTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanTriggerArgs]]]]: ...
    @triggers.setter
    def triggers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanTriggerArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def workflows(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanWorkflowArgs]]]]: ...
    @workflows.setter
    def workflows(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanWorkflowArgs]]]]
    ): ...

@pulumi.input_type
class _PlanState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        associated_alarms: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanAssociatedAlarmArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_region: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_approach: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_time_objective_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[PlanTimeoutsArgs]] = ...,
        triggers: Optional[pulumi.Input[Sequence[pulumi.Input[PlanTriggerArgs]]]] = ...,
        workflows: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanWorkflowArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associatedAlarms")
    def associated_alarms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanAssociatedAlarmArgs]]]]: ...
    @associated_alarms.setter
    def associated_alarms(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanAssociatedAlarmArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role.setter
    def execution_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryRegion")
    def primary_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_region.setter
    def primary_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryApproach")
    def recovery_approach(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_approach.setter
    def recovery_approach(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryTimeObjectiveMinutes")
    def recovery_time_objective_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_time_objective_minutes.setter
    def recovery_time_objective_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[PlanTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[PlanTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanTriggerArgs]]]]: ...
    @triggers.setter
    def triggers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanTriggerArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def workflows(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanWorkflowArgs]]]]: ...
    @workflows.setter
    def workflows(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanWorkflowArgs]]]]
    ): ...

@pulumi.type_token("aws:arcregionswitch/plan:Plan")
class Plan(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        associated_alarms: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PlanAssociatedAlarmArgs, PlanAssociatedAlarmArgsDict]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_region: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_approach: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_time_objective_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[PlanTimeoutsArgs, PlanTimeoutsArgsDict]]
        ] = ...,
        triggers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[PlanTriggerArgs, PlanTriggerArgsDict]]]
            ]
        ] = ...,
        workflows: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[PlanWorkflowArgs, PlanWorkflowArgsDict]]]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PlanArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        associated_alarms: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PlanAssociatedAlarmArgs, PlanAssociatedAlarmArgsDict]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_region: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_approach: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_time_objective_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[PlanTimeoutsArgs, PlanTimeoutsArgsDict]]
        ] = ...,
        triggers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[PlanTriggerArgs, PlanTriggerArgsDict]]]
            ]
        ] = ...,
        workflows: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[PlanWorkflowArgs, PlanWorkflowArgsDict]]]
            ]
        ] = ...,
    ) -> Plan: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associatedAlarms")
    def associated_alarms(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PlanAssociatedAlarm]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryRegion")
    def primary_region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="recoveryApproach")
    def recovery_approach(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recoveryTimeObjectiveMinutes")
    def recovery_time_objective_minutes(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.PlanTimeouts]]: ...
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Sequence[outputs.PlanTrigger]]]: ...
    @_builtins.property
    @pulumi.getter
    def workflows(self) -> pulumi.Output[Optional[Sequence[outputs.PlanWorkflow]]]: ...
