import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EventSourcesConfigEventSource",
    ...,
    "NotificationChannelFilters",
    "NotificationChannelSns",
    "ResourceCollectionCloudformation",
    "ResourceCollectionTags",
    "ServiceIntegrationKmsServerSideEncryption",
    "ServiceIntegrationLogsAnomalyDetection",
    "ServiceIntegrationOpsCenter",
    "GetNotificationChannelFilterResult",
    "GetNotificationChannelSnResult",
    "GetResourceCollectionCloudformationResult",
    "GetResourceCollectionTagResult",
]

@pulumi.output_type
class EventSourcesConfigEventSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amazon_code_guru_profilers: Sequence[
            outputs.EventSourcesConfigEventSourceAmazonCodeGuruProfiler
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonCodeGuruProfilers")
    def amazon_code_guru_profilers(
        self,
    ) -> Sequence[outputs.EventSourcesConfigEventSourceAmazonCodeGuruProfiler]: ...

@pulumi.output_type
class EventSourcesConfigEventSourceAmazonCodeGuruProfiler(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class NotificationChannelFilters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message_types: Optional[Sequence[_builtins.str]] = ...,
        severities: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageTypes")
    def message_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def severities(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class NotificationChannelSns(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, topic_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceCollectionCloudformation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, stack_names: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stackNames")
    def stack_names(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ResourceCollectionTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_boundary_key: _builtins.str,
        tag_values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appBoundaryKey")
    def app_boundary_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ServiceIntegrationKmsServerSideEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_id: Optional[_builtins.str] = ...,
        opt_in_status: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="optInStatus")
    def opt_in_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceIntegrationLogsAnomalyDetection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, opt_in_status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optInStatus")
    def opt_in_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceIntegrationOpsCenter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, opt_in_status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optInStatus")
    def opt_in_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetNotificationChannelFilterResult(dict):
    def __init__(
        __self__,
        *,
        message_types: Sequence[_builtins.str],
        severities: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageTypes")
    def message_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def severities(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetNotificationChannelSnResult(dict):
    def __init__(__self__, *, topic_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetResourceCollectionCloudformationResult(dict):
    def __init__(__self__, *, stack_names: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stackNames")
    def stack_names(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetResourceCollectionTagResult(dict):
    def __init__(
        __self__,
        *,
        app_boundary_key: _builtins.str,
        tag_values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appBoundaryKey")
    def app_boundary_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(self) -> Sequence[_builtins.str]: ...
