import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EdgeActionVersionArgs", "EdgeActionVersion"]

@pulumi.input_type
class EdgeActionVersionArgs:
    def __init__(
        __self__,
        *,
        deployment_type: pulumi.Input[
            Union[_builtins.str, EdgeActionVersionDeploymentType]
        ],
        edge_action_name: pulumi.Input[_builtins.str],
        is_default_version: pulumi.Input[
            Union[_builtins.str, EdgeActionIsDefaultVersion]
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, EdgeActionVersionDeploymentType]]: ...
    @deployment_type.setter
    def deployment_type(
        self, value: pulumi.Input[Union[_builtins.str, EdgeActionVersionDeploymentType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="edgeActionName")
    def edge_action_name(self) -> pulumi.Input[_builtins.str]: ...
    @edge_action_name.setter
    def edge_action_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(
        self,
    ) -> pulumi.Input[Union[_builtins.str, EdgeActionIsDefaultVersion]]: ...
    @is_default_version.setter
    def is_default_version(
        self, value: pulumi.Input[Union[_builtins.str, EdgeActionIsDefaultVersion]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:cdn:EdgeActionVersion")
class EdgeActionVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        deployment_type: Optional[
            pulumi.Input[Union[_builtins.str, EdgeActionVersionDeploymentType]]
        ] = ...,
        edge_action_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_default_version: Optional[
            pulumi.Input[Union[_builtins.str, EdgeActionIsDefaultVersion]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EdgeActionVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> EdgeActionVersion: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastPackageUpdateTime")
    def last_package_update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationStatus")
    def validation_status(self) -> pulumi.Output[_builtins.str]: ...
