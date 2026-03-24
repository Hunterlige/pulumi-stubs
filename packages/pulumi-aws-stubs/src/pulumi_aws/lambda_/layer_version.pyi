

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LayerVersionArgs', 'LayerVersion']
@pulumi.input_type
class LayerVersionArgs:
    def __init__(__self__, *, layer_name: pulumi.Input[_builtins.str], code: Optional[pulumi.Input[pulumi.Archive]] = ..., compatible_architectures: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., compatible_runtimes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., license_info: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_object_version: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., source_code_hash: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="layerName")
    def layer_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @layer_name.setter
    def layer_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[pulumi.Archive]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[pulumi.Archive]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compatibleArchitectures")
    def compatible_architectures(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @compatible_architectures.setter
    def compatible_architectures(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compatibleRuntimes")
    def compatible_runtimes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @compatible_runtimes.setter
    def compatible_runtimes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseInfo")
    def license_info(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_info.setter
    def license_info(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="sourceCodeHash")
    def source_code_hash(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_code_hash.setter
    def source_code_hash(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _LayerVersionState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., code: Optional[pulumi.Input[pulumi.Archive]] = ..., code_sha256: Optional[pulumi.Input[_builtins.str]] = ..., compatible_architectures: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., compatible_runtimes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., created_date: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., layer_arn: Optional[pulumi.Input[_builtins.str]] = ..., layer_name: Optional[pulumi.Input[_builtins.str]] = ..., license_info: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_object_version: Optional[pulumi.Input[_builtins.str]] = ..., signing_job_arn: Optional[pulumi.Input[_builtins.str]] = ..., signing_profile_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., source_code_hash: Optional[pulumi.Input[_builtins.str]] = ..., source_code_size: Optional[pulumi.Input[_builtins.int]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="compatibleArchitectures")
    def compatible_architectures(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @compatible_architectures.setter
    def compatible_architectures(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compatibleRuntimes")
    def compatible_runtimes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @compatible_runtimes.setter
    def compatible_runtimes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="layerArn")
    def layer_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @layer_arn.setter
    def layer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="layerName")
    def layer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @layer_name.setter
    def layer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseInfo")
    def license_info(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_info.setter
    def license_info(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:lambda/layerVersion:LayerVersion")
class LayerVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., code: Optional[pulumi.Input[pulumi.Archive]] = ..., compatible_architectures: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., compatible_runtimes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., layer_name: Optional[pulumi.Input[_builtins.str]] = ..., license_info: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_object_version: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., source_code_hash: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LayerVersionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., code: Optional[pulumi.Input[pulumi.Archive]] = ..., code_sha256: Optional[pulumi.Input[_builtins.str]] = ..., compatible_architectures: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., compatible_runtimes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., created_date: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., layer_arn: Optional[pulumi.Input[_builtins.str]] = ..., layer_name: Optional[pulumi.Input[_builtins.str]] = ..., license_info: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_key: Optional[pulumi.Input[_builtins.str]] = ..., s3_object_version: Optional[pulumi.Input[_builtins.str]] = ..., signing_job_arn: Optional[pulumi.Input[_builtins.str]] = ..., signing_profile_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., source_code_hash: Optional[pulumi.Input[_builtins.str]] = ..., source_code_size: Optional[pulumi.Input[_builtins.int]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> LayerVersion:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="compatibleArchitectures")
    def compatible_architectures(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compatibleRuntimes")
    def compatible_runtimes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="layerArn")
    def layer_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="layerName")
    def layer_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseInfo")
    def license_info(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="sourceCodeHash")
    def source_code_hash(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCodeSize")
    def source_code_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


