import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TransitHubArgs", "TransitHub"]

@pulumi.input_type
class TransitHubArgs:
    def __init__(
        __self__,
        *,
        community_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, TransitHubState]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_option: Optional[pulumi.Input[TransitOptionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="communityName")
    def community_name(self) -> pulumi.Input[_builtins.str]: ...
    @community_name.setter
    def community_name(self, value: pulumi.Input[_builtins.str]): ...
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
    def state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TransitHubState]]]: ...
    @state.setter
    def state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TransitHubState]]]
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
    @_builtins.property
    @pulumi.getter(name="transitHubName")
    def transit_hub_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_hub_name.setter
    def transit_hub_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitOption")
    def transit_option(self) -> Optional[pulumi.Input[TransitOptionArgs]]: ...
    @transit_option.setter
    def transit_option(self, value: Optional[pulumi.Input[TransitOptionArgs]]): ...

@pulumi.type_token("azure-native:mission:TransitHub")
class TransitHub(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        community_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, TransitHubState]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_option: Optional[
            pulumi.Input[Union[TransitOptionArgs, TransitOptionArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TransitHubArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> TransitHub: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter(name="resourceCollection")
    def resource_collection(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="transitOption")
    def transit_option(
        self,
    ) -> pulumi.Output[Optional[outputs.TransitOptionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
