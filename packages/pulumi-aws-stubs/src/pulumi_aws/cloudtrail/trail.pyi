import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TrailArgs", "Trail"]

@pulumi.input_type
class TrailArgs:
    def __init__(
        __self__,
        *,
        s3_bucket_name: pulumi.Input[_builtins.str],
        advanced_event_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailAdvancedEventSelectorArgs]]]
        ] = ...,
        cloud_watch_logs_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_watch_logs_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_log_file_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        event_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorArgs]]]
        ] = ...,
        include_global_service_events: Optional[pulumi.Input[_builtins.bool]] = ...,
        insight_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailInsightSelectorArgs]]]
        ] = ...,
        is_multi_region_trail: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_organization_trail: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        sns_topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="advancedEventSelectors")
    def advanced_event_selectors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TrailAdvancedEventSelectorArgs]]]
    ]: ...
    @advanced_event_selectors.setter
    def advanced_event_selectors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailAdvancedEventSelectorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogsGroupArn")
    def cloud_watch_logs_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_watch_logs_group_arn.setter
    def cloud_watch_logs_group_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogsRoleArn")
    def cloud_watch_logs_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_watch_logs_role_arn.setter
    def cloud_watch_logs_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableLogFileValidation")
    def enable_log_file_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_log_file_validation.setter
    def enable_log_file_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="eventSelectors")
    def event_selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorArgs]]]]: ...
    @event_selectors.setter
    def event_selectors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeGlobalServiceEvents")
    def include_global_service_events(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_global_service_events.setter
    def include_global_service_events(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="insightSelectors")
    def insight_selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TrailInsightSelectorArgs]]]]: ...
    @insight_selectors.setter
    def insight_selectors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TrailInsightSelectorArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isMultiRegionTrail")
    def is_multi_region_trail(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_multi_region_trail.setter
    def is_multi_region_trail(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isOrganizationTrail")
    def is_organization_trail(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_organization_trail.setter
    def is_organization_trail(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snsTopicName")
    def sns_topic_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sns_topic_name.setter
    def sns_topic_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _TrailState:
    def __init__(
        __self__,
        *,
        advanced_event_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailAdvancedEventSelectorArgs]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_watch_logs_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_watch_logs_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_log_file_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        event_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorArgs]]]
        ] = ...,
        home_region: Optional[pulumi.Input[_builtins.str]] = ...,
        include_global_service_events: Optional[pulumi.Input[_builtins.bool]] = ...,
        insight_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailInsightSelectorArgs]]]
        ] = ...,
        is_multi_region_trail: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_organization_trail: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        sns_topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedEventSelectors")
    def advanced_event_selectors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TrailAdvancedEventSelectorArgs]]]
    ]: ...
    @advanced_event_selectors.setter
    def advanced_event_selectors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailAdvancedEventSelectorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogsGroupArn")
    def cloud_watch_logs_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_watch_logs_group_arn.setter
    def cloud_watch_logs_group_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogsRoleArn")
    def cloud_watch_logs_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_watch_logs_role_arn.setter
    def cloud_watch_logs_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableLogFileValidation")
    def enable_log_file_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_log_file_validation.setter
    def enable_log_file_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="eventSelectors")
    def event_selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorArgs]]]]: ...
    @event_selectors.setter
    def event_selectors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="homeRegion")
    def home_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @home_region.setter
    def home_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includeGlobalServiceEvents")
    def include_global_service_events(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_global_service_events.setter
    def include_global_service_events(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="insightSelectors")
    def insight_selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TrailInsightSelectorArgs]]]]: ...
    @insight_selectors.setter
    def insight_selectors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TrailInsightSelectorArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isMultiRegionTrail")
    def is_multi_region_trail(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_multi_region_trail.setter
    def is_multi_region_trail(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isOrganizationTrail")
    def is_organization_trail(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_organization_trail.setter
    def is_organization_trail(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snsTopicName")
    def sns_topic_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sns_topic_name.setter
    def sns_topic_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:cloudtrail/trail:Trail")
class Trail(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_event_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TrailAdvancedEventSelectorArgs,
                            TrailAdvancedEventSelectorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        cloud_watch_logs_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_watch_logs_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_log_file_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        event_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TrailEventSelectorArgs, TrailEventSelectorArgsDict]
                    ]
                ]
            ]
        ] = ...,
        include_global_service_events: Optional[pulumi.Input[_builtins.bool]] = ...,
        insight_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TrailInsightSelectorArgs, TrailInsightSelectorArgsDict]
                    ]
                ]
            ]
        ] = ...,
        is_multi_region_trail: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_organization_trail: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        sns_topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TrailArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_event_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TrailAdvancedEventSelectorArgs,
                            TrailAdvancedEventSelectorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_watch_logs_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_watch_logs_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_log_file_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        event_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TrailEventSelectorArgs, TrailEventSelectorArgsDict]
                    ]
                ]
            ]
        ] = ...,
        home_region: Optional[pulumi.Input[_builtins.str]] = ...,
        include_global_service_events: Optional[pulumi.Input[_builtins.bool]] = ...,
        insight_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TrailInsightSelectorArgs, TrailInsightSelectorArgsDict]
                    ]
                ]
            ]
        ] = ...,
        is_multi_region_trail: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_organization_trail: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        sns_topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Trail: ...
    @_builtins.property
    @pulumi.getter(name="advancedEventSelectors")
    def advanced_event_selectors(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TrailAdvancedEventSelector]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogsGroupArn")
    def cloud_watch_logs_group_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogsRoleArn")
    def cloud_watch_logs_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableLogFileValidation")
    def enable_log_file_validation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="eventSelectors")
    def event_selectors(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TrailEventSelector]]]: ...
    @_builtins.property
    @pulumi.getter(name="homeRegion")
    def home_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeGlobalServiceEvents")
    def include_global_service_events(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="insightSelectors")
    def insight_selectors(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TrailInsightSelector]]]: ...
    @_builtins.property
    @pulumi.getter(name="isMultiRegionTrail")
    def is_multi_region_trail(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isOrganizationTrail")
    def is_organization_trail(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicName")
    def sns_topic_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
