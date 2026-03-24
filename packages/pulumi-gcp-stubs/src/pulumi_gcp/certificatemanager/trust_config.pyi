import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TrustConfigArgs", "TrustConfig"]

@pulumi.input_type
class TrustConfigArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        allowlisted_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigAllowlistedCertificateArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_stores: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowlistedCertificates")
    def allowlisted_certificates(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TrustConfigAllowlistedCertificateArgs]]]
    ]: ...
    @allowlisted_certificates.setter
    def allowlisted_certificates(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigAllowlistedCertificateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trustStores")
    def trust_stores(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreArgs]]]]: ...
    @trust_stores.setter
    def trust_stores(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreArgs]]]
        ],
    ): ...

@pulumi.input_type
class _TrustConfigState:
    def __init__(
        __self__,
        *,
        allowlisted_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigAllowlistedCertificateArgs]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        trust_stores: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreArgs]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowlistedCertificates")
    def allowlisted_certificates(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TrustConfigAllowlistedCertificateArgs]]]
    ]: ...
    @allowlisted_certificates.setter
    def allowlisted_certificates(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigAllowlistedCertificateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustStores")
    def trust_stores(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreArgs]]]]: ...
    @trust_stores.setter
    def trust_stores(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:certificatemanager/trustConfig:TrustConfig")
class TrustConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allowlisted_certificates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TrustConfigAllowlistedCertificateArgs,
                            TrustConfigAllowlistedCertificateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_stores: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TrustConfigTrustStoreArgs, TrustConfigTrustStoreArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TrustConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allowlisted_certificates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TrustConfigAllowlistedCertificateArgs,
                            TrustConfigAllowlistedCertificateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        trust_stores: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TrustConfigTrustStoreArgs, TrustConfigTrustStoreArgsDict]
                    ]
                ]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> TrustConfig: ...
    @_builtins.property
    @pulumi.getter(name="allowlistedCertificates")
    def allowlisted_certificates(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.TrustConfigAllowlistedCertificate]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trustStores")
    def trust_stores(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TrustConfigTrustStore]]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
