import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEnvironmentResult",
    "AwaitableGetEnvironmentResult",
    "get_environment",
    "get_environment_output",
]

@pulumi.output_type
class GetEnvironmentResult:
    def __init__(
        __self__,
        arm_template_display_name=...,
        azure_api_version=...,
        created_by_user=...,
        deployment_properties=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        resource_group_id=...,
        system_data=...,
        tags=...,
        type=...,
        unique_identifier=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="armTemplateDisplayName")
    def arm_template_display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdByUser")
    def created_by_user(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentProperties")
    def deployment_properties(
        self,
    ) -> Optional[outputs.EnvironmentDeploymentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> _builtins.str: ...

class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    def __await__(self): ...

def get_environment(
    expand: Optional[_builtins.str] = ...,
    lab_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    user_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEnvironmentResult: ...
def get_environment_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEnvironmentResult]: ...
