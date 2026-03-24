import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NfsLocationArgs", "NfsLocation"]

@pulumi.input_type
class NfsLocationArgs:
    def __init__(
        __self__,
        *,
        on_prem_config: pulumi.Input[NfsLocationOnPremConfigArgs],
        server_hostname: pulumi.Input[_builtins.str],
        subdirectory: pulumi.Input[_builtins.str],
        mount_options: Optional[pulumi.Input[NfsLocationMountOptionsArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onPremConfig")
    def on_prem_config(self) -> pulumi.Input[NfsLocationOnPremConfigArgs]: ...
    @on_prem_config.setter
    def on_prem_config(self, value: pulumi.Input[NfsLocationOnPremConfigArgs]): ...
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
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[NfsLocationMountOptionsArgs]]: ...
    @mount_options.setter
    def mount_options(
        self, value: Optional[pulumi.Input[NfsLocationMountOptionsArgs]]
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
class _NfsLocationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mount_options: Optional[pulumi.Input[NfsLocationMountOptionsArgs]] = ...,
        on_prem_config: Optional[pulumi.Input[NfsLocationOnPremConfigArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[NfsLocationMountOptionsArgs]]: ...
    @mount_options.setter
    def mount_options(
        self, value: Optional[pulumi.Input[NfsLocationMountOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onPremConfig")
    def on_prem_config(self) -> Optional[pulumi.Input[NfsLocationOnPremConfigArgs]]: ...
    @on_prem_config.setter
    def on_prem_config(
        self, value: Optional[pulumi.Input[NfsLocationOnPremConfigArgs]]
    ): ...
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

@pulumi.type_token("aws:datasync/nfsLocation:NfsLocation")
class NfsLocation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        mount_options: Optional[
            pulumi.Input[
                Union[NfsLocationMountOptionsArgs, NfsLocationMountOptionsArgsDict]
            ]
        ] = ...,
        on_prem_config: Optional[
            pulumi.Input[
                Union[NfsLocationOnPremConfigArgs, NfsLocationOnPremConfigArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NfsLocationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mount_options: Optional[
            pulumi.Input[
                Union[NfsLocationMountOptionsArgs, NfsLocationMountOptionsArgsDict]
            ]
        ] = ...,
        on_prem_config: Optional[
            pulumi.Input[
                Union[NfsLocationOnPremConfigArgs, NfsLocationOnPremConfigArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        server_hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NfsLocation: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(
        self,
    ) -> pulumi.Output[Optional[outputs.NfsLocationMountOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="onPremConfig")
    def on_prem_config(self) -> pulumi.Output[outputs.NfsLocationOnPremConfig]: ...
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
