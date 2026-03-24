import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FulfillmentArgs", "Fulfillment"]

@pulumi.input_type
class FulfillmentArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        features: Optional[
            pulumi.Input[Sequence[pulumi.Input[FulfillmentFeatureArgs]]]
        ] = ...,
        generic_web_service: Optional[
            pulumi.Input[FulfillmentGenericWebServiceArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FulfillmentFeatureArgs]]]]: ...
    @features.setter
    def features(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[FulfillmentFeatureArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(
        self,
    ) -> Optional[pulumi.Input[FulfillmentGenericWebServiceArgs]]: ...
    @generic_web_service.setter
    def generic_web_service(
        self, value: Optional[pulumi.Input[FulfillmentGenericWebServiceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _FulfillmentState:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        features: Optional[
            pulumi.Input[Sequence[pulumi.Input[FulfillmentFeatureArgs]]]
        ] = ...,
        generic_web_service: Optional[
            pulumi.Input[FulfillmentGenericWebServiceArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FulfillmentFeatureArgs]]]]: ...
    @features.setter
    def features(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[FulfillmentFeatureArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(
        self,
    ) -> Optional[pulumi.Input[FulfillmentGenericWebServiceArgs]]: ...
    @generic_web_service.setter
    def generic_web_service(
        self, value: Optional[pulumi.Input[FulfillmentGenericWebServiceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:diagflow/fulfillment:Fulfillment")
class Fulfillment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        features: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[FulfillmentFeatureArgs, FulfillmentFeatureArgsDict]
                    ]
                ]
            ]
        ] = ...,
        generic_web_service: Optional[
            pulumi.Input[
                Union[
                    FulfillmentGenericWebServiceArgs,
                    FulfillmentGenericWebServiceArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FulfillmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        features: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[FulfillmentFeatureArgs, FulfillmentFeatureArgsDict]
                    ]
                ]
            ]
        ] = ...,
        generic_web_service: Optional[
            pulumi.Input[
                Union[
                    FulfillmentGenericWebServiceArgs,
                    FulfillmentGenericWebServiceArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Fulfillment: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.FulfillmentFeature]]]: ...
    @_builtins.property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(
        self,
    ) -> pulumi.Output[Optional[outputs.FulfillmentGenericWebService]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
