import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HostingVersionArgs", "HostingVersion"]

@pulumi.input_type
class HostingVersionArgs:
    def __init__(
        __self__,
        *,
        site_id: pulumi.Input[_builtins.str],
        config: Optional[pulumi.Input[HostingVersionConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Input[_builtins.str]: ...
    @site_id.setter
    def site_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[HostingVersionConfigArgs]]: ...
    @config.setter
    def config(self, value: Optional[pulumi.Input[HostingVersionConfigArgs]]): ...

@pulumi.input_type
class _HostingVersionState:
    def __init__(
        __self__,
        *,
        config: Optional[pulumi.Input[HostingVersionConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[HostingVersionConfigArgs]]: ...
    @config.setter
    def config(self, value: Optional[pulumi.Input[HostingVersionConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:firebase/hostingVersion:HostingVersion")
class HostingVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        config: Optional[
            pulumi.Input[Union[HostingVersionConfigArgs, HostingVersionConfigArgsDict]]
        ] = ...,
        site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: HostingVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        config: Optional[
            pulumi.Input[Union[HostingVersionConfigArgs, HostingVersionConfigArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> HostingVersion: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[outputs.HostingVersionConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[_builtins.str]: ...
