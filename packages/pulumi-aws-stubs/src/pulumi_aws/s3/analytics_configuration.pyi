import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AnalyticsConfigurationArgs", "AnalyticsConfiguration"]

@pulumi.input_type
class AnalyticsConfigurationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        filter: Optional[pulumi.Input[AnalyticsConfigurationFilterArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class_analysis: Optional[
            pulumi.Input[AnalyticsConfigurationStorageClassAnalysisArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[AnalyticsConfigurationFilterArgs]]: ...
    @filter.setter
    def filter(
        self, value: Optional[pulumi.Input[AnalyticsConfigurationFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageClassAnalysis")
    def storage_class_analysis(
        self,
    ) -> Optional[pulumi.Input[AnalyticsConfigurationStorageClassAnalysisArgs]]: ...
    @storage_class_analysis.setter
    def storage_class_analysis(
        self,
        value: Optional[pulumi.Input[AnalyticsConfigurationStorageClassAnalysisArgs]],
    ): ...

@pulumi.input_type
class _AnalyticsConfigurationState:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[pulumi.Input[AnalyticsConfigurationFilterArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class_analysis: Optional[
            pulumi.Input[AnalyticsConfigurationStorageClassAnalysisArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[AnalyticsConfigurationFilterArgs]]: ...
    @filter.setter
    def filter(
        self, value: Optional[pulumi.Input[AnalyticsConfigurationFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageClassAnalysis")
    def storage_class_analysis(
        self,
    ) -> Optional[pulumi.Input[AnalyticsConfigurationStorageClassAnalysisArgs]]: ...
    @storage_class_analysis.setter
    def storage_class_analysis(
        self,
        value: Optional[pulumi.Input[AnalyticsConfigurationStorageClassAnalysisArgs]],
    ): ...

@pulumi.type_token(...)
class AnalyticsConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[
                Union[
                    AnalyticsConfigurationFilterArgs,
                    AnalyticsConfigurationFilterArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class_analysis: Optional[
            pulumi.Input[
                Union[
                    AnalyticsConfigurationStorageClassAnalysisArgs,
                    AnalyticsConfigurationStorageClassAnalysisArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AnalyticsConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[
                Union[
                    AnalyticsConfigurationFilterArgs,
                    AnalyticsConfigurationFilterArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class_analysis: Optional[
            pulumi.Input[
                Union[
                    AnalyticsConfigurationStorageClassAnalysisArgs,
                    AnalyticsConfigurationStorageClassAnalysisArgsDict,
                ]
            ]
        ] = ...,
    ) -> AnalyticsConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> pulumi.Output[Optional[outputs.AnalyticsConfigurationFilter]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageClassAnalysis")
    def storage_class_analysis(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AnalyticsConfigurationStorageClassAnalysis]
    ]: ...
