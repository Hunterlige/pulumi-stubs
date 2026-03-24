import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AssistantArgs", "Assistant"]

@pulumi.input_type
class AssistantArgs:
    def __init__(
        __self__,
        *,
        assistant_id: pulumi.Input[_builtins.str],
        collection_id: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        engine_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        customer_policy: Optional[pulumi.Input[AssistantCustomerPolicyArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        generation_config: Optional[pulumi.Input[AssistantGenerationConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        web_grounding_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assistantId")
    def assistant_id(self) -> pulumi.Input[_builtins.str]: ...
    @assistant_id.setter
    def assistant_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Input[_builtins.str]: ...
    @collection_id.setter
    def collection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Input[_builtins.str]: ...
    @engine_id.setter
    def engine_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customerPolicy")
    def customer_policy(
        self,
    ) -> Optional[pulumi.Input[AssistantCustomerPolicyArgs]]: ...
    @customer_policy.setter
    def customer_policy(
        self, value: Optional[pulumi.Input[AssistantCustomerPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="generationConfig")
    def generation_config(
        self,
    ) -> Optional[pulumi.Input[AssistantGenerationConfigArgs]]: ...
    @generation_config.setter
    def generation_config(
        self, value: Optional[pulumi.Input[AssistantGenerationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webGroundingType")
    def web_grounding_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_grounding_type.setter
    def web_grounding_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AssistantState:
    def __init__(
        __self__,
        *,
        assistant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        collection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_policy: Optional[pulumi.Input[AssistantCustomerPolicyArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        generation_config: Optional[pulumi.Input[AssistantGenerationConfigArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        web_grounding_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assistantId")
    def assistant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assistant_id.setter
    def assistant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerPolicy")
    def customer_policy(
        self,
    ) -> Optional[pulumi.Input[AssistantCustomerPolicyArgs]]: ...
    @customer_policy.setter
    def customer_policy(
        self, value: Optional[pulumi.Input[AssistantCustomerPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_id.setter
    def engine_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="generationConfig")
    def generation_config(
        self,
    ) -> Optional[pulumi.Input[AssistantGenerationConfigArgs]]: ...
    @generation_config.setter
    def generation_config(
        self, value: Optional[pulumi.Input[AssistantGenerationConfigArgs]]
    ): ...
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webGroundingType")
    def web_grounding_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_grounding_type.setter
    def web_grounding_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:discoveryengine/assistant:Assistant")
class Assistant(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        assistant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        collection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_policy: Optional[
            pulumi.Input[
                Union[AssistantCustomerPolicyArgs, AssistantCustomerPolicyArgsDict]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        generation_config: Optional[
            pulumi.Input[
                Union[AssistantGenerationConfigArgs, AssistantGenerationConfigArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        web_grounding_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AssistantArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        assistant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        collection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_policy: Optional[
            pulumi.Input[
                Union[AssistantCustomerPolicyArgs, AssistantCustomerPolicyArgsDict]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        generation_config: Optional[
            pulumi.Input[
                Union[AssistantGenerationConfigArgs, AssistantGenerationConfigArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        web_grounding_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Assistant: ...
    @_builtins.property
    @pulumi.getter(name="assistantId")
    def assistant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerPolicy")
    def customer_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.AssistantCustomerPolicy]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="generationConfig")
    def generation_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AssistantGenerationConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webGroundingType")
    def web_grounding_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
