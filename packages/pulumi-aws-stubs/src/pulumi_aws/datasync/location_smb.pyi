import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LocationSmbArgs", "LocationSmb"]

@pulumi.input_type
class LocationSmbArgs:
    def __init__(
        __self__,
        *,
        agent_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        password: pulumi.Input[_builtins.str],
        server_hostname: pulumi.Input[_builtins.str],
        subdirectory: pulumi.Input[_builtins.str],
        user: pulumi.Input[_builtins.str],
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        mount_options: Optional[pulumi.Input[LocationSmbMountOptionsArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @agent_arns.setter
    def agent_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]: ...
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> pulumi.Input[_builtins.str]: ...
    @server_hostname.setter
    def server_hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Input[_builtins.str]: ...
    @subdirectory.setter
    def subdirectory(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[_builtins.str]: ...
    @user.setter
    def user(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[LocationSmbMountOptionsArgs]]: ...
    @mount_options.setter
    def mount_options(
        self, value: Optional[pulumi.Input[LocationSmbMountOptionsArgs]]
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

@pulumi.input_type
class _LocationSmbState:
    def __init__(
        __self__,
        *,
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        mount_options: Optional[pulumi.Input[LocationSmbMountOptionsArgs]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @agent_arns.setter
    def agent_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[LocationSmbMountOptionsArgs]]: ...
    @mount_options.setter
    def mount_options(
        self, value: Optional[pulumi.Input[LocationSmbMountOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_hostname.setter
    def server_hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:datasync/locationSmb:LocationSmb")
class LocationSmb(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        mount_options: Optional[
            pulumi.Input[
                Union[LocationSmbMountOptionsArgs, LocationSmbMountOptionsArgsDict]
            ]
        ] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LocationSmbArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        mount_options: Optional[
            pulumi.Input[
                Union[LocationSmbMountOptionsArgs, LocationSmbMountOptionsArgsDict]
            ]
        ] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LocationSmb: ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(
        self,
    ) -> pulumi.Output[Optional[outputs.LocationSmbMountOptions]]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Output[_builtins.str]: ...
