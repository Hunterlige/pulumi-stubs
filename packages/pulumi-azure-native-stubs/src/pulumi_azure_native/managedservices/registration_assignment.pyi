import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegistrationAssignmentArgs", "RegistrationAssignment"]

@pulumi.input_type
class RegistrationAssignmentArgs:
    def __init__(
        __self__,
        *,
        scope: pulumi.Input[_builtins.str],
        properties: Optional[pulumi.Input[RegistrationAssignmentPropertiesArgs]] = ...,
        registration_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[RegistrationAssignmentPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[RegistrationAssignmentPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="registrationAssignmentId")
    def registration_assignment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_assignment_id.setter
    def registration_assignment_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class RegistrationAssignment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    RegistrationAssignmentPropertiesArgs,
                    RegistrationAssignmentPropertiesArgsDict,
                ]
            ]
        ] = ...,
        registration_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RegistrationAssignmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RegistrationAssignment: ...
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
    ) -> pulumi.Output[outputs.RegistrationAssignmentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
