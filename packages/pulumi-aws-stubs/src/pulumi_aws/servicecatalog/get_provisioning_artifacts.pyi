import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProvisioningArtifactsResult",
    "AwaitableGetProvisioningArtifactsResult",
    "get_provisioning_artifacts",
    "get_provisioning_artifacts_output",
]

@pulumi.output_type
class GetProvisioningArtifactsResult:
    def __init__(
        __self__,
        accept_language=...,
        id=...,
        product_id=...,
        provisioning_artifact_details=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningArtifactDetails")
    def provisioning_artifact_details(
        self,
    ) -> Sequence[outputs.GetProvisioningArtifactsProvisioningArtifactDetailResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetProvisioningArtifactsResult(GetProvisioningArtifactsResult):
    def __await__(self): ...

def get_provisioning_artifacts(
    accept_language: Optional[_builtins.str] = ...,
    product_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProvisioningArtifactsResult: ...
def get_provisioning_artifacts_output(
    accept_language: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    product_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProvisioningArtifactsResult]: ...
