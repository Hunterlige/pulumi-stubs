import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppArgs", "App"]

@pulumi.input_type
class AppArgs:
    def __init__(
        __self__,
        *,
        campaign_hook: Optional[pulumi.Input[AppCampaignHookArgs]] = ...,
        limits: Optional[pulumi.Input[AppLimitsArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        quiet_time: Optional[pulumi.Input[AppQuietTimeArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="campaignHook")
    def campaign_hook(self) -> Optional[pulumi.Input[AppCampaignHookArgs]]: ...
    @campaign_hook.setter
    def campaign_hook(self, value: Optional[pulumi.Input[AppCampaignHookArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[AppLimitsArgs]]: ...
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[AppLimitsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quietTime")
    def quiet_time(self) -> Optional[pulumi.Input[AppQuietTimeArgs]]: ...
    @quiet_time.setter
    def quiet_time(self, value: Optional[pulumi.Input[AppQuietTimeArgs]]): ...
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

@pulumi.input_type
class _AppState:
    def __init__(
        __self__,
        *,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        campaign_hook: Optional[pulumi.Input[AppCampaignHookArgs]] = ...,
        limits: Optional[pulumi.Input[AppLimitsArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        quiet_time: Optional[pulumi.Input[AppQuietTimeArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="campaignHook")
    def campaign_hook(self) -> Optional[pulumi.Input[AppCampaignHookArgs]]: ...
    @campaign_hook.setter
    def campaign_hook(self, value: Optional[pulumi.Input[AppCampaignHookArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[AppLimitsArgs]]: ...
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[AppLimitsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quietTime")
    def quiet_time(self) -> Optional[pulumi.Input[AppQuietTimeArgs]]: ...
    @quiet_time.setter
    def quiet_time(self, value: Optional[pulumi.Input[AppQuietTimeArgs]]): ...
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

@pulumi.type_token("aws:pinpoint/app:App")
class App(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        campaign_hook: Optional[
            pulumi.Input[Union[AppCampaignHookArgs, AppCampaignHookArgsDict]]
        ] = ...,
        limits: Optional[pulumi.Input[Union[AppLimitsArgs, AppLimitsArgsDict]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        quiet_time: Optional[
            pulumi.Input[Union[AppQuietTimeArgs, AppQuietTimeArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AppArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        campaign_hook: Optional[
            pulumi.Input[Union[AppCampaignHookArgs, AppCampaignHookArgsDict]]
        ] = ...,
        limits: Optional[pulumi.Input[Union[AppLimitsArgs, AppLimitsArgsDict]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        quiet_time: Optional[
            pulumi.Input[Union[AppQuietTimeArgs, AppQuietTimeArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> App: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="campaignHook")
    def campaign_hook(self) -> pulumi.Output[Optional[outputs.AppCampaignHook]]: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> pulumi.Output[Optional[outputs.AppLimits]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quietTime")
    def quiet_time(self) -> pulumi.Output[Optional[outputs.AppQuietTime]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
