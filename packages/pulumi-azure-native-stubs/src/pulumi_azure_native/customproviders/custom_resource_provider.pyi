import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CustomResourceProviderArgs", "CustomResourceProvider"]

@pulumi.input_type
class CustomResourceProviderArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomRPActionRouteDefinitionArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CustomRPResourceTypeRouteDefinitionArgs]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        validations: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomRPValidationsArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomRPActionRouteDefinitionArgs]]]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomRPActionRouteDefinitionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderName")
    def resource_provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_provider_name.setter
    def resource_provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomRPResourceTypeRouteDefinitionArgs]]]
    ]: ...
    @resource_types.setter
    def resource_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CustomRPResourceTypeRouteDefinitionArgs]]
            ]
        ],
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
    @pulumi.getter
    def validations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomRPValidationsArgs]]]]: ...
    @validations.setter
    def validations(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRPValidationsArgs]]]],
    ): ...

@pulumi.type_token(...)
class CustomResourceProvider(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomRPActionRouteDefinitionArgs,
                            CustomRPActionRouteDefinitionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomRPResourceTypeRouteDefinitionArgs,
                            CustomRPResourceTypeRouteDefinitionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        validations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CustomRPValidationsArgs, CustomRPValidationsArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CustomResourceProviderArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CustomResourceProvider: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.CustomRPActionRouteDefinitionResponse]]
    ]: ...
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
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.CustomRPResourceTypeRouteDefinitionResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def validations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.CustomRPValidationsResponse]]]: ...
