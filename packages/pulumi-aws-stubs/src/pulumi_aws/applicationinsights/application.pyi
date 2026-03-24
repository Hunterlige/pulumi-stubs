import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationArgs", "Application"]

@pulumi.input_type
class ApplicationArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        auto_config_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        cwe_monitor_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        grouping_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ops_center_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ops_item_sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoConfigEnabled")
    def auto_config_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_config_enabled.setter
    def auto_config_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoCreate")
    def auto_create(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_create.setter
    def auto_create(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cweMonitorEnabled")
    def cwe_monitor_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cwe_monitor_enabled.setter
    def cwe_monitor_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="groupingType")
    def grouping_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grouping_type.setter
    def grouping_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="opsCenterEnabled")
    def ops_center_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ops_center_enabled.setter
    def ops_center_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="opsItemSnsTopicArn")
    def ops_item_sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ops_item_sns_topic_arn.setter
    def ops_item_sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _ApplicationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_config_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        cwe_monitor_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        grouping_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ops_center_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ops_item_sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="autoConfigEnabled")
    def auto_config_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_config_enabled.setter
    def auto_config_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoCreate")
    def auto_create(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_create.setter
    def auto_create(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cweMonitorEnabled")
    def cwe_monitor_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cwe_monitor_enabled.setter
    def cwe_monitor_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="groupingType")
    def grouping_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grouping_type.setter
    def grouping_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="opsCenterEnabled")
    def ops_center_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ops_center_enabled.setter
    def ops_center_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="opsItemSnsTopicArn")
    def ops_item_sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ops_item_sns_topic_arn.setter
    def ops_item_sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:applicationinsights/application:Application")
class Application(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_config_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        cwe_monitor_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        grouping_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ops_center_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ops_item_sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_config_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        cwe_monitor_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        grouping_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ops_center_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ops_item_sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Application: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoConfigEnabled")
    def auto_config_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="autoCreate")
    def auto_create(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="cweMonitorEnabled")
    def cwe_monitor_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="groupingType")
    def grouping_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="opsCenterEnabled")
    def ops_center_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="opsItemSnsTopicArn")
    def ops_item_sns_topic_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
