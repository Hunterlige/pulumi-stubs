import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PlatformApplicationArgs", "PlatformApplication"]

@pulumi.input_type
class PlatformApplicationArgs:
    def __init__(
        __self__,
        *,
        platform: pulumi.Input[_builtins.str],
        platform_credential: pulumi.Input[_builtins.str],
        apple_platform_bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        apple_platform_team_id: Optional[pulumi.Input[_builtins.str]] = ...,
        event_delivery_failure_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_created_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_deleted_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_updated_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        success_feedback_sample_rate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Input[_builtins.str]: ...
    @platform.setter
    def platform(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="platformCredential")
    def platform_credential(self) -> pulumi.Input[_builtins.str]: ...
    @platform_credential.setter
    def platform_credential(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applePlatformBundleId")
    def apple_platform_bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apple_platform_bundle_id.setter
    def apple_platform_bundle_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applePlatformTeamId")
    def apple_platform_team_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apple_platform_team_id.setter
    def apple_platform_team_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventDeliveryFailureTopicArn")
    def event_delivery_failure_topic_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_delivery_failure_topic_arn.setter
    def event_delivery_failure_topic_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventEndpointCreatedTopicArn")
    def event_endpoint_created_topic_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_endpoint_created_topic_arn.setter
    def event_endpoint_created_topic_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventEndpointDeletedTopicArn")
    def event_endpoint_deleted_topic_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_endpoint_deleted_topic_arn.setter
    def event_endpoint_deleted_topic_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventEndpointUpdatedTopicArn")
    def event_endpoint_updated_topic_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_endpoint_updated_topic_arn.setter
    def event_endpoint_updated_topic_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failureFeedbackRoleArn")
    def failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_feedback_role_arn.setter
    def failure_feedback_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformPrincipal")
    def platform_principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_principal.setter
    def platform_principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="successFeedbackRoleArn")
    def success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @success_feedback_role_arn.setter
    def success_feedback_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="successFeedbackSampleRate")
    def success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @success_feedback_sample_rate.setter
    def success_feedback_sample_rate(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _PlatformApplicationState:
    def __init__(
        __self__,
        *,
        apple_platform_bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        apple_platform_team_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_delivery_failure_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_created_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_deleted_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_updated_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_credential: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        success_feedback_sample_rate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applePlatformBundleId")
    def apple_platform_bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apple_platform_bundle_id.setter
    def apple_platform_bundle_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applePlatformTeamId")
    def apple_platform_team_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apple_platform_team_id.setter
    def apple_platform_team_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventDeliveryFailureTopicArn")
    def event_delivery_failure_topic_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_delivery_failure_topic_arn.setter
    def event_delivery_failure_topic_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventEndpointCreatedTopicArn")
    def event_endpoint_created_topic_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_endpoint_created_topic_arn.setter
    def event_endpoint_created_topic_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventEndpointDeletedTopicArn")
    def event_endpoint_deleted_topic_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_endpoint_deleted_topic_arn.setter
    def event_endpoint_deleted_topic_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventEndpointUpdatedTopicArn")
    def event_endpoint_updated_topic_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_endpoint_updated_topic_arn.setter
    def event_endpoint_updated_topic_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failureFeedbackRoleArn")
    def failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_feedback_role_arn.setter
    def failure_feedback_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformCredential")
    def platform_credential(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_credential.setter
    def platform_credential(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformPrincipal")
    def platform_principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_principal.setter
    def platform_principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="successFeedbackRoleArn")
    def success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @success_feedback_role_arn.setter
    def success_feedback_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="successFeedbackSampleRate")
    def success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @success_feedback_sample_rate.setter
    def success_feedback_sample_rate(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:sns/platformApplication:PlatformApplication")
class PlatformApplication(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        apple_platform_bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        apple_platform_team_id: Optional[pulumi.Input[_builtins.str]] = ...,
        event_delivery_failure_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_created_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_deleted_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_updated_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_credential: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        success_feedback_sample_rate: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PlatformApplicationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        apple_platform_bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        apple_platform_team_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_delivery_failure_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_created_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_deleted_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_endpoint_updated_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_credential: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        success_feedback_sample_rate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PlatformApplication: ...
    @_builtins.property
    @pulumi.getter(name="applePlatformBundleId")
    def apple_platform_bundle_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="applePlatformTeamId")
    def apple_platform_team_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventDeliveryFailureTopicArn")
    def event_delivery_failure_topic_arn(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventEndpointCreatedTopicArn")
    def event_endpoint_created_topic_arn(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventEndpointDeletedTopicArn")
    def event_endpoint_deleted_topic_arn(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventEndpointUpdatedTopicArn")
    def event_endpoint_updated_topic_arn(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="failureFeedbackRoleArn")
    def failure_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformCredential")
    def platform_credential(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformPrincipal")
    def platform_principal(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="successFeedbackRoleArn")
    def success_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="successFeedbackSampleRate")
    def success_feedback_sample_rate(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
