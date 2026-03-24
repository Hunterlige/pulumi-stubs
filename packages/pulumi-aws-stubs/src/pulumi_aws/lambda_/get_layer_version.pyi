import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLayerVersionResult",
    "AwaitableGetLayerVersionResult",
    "get_layer_version",
    "get_layer_version_output",
]

@pulumi.output_type
class GetLayerVersionResult:
    def __init__(
        __self__,
        arn=...,
        code_sha256=...,
        compatible_architecture=...,
        compatible_architectures=...,
        compatible_runtime=...,
        compatible_runtimes=...,
        created_date=...,
        description=...,
        id=...,
        layer_arn=...,
        layer_name=...,
        layer_version_arn=...,
        license_info=...,
        region=...,
        signing_job_arn=...,
        signing_profile_version_arn=...,
        source_code_hash=...,
        source_code_size=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="codeSha256")
    def code_sha256(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="compatibleArchitecture")
    def compatible_architecture(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="compatibleArchitectures")
    def compatible_architectures(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="compatibleRuntime")
    def compatible_runtime(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="compatibleRuntimes")
    def compatible_runtimes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="layerArn")
    def layer_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="layerName")
    def layer_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="layerVersionArn")
    def layer_version_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseInfo")
    def license_info(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
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
    @pulumi.getter
    def version(self) -> _builtins.int: ...

class AwaitableGetLayerVersionResult(GetLayerVersionResult):
    def __await__(self): ...

def get_layer_version(
    compatible_architecture: Optional[_builtins.str] = ...,
    compatible_runtime: Optional[_builtins.str] = ...,
    layer_name: Optional[_builtins.str] = ...,
    layer_version_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    version: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLayerVersionResult: ...
def get_layer_version_output(
    compatible_architecture: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    compatible_runtime: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    layer_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    layer_version_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLayerVersionResult]: ...
