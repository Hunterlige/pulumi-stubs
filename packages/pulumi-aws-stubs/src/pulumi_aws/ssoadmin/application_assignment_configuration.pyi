import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationAssignmentConfigurationArgs",
    "ApplicationAssignmentConfiguration",
]

@pulumi.input_type
class ApplicationAssignmentConfigurationArgs:
    def __init__(
        __self__,
        *,
        application_arn: pulumi.Input[_builtins.str],
        assignment_required: pulumi.Input[_builtins.bool],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> pulumi.Input[_builtins.str]: ...
    @application_arn.setter
    def application_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assignmentRequired")
    def assignment_required(self) -> pulumi.Input[_builtins.bool]: ...
    @assignment_required.setter
    def assignment_required(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ApplicationAssignmentConfigurationState:
    def __init__(
        __self__,
        *,
        application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        assignment_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_arn.setter
    def application_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="assignmentRequired")
    def assignment_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @assignment_required.setter
    def assignment_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ApplicationAssignmentConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        assignment_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationAssignmentConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        assignment_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ApplicationAssignmentConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="assignmentRequired")
    def assignment_required(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
