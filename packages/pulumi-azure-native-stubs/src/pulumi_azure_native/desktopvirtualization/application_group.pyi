import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationGroupArgs", "ApplicationGroup"]

@pulumi.input_type
class ApplicationGroupArgs:
    def __init__(
        __self__,
        *,
        application_group_type: pulumi.Input[
            Union[_builtins.str, ApplicationGroupType]
        ],
        host_pool_arm_path: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        application_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[ResourceModelWithAllowedPropertySetIdentityArgs]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        plan: Optional[pulumi.Input[ResourceModelWithAllowedPropertySetPlanArgs]] = ...,
        show_in_feed: Optional[pulumi.Input[_builtins.bool]] = ...,
        sku: Optional[pulumi.Input[ResourceModelWithAllowedPropertySetSkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationGroupType")
    def application_group_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ApplicationGroupType]]: ...
    @application_group_type.setter
    def application_group_type(
        self, value: pulumi.Input[Union[_builtins.str, ApplicationGroupType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostPoolArmPath")
    def host_pool_arm_path(self) -> pulumi.Input[_builtins.str]: ...
    @host_pool_arm_path.setter
    def host_pool_arm_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationGroupName")
    def application_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_group_name.setter
    def application_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[pulumi.Input[ResourceModelWithAllowedPropertySetIdentityArgs]]: ...
    @identity.setter
    def identity(
        self,
        value: Optional[pulumi.Input[ResourceModelWithAllowedPropertySetIdentityArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def plan(
        self,
    ) -> Optional[pulumi.Input[ResourceModelWithAllowedPropertySetPlanArgs]]: ...
    @plan.setter
    def plan(
        self, value: Optional[pulumi.Input[ResourceModelWithAllowedPropertySetPlanArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="showInFeed")
    def show_in_feed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @show_in_feed.setter
    def show_in_feed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(
        self,
    ) -> Optional[pulumi.Input[ResourceModelWithAllowedPropertySetSkuArgs]]: ...
    @sku.setter
    def sku(
        self, value: Optional[pulumi.Input[ResourceModelWithAllowedPropertySetSkuArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class ApplicationGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        application_group_type: Optional[
            pulumi.Input[Union[_builtins.str, ApplicationGroupType]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        host_pool_arm_path: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[
                    ResourceModelWithAllowedPropertySetIdentityArgs,
                    ResourceModelWithAllowedPropertySetIdentityArgsDict,
                ]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        plan: Optional[
            pulumi.Input[
                Union[
                    ResourceModelWithAllowedPropertySetPlanArgs,
                    ResourceModelWithAllowedPropertySetPlanArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        show_in_feed: Optional[pulumi.Input[_builtins.bool]] = ...,
        sku: Optional[
            pulumi.Input[
                Union[
                    ResourceModelWithAllowedPropertySetSkuArgs,
                    ResourceModelWithAllowedPropertySetSkuArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ApplicationGroup: ...
    @_builtins.property
    @pulumi.getter(name="applicationGroupType")
    def application_group_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudPcResource")
    def cloud_pc_resource(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostPoolArmPath")
    def host_pool_arm_path(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ResourceModelWithAllowedPropertySetResponseIdentity]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plan(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ResourceModelWithAllowedPropertySetResponsePlan]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="showInFeed")
    def show_in_feed(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ResourceModelWithAllowedPropertySetResponseSku]
    ]: ...
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
    @pulumi.getter(name="workspaceArmPath")
    def workspace_arm_path(self) -> pulumi.Output[_builtins.str]: ...
