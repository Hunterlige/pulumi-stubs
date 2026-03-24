import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EnvironmentArgs", "Environment"]

@pulumi.input_type
class EnvironmentArgs:
    def __init__(
        __self__,
        *,
        application: pulumi.Input[_builtins.str],
        cname_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        poll_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgs]]]
        ] = ...,
        solution_stack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_for_ready_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def application(self) -> pulumi.Input[_builtins.str]: ...
    @application.setter
    def application(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cnamePrefix")
    def cname_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cname_prefix.setter
    def cname_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="platformArn")
    def platform_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_arn.setter
    def platform_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pollInterval")
    def poll_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @poll_interval.setter
    def poll_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgs]]]]: ...
    @settings.setter
    def settings(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @solution_stack_name.setter
    def solution_stack_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="waitForReadyTimeout")
    def wait_for_ready_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_for_ready_timeout.setter
    def wait_for_ready_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EnvironmentState:
    def __init__(
        __self__,
        *,
        all_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentAllSettingArgs]]]
        ] = ...,
        application: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        autoscaling_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cname: Optional[pulumi.Input[_builtins.str]] = ...,
        cname_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_url: Optional[pulumi.Input[_builtins.str]] = ...,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        launch_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        load_balancers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        poll_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        queues: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgs]]]
        ] = ...,
        solution_stack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        triggers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_for_ready_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allSettings")
    def all_settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentAllSettingArgs]]]]: ...
    @all_settings.setter
    def all_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentAllSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def application(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application.setter
    def application(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingGroups")
    def autoscaling_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @autoscaling_groups.setter
    def autoscaling_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cname.setter
    def cname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cnamePrefix")
    def cname_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cname_prefix.setter
    def cname_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_url.setter
    def endpoint_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instances.setter
    def instances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="launchConfigurations")
    def launch_configurations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @launch_configurations.setter
    def launch_configurations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @load_balancers.setter
    def load_balancers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformArn")
    def platform_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_arn.setter
    def platform_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pollInterval")
    def poll_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @poll_interval.setter
    def poll_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def queues(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @queues.setter
    def queues(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgs]]]]: ...
    @settings.setter
    def settings(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @solution_stack_name.setter
    def solution_stack_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @triggers.setter
    def triggers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="waitForReadyTimeout")
    def wait_for_ready_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_for_ready_timeout.setter
    def wait_for_ready_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:elasticbeanstalk/environment:Environment")
class Environment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application: Optional[pulumi.Input[_builtins.str]] = ...,
        cname_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        poll_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[EnvironmentSettingArgs, EnvironmentSettingArgsDict]
                    ]
                ]
            ]
        ] = ...,
        solution_stack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_for_ready_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        all_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[EnvironmentAllSettingArgs, EnvironmentAllSettingArgsDict]
                    ]
                ]
            ]
        ] = ...,
        application: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        autoscaling_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cname: Optional[pulumi.Input[_builtins.str]] = ...,
        cname_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_url: Optional[pulumi.Input[_builtins.str]] = ...,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        launch_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        load_balancers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        poll_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        queues: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[EnvironmentSettingArgs, EnvironmentSettingArgsDict]
                    ]
                ]
            ]
        ] = ...,
        solution_stack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        triggers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_for_ready_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Environment: ...
    @_builtins.property
    @pulumi.getter(name="allSettings")
    def all_settings(
        self,
    ) -> pulumi.Output[Sequence[outputs.EnvironmentAllSetting]]: ...
    @_builtins.property
    @pulumi.getter
    def application(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingGroups")
    def autoscaling_groups(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def cname(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cnamePrefix")
    def cname_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="launchConfigurations")
    def launch_configurations(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformArn")
    def platform_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pollInterval")
    def poll_interval(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def queues(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def settings(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.EnvironmentSetting]]]: ...
    @_builtins.property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="waitForReadyTimeout")
    def wait_for_ready_timeout(self) -> pulumi.Output[Optional[_builtins.str]]: ...
