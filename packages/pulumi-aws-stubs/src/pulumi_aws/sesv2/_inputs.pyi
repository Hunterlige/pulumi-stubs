

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountVdmAttributesDashboardAttributesArgs', 'AccountVdmAttributesDashboardAttributesArgsDict', 'AccountVdmAttributesGuardianAttributesArgs', 'AccountVdmAttributesGuardianAttributesArgsDict', 'ConfigurationSetDeliveryOptionsArgs', 'ConfigurationSetDeliveryOptionsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ConfigurationSetReputationOptionsArgs', 'ConfigurationSetReputationOptionsArgsDict', 'ConfigurationSetSendingOptionsArgs', 'ConfigurationSetSendingOptionsArgsDict', 'ConfigurationSetSuppressionOptionsArgs', 'ConfigurationSetSuppressionOptionsArgsDict', 'ConfigurationSetTrackingOptionsArgs', 'ConfigurationSetTrackingOptionsArgsDict', 'ConfigurationSetVdmOptionsArgs', 'ConfigurationSetVdmOptionsArgsDict', 'ConfigurationSetVdmOptionsDashboardOptionsArgs', 'ConfigurationSetVdmOptionsDashboardOptionsArgsDict', 'ConfigurationSetVdmOptionsGuardianOptionsArgs', 'ConfigurationSetVdmOptionsGuardianOptionsArgsDict', 'ContactListTopicArgs', 'ContactListTopicArgsDict', 'EmailIdentityDkimSigningAttributesArgs', 'EmailIdentityDkimSigningAttributesArgsDict']
class AccountVdmAttributesDashboardAttributesArgsDict(TypedDict):
    engagement_metrics: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AccountVdmAttributesDashboardAttributesArgs:
    def __init__(__self__, *, engagement_metrics: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engagementMetrics")
    def engagement_metrics(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engagement_metrics.setter
    def engagement_metrics(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AccountVdmAttributesGuardianAttributesArgsDict(TypedDict):
    optimized_shared_delivery: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AccountVdmAttributesGuardianAttributesArgs:
    def __init__(__self__, *, optimized_shared_delivery: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optimizedSharedDelivery")
    def optimized_shared_delivery(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @optimized_shared_delivery.setter
    def optimized_shared_delivery(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConfigurationSetDeliveryOptionsArgsDict(TypedDict):
    max_delivery_seconds: NotRequired[pulumi.Input[_builtins.int]]
    sending_pool_name: NotRequired[pulumi.Input[_builtins.str]]
    tls_policy: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConfigurationSetDeliveryOptionsArgs:
    def __init__(__self__, *, max_delivery_seconds: Optional[pulumi.Input[_builtins.int]] = ..., sending_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., tls_policy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDeliverySeconds")
    def max_delivery_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_delivery_seconds.setter
    def max_delivery_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendingPoolName")
    def sending_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sending_pool_name.setter
    def sending_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tls_policy.setter
    def tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConfigurationSetEventDestinationEventDestinationArgsDict(TypedDict):
    matching_event_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    cloud_watch_destination: NotRequired[pulumi.Input[ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationArgsDict]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    event_bridge_destination: NotRequired[pulumi.Input[ConfigurationSetEventDestinationEventDestinationEventBridgeDestinationArgsDict]]
    kinesis_firehose_destination: NotRequired[pulumi.Input[ConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationArgsDict]]
    pinpoint_destination: NotRequired[pulumi.Input[ConfigurationSetEventDestinationEventDestinationPinpointDestinationArgsDict]]
    sns_destination: NotRequired[pulumi.Input[ConfigurationSetEventDestinationEventDestinationSnsDestinationArgsDict]]


@pulumi.input_type
class ConfigurationSetEventDestinationEventDestinationArgs:
    def __init__(__self__, *, matching_event_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], cloud_watch_destination: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationArgs]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_bridge_destination: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationEventBridgeDestinationArgs]] = ..., kinesis_firehose_destination: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationArgs]] = ..., pinpoint_destination: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationPinpointDestinationArgs]] = ..., sns_destination: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationSnsDestinationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingEventTypes")
    def matching_event_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @matching_event_types.setter
    def matching_event_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchDestination")
    def cloud_watch_destination(self) -> Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationArgs]]:
        
        ...
    
    @cloud_watch_destination.setter
    def cloud_watch_destination(self, value: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBridgeDestination")
    def event_bridge_destination(self) -> Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationEventBridgeDestinationArgs]]:
        
        ...
    
    @event_bridge_destination.setter
    def event_bridge_destination(self, value: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationEventBridgeDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisFirehoseDestination")
    def kinesis_firehose_destination(self) -> Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationArgs]]:
        
        ...
    
    @kinesis_firehose_destination.setter
    def kinesis_firehose_destination(self, value: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pinpointDestination")
    def pinpoint_destination(self) -> Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationPinpointDestinationArgs]]:
        
        ...
    
    @pinpoint_destination.setter
    def pinpoint_destination(self, value: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationPinpointDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsDestination")
    def sns_destination(self) -> Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationSnsDestinationArgs]]:
        
        ...
    
    @sns_destination.setter
    def sns_destination(self, value: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationSnsDestinationArgs]]): # -> None:
        ...
    


class ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationArgsDict(TypedDict):
    dimension_configurations: pulumi.Input[Sequence[pulumi.Input[ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationArgsDict]]]


@pulumi.input_type
class ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationArgs:
    def __init__(__self__, *, dimension_configurations: pulumi.Input[Sequence[pulumi.Input[ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dimensionConfigurations")
    def dimension_configurations(self) -> pulumi.Input[Sequence[pulumi.Input[ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationArgs]]]:
        
        ...
    
    @dimension_configurations.setter
    def dimension_configurations(self, value: pulumi.Input[Sequence[pulumi.Input[ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationArgs]]]): # -> None:
        ...
    


class ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationArgsDict(TypedDict):
    default_dimension_value: pulumi.Input[_builtins.str]
    dimension_name: pulumi.Input[_builtins.str]
    dimension_value_source: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationArgs:
    def __init__(__self__, *, default_dimension_value: pulumi.Input[_builtins.str], dimension_name: pulumi.Input[_builtins.str], dimension_value_source: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDimensionValue")
    def default_dimension_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @default_dimension_value.setter
    def default_dimension_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dimension_name.setter
    def dimension_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dimensionValueSource")
    def dimension_value_source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dimension_value_source.setter
    def dimension_value_source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConfigurationSetEventDestinationEventDestinationEventBridgeDestinationArgsDict(TypedDict):
    event_bus_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConfigurationSetEventDestinationEventDestinationEventBridgeDestinationArgs:
    def __init__(__self__, *, event_bus_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBusArn")
    def event_bus_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_bus_arn.setter
    def event_bus_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationArgsDict(TypedDict):
    delivery_stream_arn: pulumi.Input[_builtins.str]
    iam_role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationArgs:
    def __init__(__self__, *, delivery_stream_arn: pulumi.Input[_builtins.str], iam_role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryStreamArn")
    def delivery_stream_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @delivery_stream_arn.setter
    def delivery_stream_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConfigurationSetEventDestinationEventDestinationPinpointDestinationArgsDict(TypedDict):
    application_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConfigurationSetEventDestinationEventDestinationPinpointDestinationArgs:
    def __init__(__self__, *, application_arn: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @application_arn.setter
    def application_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConfigurationSetEventDestinationEventDestinationSnsDestinationArgsDict(TypedDict):
    topic_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConfigurationSetEventDestinationEventDestinationSnsDestinationArgs:
    def __init__(__self__, *, topic_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConfigurationSetReputationOptionsArgsDict(TypedDict):
    last_fresh_start: NotRequired[pulumi.Input[_builtins.str]]
    reputation_metrics_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConfigurationSetReputationOptionsArgs:
    def __init__(__self__, *, last_fresh_start: Optional[pulumi.Input[_builtins.str]] = ..., reputation_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastFreshStart")
    def last_fresh_start(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_fresh_start.setter
    def last_fresh_start(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reputationMetricsEnabled")
    def reputation_metrics_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reputation_metrics_enabled.setter
    def reputation_metrics_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConfigurationSetSendingOptionsArgsDict(TypedDict):
    sending_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConfigurationSetSendingOptionsArgs:
    def __init__(__self__, *, sending_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendingEnabled")
    def sending_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @sending_enabled.setter
    def sending_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConfigurationSetSuppressionOptionsArgsDict(TypedDict):
    suppressed_reasons: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConfigurationSetSuppressionOptionsArgs:
    def __init__(__self__, *, suppressed_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressedReasons")
    def suppressed_reasons(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @suppressed_reasons.setter
    def suppressed_reasons(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConfigurationSetTrackingOptionsArgsDict(TypedDict):
    custom_redirect_domain: pulumi.Input[_builtins.str]
    https_policy: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConfigurationSetTrackingOptionsArgs:
    def __init__(__self__, *, custom_redirect_domain: pulumi.Input[_builtins.str], https_policy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRedirectDomain")
    def custom_redirect_domain(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @custom_redirect_domain.setter
    def custom_redirect_domain(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsPolicy")
    def https_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @https_policy.setter
    def https_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConfigurationSetVdmOptionsArgsDict(TypedDict):
    dashboard_options: NotRequired[pulumi.Input[ConfigurationSetVdmOptionsDashboardOptionsArgsDict]]
    guardian_options: NotRequired[pulumi.Input[ConfigurationSetVdmOptionsGuardianOptionsArgsDict]]


@pulumi.input_type
class ConfigurationSetVdmOptionsArgs:
    def __init__(__self__, *, dashboard_options: Optional[pulumi.Input[ConfigurationSetVdmOptionsDashboardOptionsArgs]] = ..., guardian_options: Optional[pulumi.Input[ConfigurationSetVdmOptionsGuardianOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardOptions")
    def dashboard_options(self) -> Optional[pulumi.Input[ConfigurationSetVdmOptionsDashboardOptionsArgs]]:
        
        ...
    
    @dashboard_options.setter
    def dashboard_options(self, value: Optional[pulumi.Input[ConfigurationSetVdmOptionsDashboardOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardianOptions")
    def guardian_options(self) -> Optional[pulumi.Input[ConfigurationSetVdmOptionsGuardianOptionsArgs]]:
        
        ...
    
    @guardian_options.setter
    def guardian_options(self, value: Optional[pulumi.Input[ConfigurationSetVdmOptionsGuardianOptionsArgs]]): # -> None:
        ...
    


class ConfigurationSetVdmOptionsDashboardOptionsArgsDict(TypedDict):
    engagement_metrics: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConfigurationSetVdmOptionsDashboardOptionsArgs:
    def __init__(__self__, *, engagement_metrics: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engagementMetrics")
    def engagement_metrics(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engagement_metrics.setter
    def engagement_metrics(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConfigurationSetVdmOptionsGuardianOptionsArgsDict(TypedDict):
    optimized_shared_delivery: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConfigurationSetVdmOptionsGuardianOptionsArgs:
    def __init__(__self__, *, optimized_shared_delivery: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optimizedSharedDelivery")
    def optimized_shared_delivery(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @optimized_shared_delivery.setter
    def optimized_shared_delivery(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContactListTopicArgsDict(TypedDict):
    default_subscription_status: pulumi.Input[_builtins.str]
    display_name: pulumi.Input[_builtins.str]
    topic_name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContactListTopicArgs:
    def __init__(__self__, *, default_subscription_status: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], topic_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSubscriptionStatus")
    def default_subscription_status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @default_subscription_status.setter
    def default_subscription_status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @topic_name.setter
    def topic_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EmailIdentityDkimSigningAttributesArgsDict(TypedDict):
    current_signing_key_length: NotRequired[pulumi.Input[_builtins.str]]
    domain_signing_private_key: NotRequired[pulumi.Input[_builtins.str]]
    domain_signing_selector: NotRequired[pulumi.Input[_builtins.str]]
    last_key_generation_timestamp: NotRequired[pulumi.Input[_builtins.str]]
    next_signing_key_length: NotRequired[pulumi.Input[_builtins.str]]
    signing_attributes_origin: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    tokens: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class EmailIdentityDkimSigningAttributesArgs:
    def __init__(__self__, *, current_signing_key_length: Optional[pulumi.Input[_builtins.str]] = ..., domain_signing_private_key: Optional[pulumi.Input[_builtins.str]] = ..., domain_signing_selector: Optional[pulumi.Input[_builtins.str]] = ..., last_key_generation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., next_signing_key_length: Optional[pulumi.Input[_builtins.str]] = ..., signing_attributes_origin: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tokens: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentSigningKeyLength")
    def current_signing_key_length(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @current_signing_key_length.setter
    def current_signing_key_length(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainSigningPrivateKey")
    def domain_signing_private_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_signing_private_key.setter
    def domain_signing_private_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainSigningSelector")
    def domain_signing_selector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_signing_selector.setter
    def domain_signing_selector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastKeyGenerationTimestamp")
    def last_key_generation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_key_generation_timestamp.setter
    def last_key_generation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextSigningKeyLength")
    def next_signing_key_length(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @next_signing_key_length.setter
    def next_signing_key_length(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAttributesOrigin")
    def signing_attributes_origin(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @signing_attributes_origin.setter
    def signing_attributes_origin(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tokens(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tokens.setter
    def tokens(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


