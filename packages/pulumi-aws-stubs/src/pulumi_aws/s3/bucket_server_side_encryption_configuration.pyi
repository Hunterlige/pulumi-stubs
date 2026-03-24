import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BucketServerSideEncryptionConfigurationInitArgs",
    "BucketServerSideEncryptionConfiguration",
]

@pulumi.input_type
class BucketServerSideEncryptionConfigurationInitArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        rules: pulumi.Input[
            Sequence[pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgs]]
        ],
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgs]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _BucketServerSideEncryptionConfigurationState:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgs]]
        ]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgs]]
            ]
        ],
    ): ...

@pulumi.type_token(...)
class BucketServerSideEncryptionConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketServerSideEncryptionConfigurationRuleArgs,
                            BucketServerSideEncryptionConfigurationRuleArgsDict,
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
        args: BucketServerSideEncryptionConfigurationInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BucketServerSideEncryptionConfigurationRuleArgs,
                            BucketServerSideEncryptionConfigurationRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> BucketServerSideEncryptionConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.BucketServerSideEncryptionConfigurationRule]
    ]: ...
