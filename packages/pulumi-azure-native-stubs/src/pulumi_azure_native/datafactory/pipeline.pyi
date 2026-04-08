import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PipelineArgs", "Pipeline"]

@pulumi.input_type
class PipelineArgs:
    def __init__(
        __self__,
        *,
        factory_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        activities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AppendVariableActivityArgs,
                            AzureDataExplorerCommandActivityArgs,
                            AzureFunctionActivityArgs,
                            AzureMLBatchExecutionActivityArgs,
                            AzureMLExecutePipelineActivityArgs,
                            AzureMLUpdateResourceActivityArgs,
                            ControlActivityArgs,
                            CopyActivityArgs,
                            CustomActivityArgs,
                            DataLakeAnalyticsUSQLActivityArgs,
                            DatabricksJobActivityArgs,
                            DatabricksNotebookActivityArgs,
                            DatabricksSparkJarActivityArgs,
                            DatabricksSparkPythonActivityArgs,
                            DeleteActivityArgs,
                            ExecuteDataFlowActivityArgs,
                            ExecutePipelineActivityArgs,
                            ExecuteSSISPackageActivityArgs,
                            ExecuteWranglingDataflowActivityArgs,
                            ExecutionActivityArgs,
                            FailActivityArgs,
                            FilterActivityArgs,
                            ForEachActivityArgs,
                            GetMetadataActivityArgs,
                            HDInsightHiveActivityArgs,
                            HDInsightMapReduceActivityArgs,
                            HDInsightPigActivityArgs,
                            HDInsightSparkActivityArgs,
                            HDInsightStreamingActivityArgs,
                            IfConditionActivityArgs,
                            LookupActivityArgs,
                            ScriptActivityArgs,
                            SetVariableActivityArgs,
                            SqlServerStoredProcedureActivityArgs,
                            SwitchActivityArgs,
                            SynapseNotebookActivityArgs,
                            SynapseSparkJobDefinitionActivityArgs,
                            UntilActivityArgs,
                            ValidationActivityArgs,
                            WaitActivityArgs,
                            WebActivityArgs,
                            WebHookActivityArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        annotations: Optional[pulumi.Input[Sequence[Any]]] = ...,
        concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        folder: Optional[pulumi.Input[PipelineFolderArgs]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterSpecificationArgs]]]
        ] = ...,
        pipeline_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[PipelinePolicyArgs]] = ...,
        run_dimensions: Optional[pulumi.Input[Mapping[str, Any]]] = ...,
        variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[VariableSpecificationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[_builtins.str]: ...
    @factory_name.setter
    def factory_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def activities(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        AppendVariableActivityArgs,
                        AzureDataExplorerCommandActivityArgs,
                        AzureFunctionActivityArgs,
                        AzureMLBatchExecutionActivityArgs,
                        AzureMLExecutePipelineActivityArgs,
                        AzureMLUpdateResourceActivityArgs,
                        ControlActivityArgs,
                        CopyActivityArgs,
                        CustomActivityArgs,
                        DataLakeAnalyticsUSQLActivityArgs,
                        DatabricksJobActivityArgs,
                        DatabricksNotebookActivityArgs,
                        DatabricksSparkJarActivityArgs,
                        DatabricksSparkPythonActivityArgs,
                        DeleteActivityArgs,
                        ExecuteDataFlowActivityArgs,
                        ExecutePipelineActivityArgs,
                        ExecuteSSISPackageActivityArgs,
                        ExecuteWranglingDataflowActivityArgs,
                        ExecutionActivityArgs,
                        FailActivityArgs,
                        FilterActivityArgs,
                        ForEachActivityArgs,
                        GetMetadataActivityArgs,
                        HDInsightHiveActivityArgs,
                        HDInsightMapReduceActivityArgs,
                        HDInsightPigActivityArgs,
                        HDInsightSparkActivityArgs,
                        HDInsightStreamingActivityArgs,
                        IfConditionActivityArgs,
                        LookupActivityArgs,
                        ScriptActivityArgs,
                        SetVariableActivityArgs,
                        SqlServerStoredProcedureActivityArgs,
                        SwitchActivityArgs,
                        SynapseNotebookActivityArgs,
                        SynapseSparkJobDefinitionActivityArgs,
                        UntilActivityArgs,
                        ValidationActivityArgs,
                        WaitActivityArgs,
                        WebActivityArgs,
                        WebHookActivityArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @activities.setter
    def activities(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AppendVariableActivityArgs,
                            AzureDataExplorerCommandActivityArgs,
                            AzureFunctionActivityArgs,
                            AzureMLBatchExecutionActivityArgs,
                            AzureMLExecutePipelineActivityArgs,
                            AzureMLUpdateResourceActivityArgs,
                            ControlActivityArgs,
                            CopyActivityArgs,
                            CustomActivityArgs,
                            DataLakeAnalyticsUSQLActivityArgs,
                            DatabricksJobActivityArgs,
                            DatabricksNotebookActivityArgs,
                            DatabricksSparkJarActivityArgs,
                            DatabricksSparkPythonActivityArgs,
                            DeleteActivityArgs,
                            ExecuteDataFlowActivityArgs,
                            ExecutePipelineActivityArgs,
                            ExecuteSSISPackageActivityArgs,
                            ExecuteWranglingDataflowActivityArgs,
                            ExecutionActivityArgs,
                            FailActivityArgs,
                            FilterActivityArgs,
                            ForEachActivityArgs,
                            GetMetadataActivityArgs,
                            HDInsightHiveActivityArgs,
                            HDInsightMapReduceActivityArgs,
                            HDInsightPigActivityArgs,
                            HDInsightSparkActivityArgs,
                            HDInsightStreamingActivityArgs,
                            IfConditionActivityArgs,
                            LookupActivityArgs,
                            ScriptActivityArgs,
                            SetVariableActivityArgs,
                            SqlServerStoredProcedureActivityArgs,
                            SwitchActivityArgs,
                            SynapseNotebookActivityArgs,
                            SynapseSparkJobDefinitionActivityArgs,
                            UntilActivityArgs,
                            ValidationActivityArgs,
                            WaitActivityArgs,
                            WebActivityArgs,
                            WebHookActivityArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Sequence[Any]]]: ...
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Sequence[Any]]]): ...
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @concurrency.setter
    def concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[PipelineFolderArgs]]: ...
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[PipelineFolderArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ParameterSpecificationArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterSpecificationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pipeline_name.setter
    def pipeline_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[PipelinePolicyArgs]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[PipelinePolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="runDimensions")
    def run_dimensions(self) -> Optional[pulumi.Input[Mapping[str, Any]]]: ...
    @run_dimensions.setter
    def run_dimensions(self, value: Optional[pulumi.Input[Mapping[str, Any]]]): ...
    @_builtins.property
    @pulumi.getter
    def variables(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[VariableSpecificationArgs]]]
    ]: ...
    @variables.setter
    def variables(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[VariableSpecificationArgs]]]
        ],
    ): ...

@pulumi.type_token("azure-native:datafactory:Pipeline")
class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        activities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            Union[
                                AppendVariableActivityArgs,
                                AppendVariableActivityArgsDict,
                            ],
                            Union[
                                AzureDataExplorerCommandActivityArgs,
                                AzureDataExplorerCommandActivityArgsDict,
                            ],
                            Union[
                                AzureFunctionActivityArgs, AzureFunctionActivityArgsDict
                            ],
                            Union[
                                AzureMLBatchExecutionActivityArgs,
                                AzureMLBatchExecutionActivityArgsDict,
                            ],
                            Union[
                                AzureMLExecutePipelineActivityArgs,
                                AzureMLExecutePipelineActivityArgsDict,
                            ],
                            Union[
                                AzureMLUpdateResourceActivityArgs,
                                AzureMLUpdateResourceActivityArgsDict,
                            ],
                            Union[ControlActivityArgs, ControlActivityArgsDict],
                            Union[CopyActivityArgs, CopyActivityArgsDict],
                            Union[CustomActivityArgs, CustomActivityArgsDict],
                            Union[
                                DataLakeAnalyticsUSQLActivityArgs,
                                DataLakeAnalyticsUSQLActivityArgsDict,
                            ],
                            Union[
                                DatabricksJobActivityArgs, DatabricksJobActivityArgsDict
                            ],
                            Union[
                                DatabricksNotebookActivityArgs,
                                DatabricksNotebookActivityArgsDict,
                            ],
                            Union[
                                DatabricksSparkJarActivityArgs,
                                DatabricksSparkJarActivityArgsDict,
                            ],
                            Union[
                                DatabricksSparkPythonActivityArgs,
                                DatabricksSparkPythonActivityArgsDict,
                            ],
                            Union[DeleteActivityArgs, DeleteActivityArgsDict],
                            Union[
                                ExecuteDataFlowActivityArgs,
                                ExecuteDataFlowActivityArgsDict,
                            ],
                            Union[
                                ExecutePipelineActivityArgs,
                                ExecutePipelineActivityArgsDict,
                            ],
                            Union[
                                ExecuteSSISPackageActivityArgs,
                                ExecuteSSISPackageActivityArgsDict,
                            ],
                            Union[
                                ExecuteWranglingDataflowActivityArgs,
                                ExecuteWranglingDataflowActivityArgsDict,
                            ],
                            Union[ExecutionActivityArgs, ExecutionActivityArgsDict],
                            Union[FailActivityArgs, FailActivityArgsDict],
                            Union[FilterActivityArgs, FilterActivityArgsDict],
                            Union[ForEachActivityArgs, ForEachActivityArgsDict],
                            Union[GetMetadataActivityArgs, GetMetadataActivityArgsDict],
                            Union[
                                HDInsightHiveActivityArgs, HDInsightHiveActivityArgsDict
                            ],
                            Union[
                                HDInsightMapReduceActivityArgs,
                                HDInsightMapReduceActivityArgsDict,
                            ],
                            Union[
                                HDInsightPigActivityArgs, HDInsightPigActivityArgsDict
                            ],
                            Union[
                                HDInsightSparkActivityArgs,
                                HDInsightSparkActivityArgsDict,
                            ],
                            Union[
                                HDInsightStreamingActivityArgs,
                                HDInsightStreamingActivityArgsDict,
                            ],
                            Union[IfConditionActivityArgs, IfConditionActivityArgsDict],
                            Union[LookupActivityArgs, LookupActivityArgsDict],
                            Union[ScriptActivityArgs, ScriptActivityArgsDict],
                            Union[SetVariableActivityArgs, SetVariableActivityArgsDict],
                            Union[
                                SqlServerStoredProcedureActivityArgs,
                                SqlServerStoredProcedureActivityArgsDict,
                            ],
                            Union[SwitchActivityArgs, SwitchActivityArgsDict],
                            Union[
                                SynapseNotebookActivityArgs,
                                SynapseNotebookActivityArgsDict,
                            ],
                            Union[
                                SynapseSparkJobDefinitionActivityArgs,
                                SynapseSparkJobDefinitionActivityArgsDict,
                            ],
                            Union[UntilActivityArgs, UntilActivityArgsDict],
                            Union[ValidationActivityArgs, ValidationActivityArgsDict],
                            Union[WaitActivityArgs, WaitActivityArgsDict],
                            Union[WebActivityArgs, WebActivityArgsDict],
                            Union[WebHookActivityArgs, WebHookActivityArgsDict],
                        ]
                    ]
                ]
            ]
        ] = ...,
        annotations: Optional[pulumi.Input[Sequence[Any]]] = ...,
        concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        folder: Optional[
            pulumi.Input[Union[PipelineFolderArgs, PipelineFolderArgsDict]]
        ] = ...,
        parameters: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            ParameterSpecificationArgs, ParameterSpecificationArgsDict
                        ]
                    ],
                ]
            ]
        ] = ...,
        pipeline_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[
            pulumi.Input[Union[PipelinePolicyArgs, PipelinePolicyArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        run_dimensions: Optional[pulumi.Input[Mapping[str, Any]]] = ...,
        variables: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[VariableSpecificationArgs, VariableSpecificationArgsDict]
                    ],
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PipelineArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Pipeline: ...
    @_builtins.property
    @pulumi.getter
    def activities(self) -> pulumi.Output[Optional[Sequence[Any]]]: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Sequence[Any]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Output[Optional[outputs.PipelineResponseFolder]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Output[
        Optional[Mapping[str, outputs.ParameterSpecificationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[outputs.PipelinePolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="runDimensions")
    def run_dimensions(self) -> pulumi.Output[Optional[Mapping[str, Any]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def variables(
        self,
    ) -> pulumi.Output[
        Optional[Mapping[str, outputs.VariableSpecificationResponse]]
    ]: ...
