import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SiteReferenceArgs", "SiteReference"]

@pulumi.input_type
class SiteReferenceArgs:
    def __init__(
        __self__,
        *,
        context_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        properties: Optional[pulumi.Input[SiteReferencePropertiesArgs]] = ...,
        site_reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contextName")
    def context_name(self) -> pulumi.Input[_builtins.str]: ...
    @context_name.setter
    def context_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[SiteReferencePropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[SiteReferencePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="siteReferenceName")
    def site_reference_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @site_reference_name.setter
    def site_reference_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:edge:SiteReference")
class SiteReference(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        context_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[SiteReferencePropertiesArgs, SiteReferencePropertiesArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        site_reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SiteReferenceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SiteReference: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.SiteReferencePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
