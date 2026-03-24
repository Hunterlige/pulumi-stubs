

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FunctionArgs', 'Function']
@pulumi.input_type
class FunctionArgs:
    def __init__(__self__, *, role: pulumi.Input[_builtins.str], architectures: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., capacity_provider_config: Optional[pulumi.Input[FunctionCapacityProviderConfigArgs]] = ..., code: Optional[pulumi.Input[pulumi.Archive]] = ..., code_sha256: Optional[pulumi.Input[_builtins.str]] = ..., code_signing_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., dead_letter_config: Optional[pulumi.Input[FunctionDeadLetterConfigArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., durable_config: Optional[pulumi.Input[FunctionDurableConfigArgs]] = ..., environment: Optional[pulumi.Input[FunctionEnvironmentArgs]] = ..., ephemeral_storage: Optional[pulumi.Input[FunctionEphemeralStorageArgs]] = ..., file_system_config: Optional[pulumi.Input[FunctionFileSystemConfigArgs]] = ..., handler: Optional[pulumi.Input[_builtins.str]] = ..., image_config: Optional[pulumi.Input[FunctionImageConfigArgs]] = ..., image_uri: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., layers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., logging_config: Optional[pulumi.Input[FunctionLoggingConfigArgs]] = ..., memory_size: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., package_type: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., publish_to: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_security_groups_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., replacement_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reserved_concurrent_executions: Optional[pulumi.Input[_builtins.int]] = ..., runtime: Optional[pulumi.Input[Union[_builtins.str, Runtime]]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_object_version: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., snap_start: Optional[pulumi.Input[FunctionSnapStartArgs]] = ..., source_code_hash: Optional[pulumi.Input[_builtins.str]] = ..., source_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy_config: Optional[pulumi.Input[FunctionTenancyConfigArgs]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ..., tracing_config: Optional[pulumi.Input[FunctionTracingConfigArgs]] = ..., vpc_config: Optional[pulumi.Input[FunctionVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def architectures(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @architectures.setter
    def architectures(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderConfig")
    def capacity_provider_config(self) -> Optional[pulumi.Input[FunctionCapacityProviderConfigArgs]]:
        
        ...
    
    @capacity_provider_config.setter
    def capacity_provider_config(self, value: Optional[pulumi.Input[FunctionCapacityProviderConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[pulumi.Archive]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[pulumi.Archive]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeSha256")
    def code_sha256(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code_sha256.setter
    def code_sha256(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeSigningConfigArn")
    def code_signing_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code_signing_config_arn.setter
    def code_signing_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> Optional[pulumi.Input[FunctionDeadLetterConfigArgs]]:
        
        ...
    
    @dead_letter_config.setter
    def dead_letter_config(self, value: Optional[pulumi.Input[FunctionDeadLetterConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="durableConfig")
    def durable_config(self) -> Optional[pulumi.Input[FunctionDurableConfigArgs]]:
        
        ...
    
    @durable_config.setter
    def durable_config(self, value: Optional[pulumi.Input[FunctionDurableConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[FunctionEnvironmentArgs]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[FunctionEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> Optional[pulumi.Input[FunctionEphemeralStorageArgs]]:
        
        ...
    
    @ephemeral_storage.setter
    def ephemeral_storage(self, value: Optional[pulumi.Input[FunctionEphemeralStorageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemConfig")
    def file_system_config(self) -> Optional[pulumi.Input[FunctionFileSystemConfigArgs]]:
        
        ...
    
    @file_system_config.setter
    def file_system_config(self, value: Optional[pulumi.Input[FunctionFileSystemConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def handler(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @handler.setter
    def handler(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageConfig")
    def image_config(self) -> Optional[pulumi.Input[FunctionImageConfigArgs]]:
        
        ...
    
    @image_config.setter
    def image_config(self, value: Optional[pulumi.Input[FunctionImageConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def layers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @layers.setter
    def layers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[FunctionLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[FunctionLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @memory_size.setter
    def memory_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_type.setter
    def package_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publish(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publish.setter
    def publish(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishTo")
    def publish_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publish_to.setter
    def publish_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceSecurityGroupsOnDestroy")
    def replace_security_groups_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replace_security_groups_on_destroy.setter
    def replace_security_groups_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementSecurityGroupIds")
    def replacement_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @replacement_security_group_ids.setter
    def replacement_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @reserved_concurrent_executions.setter
    def reserved_concurrent_executions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[Union[_builtins.str, Runtime]]]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[Union[_builtins.str, Runtime]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket.setter
    def s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_key.setter
    def s3_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ObjectVersion")
    def s3_object_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_object_version.setter
    def s3_object_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapStart")
    def snap_start(self) -> Optional[pulumi.Input[FunctionSnapStartArgs]]:
        
        ...
    
    @snap_start.setter
    def snap_start(self, value: Optional[pulumi.Input[FunctionSnapStartArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCodeHash")
    def source_code_hash(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_code_hash.setter
    def source_code_hash(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceKmsKeyArn")
    def source_kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_kms_key_arn.setter
    def source_kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenancyConfig")
    def tenancy_config(self) -> Optional[pulumi.Input[FunctionTenancyConfigArgs]]:
        
        ...
    
    @tenancy_config.setter
    def tenancy_config(self, value: Optional[pulumi.Input[FunctionTenancyConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tracingConfig")
    def tracing_config(self) -> Optional[pulumi.Input[FunctionTracingConfigArgs]]:
        
        ...
    
    @tracing_config.setter
    def tracing_config(self, value: Optional[pulumi.Input[FunctionTracingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[FunctionVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[FunctionVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _FunctionState:
    def __init__(__self__, *, architectures: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity_provider_config: Optional[pulumi.Input[FunctionCapacityProviderConfigArgs]] = ..., code: Optional[pulumi.Input[pulumi.Archive]] = ..., code_sha256: Optional[pulumi.Input[_builtins.str]] = ..., code_signing_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., dead_letter_config: Optional[pulumi.Input[FunctionDeadLetterConfigArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., durable_config: Optional[pulumi.Input[FunctionDurableConfigArgs]] = ..., environment: Optional[pulumi.Input[FunctionEnvironmentArgs]] = ..., ephemeral_storage: Optional[pulumi.Input[FunctionEphemeralStorageArgs]] = ..., file_system_config: Optional[pulumi.Input[FunctionFileSystemConfigArgs]] = ..., handler: Optional[pulumi.Input[_builtins.str]] = ..., image_config: Optional[pulumi.Input[FunctionImageConfigArgs]] = ..., image_uri: Optional[pulumi.Input[_builtins.str]] = ..., invoke_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., last_modified: Optional[pulumi.Input[_builtins.str]] = ..., layers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., logging_config: Optional[pulumi.Input[FunctionLoggingConfigArgs]] = ..., memory_size: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., package_type: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., publish_to: Optional[pulumi.Input[_builtins.str]] = ..., qualified_arn: Optional[pulumi.Input[_builtins.str]] = ..., qualified_invoke_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_security_groups_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., replacement_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reserved_concurrent_executions: Optional[pulumi.Input[_builtins.int]] = ..., response_streaming_invoke_arn: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., runtime: Optional[pulumi.Input[Union[_builtins.str, Runtime]]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_object_version: Optional[pulumi.Input[_builtins.str]] = ..., signing_job_arn: Optional[pulumi.Input[_builtins.str]] = ..., signing_profile_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., snap_start: Optional[pulumi.Input[FunctionSnapStartArgs]] = ..., source_code_hash: Optional[pulumi.Input[_builtins.str]] = ..., source_code_size: Optional[pulumi.Input[_builtins.int]] = ..., source_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy_config: Optional[pulumi.Input[FunctionTenancyConfigArgs]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ..., tracing_config: Optional[pulumi.Input[FunctionTracingConfigArgs]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[FunctionVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def architectures(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @architectures.setter
    def architectures(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderConfig")
    def capacity_provider_config(self) -> Optional[pulumi.Input[FunctionCapacityProviderConfigArgs]]:
        
        ...
    
    @capacity_provider_config.setter
    def capacity_provider_config(self, value: Optional[pulumi.Input[FunctionCapacityProviderConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[pulumi.Archive]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[pulumi.Archive]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeSha256")
    def code_sha256(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code_sha256.setter
    def code_sha256(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeSigningConfigArn")
    def code_signing_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code_signing_config_arn.setter
    def code_signing_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> Optional[pulumi.Input[FunctionDeadLetterConfigArgs]]:
        
        ...
    
    @dead_letter_config.setter
    def dead_letter_config(self, value: Optional[pulumi.Input[FunctionDeadLetterConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="durableConfig")
    def durable_config(self) -> Optional[pulumi.Input[FunctionDurableConfigArgs]]:
        
        ...
    
    @durable_config.setter
    def durable_config(self, value: Optional[pulumi.Input[FunctionDurableConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[FunctionEnvironmentArgs]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[FunctionEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> Optional[pulumi.Input[FunctionEphemeralStorageArgs]]:
        
        ...
    
    @ephemeral_storage.setter
    def ephemeral_storage(self, value: Optional[pulumi.Input[FunctionEphemeralStorageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemConfig")
    def file_system_config(self) -> Optional[pulumi.Input[FunctionFileSystemConfigArgs]]:
        
        ...
    
    @file_system_config.setter
    def file_system_config(self, value: Optional[pulumi.Input[FunctionFileSystemConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def handler(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @handler.setter
    def handler(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageConfig")
    def image_config(self) -> Optional[pulumi.Input[FunctionImageConfigArgs]]:
        
        ...
    
    @image_config.setter
    def image_config(self, value: Optional[pulumi.Input[FunctionImageConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeArn")
    def invoke_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @invoke_arn.setter
    def invoke_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def layers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @layers.setter
    def layers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[FunctionLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[FunctionLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @memory_size.setter
    def memory_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_type.setter
    def package_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publish(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publish.setter
    def publish(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishTo")
    def publish_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publish_to.setter
    def publish_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="qualifiedArn")
    def qualified_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qualified_arn.setter
    def qualified_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="qualifiedInvokeArn")
    def qualified_invoke_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qualified_invoke_arn.setter
    def qualified_invoke_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceSecurityGroupsOnDestroy")
    def replace_security_groups_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replace_security_groups_on_destroy.setter
    def replace_security_groups_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementSecurityGroupIds")
    def replacement_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @replacement_security_group_ids.setter
    def replacement_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @reserved_concurrent_executions.setter
    def reserved_concurrent_executions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseStreamingInvokeArn")
    def response_streaming_invoke_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_streaming_invoke_arn.setter
    def response_streaming_invoke_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[Union[_builtins.str, Runtime]]]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[Union[_builtins.str, Runtime]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket.setter
    def s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_key.setter
    def s3_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ObjectVersion")
    def s3_object_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_object_version.setter
    def s3_object_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingJobArn")
    def signing_job_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @signing_job_arn.setter
    def signing_job_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingProfileVersionArn")
    def signing_profile_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @signing_profile_version_arn.setter
    def signing_profile_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapStart")
    def snap_start(self) -> Optional[pulumi.Input[FunctionSnapStartArgs]]:
        
        ...
    
    @snap_start.setter
    def snap_start(self, value: Optional[pulumi.Input[FunctionSnapStartArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCodeHash")
    def source_code_hash(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_code_hash.setter
    def source_code_hash(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCodeSize")
    def source_code_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @source_code_size.setter
    def source_code_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceKmsKeyArn")
    def source_kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_kms_key_arn.setter
    def source_kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenancyConfig")
    def tenancy_config(self) -> Optional[pulumi.Input[FunctionTenancyConfigArgs]]:
        
        ...
    
    @tenancy_config.setter
    def tenancy_config(self, value: Optional[pulumi.Input[FunctionTenancyConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tracingConfig")
    def tracing_config(self) -> Optional[pulumi.Input[FunctionTracingConfigArgs]]:
        
        ...
    
    @tracing_config.setter
    def tracing_config(self, value: Optional[pulumi.Input[FunctionTracingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[FunctionVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[FunctionVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:lambda/function:Function")
class Function(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., architectures: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., capacity_provider_config: Optional[pulumi.Input[Union[FunctionCapacityProviderConfigArgs, FunctionCapacityProviderConfigArgsDict]]] = ..., code: Optional[pulumi.Input[pulumi.Archive]] = ..., code_sha256: Optional[pulumi.Input[_builtins.str]] = ..., code_signing_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., dead_letter_config: Optional[pulumi.Input[Union[FunctionDeadLetterConfigArgs, FunctionDeadLetterConfigArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., durable_config: Optional[pulumi.Input[Union[FunctionDurableConfigArgs, FunctionDurableConfigArgsDict]]] = ..., environment: Optional[pulumi.Input[Union[FunctionEnvironmentArgs, FunctionEnvironmentArgsDict]]] = ..., ephemeral_storage: Optional[pulumi.Input[Union[FunctionEphemeralStorageArgs, FunctionEphemeralStorageArgsDict]]] = ..., file_system_config: Optional[pulumi.Input[Union[FunctionFileSystemConfigArgs, FunctionFileSystemConfigArgsDict]]] = ..., handler: Optional[pulumi.Input[_builtins.str]] = ..., image_config: Optional[pulumi.Input[Union[FunctionImageConfigArgs, FunctionImageConfigArgsDict]]] = ..., image_uri: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., layers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., logging_config: Optional[pulumi.Input[Union[FunctionLoggingConfigArgs, FunctionLoggingConfigArgsDict]]] = ..., memory_size: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., package_type: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., publish_to: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_security_groups_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., replacement_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reserved_concurrent_executions: Optional[pulumi.Input[_builtins.int]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., runtime: Optional[pulumi.Input[Union[_builtins.str, Runtime]]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_object_version: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., snap_start: Optional[pulumi.Input[Union[FunctionSnapStartArgs, FunctionSnapStartArgsDict]]] = ..., source_code_hash: Optional[pulumi.Input[_builtins.str]] = ..., source_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy_config: Optional[pulumi.Input[Union[FunctionTenancyConfigArgs, FunctionTenancyConfigArgsDict]]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ..., tracing_config: Optional[pulumi.Input[Union[FunctionTracingConfigArgs, FunctionTracingConfigArgsDict]]] = ..., vpc_config: Optional[pulumi.Input[Union[FunctionVpcConfigArgs, FunctionVpcConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FunctionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., architectures: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity_provider_config: Optional[pulumi.Input[Union[FunctionCapacityProviderConfigArgs, FunctionCapacityProviderConfigArgsDict]]] = ..., code: Optional[pulumi.Input[pulumi.Archive]] = ..., code_sha256: Optional[pulumi.Input[_builtins.str]] = ..., code_signing_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., dead_letter_config: Optional[pulumi.Input[Union[FunctionDeadLetterConfigArgs, FunctionDeadLetterConfigArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., durable_config: Optional[pulumi.Input[Union[FunctionDurableConfigArgs, FunctionDurableConfigArgsDict]]] = ..., environment: Optional[pulumi.Input[Union[FunctionEnvironmentArgs, FunctionEnvironmentArgsDict]]] = ..., ephemeral_storage: Optional[pulumi.Input[Union[FunctionEphemeralStorageArgs, FunctionEphemeralStorageArgsDict]]] = ..., file_system_config: Optional[pulumi.Input[Union[FunctionFileSystemConfigArgs, FunctionFileSystemConfigArgsDict]]] = ..., handler: Optional[pulumi.Input[_builtins.str]] = ..., image_config: Optional[pulumi.Input[Union[FunctionImageConfigArgs, FunctionImageConfigArgsDict]]] = ..., image_uri: Optional[pulumi.Input[_builtins.str]] = ..., invoke_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., last_modified: Optional[pulumi.Input[_builtins.str]] = ..., layers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., logging_config: Optional[pulumi.Input[Union[FunctionLoggingConfigArgs, FunctionLoggingConfigArgsDict]]] = ..., memory_size: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., package_type: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., publish_to: Optional[pulumi.Input[_builtins.str]] = ..., qualified_arn: Optional[pulumi.Input[_builtins.str]] = ..., qualified_invoke_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_security_groups_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., replacement_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reserved_concurrent_executions: Optional[pulumi.Input[_builtins.int]] = ..., response_streaming_invoke_arn: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., runtime: Optional[pulumi.Input[Union[_builtins.str, Runtime]]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_object_version: Optional[pulumi.Input[_builtins.str]] = ..., signing_job_arn: Optional[pulumi.Input[_builtins.str]] = ..., signing_profile_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., snap_start: Optional[pulumi.Input[Union[FunctionSnapStartArgs, FunctionSnapStartArgsDict]]] = ..., source_code_hash: Optional[pulumi.Input[_builtins.str]] = ..., source_code_size: Optional[pulumi.Input[_builtins.int]] = ..., source_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy_config: Optional[pulumi.Input[Union[FunctionTenancyConfigArgs, FunctionTenancyConfigArgsDict]]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ..., tracing_config: Optional[pulumi.Input[Union[FunctionTracingConfigArgs, FunctionTracingConfigArgsDict]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[Union[FunctionVpcConfigArgs, FunctionVpcConfigArgsDict]]] = ...) -> Function:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def architectures(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderConfig")
    def capacity_provider_config(self) -> pulumi.Output[Optional[outputs.FunctionCapacityProviderConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Output[Optional[pulumi.Archive]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeSha256")
    def code_sha256(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeSigningConfigArn")
    def code_signing_config_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> pulumi.Output[Optional[outputs.FunctionDeadLetterConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durableConfig")
    def durable_config(self) -> pulumi.Output[Optional[outputs.FunctionDurableConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Output[Optional[outputs.FunctionEnvironment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> pulumi.Output[outputs.FunctionEphemeralStorage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemConfig")
    def file_system_config(self) -> pulumi.Output[Optional[outputs.FunctionFileSystemConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def handler(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageConfig")
    def image_config(self) -> pulumi.Output[Optional[outputs.FunctionImageConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeArn")
    def invoke_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def layers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[outputs.FunctionLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publish(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishTo")
    def publish_to(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qualifiedArn")
    def qualified_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qualifiedInvokeArn")
    def qualified_invoke_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceSecurityGroupsOnDestroy")
    def replace_security_groups_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementSecurityGroupIds")
    def replacement_security_group_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseStreamingInvokeArn")
    def response_streaming_invoke_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ObjectVersion")
    def s3_object_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingJobArn")
    def signing_job_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingProfileVersionArn")
    def signing_profile_version_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapStart")
    def snap_start(self) -> pulumi.Output[Optional[outputs.FunctionSnapStart]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCodeHash")
    def source_code_hash(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCodeSize")
    def source_code_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceKmsKeyArn")
    def source_kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenancyConfig")
    def tenancy_config(self) -> pulumi.Output[Optional[outputs.FunctionTenancyConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tracingConfig")
    def tracing_config(self) -> pulumi.Output[outputs.FunctionTracingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[Optional[outputs.FunctionVpcConfig]]:
        
        ...
    


