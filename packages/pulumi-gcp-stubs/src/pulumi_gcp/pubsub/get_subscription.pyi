

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSubscriptionResult', 'AwaitableGetSubscriptionResult', 'get_subscription', 'get_subscription_output']
@pulumi.output_type
class GetSubscriptionResult:
    
    def __init__(__self__, ack_deadline_seconds=..., bigquery_configs=..., cloud_storage_configs=..., dead_letter_policies=..., effective_labels=..., enable_exactly_once_delivery=..., enable_message_ordering=..., expiration_policies=..., filter=..., id=..., labels=..., message_retention_duration=..., message_transforms=..., name=..., project=..., pulumi_labels=..., push_configs=..., retain_acked_messages=..., retry_policies=..., tags=..., topic=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ackDeadlineSeconds")
    def ack_deadline_seconds(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryConfigs")
    def bigquery_configs(self) -> Sequence[outputs.GetSubscriptionBigqueryConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageConfigs")
    def cloud_storage_configs(self) -> Sequence[outputs.GetSubscriptionCloudStorageConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterPolicies")
    def dead_letter_policies(self) -> Sequence[outputs.GetSubscriptionDeadLetterPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExactlyOnceDelivery")
    def enable_exactly_once_delivery(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMessageOrdering")
    def enable_message_ordering(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationPolicies")
    def expiration_policies(self) -> Sequence[outputs.GetSubscriptionExpirationPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRetentionDuration")
    def message_retention_duration(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageTransforms")
    def message_transforms(self) -> Sequence[outputs.GetSubscriptionMessageTransformResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pushConfigs")
    def push_configs(self) -> Sequence[outputs.GetSubscriptionPushConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainAckedMessages")
    def retain_acked_messages(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicies")
    def retry_policies(self) -> Sequence[outputs.GetSubscriptionRetryPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        ...
    


class AwaitableGetSubscriptionResult(GetSubscriptionResult):
    def __await__(self): # -> Generator[Never, Any, GetSubscriptionResult]:
        ...
    


def get_subscription(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSubscriptionResult:
    
    ...

def get_subscription_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSubscriptionResult]:
    
    ...

