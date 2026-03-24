import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeystoresAliasesPkcs12Args", "KeystoresAliasesPkcs12"]

@pulumi.input_type
class KeystoresAliasesPkcs12Args:
    def __init__(
        __self__,
        *,
        alias: pulumi.Input[_builtins.str],
        environment: pulumi.Input[_builtins.str],
        file: pulumi.Input[_builtins.str],
        filehash: pulumi.Input[_builtins.str],
        keystore: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        password: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Input[_builtins.str]: ...
    @alias.setter
    def alias(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Input[_builtins.str]: ...
    @environment.setter
    def environment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> pulumi.Input[_builtins.str]: ...
    @file.setter
    def file(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filehash(self) -> pulumi.Input[_builtins.str]: ...
    @filehash.setter
    def filehash(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def keystore(self) -> pulumi.Input[_builtins.str]: ...
    @keystore.setter
    def keystore(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _KeystoresAliasesPkcs12State:
    def __init__(
        __self__,
        *,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        certs_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesPkcs12CertsInfoArgs]]]
        ] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        file: Optional[pulumi.Input[_builtins.str]] = ...,
        filehash: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certsInfos")
    def certs_infos(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesPkcs12CertsInfoArgs]]]
    ]: ...
    @certs_infos.setter
    def certs_infos(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesPkcs12CertsInfoArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file.setter
    def file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filehash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filehash.setter
    def filehash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def keystore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keystore.setter
    def keystore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class KeystoresAliasesPkcs12(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        file: Optional[pulumi.Input[_builtins.str]] = ...,
        filehash: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KeystoresAliasesPkcs12Args,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        certs_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KeystoresAliasesPkcs12CertsInfoArgs,
                            KeystoresAliasesPkcs12CertsInfoArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        file: Optional[pulumi.Input[_builtins.str]] = ...,
        filehash: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> KeystoresAliasesPkcs12: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certsInfos")
    def certs_infos(
        self,
    ) -> pulumi.Output[Sequence[outputs.KeystoresAliasesPkcs12CertsInfo]]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filehash(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def keystore(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
