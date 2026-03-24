import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OrganizationFeedArgs", "OrganizationFeed"]

@pulumi.input_type
class OrganizationFeedArgs:
    def __init__(
        __self__,
        *,
        billing_project: pulumi.Input[_builtins.str],
        feed_id: pulumi.Input[_builtins.str],
        feed_output_config: pulumi.Input[OrganizationFeedFeedOutputConfigArgs],
        org_id: pulumi.Input[_builtins.str],
        asset_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        asset_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        condition: Optional[pulumi.Input[OrganizationFeedConditionArgs]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingProject")
    def billing_project(self) -> pulumi.Input[_builtins.str]: ...
    @billing_project.setter
    def billing_project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="feedId")
    def feed_id(self) -> pulumi.Input[_builtins.str]: ...
    @feed_id.setter
    def feed_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="feedOutputConfig")
    def feed_output_config(
        self,
    ) -> pulumi.Input[OrganizationFeedFeedOutputConfigArgs]: ...
    @feed_output_config.setter
    def feed_output_config(
        self, value: pulumi.Input[OrganizationFeedFeedOutputConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assetNames")
    def asset_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @asset_names.setter
    def asset_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="assetTypes")
    def asset_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @asset_types.setter
    def asset_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[OrganizationFeedConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[OrganizationFeedConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _OrganizationFeedState:
    def __init__(
        __self__,
        *,
        asset_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        asset_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        billing_project: Optional[pulumi.Input[_builtins.str]] = ...,
        condition: Optional[pulumi.Input[OrganizationFeedConditionArgs]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        feed_id: Optional[pulumi.Input[_builtins.str]] = ...,
        feed_output_config: Optional[
            pulumi.Input[OrganizationFeedFeedOutputConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetNames")
    def asset_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @asset_names.setter
    def asset_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="assetTypes")
    def asset_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @asset_types.setter
    def asset_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingProject")
    def billing_project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_project.setter
    def billing_project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[OrganizationFeedConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[OrganizationFeedConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="feedId")
    def feed_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @feed_id.setter
    def feed_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="feedOutputConfig")
    def feed_output_config(
        self,
    ) -> Optional[pulumi.Input[OrganizationFeedFeedOutputConfigArgs]]: ...
    @feed_output_config.setter
    def feed_output_config(
        self, value: Optional[pulumi.Input[OrganizationFeedFeedOutputConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:cloudasset/organizationFeed:OrganizationFeed")
class OrganizationFeed(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        asset_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        asset_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        billing_project: Optional[pulumi.Input[_builtins.str]] = ...,
        condition: Optional[
            pulumi.Input[
                Union[OrganizationFeedConditionArgs, OrganizationFeedConditionArgsDict]
            ]
        ] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        feed_id: Optional[pulumi.Input[_builtins.str]] = ...,
        feed_output_config: Optional[
            pulumi.Input[
                Union[
                    OrganizationFeedFeedOutputConfigArgs,
                    OrganizationFeedFeedOutputConfigArgsDict,
                ]
            ]
        ] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OrganizationFeedArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        asset_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        asset_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        billing_project: Optional[pulumi.Input[_builtins.str]] = ...,
        condition: Optional[
            pulumi.Input[
                Union[OrganizationFeedConditionArgs, OrganizationFeedConditionArgsDict]
            ]
        ] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        feed_id: Optional[pulumi.Input[_builtins.str]] = ...,
        feed_output_config: Optional[
            pulumi.Input[
                Union[
                    OrganizationFeedFeedOutputConfigArgs,
                    OrganizationFeedFeedOutputConfigArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> OrganizationFeed: ...
    @_builtins.property
    @pulumi.getter(name="assetNames")
    def asset_names(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="assetTypes")
    def asset_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="billingProject")
    def billing_project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> pulumi.Output[Optional[outputs.OrganizationFeedCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="feedId")
    def feed_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="feedOutputConfig")
    def feed_output_config(
        self,
    ) -> pulumi.Output[outputs.OrganizationFeedFeedOutputConfig]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
