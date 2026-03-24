import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ResolverArgs", "Resolver"]

@pulumi.input_type
class ResolverArgs:
    def __init__(
        __self__,
        *,
        api_id: pulumi.Input[_builtins.str],
        field: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        caching_config: Optional[pulumi.Input[ResolverCachingConfigArgs]] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        pipeline_config: Optional[pulumi.Input[ResolverPipelineConfigArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_template: Optional[pulumi.Input[_builtins.str]] = ...,
        response_template: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[pulumi.Input[ResolverRuntimeArgs]] = ...,
        sync_config: Optional[pulumi.Input[ResolverSyncConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]: ...
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Input[_builtins.str]: ...
    @field.setter
    def field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cachingConfig")
    def caching_config(self) -> Optional[pulumi.Input[ResolverCachingConfigArgs]]: ...
    @caching_config.setter
    def caching_config(
        self, value: Optional[pulumi.Input[ResolverCachingConfigArgs]]
    ): ...
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
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_batch_size.setter
    def max_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineConfig")
    def pipeline_config(self) -> Optional[pulumi.Input[ResolverPipelineConfigArgs]]: ...
    @pipeline_config.setter
    def pipeline_config(
        self, value: Optional[pulumi.Input[ResolverPipelineConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestTemplate")
    def request_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_template.setter
    def request_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseTemplate")
    def response_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response_template.setter
    def response_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[ResolverRuntimeArgs]]: ...
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[ResolverRuntimeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="syncConfig")
    def sync_config(self) -> Optional[pulumi.Input[ResolverSyncConfigArgs]]: ...
    @sync_config.setter
    def sync_config(self, value: Optional[pulumi.Input[ResolverSyncConfigArgs]]): ...

@pulumi.input_type
class _ResolverState:
    def __init__(
        __self__,
        *,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        caching_config: Optional[pulumi.Input[ResolverCachingConfigArgs]] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
        field: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        pipeline_config: Optional[pulumi.Input[ResolverPipelineConfigArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_template: Optional[pulumi.Input[_builtins.str]] = ...,
        response_template: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[pulumi.Input[ResolverRuntimeArgs]] = ...,
        sync_config: Optional[pulumi.Input[ResolverSyncConfigArgs]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="cachingConfig")
    def caching_config(self) -> Optional[pulumi.Input[ResolverCachingConfigArgs]]: ...
    @caching_config.setter
    def caching_config(
        self, value: Optional[pulumi.Input[ResolverCachingConfigArgs]]
    ): ...
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
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_batch_size.setter
    def max_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineConfig")
    def pipeline_config(self) -> Optional[pulumi.Input[ResolverPipelineConfigArgs]]: ...
    @pipeline_config.setter
    def pipeline_config(
        self, value: Optional[pulumi.Input[ResolverPipelineConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestTemplate")
    def request_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_template.setter
    def request_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseTemplate")
    def response_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response_template.setter
    def response_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[ResolverRuntimeArgs]]: ...
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[ResolverRuntimeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="syncConfig")
    def sync_config(self) -> Optional[pulumi.Input[ResolverSyncConfigArgs]]: ...
    @sync_config.setter
    def sync_config(self, value: Optional[pulumi.Input[ResolverSyncConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:appsync/resolver:Resolver")
class Resolver(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        caching_config: Optional[
            pulumi.Input[
                Union[ResolverCachingConfigArgs, ResolverCachingConfigArgsDict]
            ]
        ] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
        field: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        pipeline_config: Optional[
            pulumi.Input[
                Union[ResolverPipelineConfigArgs, ResolverPipelineConfigArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_template: Optional[pulumi.Input[_builtins.str]] = ...,
        response_template: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[
            pulumi.Input[Union[ResolverRuntimeArgs, ResolverRuntimeArgsDict]]
        ] = ...,
        sync_config: Optional[
            pulumi.Input[Union[ResolverSyncConfigArgs, ResolverSyncConfigArgsDict]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ResolverArgs,
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
        caching_config: Optional[
            pulumi.Input[
                Union[ResolverCachingConfigArgs, ResolverCachingConfigArgsDict]
            ]
        ] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
        field: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        pipeline_config: Optional[
            pulumi.Input[
                Union[ResolverPipelineConfigArgs, ResolverPipelineConfigArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_template: Optional[pulumi.Input[_builtins.str]] = ...,
        response_template: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime: Optional[
            pulumi.Input[Union[ResolverRuntimeArgs, ResolverRuntimeArgsDict]]
        ] = ...,
        sync_config: Optional[
            pulumi.Input[Union[ResolverSyncConfigArgs, ResolverSyncConfigArgsDict]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Resolver: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cachingConfig")
    def caching_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ResolverCachingConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="pipelineConfig")
    def pipeline_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ResolverPipelineConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestTemplate")
    def request_template(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="responseTemplate")
    def response_template(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Output[Optional[outputs.ResolverRuntime]]: ...
    @_builtins.property
    @pulumi.getter(name="syncConfig")
    def sync_config(self) -> pulumi.Output[Optional[outputs.ResolverSyncConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
