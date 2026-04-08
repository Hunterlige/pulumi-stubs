import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeyGroupArgs", "KeyGroup"]

@pulumi.input_type
class KeyGroupArgs:
    def __init__(
        __self__,
        *,
        profile_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        key_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_references: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]: ...
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyGroupName")
    def key_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_group_name.setter
    def key_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyReferences")
    def key_references(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]]: ...
    @key_references.setter
    def key_references(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]],
    ): ...

@pulumi.type_token("azure-native:cdn:KeyGroup")
class KeyGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        key_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ResourceReferenceArgs, ResourceReferenceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KeyGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> KeyGroup: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyReferences")
    def key_references(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ResourceReferenceResponse]]]: ...
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
    def type(self) -> pulumi.Output[_builtins.str]: ...
