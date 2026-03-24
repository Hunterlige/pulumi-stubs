import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "LinkLinkConfiguration",
    "LinkLinkConfigurationLogGroupConfiguration",
    "LinkLinkConfigurationMetricConfiguration",
    "GetLinkLinkConfigurationResult",
    ...,
    "GetLinkLinkConfigurationMetricConfigurationResult",
]

@pulumi.output_type
class LinkLinkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        log_group_configuration: Optional[
            outputs.LinkLinkConfigurationLogGroupConfiguration
        ] = ...,
        metric_configuration: Optional[
            outputs.LinkLinkConfigurationMetricConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupConfiguration")
    def log_group_configuration(
        self,
    ) -> Optional[outputs.LinkLinkConfigurationLogGroupConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="metricConfiguration")
    def metric_configuration(
        self,
    ) -> Optional[outputs.LinkLinkConfigurationMetricConfiguration]: ...

@pulumi.output_type
class LinkLinkConfigurationLogGroupConfiguration(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...

@pulumi.output_type
class LinkLinkConfigurationMetricConfiguration(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...

@pulumi.output_type
class GetLinkLinkConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        log_group_configurations: Sequence[
            outputs.GetLinkLinkConfigurationLogGroupConfigurationResult
        ],
        metric_configurations: Sequence[
            outputs.GetLinkLinkConfigurationMetricConfigurationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupConfigurations")
    def log_group_configurations(
        self,
    ) -> Sequence[outputs.GetLinkLinkConfigurationLogGroupConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="metricConfigurations")
    def metric_configurations(
        self,
    ) -> Sequence[outputs.GetLinkLinkConfigurationMetricConfigurationResult]: ...

@pulumi.output_type
class GetLinkLinkConfigurationLogGroupConfigurationResult(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...

@pulumi.output_type
class GetLinkLinkConfigurationMetricConfigurationResult(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
