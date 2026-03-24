import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HealthCheckArgs", "HealthCheck"]

@pulumi.input_type
class HealthCheckArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        child_health_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        child_healthchecks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cloudwatch_alarm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_alarm_region: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_sni: Optional[pulumi.Input[_builtins.bool]] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        insufficient_data_health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_healthcheck: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        measure_latency: Optional[pulumi.Input[_builtins.bool]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        request_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_path: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_control_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        search_string: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        triggers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="childHealthThreshold")
    def child_health_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @child_health_threshold.setter
    def child_health_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="childHealthchecks")
    def child_healthchecks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @child_healthchecks.setter
    def child_healthchecks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarmName")
    def cloudwatch_alarm_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_alarm_name.setter
    def cloudwatch_alarm_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarmRegion")
    def cloudwatch_alarm_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_alarm_region.setter
    def cloudwatch_alarm_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableSni")
    def enable_sni(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_sni.setter
    def enable_sni(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="insufficientDataHealthStatus")
    def insufficient_data_health_status(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @insufficient_data_health_status.setter
    def insufficient_data_health_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="invertHealthcheck")
    def invert_healthcheck(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_healthcheck.setter
    def invert_healthcheck(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="measureLatency")
    def measure_latency(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @measure_latency.setter
    def measure_latency(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="referenceName")
    def reference_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reference_name.setter
    def reference_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="requestInterval")
    def request_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @request_interval.setter
    def request_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourcePath")
    def resource_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_path.setter
    def resource_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingControlArn")
    def routing_control_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_control_arn.setter
    def routing_control_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="searchString")
    def search_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @search_string.setter
    def search_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def triggers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @triggers.setter
    def triggers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _HealthCheckState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        child_health_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        child_healthchecks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cloudwatch_alarm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_alarm_region: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_sni: Optional[pulumi.Input[_builtins.bool]] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        insufficient_data_health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_healthcheck: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        measure_latency: Optional[pulumi.Input[_builtins.bool]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        request_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_path: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_control_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        search_string: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        triggers: Optional[
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
    @pulumi.getter(name="childHealthThreshold")
    def child_health_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @child_health_threshold.setter
    def child_health_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="childHealthchecks")
    def child_healthchecks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @child_healthchecks.setter
    def child_healthchecks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarmName")
    def cloudwatch_alarm_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_alarm_name.setter
    def cloudwatch_alarm_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarmRegion")
    def cloudwatch_alarm_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_alarm_region.setter
    def cloudwatch_alarm_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableSni")
    def enable_sni(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_sni.setter
    def enable_sni(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="insufficientDataHealthStatus")
    def insufficient_data_health_status(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @insufficient_data_health_status.setter
    def insufficient_data_health_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="invertHealthcheck")
    def invert_healthcheck(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_healthcheck.setter
    def invert_healthcheck(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="measureLatency")
    def measure_latency(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @measure_latency.setter
    def measure_latency(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="referenceName")
    def reference_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reference_name.setter
    def reference_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="requestInterval")
    def request_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @request_interval.setter
    def request_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourcePath")
    def resource_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_path.setter
    def resource_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingControlArn")
    def routing_control_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_control_arn.setter
    def routing_control_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="searchString")
    def search_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @search_string.setter
    def search_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def triggers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @triggers.setter
    def triggers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:route53/healthCheck:HealthCheck")
class HealthCheck(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        child_health_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        child_healthchecks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cloudwatch_alarm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_alarm_region: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_sni: Optional[pulumi.Input[_builtins.bool]] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        insufficient_data_health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_healthcheck: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        measure_latency: Optional[pulumi.Input[_builtins.bool]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        request_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_path: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_control_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        search_string: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        triggers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: HealthCheckArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        child_health_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        child_healthchecks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cloudwatch_alarm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_alarm_region: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_sni: Optional[pulumi.Input[_builtins.bool]] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        insufficient_data_health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_healthcheck: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        measure_latency: Optional[pulumi.Input[_builtins.bool]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        request_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_path: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_control_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        search_string: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        triggers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> HealthCheck: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="childHealthThreshold")
    def child_health_threshold(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="childHealthchecks")
    def child_healthchecks(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarmName")
    def cloudwatch_alarm_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarmRegion")
    def cloudwatch_alarm_region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableSni")
    def enable_sni(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="insufficientDataHealthStatus")
    def insufficient_data_health_status(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="invertHealthcheck")
    def invert_healthcheck(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="measureLatency")
    def measure_latency(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="referenceName")
    def reference_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requestInterval")
    def request_interval(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="resourcePath")
    def resource_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="routingControlArn")
    def routing_control_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="searchString")
    def search_string(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
