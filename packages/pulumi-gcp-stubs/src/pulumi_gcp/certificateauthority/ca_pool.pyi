import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CaPoolArgs", "CaPool"]

@pulumi.input_type
class CaPoolArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        tier: pulumi.Input[_builtins.str],
        encryption_spec: Optional[pulumi.Input[CaPoolEncryptionSpecArgs]] = ...,
        issuance_policy: Optional[pulumi.Input[CaPoolIssuancePolicyArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        publishing_options: Optional[pulumi.Input[CaPoolPublishingOptionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[_builtins.str]: ...
    @tier.setter
    def tier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> Optional[pulumi.Input[CaPoolEncryptionSpecArgs]]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: Optional[pulumi.Input[CaPoolEncryptionSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="issuancePolicy")
    def issuance_policy(self) -> Optional[pulumi.Input[CaPoolIssuancePolicyArgs]]: ...
    @issuance_policy.setter
    def issuance_policy(
        self, value: Optional[pulumi.Input[CaPoolIssuancePolicyArgs]]
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publishingOptions")
    def publishing_options(
        self,
    ) -> Optional[pulumi.Input[CaPoolPublishingOptionsArgs]]: ...
    @publishing_options.setter
    def publishing_options(
        self, value: Optional[pulumi.Input[CaPoolPublishingOptionsArgs]]
    ): ...

@pulumi.input_type
class _CaPoolState:
    def __init__(
        __self__,
        *,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_spec: Optional[pulumi.Input[CaPoolEncryptionSpecArgs]] = ...,
        issuance_policy: Optional[pulumi.Input[CaPoolIssuancePolicyArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        publishing_options: Optional[pulumi.Input[CaPoolPublishingOptionsArgs]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> Optional[pulumi.Input[CaPoolEncryptionSpecArgs]]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: Optional[pulumi.Input[CaPoolEncryptionSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="issuancePolicy")
    def issuance_policy(self) -> Optional[pulumi.Input[CaPoolIssuancePolicyArgs]]: ...
    @issuance_policy.setter
    def issuance_policy(
        self, value: Optional[pulumi.Input[CaPoolIssuancePolicyArgs]]
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
    @pulumi.getter(name="publishingOptions")
    def publishing_options(
        self,
    ) -> Optional[pulumi.Input[CaPoolPublishingOptionsArgs]]: ...
    @publishing_options.setter
    def publishing_options(
        self, value: Optional[pulumi.Input[CaPoolPublishingOptionsArgs]]
    ): ...
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
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:certificateauthority/caPool:CaPool")
class CaPool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        encryption_spec: Optional[
            pulumi.Input[Union[CaPoolEncryptionSpecArgs, CaPoolEncryptionSpecArgsDict]]
        ] = ...,
        issuance_policy: Optional[
            pulumi.Input[Union[CaPoolIssuancePolicyArgs, CaPoolIssuancePolicyArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        publishing_options: Optional[
            pulumi.Input[
                Union[CaPoolPublishingOptionsArgs, CaPoolPublishingOptionsArgsDict]
            ]
        ] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CaPoolArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_spec: Optional[
            pulumi.Input[Union[CaPoolEncryptionSpecArgs, CaPoolEncryptionSpecArgsDict]]
        ] = ...,
        issuance_policy: Optional[
            pulumi.Input[Union[CaPoolIssuancePolicyArgs, CaPoolIssuancePolicyArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        publishing_options: Optional[
            pulumi.Input[
                Union[CaPoolPublishingOptionsArgs, CaPoolPublishingOptionsArgsDict]
            ]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CaPool: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> pulumi.Output[Optional[outputs.CaPoolEncryptionSpec]]: ...
    @_builtins.property
    @pulumi.getter(name="issuancePolicy")
    def issuance_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.CaPoolIssuancePolicy]]: ...
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
    @pulumi.getter(name="publishingOptions")
    def publishing_options(
        self,
    ) -> pulumi.Output[Optional[outputs.CaPoolPublishingOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Output[_builtins.str]: ...
