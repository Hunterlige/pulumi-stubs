import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRemediationAtResourceGroupResult",
    "AwaitableGetRemediationAtResourceGroupResult",
    "get_remediation_at_resource_group",
    "get_remediation_at_resource_group_output",
]

@pulumi.output_type
class GetRemediationAtResourceGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        correlation_id=...,
        created_on=...,
        deployment_status=...,
        failure_threshold=...,
        filters=...,
        id=...,
        last_updated_on=...,
        name=...,
        parallel_deployments=...,
        policy_assignment_id=...,
        policy_definition_reference_id=...,
        provisioning_state=...,
        resource_count=...,
        resource_discovery_mode=...,
        status_message=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> outputs.RemediationDeploymentSummaryResponse: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(
        self,
    ) -> Optional[outputs.RemediationPropertiesResponseFailureThreshold]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[outputs.RemediationFiltersResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parallelDeployments")
    def parallel_deployments(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceCount")
    def resource_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="resourceDiscoveryMode")
    def resource_discovery_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRemediationAtResourceGroupResult(GetRemediationAtResourceGroupResult):
    def __await__(self): ...

def get_remediation_at_resource_group(
    remediation_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRemediationAtResourceGroupResult: ...
def get_remediation_at_resource_group_output(
    remediation_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRemediationAtResourceGroupResult]: ...
