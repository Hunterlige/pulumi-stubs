import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TrustStoreArgs", "TrustStore"]

@pulumi.input_type
class TrustStoreArgs:
    def __init__(
        __self__,
        *,
        ca_certificates_bundle_source: pulumi.Input[
            TrustStoreCaCertificatesBundleSourceArgs
        ],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[TrustStoreTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleSource")
    def ca_certificates_bundle_source(
        self,
    ) -> pulumi.Input[TrustStoreCaCertificatesBundleSourceArgs]: ...
    @ca_certificates_bundle_source.setter
    def ca_certificates_bundle_source(
        self, value: pulumi.Input[TrustStoreCaCertificatesBundleSourceArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[TrustStoreTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[TrustStoreTimeoutsArgs]]): ...

@pulumi.input_type
class _TrustStoreState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_source: Optional[
            pulumi.Input[TrustStoreCaCertificatesBundleSourceArgs]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_ca_certificates: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[TrustStoreTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleSource")
    def ca_certificates_bundle_source(
        self,
    ) -> Optional[pulumi.Input[TrustStoreCaCertificatesBundleSourceArgs]]: ...
    @ca_certificates_bundle_source.setter
    def ca_certificates_bundle_source(
        self, value: Optional[pulumi.Input[TrustStoreCaCertificatesBundleSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfCaCertificates")
    def number_of_ca_certificates(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_ca_certificates.setter
    def number_of_ca_certificates(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[TrustStoreTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[TrustStoreTimeoutsArgs]]): ...

@pulumi.type_token("aws:cloudfront/trustStore:TrustStore")
class TrustStore(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ca_certificates_bundle_source: Optional[
            pulumi.Input[
                Union[
                    TrustStoreCaCertificatesBundleSourceArgs,
                    TrustStoreCaCertificatesBundleSourceArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[TrustStoreTimeoutsArgs, TrustStoreTimeoutsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TrustStoreArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_source: Optional[
            pulumi.Input[
                Union[
                    TrustStoreCaCertificatesBundleSourceArgs,
                    TrustStoreCaCertificatesBundleSourceArgsDict,
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_ca_certificates: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[TrustStoreTimeoutsArgs, TrustStoreTimeoutsArgsDict]]
        ] = ...,
    ) -> TrustStore: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleSource")
    def ca_certificates_bundle_source(
        self,
    ) -> pulumi.Output[outputs.TrustStoreCaCertificatesBundleSource]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfCaCertificates")
    def number_of_ca_certificates(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.TrustStoreTimeouts]]: ...
