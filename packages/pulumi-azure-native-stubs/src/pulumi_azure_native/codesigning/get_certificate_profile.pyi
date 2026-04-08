import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCertificateProfileResult",
    "AwaitableGetCertificateProfileResult",
    "get_certificate_profile",
    "get_certificate_profile_output",
]

@pulumi.output_type
class GetCertificateProfileResult:
    def __init__(
        __self__,
        azure_api_version=...,
        certificates=...,
        id=...,
        identity_validation_id=...,
        include_city=...,
        include_country=...,
        include_postal_code=...,
        include_state=...,
        include_street_address=...,
        name=...,
        profile_type=...,
        provisioning_state=...,
        status=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Sequence[outputs.CertificateResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityValidationId")
    def identity_validation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeCity")
    def include_city(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="includeCountry")
    def include_country(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="includePostalCode")
    def include_postal_code(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="includeState")
    def include_state(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="includeStreetAddress")
    def include_street_address(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="profileType")
    def profile_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetCertificateProfileResult(GetCertificateProfileResult):
    def __await__(self): ...

def get_certificate_profile(
    account_name: Optional[_builtins.str] = ...,
    profile_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCertificateProfileResult: ...
def get_certificate_profile_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCertificateProfileResult]: ...
