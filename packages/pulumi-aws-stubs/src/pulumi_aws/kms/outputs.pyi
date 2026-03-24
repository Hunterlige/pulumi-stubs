import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CustomKeyStoreXksProxyAuthenticationCredential",
    "GrantConstraint",
    "GetKeyMultiRegionConfigurationResult",
    "GetKeyMultiRegionConfigurationPrimaryKeyResult",
    "GetKeyMultiRegionConfigurationReplicaKeyResult",
    "GetKeyXksKeyConfigurationResult",
    "GetSecretSecretResult",
    "GetSecretsSecretResult",
]

@pulumi.output_type
class CustomKeyStoreXksProxyAuthenticationCredential(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, access_key_id: _builtins.str, raw_secret_access_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rawSecretAccessKey")
    def raw_secret_access_key(self) -> _builtins.str: ...

@pulumi.output_type
class GrantConstraint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_context_equals: Optional[Mapping[str, _builtins.str]] = ...,
        encryption_context_subset: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionContextEquals")
    def encryption_context_equals(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionContextSubset")
    def encryption_context_subset(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class GetKeyMultiRegionConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        multi_region_key_type: _builtins.str,
        primary_keys: Sequence[outputs.GetKeyMultiRegionConfigurationPrimaryKeyResult],
        replica_keys: Sequence[outputs.GetKeyMultiRegionConfigurationReplicaKeyResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="multiRegionKeyType")
    def multi_region_key_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryKeys")
    def primary_keys(
        self,
    ) -> Sequence[outputs.GetKeyMultiRegionConfigurationPrimaryKeyResult]: ...
    @_builtins.property
    @pulumi.getter(name="replicaKeys")
    def replica_keys(
        self,
    ) -> Sequence[outputs.GetKeyMultiRegionConfigurationReplicaKeyResult]: ...

@pulumi.output_type
class GetKeyMultiRegionConfigurationPrimaryKeyResult(dict):
    def __init__(__self__, *, arn: _builtins.str, region: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class GetKeyMultiRegionConfigurationReplicaKeyResult(dict):
    def __init__(__self__, *, arn: _builtins.str, region: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class GetKeyXksKeyConfigurationResult(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class GetSecretSecretResult(dict):
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
    @_builtins.property
    @pulumi.getter
    def payload(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="grantTokens")
    def grant_tokens(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetSecretsSecretResult(dict):
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
    @_builtins.property
    @pulumi.getter
    def payload(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantTokens")
    def grant_tokens(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]: ...
