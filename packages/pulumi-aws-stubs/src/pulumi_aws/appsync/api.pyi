import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApiArgs", "Api"]

@pulumi.input_type
class ApiArgs:
    def __init__(
        __self__,
        *,
        event_config: pulumi.Input[ApiEventConfigArgs],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventConfig")
    def event_config(self) -> pulumi.Input[ApiEventConfigArgs]: ...
    @event_config.setter
    def event_config(self, value: pulumi.Input[ApiEventConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerContact")
    def owner_contact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_contact.setter
    def owner_contact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _ApiState:
    def __init__(
        __self__,
        *,
        api_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dns: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        event_config: Optional[pulumi.Input[ApiEventConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        waf_web_acl_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        xray_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiArn")
    def api_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_arn.setter
    def api_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dns(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @dns.setter
    def dns(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventConfig")
    def event_config(self) -> Optional[pulumi.Input[ApiEventConfigArgs]]: ...
    @event_config.setter
    def event_config(self, value: Optional[pulumi.Input[ApiEventConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerContact")
    def owner_contact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_contact.setter
    def owner_contact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="wafWebAclArn")
    def waf_web_acl_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @waf_web_acl_arn.setter
    def waf_web_acl_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="xrayEnabled")
    def xray_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @xray_enabled.setter
    def xray_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("aws:appsync/api:Api")
class Api(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        event_config: Optional[
            pulumi.Input[Union[ApiEventConfigArgs, ApiEventConfigArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApiArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dns: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        event_config: Optional[
            pulumi.Input[Union[ApiEventConfigArgs, ApiEventConfigArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        waf_web_acl_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        xray_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> Api: ...
    @_builtins.property
    @pulumi.getter(name="apiArn")
    def api_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dns(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventConfig")
    def event_config(self) -> pulumi.Output[outputs.ApiEventConfig]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerContact")
    def owner_contact(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="wafWebAclArn")
    def waf_web_acl_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="xrayEnabled")
    def xray_enabled(self) -> pulumi.Output[_builtins.bool]: ...
