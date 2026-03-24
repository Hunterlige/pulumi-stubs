import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFunctionResult",
    "AwaitableGetFunctionResult",
    "get_function",
    "get_function_output",
]

@pulumi.output_type
class GetFunctionResult:
    def __init__(
        __self__,
        architectures=...,
        arn=...,
        capacity_provider_configs=...,
        code_sha256=...,
        code_signing_config_arn=...,
        dead_letter_config=...,
        description=...,
        durable_configs=...,
        environment=...,
        ephemeral_storages=...,
        file_system_configs=...,
        function_name=...,
        handler=...,
        id=...,
        image_uri=...,
        invoke_arn=...,
        kms_key_arn=...,
        last_modified=...,
        layers=...,
        logging_configs=...,
        memory_size=...,
        qualified_arn=...,
        qualified_invoke_arn=...,
        qualifier=...,
        region=...,
        reserved_concurrent_executions=...,
        response_streaming_invoke_arn=...,
        role=...,
        runtime=...,
        signing_job_arn=...,
        signing_profile_version_arn=...,
        source_code_hash=...,
        source_code_size=...,
        source_kms_key_arn=...,
        tags=...,
        tenancy_configs=...,
        timeout=...,
        tracing_config=...,
        version=...,
        vpc_config=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def architectures(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderConfigs")
    def capacity_provider_configs(
        self,
    ) -> Sequence[outputs.GetFunctionCapacityProviderConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="codeSha256")
    def code_sha256(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="codeSigningConfigArn")
    def code_signing_config_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> outputs.GetFunctionDeadLetterConfigResult: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="durableConfigs")
    def durable_configs(self) -> Sequence[outputs.GetFunctionDurableConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> outputs.GetFunctionEnvironmentResult: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorages")
    def ephemeral_storages(
        self,
    ) -> Sequence[outputs.GetFunctionEphemeralStorageResult]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemConfigs")
    def file_system_configs(
        self,
    ) -> Sequence[outputs.GetFunctionFileSystemConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def handler(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invokeArn")
    def invoke_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def layers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfigs")
    def logging_configs(self) -> Sequence[outputs.GetFunctionLoggingConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="qualifiedArn")
    def qualified_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="qualifiedInvokeArn")
    def qualified_invoke_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="responseStreamingInvokeArn")
    def response_streaming_invoke_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signingJobArn")
    def signing_job_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signingProfileVersionArn")
    def signing_profile_version_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceCodeHash")
    @_utilities.deprecated(...)
    def source_code_hash(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceCodeSize")
    def source_code_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sourceKmsKeyArn")
    def source_kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenancyConfigs")
    def tenancy_configs(self) -> Sequence[outputs.GetFunctionTenancyConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="tracingConfig")
    def tracing_config(self) -> outputs.GetFunctionTracingConfigResult: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> outputs.GetFunctionVpcConfigResult: ...

class AwaitableGetFunctionResult(GetFunctionResult):
    def __await__(self): ...

def get_function(
    function_name: Optional[_builtins.str] = ...,
    qualifier: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFunctionResult: ...
def get_function_output(
    function_name: Optional[pulumi.Input[_builtins.str]] = ...,
    qualifier: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFunctionResult]: ...
