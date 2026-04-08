import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "LinkLinkConfigurationArgs",
    "LinkLinkConfigurationArgsDict",
    "LinkLinkConfigurationLogGroupConfigurationArgs",
    "LinkLinkConfigurationLogGroupConfigurationArgsDict",
    "LinkLinkConfigurationMetricConfigurationArgs",
    "LinkLinkConfigurationMetricConfigurationArgsDict",
]

class LinkLinkConfigurationArgsDict(TypedDict):
    log_group_configuration: NotRequired[
        pulumi.Input[LinkLinkConfigurationLogGroupConfigurationArgsDict]
    ]
    metric_configuration: NotRequired[
        pulumi.Input[LinkLinkConfigurationMetricConfigurationArgsDict]
    ]

@pulumi.input_type
class LinkLinkConfigurationArgs:
    def __init__(
        __self__,
        *,
        log_group_configuration: Optional[
            pulumi.Input[LinkLinkConfigurationLogGroupConfigurationArgs]
        ] = ...,
        metric_configuration: Optional[
            pulumi.Input[LinkLinkConfigurationMetricConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupConfiguration")
    def log_group_configuration(
        self,
    ) -> Optional[pulumi.Input[LinkLinkConfigurationLogGroupConfigurationArgs]]: ...
    @log_group_configuration.setter
    def log_group_configuration(
        self,
        value: Optional[pulumi.Input[LinkLinkConfigurationLogGroupConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricConfiguration")
    def metric_configuration(
        self,
    ) -> Optional[pulumi.Input[LinkLinkConfigurationMetricConfigurationArgs]]: ...
    @metric_configuration.setter
    def metric_configuration(
        self,
        value: Optional[pulumi.Input[LinkLinkConfigurationMetricConfigurationArgs]],
    ): ...

class LinkLinkConfigurationLogGroupConfigurationArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]

@pulumi.input_type
class LinkLinkConfigurationLogGroupConfigurationArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): ...

class LinkLinkConfigurationMetricConfigurationArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]

@pulumi.input_type
class LinkLinkConfigurationMetricConfigurationArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): ...
