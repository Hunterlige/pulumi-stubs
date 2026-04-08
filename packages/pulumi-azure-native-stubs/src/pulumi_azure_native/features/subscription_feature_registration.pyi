import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SubscriptionFeatureRegistrationArgs", "SubscriptionFeatureRegistration"]

@pulumi.input_type
class SubscriptionFeatureRegistrationArgs:
    def __init__(
        __self__,
        *,
        provider_namespace: pulumi.Input[_builtins.str],
        feature_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[SubscriptionFeatureRegistrationPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerNamespace")
    def provider_namespace(self) -> pulumi.Input[_builtins.str]: ...
    @provider_namespace.setter
    def provider_namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="featureName")
    def feature_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @feature_name.setter
    def feature_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[SubscriptionFeatureRegistrationPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[pulumi.Input[SubscriptionFeatureRegistrationPropertiesArgs]],
    ): ...

@pulumi.type_token(...)
class SubscriptionFeatureRegistration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        feature_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    SubscriptionFeatureRegistrationPropertiesArgs,
                    SubscriptionFeatureRegistrationPropertiesArgsDict,
                ]
            ]
        ] = ...,
        provider_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SubscriptionFeatureRegistrationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SubscriptionFeatureRegistration: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.SubscriptionFeatureRegistrationResponseProperties]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
