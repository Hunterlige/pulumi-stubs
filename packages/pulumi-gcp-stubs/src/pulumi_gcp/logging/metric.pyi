import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MetricArgs", "Metric"]

@pulumi.input_type
class MetricArgs:
    def __init__(
        __self__,
        *,
        filter: pulumi.Input[_builtins.str],
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_options: Optional[pulumi.Input[MetricBucketOptionsArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        label_extractors: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metric_descriptor: Optional[pulumi.Input[MetricMetricDescriptorArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        value_extractor: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketOptions")
    def bucket_options(self) -> Optional[pulumi.Input[MetricBucketOptionsArgs]]: ...
    @bucket_options.setter
    def bucket_options(
        self, value: Optional[pulumi.Input[MetricBucketOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="labelExtractors")
    def label_extractors(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @label_extractors.setter
    def label_extractors(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricDescriptor")
    def metric_descriptor(
        self,
    ) -> Optional[pulumi.Input[MetricMetricDescriptorArgs]]: ...
    @metric_descriptor.setter
    def metric_descriptor(
        self, value: Optional[pulumi.Input[MetricMetricDescriptorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueExtractor")
    def value_extractor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value_extractor.setter
    def value_extractor(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MetricState:
    def __init__(
        __self__,
        *,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_options: Optional[pulumi.Input[MetricBucketOptionsArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        label_extractors: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metric_descriptor: Optional[pulumi.Input[MetricMetricDescriptorArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        value_extractor: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketOptions")
    def bucket_options(self) -> Optional[pulumi.Input[MetricBucketOptionsArgs]]: ...
    @bucket_options.setter
    def bucket_options(
        self, value: Optional[pulumi.Input[MetricBucketOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labelExtractors")
    def label_extractors(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @label_extractors.setter
    def label_extractors(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricDescriptor")
    def metric_descriptor(
        self,
    ) -> Optional[pulumi.Input[MetricMetricDescriptorArgs]]: ...
    @metric_descriptor.setter
    def metric_descriptor(
        self, value: Optional[pulumi.Input[MetricMetricDescriptorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueExtractor")
    def value_extractor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value_extractor.setter
    def value_extractor(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:logging/metric:Metric")
class Metric(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_options: Optional[
            pulumi.Input[Union[MetricBucketOptionsArgs, MetricBucketOptionsArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        label_extractors: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metric_descriptor: Optional[
            pulumi.Input[
                Union[MetricMetricDescriptorArgs, MetricMetricDescriptorArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        value_extractor: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MetricArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_options: Optional[
            pulumi.Input[Union[MetricBucketOptionsArgs, MetricBucketOptionsArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        label_extractors: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metric_descriptor: Optional[
            pulumi.Input[
                Union[MetricMetricDescriptorArgs, MetricMetricDescriptorArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        value_extractor: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Metric: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bucketOptions")
    def bucket_options(
        self,
    ) -> pulumi.Output[Optional[outputs.MetricBucketOptions]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labelExtractors")
    def label_extractors(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="metricDescriptor")
    def metric_descriptor(self) -> pulumi.Output[outputs.MetricMetricDescriptor]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueExtractor")
    def value_extractor(self) -> pulumi.Output[Optional[_builtins.str]]: ...
