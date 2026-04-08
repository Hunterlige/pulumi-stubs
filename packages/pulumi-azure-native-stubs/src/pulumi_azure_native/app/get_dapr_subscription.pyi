import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDaprSubscriptionResult",
    "AwaitableGetDaprSubscriptionResult",
    "get_dapr_subscription",
    "get_dapr_subscription_output",
]

@pulumi.output_type
class GetDaprSubscriptionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        bulk_subscribe=...,
        dead_letter_topic=...,
        id=...,
        metadata=...,
        name=...,
        pubsub_name=...,
        routes=...,
        scopes=...,
        system_data=...,
        topic=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bulkSubscribe")
    def bulk_subscribe(
        self,
    ) -> Optional[outputs.DaprSubscriptionBulkSubscribeOptionsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterTopic")
    def dead_letter_topic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pubsubName")
    def pubsub_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[outputs.DaprSubscriptionRoutesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDaprSubscriptionResult(GetDaprSubscriptionResult):
    def __await__(self): ...

def get_dapr_subscription(
    environment_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDaprSubscriptionResult: ...
def get_dapr_subscription_output(
    environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDaprSubscriptionResult]: ...
