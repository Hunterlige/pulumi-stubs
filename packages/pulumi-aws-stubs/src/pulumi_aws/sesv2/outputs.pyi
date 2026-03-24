import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccountVdmAttributesDashboardAttributes",
    "AccountVdmAttributesGuardianAttributes",
    "ConfigurationSetDeliveryOptions",
    "ConfigurationSetEventDestinationEventDestination",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ConfigurationSetReputationOptions",
    "ConfigurationSetSendingOptions",
    "ConfigurationSetSuppressionOptions",
    "ConfigurationSetTrackingOptions",
    "ConfigurationSetVdmOptions",
    "ConfigurationSetVdmOptionsDashboardOptions",
    "ConfigurationSetVdmOptionsGuardianOptions",
    "ContactListTopic",
    "EmailIdentityDkimSigningAttributes",
    "GetConfigurationSetDeliveryOptionResult",
    "GetConfigurationSetReputationOptionResult",
    "GetConfigurationSetSendingOptionResult",
    "GetConfigurationSetSuppressionOptionResult",
    "GetConfigurationSetTrackingOptionResult",
    "GetConfigurationSetVdmOptionResult",
    "GetConfigurationSetVdmOptionDashboardOptionResult",
    "GetConfigurationSetVdmOptionGuardianOptionResult",
    "GetDedicatedIpPoolDedicatedIpResult",
    "GetEmailIdentityDkimSigningAttributeResult",
]

@pulumi.output_type
class AccountVdmAttributesDashboardAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, engagement_metrics: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="engagementMetrics")
    def engagement_metrics(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccountVdmAttributesGuardianAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, optimized_shared_delivery: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optimizedSharedDelivery")
    def optimized_shared_delivery(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigurationSetDeliveryOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_delivery_seconds: Optional[_builtins.int] = ...,
        sending_pool_name: Optional[_builtins.str] = ...,
        tls_policy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxDeliverySeconds")
    def max_delivery_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sendingPoolName")
    def sending_pool_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigurationSetEventDestinationEventDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        matching_event_types: Sequence[_builtins.str],
        cloud_watch_destination: Optional[
            outputs.ConfigurationSetEventDestinationEventDestinationCloudWatchDestination
        ] = ...,
        enabled: Optional[_builtins.bool] = ...,
        event_bridge_destination: Optional[
            outputs.ConfigurationSetEventDestinationEventDestinationEventBridgeDestination
        ] = ...,
        kinesis_firehose_destination: Optional[
            outputs.ConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestination
        ] = ...,
        pinpoint_destination: Optional[
            outputs.ConfigurationSetEventDestinationEventDestinationPinpointDestination
        ] = ...,
        sns_destination: Optional[
            outputs.ConfigurationSetEventDestinationEventDestinationSnsDestination
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchingEventTypes")
    def matching_event_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchDestination")
    def cloud_watch_destination(
        self,
    ) -> Optional[
        outputs.ConfigurationSetEventDestinationEventDestinationCloudWatchDestination
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="eventBridgeDestination")
    def event_bridge_destination(
        self,
    ) -> Optional[
        outputs.ConfigurationSetEventDestinationEventDestinationEventBridgeDestination
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisFirehoseDestination")
    def kinesis_firehose_destination(
        self,
    ) -> Optional[
        outputs.ConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestination
    ]: ...
    @_builtins.property
    @pulumi.getter(name="pinpointDestination")
    def pinpoint_destination(
        self,
    ) -> Optional[
        outputs.ConfigurationSetEventDestinationEventDestinationPinpointDestination
    ]: ...
    @_builtins.property
    @pulumi.getter(name="snsDestination")
    def sns_destination(
        self,
    ) -> Optional[
        outputs.ConfigurationSetEventDestinationEventDestinationSnsDestination
    ]: ...

@pulumi.output_type
class ConfigurationSetEventDestinationEventDestinationCloudWatchDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimension_configurations: Sequence[
            outputs.ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfiguration
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dimensionConfigurations")
    def dimension_configurations(
        self,
    ) -> Sequence[
        outputs.ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfiguration
    ]: ...

@pulumi.output_type
class ConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_dimension_value: _builtins.str,
        dimension_name: _builtins.str,
        dimension_value_source: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultDimensionValue")
    def default_dimension_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dimensionValueSource")
    def dimension_value_source(self) -> _builtins.str: ...

@pulumi.output_type
class ConfigurationSetEventDestinationEventDestinationEventBridgeDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, event_bus_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventBusArn")
    def event_bus_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, delivery_stream_arn: _builtins.str, iam_role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStreamArn")
    def delivery_stream_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ConfigurationSetEventDestinationEventDestinationPinpointDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, application_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ConfigurationSetEventDestinationEventDestinationSnsDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, topic_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ConfigurationSetReputationOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_fresh_start: Optional[_builtins.str] = ...,
        reputation_metrics_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastFreshStart")
    def last_fresh_start(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reputationMetricsEnabled")
    def reputation_metrics_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConfigurationSetSendingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, sending_enabled: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sendingEnabled")
    def sending_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConfigurationSetSuppressionOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, suppressed_reasons: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="suppressedReasons")
    def suppressed_reasons(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConfigurationSetTrackingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_redirect_domain: _builtins.str,
        https_policy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRedirectDomain")
    def custom_redirect_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpsPolicy")
    def https_policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigurationSetVdmOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dashboard_options: Optional[
            outputs.ConfigurationSetVdmOptionsDashboardOptions
        ] = ...,
        guardian_options: Optional[
            outputs.ConfigurationSetVdmOptionsGuardianOptions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dashboardOptions")
    def dashboard_options(
        self,
    ) -> Optional[outputs.ConfigurationSetVdmOptionsDashboardOptions]: ...
    @_builtins.property
    @pulumi.getter(name="guardianOptions")
    def guardian_options(
        self,
    ) -> Optional[outputs.ConfigurationSetVdmOptionsGuardianOptions]: ...

@pulumi.output_type
class ConfigurationSetVdmOptionsDashboardOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, engagement_metrics: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="engagementMetrics")
    def engagement_metrics(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigurationSetVdmOptionsGuardianOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, optimized_shared_delivery: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optimizedSharedDelivery")
    def optimized_shared_delivery(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContactListTopic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_subscription_status: _builtins.str,
        display_name: _builtins.str,
        topic_name: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultSubscriptionStatus")
    def default_subscription_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EmailIdentityDkimSigningAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_signing_key_length: Optional[_builtins.str] = ...,
        domain_signing_private_key: Optional[_builtins.str] = ...,
        domain_signing_selector: Optional[_builtins.str] = ...,
        last_key_generation_timestamp: Optional[_builtins.str] = ...,
        next_signing_key_length: Optional[_builtins.str] = ...,
        signing_attributes_origin: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        tokens: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentSigningKeyLength")
    def current_signing_key_length(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainSigningPrivateKey")
    def domain_signing_private_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainSigningSelector")
    def domain_signing_selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastKeyGenerationTimestamp")
    def last_key_generation_timestamp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextSigningKeyLength")
    def next_signing_key_length(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signingAttributesOrigin")
    def signing_attributes_origin(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tokens(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetConfigurationSetDeliveryOptionResult(dict):
    def __init__(
        __self__,
        *,
        max_delivery_seconds: _builtins.int,
        sending_pool_name: _builtins.str,
        tls_policy: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxDeliverySeconds")
    def max_delivery_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sendingPoolName")
    def sending_pool_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetConfigurationSetReputationOptionResult(dict):
    def __init__(
        __self__,
        *,
        last_fresh_start: _builtins.str,
        reputation_metrics_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastFreshStart")
    def last_fresh_start(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reputationMetricsEnabled")
    def reputation_metrics_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetConfigurationSetSendingOptionResult(dict):
    def __init__(__self__, *, sending_enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sendingEnabled")
    def sending_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetConfigurationSetSuppressionOptionResult(dict):
    def __init__(__self__, *, suppressed_reasons: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="suppressedReasons")
    def suppressed_reasons(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetConfigurationSetTrackingOptionResult(dict):
    def __init__(
        __self__, *, custom_redirect_domain: _builtins.str, https_policy: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRedirectDomain")
    def custom_redirect_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpsPolicy")
    def https_policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetConfigurationSetVdmOptionResult(dict):
    def __init__(
        __self__,
        *,
        dashboard_options: Sequence[
            outputs.GetConfigurationSetVdmOptionDashboardOptionResult
        ],
        guardian_options: Sequence[
            outputs.GetConfigurationSetVdmOptionGuardianOptionResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dashboardOptions")
    def dashboard_options(
        self,
    ) -> Sequence[outputs.GetConfigurationSetVdmOptionDashboardOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="guardianOptions")
    def guardian_options(
        self,
    ) -> Sequence[outputs.GetConfigurationSetVdmOptionGuardianOptionResult]: ...

@pulumi.output_type
class GetConfigurationSetVdmOptionDashboardOptionResult(dict):
    def __init__(__self__, *, engagement_metrics: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="engagementMetrics")
    def engagement_metrics(self) -> _builtins.str: ...

@pulumi.output_type
class GetConfigurationSetVdmOptionGuardianOptionResult(dict):
    def __init__(__self__, *, optimized_shared_delivery: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optimizedSharedDelivery")
    def optimized_shared_delivery(self) -> _builtins.str: ...

@pulumi.output_type
class GetDedicatedIpPoolDedicatedIpResult(dict):
    def __init__(
        __self__,
        *,
        ip: _builtins.str,
        warmup_percentage: _builtins.int,
        warmup_status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="warmupPercentage")
    def warmup_percentage(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="warmupStatus")
    def warmup_status(self) -> _builtins.str: ...

@pulumi.output_type
class GetEmailIdentityDkimSigningAttributeResult(dict):
    def __init__(
        __self__,
        *,
        current_signing_key_length: _builtins.str,
        domain_signing_private_key: _builtins.str,
        domain_signing_selector: _builtins.str,
        last_key_generation_timestamp: _builtins.str,
        next_signing_key_length: _builtins.str,
        signing_attributes_origin: _builtins.str,
        status: _builtins.str,
        tokens: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentSigningKeyLength")
    def current_signing_key_length(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainSigningPrivateKey")
    def domain_signing_private_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainSigningSelector")
    def domain_signing_selector(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastKeyGenerationTimestamp")
    def last_key_generation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextSigningKeyLength")
    def next_signing_key_length(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signingAttributesOrigin")
    def signing_attributes_origin(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tokens(self) -> Sequence[_builtins.str]: ...
