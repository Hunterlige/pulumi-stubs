import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NspAssociationArgs", "NspAssociation"]

@pulumi.input_type
class NspAssociationArgs:
    def __init__(
        __self__,
        *,
        network_security_perimeter_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        access_mode: Optional[
            pulumi.Input[Union[_builtins.str, AssociationAccessMode]]
        ] = ...,
        association_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_resource: Optional[pulumi.Input[SubResourceArgs]] = ...,
        profile: Optional[pulumi.Input[SubResourceArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityPerimeterName")
    def network_security_perimeter_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_security_perimeter_name.setter
    def network_security_perimeter_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AssociationAccessMode]]]: ...
    @access_mode.setter
    def access_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AssociationAccessMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="associationName")
    def association_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @association_name.setter
    def association_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="privateLinkResource")
    def private_link_resource(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @private_link_resource.setter
    def private_link_resource(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:network:NspAssociation")
class NspAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_mode: Optional[
            pulumi.Input[Union[_builtins.str, AssociationAccessMode]]
        ] = ...,
        association_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_security_perimeter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_resource: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        profile: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NspAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NspAssociation: ...
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hasProvisioningIssues")
    def has_provisioning_issues(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResource")
    def private_link_resource(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
