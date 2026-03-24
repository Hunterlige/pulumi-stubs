import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UsagePlanArgs", "UsagePlan"]

@pulumi.input_type
class UsagePlanArgs:
    def __init__(
        __self__,
        *,
        api_stages: Optional[
            pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_code: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_settings: Optional[pulumi.Input[UsagePlanQuotaSettingsArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throttle_settings: Optional[pulumi.Input[UsagePlanThrottleSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiStages")
    def api_stages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageArgs]]]]: ...
    @api_stages.setter
    def api_stages(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_code.setter
    def product_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaSettings")
    def quota_settings(self) -> Optional[pulumi.Input[UsagePlanQuotaSettingsArgs]]: ...
    @quota_settings.setter
    def quota_settings(
        self, value: Optional[pulumi.Input[UsagePlanQuotaSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="throttleSettings")
    def throttle_settings(
        self,
    ) -> Optional[pulumi.Input[UsagePlanThrottleSettingsArgs]]: ...
    @throttle_settings.setter
    def throttle_settings(
        self, value: Optional[pulumi.Input[UsagePlanThrottleSettingsArgs]]
    ): ...

@pulumi.input_type
class _UsagePlanState:
    def __init__(
        __self__,
        *,
        api_stages: Optional[
            pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageArgs]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_code: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_settings: Optional[pulumi.Input[UsagePlanQuotaSettingsArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throttle_settings: Optional[pulumi.Input[UsagePlanThrottleSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiStages")
    def api_stages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageArgs]]]]: ...
    @api_stages.setter
    def api_stages(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_code.setter
    def product_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaSettings")
    def quota_settings(self) -> Optional[pulumi.Input[UsagePlanQuotaSettingsArgs]]: ...
    @quota_settings.setter
    def quota_settings(
        self, value: Optional[pulumi.Input[UsagePlanQuotaSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="throttleSettings")
    def throttle_settings(
        self,
    ) -> Optional[pulumi.Input[UsagePlanThrottleSettingsArgs]]: ...
    @throttle_settings.setter
    def throttle_settings(
        self, value: Optional[pulumi.Input[UsagePlanThrottleSettingsArgs]]
    ): ...

@pulumi.type_token("aws:apigateway/usagePlan:UsagePlan")
class UsagePlan(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_stages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[UsagePlanApiStageArgs, UsagePlanApiStageArgsDict]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_code: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_settings: Optional[
            pulumi.Input[
                Union[UsagePlanQuotaSettingsArgs, UsagePlanQuotaSettingsArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throttle_settings: Optional[
            pulumi.Input[
                Union[UsagePlanThrottleSettingsArgs, UsagePlanThrottleSettingsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[UsagePlanArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_stages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[UsagePlanApiStageArgs, UsagePlanApiStageArgsDict]
                    ]
                ]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_code: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_settings: Optional[
            pulumi.Input[
                Union[UsagePlanQuotaSettingsArgs, UsagePlanQuotaSettingsArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throttle_settings: Optional[
            pulumi.Input[
                Union[UsagePlanThrottleSettingsArgs, UsagePlanThrottleSettingsArgsDict]
            ]
        ] = ...,
    ) -> UsagePlan: ...
    @_builtins.property
    @pulumi.getter(name="apiStages")
    def api_stages(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.UsagePlanApiStage]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="quotaSettings")
    def quota_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.UsagePlanQuotaSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="throttleSettings")
    def throttle_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.UsagePlanThrottleSettings]]: ...
