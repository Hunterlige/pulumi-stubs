import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccessPolicyAssignmentResult",
    "AwaitableGetAccessPolicyAssignmentResult",
    "get_access_policy_assignment",
    "get_access_policy_assignment_output",
]

@pulumi.output_type
class GetAccessPolicyAssignmentResult:
    def __init__(
        __self__,
        access_policy_name=...,
        azure_api_version=...,
        id=...,
        name=...,
        object_id=...,
        object_id_alias=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicyName")
    def access_policy_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectIdAlias")
    def object_id_alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAccessPolicyAssignmentResult(GetAccessPolicyAssignmentResult):
    def __await__(self): ...

def get_access_policy_assignment(
    access_policy_assignment_name: Optional[_builtins.str] = ...,
    cache_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAccessPolicyAssignmentResult: ...
def get_access_policy_assignment_output(
    access_policy_assignment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    cache_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccessPolicyAssignmentResult]: ...
