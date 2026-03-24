import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InsightsReportConfigArgs", "InsightsReportConfig"]

@pulumi.input_type
class InsightsReportConfigArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        csv_options: Optional[pulumi.Input[InsightsReportConfigCsvOptionsArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        frequency_options: Optional[
            pulumi.Input[InsightsReportConfigFrequencyOptionsArgs]
        ] = ...,
        object_metadata_report_options: Optional[
            pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsArgs]
        ] = ...,
        parquet_options: Optional[
            pulumi.Input[InsightsReportConfigParquetOptionsArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> Optional[pulumi.Input[InsightsReportConfigCsvOptionsArgs]]: ...
    @csv_options.setter
    def csv_options(
        self, value: Optional[pulumi.Input[InsightsReportConfigCsvOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="frequencyOptions")
    def frequency_options(
        self,
    ) -> Optional[pulumi.Input[InsightsReportConfigFrequencyOptionsArgs]]: ...
    @frequency_options.setter
    def frequency_options(
        self, value: Optional[pulumi.Input[InsightsReportConfigFrequencyOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectMetadataReportOptions")
    def object_metadata_report_options(
        self,
    ) -> Optional[
        pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsArgs]
    ]: ...
    @object_metadata_report_options.setter
    def object_metadata_report_options(
        self,
        value: Optional[
            pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parquetOptions")
    def parquet_options(
        self,
    ) -> Optional[pulumi.Input[InsightsReportConfigParquetOptionsArgs]]: ...
    @parquet_options.setter
    def parquet_options(
        self, value: Optional[pulumi.Input[InsightsReportConfigParquetOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _InsightsReportConfigState:
    def __init__(
        __self__,
        *,
        csv_options: Optional[pulumi.Input[InsightsReportConfigCsvOptionsArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        frequency_options: Optional[
            pulumi.Input[InsightsReportConfigFrequencyOptionsArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        object_metadata_report_options: Optional[
            pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsArgs]
        ] = ...,
        parquet_options: Optional[
            pulumi.Input[InsightsReportConfigParquetOptionsArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> Optional[pulumi.Input[InsightsReportConfigCsvOptionsArgs]]: ...
    @csv_options.setter
    def csv_options(
        self, value: Optional[pulumi.Input[InsightsReportConfigCsvOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="frequencyOptions")
    def frequency_options(
        self,
    ) -> Optional[pulumi.Input[InsightsReportConfigFrequencyOptionsArgs]]: ...
    @frequency_options.setter
    def frequency_options(
        self, value: Optional[pulumi.Input[InsightsReportConfigFrequencyOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectMetadataReportOptions")
    def object_metadata_report_options(
        self,
    ) -> Optional[
        pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsArgs]
    ]: ...
    @object_metadata_report_options.setter
    def object_metadata_report_options(
        self,
        value: Optional[
            pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parquetOptions")
    def parquet_options(
        self,
    ) -> Optional[pulumi.Input[InsightsReportConfigParquetOptionsArgs]]: ...
    @parquet_options.setter
    def parquet_options(
        self, value: Optional[pulumi.Input[InsightsReportConfigParquetOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class InsightsReportConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        csv_options: Optional[
            pulumi.Input[
                Union[
                    InsightsReportConfigCsvOptionsArgs,
                    InsightsReportConfigCsvOptionsArgsDict,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        frequency_options: Optional[
            pulumi.Input[
                Union[
                    InsightsReportConfigFrequencyOptionsArgs,
                    InsightsReportConfigFrequencyOptionsArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        object_metadata_report_options: Optional[
            pulumi.Input[
                Union[
                    InsightsReportConfigObjectMetadataReportOptionsArgs,
                    InsightsReportConfigObjectMetadataReportOptionsArgsDict,
                ]
            ]
        ] = ...,
        parquet_options: Optional[
            pulumi.Input[
                Union[
                    InsightsReportConfigParquetOptionsArgs,
                    InsightsReportConfigParquetOptionsArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InsightsReportConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        csv_options: Optional[
            pulumi.Input[
                Union[
                    InsightsReportConfigCsvOptionsArgs,
                    InsightsReportConfigCsvOptionsArgsDict,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        frequency_options: Optional[
            pulumi.Input[
                Union[
                    InsightsReportConfigFrequencyOptionsArgs,
                    InsightsReportConfigFrequencyOptionsArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        object_metadata_report_options: Optional[
            pulumi.Input[
                Union[
                    InsightsReportConfigObjectMetadataReportOptionsArgs,
                    InsightsReportConfigObjectMetadataReportOptionsArgsDict,
                ]
            ]
        ] = ...,
        parquet_options: Optional[
            pulumi.Input[
                Union[
                    InsightsReportConfigParquetOptionsArgs,
                    InsightsReportConfigParquetOptionsArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> InsightsReportConfig: ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> pulumi.Output[Optional[outputs.InsightsReportConfigCsvOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="frequencyOptions")
    def frequency_options(
        self,
    ) -> pulumi.Output[Optional[outputs.InsightsReportConfigFrequencyOptions]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectMetadataReportOptions")
    def object_metadata_report_options(
        self,
    ) -> pulumi.Output[
        Optional[outputs.InsightsReportConfigObjectMetadataReportOptions]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="parquetOptions")
    def parquet_options(
        self,
    ) -> pulumi.Output[Optional[outputs.InsightsReportConfigParquetOptions]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
