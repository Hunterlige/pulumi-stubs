import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PreviewFeatureArgs", "PreviewFeature"]

@pulumi.input_type
class PreviewFeatureArgs:
    def __init__(
        __self__,
        *,
        activation_status: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_operation: Optional[
            pulumi.Input[PreviewFeatureRolloutOperationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activationStatus")
    def activation_status(self) -> pulumi.Input[_builtins.str]: ...
    @activation_status.setter
    def activation_status(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="rolloutOperation")
    def rollout_operation(
        self,
    ) -> Optional[pulumi.Input[PreviewFeatureRolloutOperationArgs]]: ...
    @rollout_operation.setter
    def rollout_operation(
        self, value: Optional[pulumi.Input[PreviewFeatureRolloutOperationArgs]]
    ): ...

@pulumi.input_type
class _PreviewFeatureState:
    def __init__(
        __self__,
        *,
        activation_status: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_operation: Optional[
            pulumi.Input[PreviewFeatureRolloutOperationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activationStatus")
    def activation_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @activation_status.setter
    def activation_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="rolloutOperation")
    def rollout_operation(
        self,
    ) -> Optional[pulumi.Input[PreviewFeatureRolloutOperationArgs]]: ...
    @rollout_operation.setter
    def rollout_operation(
        self, value: Optional[pulumi.Input[PreviewFeatureRolloutOperationArgs]]
    ): ...

@pulumi.type_token("gcp:compute/previewFeature:PreviewFeature")
class PreviewFeature(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        activation_status: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_operation: Optional[
            pulumi.Input[
                Union[
                    PreviewFeatureRolloutOperationArgs,
                    PreviewFeatureRolloutOperationArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PreviewFeatureArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        activation_status: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_operation: Optional[
            pulumi.Input[
                Union[
                    PreviewFeatureRolloutOperationArgs,
                    PreviewFeatureRolloutOperationArgsDict,
                ]
            ]
        ] = ...,
    ) -> PreviewFeature: ...
    @_builtins.property
    @pulumi.getter(name="activationStatus")
    def activation_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutOperation")
    def rollout_operation(
        self,
    ) -> pulumi.Output[Optional[outputs.PreviewFeatureRolloutOperation]]: ...
