import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppServiceCertificateOrderArgs", "AppServiceCertificateOrder"]

@pulumi.input_type
class AppServiceCertificateOrderArgs:
    def __init__(
        __self__,
        *,
        product_type: pulumi.Input[CertificateProductType],
        resource_group_name: pulumi.Input[_builtins.str],
        auto_renew: Optional[pulumi.Input[_builtins.bool]] = ...,
        certificate_order_name: Optional[pulumi.Input[_builtins.str]] = ...,
        certificates: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[AppServiceCertificateArgs]]]
        ] = ...,
        csr: Optional[pulumi.Input[_builtins.str]] = ...,
        distinguished_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        validity_in_years: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="productType")
    def product_type(self) -> pulumi.Input[CertificateProductType]: ...
    @product_type.setter
    def product_type(self, value: pulumi.Input[CertificateProductType]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateOrderName")
    def certificate_order_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_order_name.setter
    def certificate_order_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[AppServiceCertificateArgs]]]
    ]: ...
    @certificates.setter
    def certificates(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[AppServiceCertificateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def csr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csr.setter
    def csr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="distinguishedName")
    def distinguished_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distinguished_name.setter
    def distinguished_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keySize")
    def key_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @key_size.setter
    def key_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validityInYears")
    def validity_in_years(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @validity_in_years.setter
    def validity_in_years(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class AppServiceCertificateOrder(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_renew: Optional[pulumi.Input[_builtins.bool]] = ...,
        certificate_order_name: Optional[pulumi.Input[_builtins.str]] = ...,
        certificates: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[AppServiceCertificateArgs, AppServiceCertificateArgsDict]
                    ],
                ]
            ]
        ] = ...,
        csr: Optional[pulumi.Input[_builtins.str]] = ...,
        distinguished_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        product_type: Optional[pulumi.Input[CertificateProductType]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        validity_in_years: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppServiceCertificateOrderArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AppServiceCertificateOrder: ...
    @_builtins.property
    @pulumi.getter(name="appServiceCertificateNotRenewableReasons")
    def app_service_certificate_not_renewable_reasons(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> pulumi.Output[
        Optional[Mapping[str, outputs.AppServiceCertificateResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def contact(self) -> pulumi.Output[outputs.CertificateOrderContactResponse]: ...
    @_builtins.property
    @pulumi.getter
    def csr(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="distinguishedName")
    def distinguished_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainVerificationToken")
    def domain_verification_token(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def intermediate(self) -> pulumi.Output[outputs.CertificateDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="isPrivateKeyExternal")
    def is_private_key_external(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keySize")
    def key_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastCertificateIssuanceTime")
    def last_certificate_issuance_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextAutoRenewalTimeStamp")
    def next_auto_renewal_time_stamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productType")
    def product_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def root(self) -> pulumi.Output[outputs.CertificateDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signedCertificate")
    def signed_certificate(
        self,
    ) -> pulumi.Output[outputs.CertificateDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validityInYears")
    def validity_in_years(self) -> pulumi.Output[Optional[_builtins.int]]: ...
