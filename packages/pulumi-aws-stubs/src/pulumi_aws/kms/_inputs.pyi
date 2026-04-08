import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CustomKeyStoreXksProxyAuthenticationCredentialArgs",
    ...,
    "GrantConstraintArgs",
    "GrantConstraintArgsDict",
    "GetSecretSecretArgs",
    "GetSecretSecretArgsDict",
    "GetSecretsSecretArgs",
    "GetSecretsSecretArgsDict",
]

class CustomKeyStoreXksProxyAuthenticationCredentialArgsDict(TypedDict):
    access_key_id: pulumi.Input[_builtins.str]
    raw_secret_access_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class CustomKeyStoreXksProxyAuthenticationCredentialArgs:
    def __init__(
        __self__,
        *,
        access_key_id: pulumi.Input[_builtins.str],
        raw_secret_access_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> pulumi.Input[_builtins.str]: ...
    @access_key_id.setter
    def access_key_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rawSecretAccessKey")
    def raw_secret_access_key(self) -> pulumi.Input[_builtins.str]: ...
    @raw_secret_access_key.setter
    def raw_secret_access_key(self, value: pulumi.Input[_builtins.str]): ...

class GrantConstraintArgsDict(TypedDict):
    encryption_context_equals: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    encryption_context_subset: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class GrantConstraintArgs:
    def __init__(
        __self__,
        *,
        encryption_context_equals: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_context_subset: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionContextEquals")
    def encryption_context_equals(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @encryption_context_equals.setter
    def encryption_context_equals(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionContextSubset")
    def encryption_context_subset(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @encryption_context_subset.setter
    def encryption_context_subset(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class GetSecretSecretArgsDict(TypedDict):
    name: _builtins.str
    payload: _builtins.str
    context: NotRequired[Mapping[str, _builtins.str]]
    grant_tokens: NotRequired[Sequence[_builtins.str]]

@pulumi.input_type
class GetSecretSecretArgs:
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        payload: _builtins.str,
        context: Optional[Mapping[str, _builtins.str]] = ...,
        grant_tokens: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> _builtins.str: ...
    @payload.setter
    def payload(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @context.setter
    def context(self, value: Optional[Mapping[str, _builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantTokens")
    def grant_tokens(self) -> Optional[Sequence[_builtins.str]]: ...
    @grant_tokens.setter
    def grant_tokens(self, value: Optional[Sequence[_builtins.str]]): ...

class GetSecretsSecretArgsDict(TypedDict):
    name: _builtins.str
    payload: _builtins.str
    context: NotRequired[Mapping[str, _builtins.str]]
    encryption_algorithm: NotRequired[_builtins.str]
    grant_tokens: NotRequired[Sequence[_builtins.str]]
    key_id: NotRequired[_builtins.str]

@pulumi.input_type
class GetSecretsSecretArgs:
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        payload: _builtins.str,
        context: Optional[Mapping[str, _builtins.str]] = ...,
        encryption_algorithm: Optional[_builtins.str] = ...,
        grant_tokens: Optional[Sequence[_builtins.str]] = ...,
        key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> _builtins.str: ...
    @payload.setter
    def payload(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @context.setter
    def context(self, value: Optional[Mapping[str, _builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> Optional[_builtins.str]: ...
    @encryption_algorithm.setter
    def encryption_algorithm(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="grantTokens")
    def grant_tokens(self) -> Optional[Sequence[_builtins.str]]: ...
    @grant_tokens.setter
    def grant_tokens(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]: ...
    @key_id.setter
    def key_id(self, value: Optional[_builtins.str]): ...
