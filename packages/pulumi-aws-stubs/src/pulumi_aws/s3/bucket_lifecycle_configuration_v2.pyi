import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BucketLifecycleConfigurationV2Args", "BucketLifecycleConfigurationV2"]

@pulumi.input_type
class BucketLifecycleConfigurationV2Args:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleArgs]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[BucketLifecycleConfigurationV2TimeoutsArgs]
        ] = ...,
        transition_default_minimum_object_size: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
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
        pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleArgs]]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[BucketLifecycleConfigurationV2TimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[BucketLifecycleConfigurationV2TimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitionDefaultMinimumObjectSize")
    def transition_default_minimum_object_size(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transition_default_minimum_object_size.setter
    def transition_default_minimum_object_size(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _BucketLifecycleConfigurationV2State:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleArgs]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[BucketLifecycleConfigurationV2TimeoutsArgs]
        ] = ...,
        transition_default_minimum_object_size: Optional[
            pulumi.Input[_builtins.str]
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
        pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleArgs]]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[BucketLifecycleConfigurationV2TimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[BucketLifecycleConfigurationV2TimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitionDefaultMinimumObjectSize")
    def transition_default_minimum_object_size(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transition_default_minimum_object_size.setter
    def transition_default_minimum_object_size(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class BucketLifecycleConfigurationV2(pulumi.CustomResource):
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
                            BucketLifecycleConfigurationV2RuleArgs,
                            BucketLifecycleConfigurationV2RuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    BucketLifecycleConfigurationV2TimeoutsArgs,
                    BucketLifecycleConfigurationV2TimeoutsArgsDict,
                ]
            ]
        ] = ...,
        transition_default_minimum_object_size: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BucketLifecycleConfigurationV2Args,
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
                            BucketLifecycleConfigurationV2RuleArgs,
                            BucketLifecycleConfigurationV2RuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    BucketLifecycleConfigurationV2TimeoutsArgs,
                    BucketLifecycleConfigurationV2TimeoutsArgsDict,
                ]
            ]
        ] = ...,
        transition_default_minimum_object_size: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> BucketLifecycleConfigurationV2: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    @_utilities.deprecated(...)
    def expected_bucket_owner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.BucketLifecycleConfigurationV2Rule]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.BucketLifecycleConfigurationV2Timeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="transitionDefaultMinimumObjectSize")
    def transition_default_minimum_object_size(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
