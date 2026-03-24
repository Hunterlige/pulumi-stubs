import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeyvaluestoreKeysExclusiveArgs", "KeyvaluestoreKeysExclusive"]

@pulumi.input_type
class KeyvaluestoreKeysExclusiveArgs:
    def __init__(
        __self__,
        *,
        key_value_store_arn: pulumi.Input[_builtins.str],
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_key_value_pairs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyValueStoreArn")
    def key_value_store_arn(self) -> pulumi.Input[_builtins.str]: ...
    @key_value_store_arn.setter
    def key_value_store_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_batch_size.setter
    def max_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceKeyValuePairs")
    def resource_key_value_pairs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs]]
        ]
    ]: ...
    @resource_key_value_pairs.setter
    def resource_key_value_pairs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs]
                ]
            ]
        ],
    ): ...

@pulumi.input_type
class _KeyvaluestoreKeysExclusiveState:
    def __init__(
        __self__,
        *,
        key_value_store_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_key_value_pairs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs]
                ]
            ]
        ] = ...,
        total_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyValueStoreArn")
    def key_value_store_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_value_store_arn.setter
    def key_value_store_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_batch_size.setter
    def max_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceKeyValuePairs")
    def resource_key_value_pairs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs]]
        ]
    ]: ...
    @resource_key_value_pairs.setter
    def resource_key_value_pairs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="totalSizeInBytes")
    def total_size_in_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_size_in_bytes.setter
    def total_size_in_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class KeyvaluestoreKeysExclusive(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        key_value_store_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_key_value_pairs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs,
                            KeyvaluestoreKeysExclusiveResourceKeyValuePairArgsDict,
                        ]
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
        args: KeyvaluestoreKeysExclusiveArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        key_value_store_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_key_value_pairs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs,
                            KeyvaluestoreKeysExclusiveResourceKeyValuePairArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        total_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> KeyvaluestoreKeysExclusive: ...
    @_builtins.property
    @pulumi.getter(name="keyValueStoreArn")
    def key_value_store_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="resourceKeyValuePairs")
    def resource_key_value_pairs(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.KeyvaluestoreKeysExclusiveResourceKeyValuePair]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="totalSizeInBytes")
    def total_size_in_bytes(self) -> pulumi.Output[_builtins.int]: ...
