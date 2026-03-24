import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSigningProfileResult",
    "AwaitableGetSigningProfileResult",
    "get_signing_profile",
    "get_signing_profile_output",
]

@pulumi.output_type
class GetSigningProfileResult:
    def __init__(
        __self__,
        arn=...,
        id=...,
        name=...,
        platform_display_name=...,
        platform_id=...,
        region=...,
        revocation_records=...,
        signature_validity_periods=...,
        signing_materials=...,
        signing_parameters=...,
        status=...,
        tags=...,
        version=...,
        version_arn=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="platformDisplayName")
    def platform_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="revocationRecords")
    def revocation_records(
        self,
    ) -> Sequence[outputs.GetSigningProfileRevocationRecordResult]: ...
    @_builtins.property
    @pulumi.getter(name="signatureValidityPeriods")
    def signature_validity_periods(
        self,
    ) -> Sequence[outputs.GetSigningProfileSignatureValidityPeriodResult]: ...
    @_builtins.property
    @pulumi.getter(name="signingMaterials")
    def signing_materials(
        self,
    ) -> Sequence[outputs.GetSigningProfileSigningMaterialResult]: ...
    @_builtins.property
    @pulumi.getter(name="signingParameters")
    def signing_parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionArn")
    def version_arn(self) -> _builtins.str: ...

class AwaitableGetSigningProfileResult(GetSigningProfileResult):
    def __await__(self): ...

def get_signing_profile(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSigningProfileResult: ...
def get_signing_profile_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSigningProfileResult]: ...
