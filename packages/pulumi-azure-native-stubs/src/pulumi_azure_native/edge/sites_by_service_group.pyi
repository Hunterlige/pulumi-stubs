import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SitesByServiceGroupArgs", "SitesByServiceGroup"]

@pulumi.input_type
class SitesByServiceGroupArgs:
    def __init__(
        __self__,
        *,
        servicegroup_name: pulumi.Input[_builtins.str],
        properties: Optional[pulumi.Input[SitePropertiesArgs]] = ...,
        site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="servicegroupName")
    def servicegroup_name(self) -> pulumi.Input[_builtins.str]: ...
    @servicegroup_name.setter
    def servicegroup_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[SitePropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[SitePropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @site_name.setter
    def site_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:edge:SitesByServiceGroup")
class SitesByServiceGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        properties: Optional[
            pulumi.Input[Union[SitePropertiesArgs, SitePropertiesArgsDict]]
        ] = ...,
        servicegroup_name: Optional[pulumi.Input[_builtins.str]] = ...,
        site_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SitesByServiceGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SitesByServiceGroup: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.SitePropertiesResponseV1]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
