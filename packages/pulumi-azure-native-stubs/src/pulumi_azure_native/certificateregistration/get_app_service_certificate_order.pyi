import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAppServiceCertificateOrderResult",
    "AwaitableGetAppServiceCertificateOrderResult",
    "get_app_service_certificate_order",
    "get_app_service_certificate_order_output",
]

@pulumi.output_type
class GetAppServiceCertificateOrderResult:
    def __init__(
        __self__,
        app_service_certificate_not_renewable_reasons=...,
        auto_renew=...,
        azure_api_version=...,
        certificates=...,
        contact=...,
        csr=...,
        distinguished_name=...,
        domain_verification_token=...,
        expiration_time=...,
        id=...,
        intermediate=...,
        is_private_key_external=...,
        key_size=...,
        kind=...,
        last_certificate_issuance_time=...,
        location=...,
        name=...,
        next_auto_renewal_time_stamp=...,
        product_type=...,
        provisioning_state=...,
        root=...,
        serial_number=...,
        signed_certificate=...,
        status=...,
        tags=...,
        type=...,
        validity_in_years=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appServiceCertificateNotRenewableReasons")
    def app_service_certificate_not_renewable_reasons(
        self,
    ) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Optional[Mapping[str, outputs.AppServiceCertificateResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def contact(self) -> outputs.CertificateOrderContactResponse: ...
    @_builtins.property
    @pulumi.getter
    def csr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="distinguishedName")
    def distinguished_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainVerificationToken")
    def domain_verification_token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def intermediate(self) -> outputs.CertificateDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="isPrivateKeyExternal")
    def is_private_key_external(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="keySize")
    def key_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastCertificateIssuanceTime")
    def last_certificate_issuance_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextAutoRenewalTimeStamp")
    def next_auto_renewal_time_stamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productType")
    def product_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def root(self) -> outputs.CertificateDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signedCertificate")
    def signed_certificate(self) -> outputs.CertificateDetailsResponse: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validityInYears")
    def validity_in_years(self) -> Optional[_builtins.int]: ...

class AwaitableGetAppServiceCertificateOrderResult(GetAppServiceCertificateOrderResult):
    def __await__(self): ...

def get_app_service_certificate_order(
    certificate_order_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAppServiceCertificateOrderResult: ...
def get_app_service_certificate_order_output(
    certificate_order_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAppServiceCertificateOrderResult]: ...
