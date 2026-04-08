import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OutputInitArgs", "Output"]

@pulumi.input_type
class OutputInitArgs:
    def __init__(
        __self__,
        *,
        job_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        datasource: Optional[
            pulumi.Input[
                Union[
                    AzureDataLakeStoreOutputDataSourceArgs,
                    AzureFunctionOutputDataSourceArgs,
                    AzureSqlDatabaseOutputDataSourceArgs,
                    AzureSynapseOutputDataSourceArgs,
                    AzureTableOutputDataSourceArgs,
                    BlobOutputDataSourceArgs,
                    DocumentDbOutputDataSourceArgs,
                    EventHubOutputDataSourceArgs,
                    EventHubV2OutputDataSourceArgs,
                    GatewayMessageBusOutputDataSourceArgs,
                    PowerBIOutputDataSourceArgs,
                    ServiceBusQueueOutputDataSourceArgs,
                    ServiceBusTopicOutputDataSourceArgs,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_name: Optional[pulumi.Input[_builtins.str]] = ...,
        serialization: Optional[
            pulumi.Input[
                Union[
                    AvroSerializationArgs,
                    CsvSerializationArgs,
                    JsonSerializationArgs,
                    ParquetSerializationArgs,
                ]
            ]
        ] = ...,
        size_window: Optional[pulumi.Input[_builtins.int]] = ...,
        time_window: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[_builtins.str]: ...
    @job_name.setter
    def job_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def datasource(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AzureDataLakeStoreOutputDataSourceArgs,
                AzureFunctionOutputDataSourceArgs,
                AzureSqlDatabaseOutputDataSourceArgs,
                AzureSynapseOutputDataSourceArgs,
                AzureTableOutputDataSourceArgs,
                BlobOutputDataSourceArgs,
                DocumentDbOutputDataSourceArgs,
                EventHubOutputDataSourceArgs,
                EventHubV2OutputDataSourceArgs,
                GatewayMessageBusOutputDataSourceArgs,
                PowerBIOutputDataSourceArgs,
                ServiceBusQueueOutputDataSourceArgs,
                ServiceBusTopicOutputDataSourceArgs,
            ]
        ]
    ]: ...
    @datasource.setter
    def datasource(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AzureDataLakeStoreOutputDataSourceArgs,
                    AzureFunctionOutputDataSourceArgs,
                    AzureSqlDatabaseOutputDataSourceArgs,
                    AzureSynapseOutputDataSourceArgs,
                    AzureTableOutputDataSourceArgs,
                    BlobOutputDataSourceArgs,
                    DocumentDbOutputDataSourceArgs,
                    EventHubOutputDataSourceArgs,
                    EventHubV2OutputDataSourceArgs,
                    GatewayMessageBusOutputDataSourceArgs,
                    PowerBIOutputDataSourceArgs,
                    ServiceBusQueueOutputDataSourceArgs,
                    ServiceBusTopicOutputDataSourceArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputName")
    def output_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_name.setter
    def output_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def serialization(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AvroSerializationArgs,
                CsvSerializationArgs,
                JsonSerializationArgs,
                ParquetSerializationArgs,
            ]
        ]
    ]: ...
    @serialization.setter
    def serialization(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AvroSerializationArgs,
                    CsvSerializationArgs,
                    JsonSerializationArgs,
                    ParquetSerializationArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sizeWindow")
    def size_window(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_window.setter
    def size_window(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_window.setter
    def time_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:streamanalytics:Output")
class Output(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        datasource: Optional[
            pulumi.Input[
                Union[
                    Union[
                        AzureDataLakeStoreOutputDataSourceArgs,
                        AzureDataLakeStoreOutputDataSourceArgsDict,
                    ],
                    Union[
                        AzureFunctionOutputDataSourceArgs,
                        AzureFunctionOutputDataSourceArgsDict,
                    ],
                    Union[
                        AzureSqlDatabaseOutputDataSourceArgs,
                        AzureSqlDatabaseOutputDataSourceArgsDict,
                    ],
                    Union[
                        AzureSynapseOutputDataSourceArgs,
                        AzureSynapseOutputDataSourceArgsDict,
                    ],
                    Union[
                        AzureTableOutputDataSourceArgs,
                        AzureTableOutputDataSourceArgsDict,
                    ],
                    Union[BlobOutputDataSourceArgs, BlobOutputDataSourceArgsDict],
                    Union[
                        DocumentDbOutputDataSourceArgs,
                        DocumentDbOutputDataSourceArgsDict,
                    ],
                    Union[
                        EventHubOutputDataSourceArgs, EventHubOutputDataSourceArgsDict
                    ],
                    Union[
                        EventHubV2OutputDataSourceArgs,
                        EventHubV2OutputDataSourceArgsDict,
                    ],
                    Union[
                        GatewayMessageBusOutputDataSourceArgs,
                        GatewayMessageBusOutputDataSourceArgsDict,
                    ],
                    Union[PowerBIOutputDataSourceArgs, PowerBIOutputDataSourceArgsDict],
                    Union[
                        ServiceBusQueueOutputDataSourceArgs,
                        ServiceBusQueueOutputDataSourceArgsDict,
                    ],
                    Union[
                        ServiceBusTopicOutputDataSourceArgs,
                        ServiceBusTopicOutputDataSourceArgsDict,
                    ],
                ]
            ]
        ] = ...,
        job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        serialization: Optional[
            pulumi.Input[
                Union[
                    Union[AvroSerializationArgs, AvroSerializationArgsDict],
                    Union[CsvSerializationArgs, CsvSerializationArgsDict],
                    Union[JsonSerializationArgs, JsonSerializationArgsDict],
                    Union[ParquetSerializationArgs, ParquetSerializationArgsDict],
                ]
            ]
        ] = ...,
        size_window: Optional[pulumi.Input[_builtins.int]] = ...,
        time_window: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OutputInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Output: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def datasource(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> pulumi.Output[outputs.DiagnosticsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def serialization(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="sizeWindow")
    def size_window(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
