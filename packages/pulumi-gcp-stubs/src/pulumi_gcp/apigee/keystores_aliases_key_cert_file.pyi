import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeystoresAliasesKeyCertFileArgs", "KeystoresAliasesKeyCertFile"]

@pulumi.input_type
class KeystoresAliasesKeyCertFileArgs:
    def __init__(
        __self__,
        *,
        alias: pulumi.Input[_builtins.str],
        cert: pulumi.Input[_builtins.str],
        environment: pulumi.Input[_builtins.str],
        keystore: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[KeystoresAliasesKeyCertFileTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Input[_builtins.str]: ...
    @alias.setter
    def alias(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> pulumi.Input[_builtins.str]: ...
    @cert.setter
    def cert(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Input[_builtins.str]: ...
    @environment.setter
    def environment(self, value: pulumi.Input[_builtins.str]): ...
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
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[KeystoresAliasesKeyCertFileTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[KeystoresAliasesKeyCertFileTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _KeystoresAliasesKeyCertFileState:
    def __init__(
        __self__,
        *,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        cert: Optional[pulumi.Input[_builtins.str]] = ...,
        certs_infos: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KeystoresAliasesKeyCertFileCertsInfoArgs]]
            ]
        ] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[KeystoresAliasesKeyCertFileTimeoutsArgs]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certsInfos")
    def certs_infos(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesKeyCertFileCertsInfoArgs]]]
    ]: ...
    @certs_infos.setter
    def certs_infos(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KeystoresAliasesKeyCertFileCertsInfoArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[KeystoresAliasesKeyCertFileTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[KeystoresAliasesKeyCertFileTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class KeystoresAliasesKeyCertFile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        cert: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    KeystoresAliasesKeyCertFileTimeoutsArgs,
                    KeystoresAliasesKeyCertFileTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KeystoresAliasesKeyCertFileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        cert: Optional[pulumi.Input[_builtins.str]] = ...,
        certs_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KeystoresAliasesKeyCertFileCertsInfoArgs,
                            KeystoresAliasesKeyCertFileCertsInfoArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    KeystoresAliasesKeyCertFileTimeoutsArgs,
                    KeystoresAliasesKeyCertFileTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> KeystoresAliasesKeyCertFile: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certsInfos")
    def certs_infos(
        self,
    ) -> pulumi.Output[Sequence[outputs.KeystoresAliasesKeyCertFileCertsInfo]]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def keystore(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.KeystoresAliasesKeyCertFileTimeouts]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
