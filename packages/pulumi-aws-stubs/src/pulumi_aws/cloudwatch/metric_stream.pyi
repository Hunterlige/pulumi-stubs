import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MetricStreamArgs", "MetricStream"]

@pulumi.input_type
class MetricStreamArgs:
    def __init__(
        __self__,
        *,
        firehose_arn: pulumi.Input[_builtins.str],
        output_format: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        exclude_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricStreamExcludeFilterArgs]]]
        ] = ...,
        include_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricStreamIncludeFilterArgs]]]
        ] = ...,
        include_linked_accounts_metrics: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        statistics_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MetricStreamStatisticsConfigurationArgs]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firehoseArn")
    def firehose_arn(self) -> pulumi.Input[_builtins.str]: ...
    @firehose_arn.setter
    def firehose_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> pulumi.Input[_builtins.str]: ...
    @output_format.setter
    def output_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="excludeFilters")
    def exclude_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MetricStreamExcludeFilterArgs]]]
    ]: ...
    @exclude_filters.setter
    def exclude_filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricStreamExcludeFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeFilters")
    def include_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MetricStreamIncludeFilterArgs]]]
    ]: ...
    @include_filters.setter
    def include_filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricStreamIncludeFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeLinkedAccountsMetrics")
    def include_linked_accounts_metrics(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_linked_accounts_metrics.setter
    def include_linked_accounts_metrics(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statisticsConfigurations")
    def statistics_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MetricStreamStatisticsConfigurationArgs]]]
    ]: ...
    @statistics_configurations.setter
    def statistics_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MetricStreamStatisticsConfigurationArgs]]
            ]
        ],
    ): ...
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
class _MetricStreamState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_date: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricStreamExcludeFilterArgs]]]
        ] = ...,
        firehose_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        include_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricStreamIncludeFilterArgs]]]
        ] = ...,
        include_linked_accounts_metrics: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_update_date: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        output_format: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        statistics_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MetricStreamStatisticsConfigurationArgs]]
            ]
        ] = ...,
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
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludeFilters")
    def exclude_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MetricStreamExcludeFilterArgs]]]
    ]: ...
    @exclude_filters.setter
    def exclude_filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricStreamExcludeFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="firehoseArn")
    def firehose_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firehose_arn.setter
    def firehose_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includeFilters")
    def include_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MetricStreamIncludeFilterArgs]]]
    ]: ...
    @include_filters.setter
    def include_filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricStreamIncludeFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeLinkedAccountsMetrics")
    def include_linked_accounts_metrics(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_linked_accounts_metrics.setter
    def include_linked_accounts_metrics(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateDate")
    def last_update_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_update_date.setter
    def last_update_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_format.setter
    def output_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statisticsConfigurations")
    def statistics_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MetricStreamStatisticsConfigurationArgs]]]
    ]: ...
    @statistics_configurations.setter
    def statistics_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MetricStreamStatisticsConfigurationArgs]]
            ]
        ],
    ): ...
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

@pulumi.type_token("aws:cloudwatch/metricStream:MetricStream")
class MetricStream(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        exclude_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MetricStreamExcludeFilterArgs,
                            MetricStreamExcludeFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        firehose_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        include_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MetricStreamIncludeFilterArgs,
                            MetricStreamIncludeFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        include_linked_accounts_metrics: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        output_format: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        statistics_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MetricStreamStatisticsConfigurationArgs,
                            MetricStreamStatisticsConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MetricStreamArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_date: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MetricStreamExcludeFilterArgs,
                            MetricStreamExcludeFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        firehose_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        include_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MetricStreamIncludeFilterArgs,
                            MetricStreamIncludeFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        include_linked_accounts_metrics: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_update_date: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        output_format: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        statistics_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MetricStreamStatisticsConfigurationArgs,
                            MetricStreamStatisticsConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> MetricStream: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludeFilters")
    def exclude_filters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.MetricStreamExcludeFilter]]]: ...
    @_builtins.property
    @pulumi.getter(name="firehoseArn")
    def firehose_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeFilters")
    def include_filters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.MetricStreamIncludeFilter]]]: ...
    @_builtins.property
    @pulumi.getter(name="includeLinkedAccountsMetrics")
    def include_linked_accounts_metrics(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateDate")
    def last_update_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statisticsConfigurations")
    def statistics_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.MetricStreamStatisticsConfiguration]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
