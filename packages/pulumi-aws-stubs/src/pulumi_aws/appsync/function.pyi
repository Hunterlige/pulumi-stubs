import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FunctionArgs", "Function"]

@pulumi.input_type
class FunctionArgs:
    def __init__(
        __self__,
        *,
        api_id: pulumi.Input[_builtins.str],
        data_source: pulumi.Input[_builtins.str],
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        function_version: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_mapping_template: Optional[pulumi.Input[_builtins.str]] = ...,
        response_mapping_template: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[pulumi.Input[FunctionRuntimeArgs]] = ...,
        sync_config: Optional[pulumi.Input[FunctionSyncConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]: ...
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]: ...
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="functionVersion")
    def function_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function_version.setter
    def function_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_batch_size.setter
    def max_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="requestMappingTemplate")
    def request_mapping_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_mapping_template.setter
    def request_mapping_template(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="responseMappingTemplate")
    def response_mapping_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response_mapping_template.setter
    def response_mapping_template(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[FunctionRuntimeArgs]]: ...
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[FunctionRuntimeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="syncConfig")
    def sync_config(self) -> Optional[pulumi.Input[FunctionSyncConfigArgs]]: ...
    @sync_config.setter
    def sync_config(self, value: Optional[pulumi.Input[FunctionSyncConfigArgs]]): ...

@pulumi.input_type
class _FunctionState:
    def __init__(
        __self__,
        *,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        function_id: Optional[pulumi.Input[_builtins.str]] = ...,
        function_version: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_mapping_template: Optional[pulumi.Input[_builtins.str]] = ...,
        response_mapping_template: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[pulumi.Input[FunctionRuntimeArgs]] = ...,
        sync_config: Optional[pulumi.Input[FunctionSyncConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="functionId")
    def function_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function_id.setter
    def function_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="functionVersion")
    def function_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function_version.setter
    def function_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_batch_size.setter
    def max_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="requestMappingTemplate")
    def request_mapping_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_mapping_template.setter
    def request_mapping_template(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="responseMappingTemplate")
    def response_mapping_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response_mapping_template.setter
    def response_mapping_template(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[FunctionRuntimeArgs]]: ...
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[FunctionRuntimeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="syncConfig")
    def sync_config(self) -> Optional[pulumi.Input[FunctionSyncConfigArgs]]: ...
    @sync_config.setter
    def sync_config(self, value: Optional[pulumi.Input[FunctionSyncConfigArgs]]): ...

@pulumi.type_token("aws:appsync/function:Function")
class Function(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        function_version: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_mapping_template: Optional[pulumi.Input[_builtins.str]] = ...,
        response_mapping_template: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[
            pulumi.Input[Union[FunctionRuntimeArgs, FunctionRuntimeArgsDict]]
        ] = ...,
        sync_config: Optional[
            pulumi.Input[Union[FunctionSyncConfigArgs, FunctionSyncConfigArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FunctionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        function_id: Optional[pulumi.Input[_builtins.str]] = ...,
        function_version: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_mapping_template: Optional[pulumi.Input[_builtins.str]] = ...,
        response_mapping_template: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[
            pulumi.Input[Union[FunctionRuntimeArgs, FunctionRuntimeArgsDict]]
        ] = ...,
        sync_config: Optional[
            pulumi.Input[Union[FunctionSyncConfigArgs, FunctionSyncConfigArgsDict]]
        ] = ...,
    ) -> Function: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="functionId")
    def function_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="functionVersion")
    def function_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestMappingTemplate")
    def request_mapping_template(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="responseMappingTemplate")
    def response_mapping_template(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Output[Optional[outputs.FunctionRuntime]]: ...
    @_builtins.property
    @pulumi.getter(name="syncConfig")
    def sync_config(self) -> pulumi.Output[Optional[outputs.FunctionSyncConfig]]: ...
