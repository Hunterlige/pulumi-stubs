import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeyArgs", "Key"]

@pulumi.input_type
class KeyArgs:
    def __init__(
        __self__,
        *,
        service_account_id: pulumi.Input[_builtins.str],
        keepers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        key_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key_data: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @service_account_id.setter
    def service_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def keepers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @keepers.setter
    def keepers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_algorithm.setter
    def key_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKeyType")
    def private_key_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key_type.setter
    def private_key_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKeyData")
    def public_key_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key_data.setter
    def public_key_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKeyType")
    def public_key_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key_type.setter
    def public_key_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _KeyState:
    def __init__(
        __self__,
        *,
        keepers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        key_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key_data: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        valid_after: Optional[pulumi.Input[_builtins.str]] = ...,
        valid_before: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def keepers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @keepers.setter
    def keepers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_algorithm.setter
    def key_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKeyType")
    def private_key_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key_type.setter
    def private_key_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKeyData")
    def public_key_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key_data.setter
    def public_key_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKeyType")
    def public_key_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key_type.setter
    def public_key_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validAfter")
    def valid_after(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @valid_after.setter
    def valid_after(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validBefore")
    def valid_before(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @valid_before.setter
    def valid_before(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:serviceaccount/key:Key")
class Key(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        keepers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        key_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key_data: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KeyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        keepers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        key_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key_data: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        valid_after: Optional[pulumi.Input[_builtins.str]] = ...,
        valid_before: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Key: ...
    @_builtins.property
    @pulumi.getter
    def keepers(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateKeyType")
    def private_key_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicKeyData")
    def public_key_data(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicKeyType")
    def public_key_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validAfter")
    def valid_after(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validBefore")
    def valid_before(self) -> pulumi.Output[_builtins.str]: ...
