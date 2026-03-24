import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LicenseConfigArgs", "LicenseConfig"]

@pulumi.input_type
class LicenseConfigArgs:
    def __init__(
        __self__,
        *,
        license_config_id: pulumi.Input[_builtins.str],
        license_count: pulumi.Input[_builtins.int],
        location: pulumi.Input[_builtins.str],
        start_date: pulumi.Input[LicenseConfigStartDateArgs],
        subscription_term: pulumi.Input[_builtins.str],
        subscription_tier: pulumi.Input[_builtins.str],
        auto_renew: Optional[pulumi.Input[_builtins.bool]] = ...,
        end_date: Optional[pulumi.Input[LicenseConfigEndDateArgs]] = ...,
        free_trial: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licenseConfigId")
    def license_config_id(self) -> pulumi.Input[_builtins.str]: ...
    @license_config_id.setter
    def license_config_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="licenseCount")
    def license_count(self) -> pulumi.Input[_builtins.int]: ...
    @license_count.setter
    def license_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Input[LicenseConfigStartDateArgs]: ...
    @start_date.setter
    def start_date(self, value: pulumi.Input[LicenseConfigStartDateArgs]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionTerm")
    def subscription_term(self) -> pulumi.Input[_builtins.str]: ...
    @subscription_term.setter
    def subscription_term(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionTier")
    def subscription_tier(self) -> pulumi.Input[_builtins.str]: ...
    @subscription_tier.setter
    def subscription_tier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[LicenseConfigEndDateArgs]]: ...
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[LicenseConfigEndDateArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="freeTrial")
    def free_trial(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @free_trial.setter
    def free_trial(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LicenseConfigState:
    def __init__(
        __self__,
        *,
        auto_renew: Optional[pulumi.Input[_builtins.bool]] = ...,
        end_date: Optional[pulumi.Input[LicenseConfigEndDateArgs]] = ...,
        free_trial: Optional[pulumi.Input[_builtins.bool]] = ...,
        license_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        license_count: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        start_date: Optional[pulumi.Input[LicenseConfigStartDateArgs]] = ...,
        subscription_term: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[LicenseConfigEndDateArgs]]: ...
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[LicenseConfigEndDateArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="freeTrial")
    def free_trial(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @free_trial.setter
    def free_trial(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="licenseConfigId")
    def license_config_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @license_config_id.setter
    def license_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="licenseCount")
    def license_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @license_count.setter
    def license_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[LicenseConfigStartDateArgs]]: ...
    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[LicenseConfigStartDateArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionTerm")
    def subscription_term(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_term.setter
    def subscription_term(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionTier")
    def subscription_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_tier.setter
    def subscription_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:discoveryengine/licenseConfig:LicenseConfig")
class LicenseConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_renew: Optional[pulumi.Input[_builtins.bool]] = ...,
        end_date: Optional[
            pulumi.Input[Union[LicenseConfigEndDateArgs, LicenseConfigEndDateArgsDict]]
        ] = ...,
        free_trial: Optional[pulumi.Input[_builtins.bool]] = ...,
        license_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        license_count: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        start_date: Optional[
            pulumi.Input[
                Union[LicenseConfigStartDateArgs, LicenseConfigStartDateArgsDict]
            ]
        ] = ...,
        subscription_term: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LicenseConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_renew: Optional[pulumi.Input[_builtins.bool]] = ...,
        end_date: Optional[
            pulumi.Input[Union[LicenseConfigEndDateArgs, LicenseConfigEndDateArgsDict]]
        ] = ...,
        free_trial: Optional[pulumi.Input[_builtins.bool]] = ...,
        license_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        license_count: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        start_date: Optional[
            pulumi.Input[
                Union[LicenseConfigStartDateArgs, LicenseConfigStartDateArgsDict]
            ]
        ] = ...,
        subscription_term: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LicenseConfig: ...
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[outputs.LicenseConfigEndDate]]: ...
    @_builtins.property
    @pulumi.getter(name="freeTrial")
    def free_trial(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="licenseConfigId")
    def license_config_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="licenseCount")
    def license_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[outputs.LicenseConfigStartDate]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionTerm")
    def subscription_term(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionTier")
    def subscription_tier(self) -> pulumi.Output[_builtins.str]: ...
