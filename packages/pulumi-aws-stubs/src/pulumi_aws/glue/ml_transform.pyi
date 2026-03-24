import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MLTransformArgs", "MLTransform"]

@pulumi.input_type
class MLTransformArgs:
    def __init__(
        __self__,
        *,
        input_record_tables: pulumi.Input[
            Sequence[pulumi.Input[MLTransformInputRecordTableArgs]]
        ],
        parameters: pulumi.Input[MLTransformParametersArgs],
        role_arn: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        glue_version: Optional[pulumi.Input[_builtins.str]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputRecordTables")
    def input_record_tables(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[MLTransformInputRecordTableArgs]]]: ...
    @input_record_tables.setter
    def input_record_tables(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[MLTransformInputRecordTableArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[MLTransformParametersArgs]: ...
    @parameters.setter
    def parameters(self, value: pulumi.Input[MLTransformParametersArgs]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @glue_version.setter
    def glue_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_type.setter
    def worker_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MLTransformState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        glue_version: Optional[pulumi.Input[_builtins.str]] = ...,
        input_record_tables: Optional[
            pulumi.Input[Sequence[pulumi.Input[MLTransformInputRecordTableArgs]]]
        ] = ...,
        label_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        parameters: Optional[pulumi.Input[MLTransformParametersArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        schemas: Optional[
            pulumi.Input[Sequence[pulumi.Input[MLTransformSchemaArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @glue_version.setter
    def glue_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputRecordTables")
    def input_record_tables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MLTransformInputRecordTableArgs]]]
    ]: ...
    @input_record_tables.setter
    def input_record_tables(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MLTransformInputRecordTableArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="labelCount")
    def label_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @label_count.setter
    def label_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[MLTransformParametersArgs]]: ...
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[MLTransformParametersArgs]]): ...
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
    def schemas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MLTransformSchemaArgs]]]]: ...
    @schemas.setter
    def schemas(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[MLTransformSchemaArgs]]]],
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
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_type.setter
    def worker_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:glue/mLTransform:MLTransform")
class MLTransform(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        glue_version: Optional[pulumi.Input[_builtins.str]] = ...,
        input_record_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MLTransformInputRecordTableArgs,
                            MLTransformInputRecordTableArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        parameters: Optional[
            pulumi.Input[
                Union[MLTransformParametersArgs, MLTransformParametersArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MLTransformArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        glue_version: Optional[pulumi.Input[_builtins.str]] = ...,
        input_record_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MLTransformInputRecordTableArgs,
                            MLTransformInputRecordTableArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        label_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        parameters: Optional[
            pulumi.Input[
                Union[MLTransformParametersArgs, MLTransformParametersArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        schemas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[MLTransformSchemaArgs, MLTransformSchemaArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> MLTransform: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputRecordTables")
    def input_record_tables(
        self,
    ) -> pulumi.Output[Sequence[outputs.MLTransformInputRecordTable]]: ...
    @_builtins.property
    @pulumi.getter(name="labelCount")
    def label_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[outputs.MLTransformParameters]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> pulumi.Output[Sequence[outputs.MLTransformSchema]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
