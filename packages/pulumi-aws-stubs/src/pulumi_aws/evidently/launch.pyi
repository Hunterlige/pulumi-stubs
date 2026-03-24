import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LaunchArgs", "Launch"]

@pulumi.input_type
class LaunchArgs:
    def __init__(
        __self__,
        *,
        groups: pulumi.Input[Sequence[pulumi.Input[LaunchGroupArgs]]],
        project: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_monitors: Optional[
            pulumi.Input[Sequence[pulumi.Input[LaunchMetricMonitorArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        randomization_salt: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduled_splits_config: Optional[
            pulumi.Input[LaunchScheduledSplitsConfigArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> pulumi.Input[Sequence[pulumi.Input[LaunchGroupArgs]]]: ...
    @groups.setter
    def groups(self, value: pulumi.Input[Sequence[pulumi.Input[LaunchGroupArgs]]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricMonitors")
    def metric_monitors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchMetricMonitorArgs]]]]: ...
    @metric_monitors.setter
    def metric_monitors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchMetricMonitorArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="randomizationSalt")
    def randomization_salt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @randomization_salt.setter
    def randomization_salt(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduledSplitsConfig")
    def scheduled_splits_config(
        self,
    ) -> Optional[pulumi.Input[LaunchScheduledSplitsConfigArgs]]: ...
    @scheduled_splits_config.setter
    def scheduled_splits_config(
        self, value: Optional[pulumi.Input[LaunchScheduledSplitsConfigArgs]]
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
class _LaunchState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        executions: Optional[
            pulumi.Input[Sequence[pulumi.Input[LaunchExecutionArgs]]]
        ] = ...,
        groups: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchGroupArgs]]]] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_monitors: Optional[
            pulumi.Input[Sequence[pulumi.Input[LaunchMetricMonitorArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        randomization_salt: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduled_splits_config: Optional[
            pulumi.Input[LaunchScheduledSplitsConfigArgs]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def executions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchExecutionArgs]]]]: ...
    @executions.setter
    def executions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchExecutionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchGroupArgs]]]]: ...
    @groups.setter
    def groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchGroupArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricMonitors")
    def metric_monitors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchMetricMonitorArgs]]]]: ...
    @metric_monitors.setter
    def metric_monitors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchMetricMonitorArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="randomizationSalt")
    def randomization_salt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @randomization_salt.setter
    def randomization_salt(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduledSplitsConfig")
    def scheduled_splits_config(
        self,
    ) -> Optional[pulumi.Input[LaunchScheduledSplitsConfigArgs]]: ...
    @scheduled_splits_config.setter
    def scheduled_splits_config(
        self, value: Optional[pulumi.Input[LaunchScheduledSplitsConfigArgs]]
    ): ...
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

@pulumi.type_token("aws:evidently/launch:Launch")
class Launch(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        groups: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[LaunchGroupArgs, LaunchGroupArgsDict]]]
            ]
        ] = ...,
        metric_monitors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[LaunchMetricMonitorArgs, LaunchMetricMonitorArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        randomization_salt: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduled_splits_config: Optional[
            pulumi.Input[
                Union[
                    LaunchScheduledSplitsConfigArgs, LaunchScheduledSplitsConfigArgsDict
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LaunchArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        executions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[LaunchExecutionArgs, LaunchExecutionArgsDict]]
                ]
            ]
        ] = ...,
        groups: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[LaunchGroupArgs, LaunchGroupArgsDict]]]
            ]
        ] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_monitors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[LaunchMetricMonitorArgs, LaunchMetricMonitorArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        randomization_salt: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduled_splits_config: Optional[
            pulumi.Input[
                Union[
                    LaunchScheduledSplitsConfigArgs, LaunchScheduledSplitsConfigArgsDict
                ]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Launch: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def executions(self) -> pulumi.Output[Sequence[outputs.LaunchExecution]]: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Sequence[outputs.LaunchGroup]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricMonitors")
    def metric_monitors(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.LaunchMetricMonitor]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="randomizationSalt")
    def randomization_salt(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduledSplitsConfig")
    def scheduled_splits_config(
        self,
    ) -> pulumi.Output[Optional[outputs.LaunchScheduledSplitsConfig]]: ...
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
