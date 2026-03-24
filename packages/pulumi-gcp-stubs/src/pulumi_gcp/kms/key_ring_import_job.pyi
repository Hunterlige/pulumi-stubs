import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeyRingImportJobArgs", "KeyRingImportJob"]

@pulumi.input_type
class KeyRingImportJobArgs:
    def __init__(
        __self__,
        *,
        import_job_id: pulumi.Input[_builtins.str],
        import_method: pulumi.Input[_builtins.str],
        key_ring: pulumi.Input[_builtins.str],
        protection_level: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="importJobId")
    def import_job_id(self) -> pulumi.Input[_builtins.str]: ...
    @import_job_id.setter
    def import_job_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="importMethod")
    def import_method(self) -> pulumi.Input[_builtins.str]: ...
    @import_method.setter
    def import_method(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyRing")
    def key_ring(self) -> pulumi.Input[_builtins.str]: ...
    @key_ring.setter
    def key_ring(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> pulumi.Input[_builtins.str]: ...
    @protection_level.setter
    def protection_level(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _KeyRingImportJobState:
    def __init__(
        __self__,
        *,
        attestations: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeyRingImportJobAttestationArgs]]]
        ] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        import_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        import_method: Optional[pulumi.Input[_builtins.str]] = ...,
        key_ring: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_level: Optional[pulumi.Input[_builtins.str]] = ...,
        public_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeyRingImportJobPublicKeyArgs]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attestations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KeyRingImportJobAttestationArgs]]]
    ]: ...
    @attestations.setter
    def attestations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeyRingImportJobAttestationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="importJobId")
    def import_job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @import_job_id.setter
    def import_job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="importMethod")
    def import_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @import_method.setter
    def import_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyRing")
    def key_ring(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_ring.setter
    def key_ring(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KeyRingImportJobPublicKeyArgs]]]
    ]: ...
    @public_keys.setter
    def public_keys(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeyRingImportJobPublicKeyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:kms/keyRingImportJob:KeyRingImportJob")
class KeyRingImportJob(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        import_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        import_method: Optional[pulumi.Input[_builtins.str]] = ...,
        key_ring: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_level: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KeyRingImportJobArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        attestations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KeyRingImportJobAttestationArgs,
                            KeyRingImportJobAttestationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        import_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        import_method: Optional[pulumi.Input[_builtins.str]] = ...,
        key_ring: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_level: Optional[pulumi.Input[_builtins.str]] = ...,
        public_keys: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KeyRingImportJobPublicKeyArgs,
                            KeyRingImportJobPublicKeyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> KeyRingImportJob: ...
    @_builtins.property
    @pulumi.getter
    def attestations(
        self,
    ) -> pulumi.Output[Sequence[outputs.KeyRingImportJobAttestation]]: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="importJobId")
    def import_job_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="importMethod")
    def import_method(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyRing")
    def key_ring(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> pulumi.Output[Sequence[outputs.KeyRingImportJobPublicKey]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
