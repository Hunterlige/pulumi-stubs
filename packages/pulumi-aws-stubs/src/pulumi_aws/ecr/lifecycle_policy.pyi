import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LifecyclePolicyArgs", "LifecyclePolicy"]

@pulumi.input_type
class LifecyclePolicyArgs:
    def __init__(
        __self__,
        *,
        policy: pulumi.Input[Union[_builtins.str, LifecyclePolicyDocumentArgs]],
        repository: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(
        self,
    ) -> pulumi.Input[Union[_builtins.str, LifecyclePolicyDocumentArgs]]: ...
    @policy.setter
    def policy(
        self, value: pulumi.Input[Union[_builtins.str, LifecyclePolicyDocumentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Input[_builtins.str]: ...
    @repository.setter
    def repository(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LifecyclePolicyState:
    def __init__(
        __self__,
        *,
        policy: Optional[
            pulumi.Input[Union[_builtins.str, LifecyclePolicyDocumentArgs]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LifecyclePolicyDocumentArgs]]]: ...
    @policy.setter
    def policy(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, LifecyclePolicyDocumentArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ecr/lifecyclePolicy:LifecyclePolicy")
class LifecyclePolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        policy: Optional[
            pulumi.Input[
                Union[
                    _builtins.str,
                    Union[LifecyclePolicyDocumentArgs, LifecyclePolicyDocumentArgsDict],
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LifecyclePolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        policy: Optional[
            pulumi.Input[
                Union[
                    _builtins.str,
                    Union[LifecyclePolicyDocumentArgs, LifecyclePolicyDocumentArgsDict],
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LifecyclePolicy: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Output[_builtins.str]: ...
