import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CryptoKeyVersionArgs", "CryptoKeyVersion"]

@pulumi.input_type
class CryptoKeyVersionArgs:
    def __init__(
        __self__,
        *,
        crypto_key: pulumi.Input[_builtins.str],
        external_protection_level_options: Optional[
            pulumi.Input[CryptoKeyVersionExternalProtectionLevelOptionsArgs]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key.setter
    def crypto_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="externalProtectionLevelOptions")
    def external_protection_level_options(
        self,
    ) -> Optional[pulumi.Input[CryptoKeyVersionExternalProtectionLevelOptionsArgs]]: ...
    @external_protection_level_options.setter
    def external_protection_level_options(
        self,
        value: Optional[
            pulumi.Input[CryptoKeyVersionExternalProtectionLevelOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CryptoKeyVersionState:
    def __init__(
        __self__,
        *,
        algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        attestations: Optional[
            pulumi.Input[Sequence[pulumi.Input[CryptoKeyVersionAttestationArgs]]]
        ] = ...,
        crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
        external_protection_level_options: Optional[
            pulumi.Input[CryptoKeyVersionExternalProtectionLevelOptionsArgs]
        ] = ...,
        generate_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_level: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def attestations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CryptoKeyVersionAttestationArgs]]]
    ]: ...
    @attestations.setter
    def attestations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CryptoKeyVersionAttestationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @crypto_key.setter
    def crypto_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalProtectionLevelOptions")
    def external_protection_level_options(
        self,
    ) -> Optional[pulumi.Input[CryptoKeyVersionExternalProtectionLevelOptionsArgs]]: ...
    @external_protection_level_options.setter
    def external_protection_level_options(
        self,
        value: Optional[
            pulumi.Input[CryptoKeyVersionExternalProtectionLevelOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="generateTime")
    def generate_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generate_time.setter
    def generate_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_level.setter
    def protection_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:kms/cryptoKeyVersion:CryptoKeyVersion")
class CryptoKeyVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
        external_protection_level_options: Optional[
            pulumi.Input[
                Union[
                    CryptoKeyVersionExternalProtectionLevelOptionsArgs,
                    CryptoKeyVersionExternalProtectionLevelOptionsArgsDict,
                ]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CryptoKeyVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        attestations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CryptoKeyVersionAttestationArgs,
                            CryptoKeyVersionAttestationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
        external_protection_level_options: Optional[
            pulumi.Input[
                Union[
                    CryptoKeyVersionExternalProtectionLevelOptionsArgs,
                    CryptoKeyVersionExternalProtectionLevelOptionsArgsDict,
                ]
            ]
        ] = ...,
        generate_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_level: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CryptoKeyVersion: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def attestations(
        self,
    ) -> pulumi.Output[Sequence[outputs.CryptoKeyVersionAttestation]]: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalProtectionLevelOptions")
    def external_protection_level_options(
        self,
    ) -> pulumi.Output[
        Optional[outputs.CryptoKeyVersionExternalProtectionLevelOptions]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="generateTime")
    def generate_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
