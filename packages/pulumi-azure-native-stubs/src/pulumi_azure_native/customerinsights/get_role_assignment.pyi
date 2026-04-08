import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRoleAssignmentResult",
    "AwaitableGetRoleAssignmentResult",
    "get_role_assignment",
    "get_role_assignment_output",
]

@pulumi.output_type
class GetRoleAssignmentResult:
    def __init__(
        __self__,
        assignment_name=...,
        azure_api_version=...,
        conflation_policies=...,
        connectors=...,
        description=...,
        display_name=...,
        id=...,
        interactions=...,
        kpis=...,
        links=...,
        name=...,
        principals=...,
        profiles=...,
        provisioning_state=...,
        relationship_links=...,
        relationships=...,
        role=...,
        role_assignments=...,
        sas_policies=...,
        segments=...,
        tenant_id=...,
        type=...,
        views=...,
        widget_types=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignmentName")
    def assignment_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="conflationPolicies")
    def conflation_policies(
        self,
    ) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def connectors(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def interactions(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def kpis(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def links(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Sequence[outputs.AssignmentPrincipalResponse]: ...
    @_builtins.property
    @pulumi.getter
    def profiles(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relationshipLinks")
    def relationship_links(
        self,
    ) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def relationships(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleAssignments")
    def role_assignments(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sasPolicies")
    def sas_policies(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def segments(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def views(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="widgetTypes")
    def widget_types(self) -> Optional[outputs.ResourceSetDescriptionResponse]: ...

class AwaitableGetRoleAssignmentResult(GetRoleAssignmentResult):
    def __await__(self): ...

def get_role_assignment(
    assignment_name: Optional[_builtins.str] = ...,
    hub_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRoleAssignmentResult: ...
def get_role_assignment_output(
    assignment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRoleAssignmentResult]: ...
