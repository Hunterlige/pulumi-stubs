import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BillingAccountBucketConfigArgs", "BillingAccountBucketConfig"]

@pulumi.input_type
class BillingAccountBucketConfigArgs:
    def __init__(
        __self__,
        *,
        billing_account: pulumi.Input[_builtins.str],
        bucket_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        cmek_settings: Optional[
            pulumi.Input[BillingAccountBucketConfigCmekSettingsArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        index_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BillingAccountBucketConfigIndexConfigArgs]]
            ]
        ] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Input[_builtins.str]: ...
    @billing_account.setter
    def billing_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_id.setter
    def bucket_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cmekSettings")
    def cmek_settings(
        self,
    ) -> Optional[pulumi.Input[BillingAccountBucketConfigCmekSettingsArgs]]: ...
    @cmek_settings.setter
    def cmek_settings(
        self, value: Optional[pulumi.Input[BillingAccountBucketConfigCmekSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexConfigs")
    def index_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BillingAccountBucketConfigIndexConfigArgs]]]
    ]: ...
    @index_configs.setter
    def index_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BillingAccountBucketConfigIndexConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _BillingAccountBucketConfigState:
    def __init__(
        __self__,
        *,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cmek_settings: Optional[
            pulumi.Input[BillingAccountBucketConfigCmekSettingsArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        index_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BillingAccountBucketConfigIndexConfigArgs]]
            ]
        ] = ...,
        lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_account.setter
    def billing_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_id.setter
    def bucket_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cmekSettings")
    def cmek_settings(
        self,
    ) -> Optional[pulumi.Input[BillingAccountBucketConfigCmekSettingsArgs]]: ...
    @cmek_settings.setter
    def cmek_settings(
        self, value: Optional[pulumi.Input[BillingAccountBucketConfigCmekSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexConfigs")
    def index_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BillingAccountBucketConfigIndexConfigArgs]]]
    ]: ...
    @index_configs.setter
    def index_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BillingAccountBucketConfigIndexConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_state.setter
    def lifecycle_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class BillingAccountBucketConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cmek_settings: Optional[
            pulumi.Input[
                Union[
                    BillingAccountBucketConfigCmekSettingsArgs,
                    BillingAccountBucketConfigCmekSettingsArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        index_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BillingAccountBucketConfigIndexConfigArgs,
                            BillingAccountBucketConfigIndexConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BillingAccountBucketConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cmek_settings: Optional[
            pulumi.Input[
                Union[
                    BillingAccountBucketConfigCmekSettingsArgs,
                    BillingAccountBucketConfigCmekSettingsArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        index_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BillingAccountBucketConfigIndexConfigArgs,
                            BillingAccountBucketConfigIndexConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> BillingAccountBucketConfig: ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cmekSettings")
    def cmek_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.BillingAccountBucketConfigCmekSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexConfigs")
    def index_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.BillingAccountBucketConfigIndexConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
