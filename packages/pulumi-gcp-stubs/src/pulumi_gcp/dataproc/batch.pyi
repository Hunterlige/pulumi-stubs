import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BatchArgs", "Batch"]

@pulumi.input_type
class BatchArgs:
    def __init__(
        __self__,
        *,
        batch_id: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_config: Optional[pulumi.Input[BatchEnvironmentConfigArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pyspark_batch: Optional[pulumi.Input[BatchPysparkBatchArgs]] = ...,
        runtime_config: Optional[pulumi.Input[BatchRuntimeConfigArgs]] = ...,
        spark_batch: Optional[pulumi.Input[BatchSparkBatchArgs]] = ...,
        spark_r_batch: Optional[pulumi.Input[BatchSparkRBatchArgs]] = ...,
        spark_sql_batch: Optional[pulumi.Input[BatchSparkSqlBatchArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchId")
    def batch_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @batch_id.setter
    def batch_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentConfig")
    def environment_config(
        self,
    ) -> Optional[pulumi.Input[BatchEnvironmentConfigArgs]]: ...
    @environment_config.setter
    def environment_config(
        self, value: Optional[pulumi.Input[BatchEnvironmentConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pysparkBatch")
    def pyspark_batch(self) -> Optional[pulumi.Input[BatchPysparkBatchArgs]]: ...
    @pyspark_batch.setter
    def pyspark_batch(self, value: Optional[pulumi.Input[BatchPysparkBatchArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfig")
    def runtime_config(self) -> Optional[pulumi.Input[BatchRuntimeConfigArgs]]: ...
    @runtime_config.setter
    def runtime_config(self, value: Optional[pulumi.Input[BatchRuntimeConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkBatch")
    def spark_batch(self) -> Optional[pulumi.Input[BatchSparkBatchArgs]]: ...
    @spark_batch.setter
    def spark_batch(self, value: Optional[pulumi.Input[BatchSparkBatchArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkRBatch")
    def spark_r_batch(self) -> Optional[pulumi.Input[BatchSparkRBatchArgs]]: ...
    @spark_r_batch.setter
    def spark_r_batch(self, value: Optional[pulumi.Input[BatchSparkRBatchArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkSqlBatch")
    def spark_sql_batch(self) -> Optional[pulumi.Input[BatchSparkSqlBatchArgs]]: ...
    @spark_sql_batch.setter
    def spark_sql_batch(
        self, value: Optional[pulumi.Input[BatchSparkSqlBatchArgs]]
    ): ...

@pulumi.input_type
class _BatchState:
    def __init__(
        __self__,
        *,
        batch_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        environment_config: Optional[pulumi.Input[BatchEnvironmentConfigArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operation: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pyspark_batch: Optional[pulumi.Input[BatchPysparkBatchArgs]] = ...,
        runtime_config: Optional[pulumi.Input[BatchRuntimeConfigArgs]] = ...,
        runtime_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoArgs]]]
        ] = ...,
        spark_batch: Optional[pulumi.Input[BatchSparkBatchArgs]] = ...,
        spark_r_batch: Optional[pulumi.Input[BatchSparkRBatchArgs]] = ...,
        spark_sql_batch: Optional[pulumi.Input[BatchSparkSqlBatchArgs]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_histories: Optional[
            pulumi.Input[Sequence[pulumi.Input[BatchStateHistoryArgs]]]
        ] = ...,
        state_message: Optional[pulumi.Input[_builtins.str]] = ...,
        state_time: Optional[pulumi.Input[_builtins.str]] = ...,
        uuid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchId")
    def batch_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @batch_id.setter
    def batch_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def creator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creator.setter
    def creator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentConfig")
    def environment_config(
        self,
    ) -> Optional[pulumi.Input[BatchEnvironmentConfigArgs]]: ...
    @environment_config.setter
    def environment_config(
        self, value: Optional[pulumi.Input[BatchEnvironmentConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
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
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation.setter
    def operation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pysparkBatch")
    def pyspark_batch(self) -> Optional[pulumi.Input[BatchPysparkBatchArgs]]: ...
    @pyspark_batch.setter
    def pyspark_batch(self, value: Optional[pulumi.Input[BatchPysparkBatchArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfig")
    def runtime_config(self) -> Optional[pulumi.Input[BatchRuntimeConfigArgs]]: ...
    @runtime_config.setter
    def runtime_config(self, value: Optional[pulumi.Input[BatchRuntimeConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeInfos")
    def runtime_infos(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoArgs]]]]: ...
    @runtime_infos.setter
    def runtime_infos(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkBatch")
    def spark_batch(self) -> Optional[pulumi.Input[BatchSparkBatchArgs]]: ...
    @spark_batch.setter
    def spark_batch(self, value: Optional[pulumi.Input[BatchSparkBatchArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkRBatch")
    def spark_r_batch(self) -> Optional[pulumi.Input[BatchSparkRBatchArgs]]: ...
    @spark_r_batch.setter
    def spark_r_batch(self, value: Optional[pulumi.Input[BatchSparkRBatchArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkSqlBatch")
    def spark_sql_batch(self) -> Optional[pulumi.Input[BatchSparkSqlBatchArgs]]: ...
    @spark_sql_batch.setter
    def spark_sql_batch(
        self, value: Optional[pulumi.Input[BatchSparkSqlBatchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateHistories")
    def state_histories(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BatchStateHistoryArgs]]]]: ...
    @state_histories.setter
    def state_histories(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BatchStateHistoryArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_message.setter
    def state_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateTime")
    def state_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_time.setter
    def state_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:dataproc/batch:Batch")
class Batch(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        batch_id: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_config: Optional[
            pulumi.Input[
                Union[BatchEnvironmentConfigArgs, BatchEnvironmentConfigArgsDict]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pyspark_batch: Optional[
            pulumi.Input[Union[BatchPysparkBatchArgs, BatchPysparkBatchArgsDict]]
        ] = ...,
        runtime_config: Optional[
            pulumi.Input[Union[BatchRuntimeConfigArgs, BatchRuntimeConfigArgsDict]]
        ] = ...,
        spark_batch: Optional[
            pulumi.Input[Union[BatchSparkBatchArgs, BatchSparkBatchArgsDict]]
        ] = ...,
        spark_r_batch: Optional[
            pulumi.Input[Union[BatchSparkRBatchArgs, BatchSparkRBatchArgsDict]]
        ] = ...,
        spark_sql_batch: Optional[
            pulumi.Input[Union[BatchSparkSqlBatchArgs, BatchSparkSqlBatchArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[BatchArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        batch_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        environment_config: Optional[
            pulumi.Input[
                Union[BatchEnvironmentConfigArgs, BatchEnvironmentConfigArgsDict]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operation: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pyspark_batch: Optional[
            pulumi.Input[Union[BatchPysparkBatchArgs, BatchPysparkBatchArgsDict]]
        ] = ...,
        runtime_config: Optional[
            pulumi.Input[Union[BatchRuntimeConfigArgs, BatchRuntimeConfigArgsDict]]
        ] = ...,
        runtime_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[BatchRuntimeInfoArgs, BatchRuntimeInfoArgsDict]]
                ]
            ]
        ] = ...,
        spark_batch: Optional[
            pulumi.Input[Union[BatchSparkBatchArgs, BatchSparkBatchArgsDict]]
        ] = ...,
        spark_r_batch: Optional[
            pulumi.Input[Union[BatchSparkRBatchArgs, BatchSparkRBatchArgsDict]]
        ] = ...,
        spark_sql_batch: Optional[
            pulumi.Input[Union[BatchSparkSqlBatchArgs, BatchSparkSqlBatchArgsDict]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_histories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[BatchStateHistoryArgs, BatchStateHistoryArgsDict]
                    ]
                ]
            ]
        ] = ...,
        state_message: Optional[pulumi.Input[_builtins.str]] = ...,
        state_time: Optional[pulumi.Input[_builtins.str]] = ...,
        uuid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Batch: ...
    @_builtins.property
    @pulumi.getter(name="batchId")
    def batch_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def creator(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="environmentConfig")
    def environment_config(
        self,
    ) -> pulumi.Output[Optional[outputs.BatchEnvironmentConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pysparkBatch")
    def pyspark_batch(self) -> pulumi.Output[Optional[outputs.BatchPysparkBatch]]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfig")
    def runtime_config(self) -> pulumi.Output[Optional[outputs.BatchRuntimeConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeInfos")
    def runtime_infos(self) -> pulumi.Output[Sequence[outputs.BatchRuntimeInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="sparkBatch")
    def spark_batch(self) -> pulumi.Output[Optional[outputs.BatchSparkBatch]]: ...
    @_builtins.property
    @pulumi.getter(name="sparkRBatch")
    def spark_r_batch(self) -> pulumi.Output[Optional[outputs.BatchSparkRBatch]]: ...
    @_builtins.property
    @pulumi.getter(name="sparkSqlBatch")
    def spark_sql_batch(
        self,
    ) -> pulumi.Output[Optional[outputs.BatchSparkSqlBatch]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateHistories")
    def state_histories(self) -> pulumi.Output[Sequence[outputs.BatchStateHistory]]: ...
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateTime")
    def state_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[_builtins.str]: ...
