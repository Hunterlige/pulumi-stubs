import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RemediationAtSubscriptionArgs", "RemediationAtSubscription"]

@pulumi.input_type
class RemediationAtSubscriptionArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[
            pulumi.Input[RemediationPropertiesFailureThresholdArgs]
        ] = ...,
        filters: Optional[pulumi.Input[RemediationFiltersArgs]] = ...,
        parallel_deployments: Optional[pulumi.Input[_builtins.int]] = ...,
        policy_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_definition_reference_id: Optional[pulumi.Input[_builtins.str]] = ...,
        remediation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_count: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_discovery_mode: Optional[
            pulumi.Input[Union[_builtins.str, ResourceDiscoveryMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(
        self,
    ) -> Optional[pulumi.Input[RemediationPropertiesFailureThresholdArgs]]: ...
    @failure_threshold.setter
    def failure_threshold(
        self, value: Optional[pulumi.Input[RemediationPropertiesFailureThresholdArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[RemediationFiltersArgs]]: ...
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[RemediationFiltersArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="parallelDeployments")
    def parallel_deployments(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @parallel_deployments.setter
    def parallel_deployments(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_assignment_id.setter
    def policy_assignment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_definition_reference_id.setter
    def policy_definition_reference_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="remediationName")
    def remediation_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remediation_name.setter
    def remediation_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceCount")
    def resource_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @resource_count.setter
    def resource_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceDiscoveryMode")
    def resource_discovery_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceDiscoveryMode]]]: ...
    @resource_discovery_mode.setter
    def resource_discovery_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceDiscoveryMode]]]
    ): ...

@pulumi.type_token(...)
class RemediationAtSubscription(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        failure_threshold: Optional[
            pulumi.Input[
                Union[
                    RemediationPropertiesFailureThresholdArgs,
                    RemediationPropertiesFailureThresholdArgsDict,
                ]
            ]
        ] = ...,
        filters: Optional[
            pulumi.Input[Union[RemediationFiltersArgs, RemediationFiltersArgsDict]]
        ] = ...,
        parallel_deployments: Optional[pulumi.Input[_builtins.int]] = ...,
        policy_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_definition_reference_id: Optional[pulumi.Input[_builtins.str]] = ...,
        remediation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_count: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_discovery_mode: Optional[
            pulumi.Input[Union[_builtins.str, ResourceDiscoveryMode]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[RemediationAtSubscriptionArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RemediationAtSubscription: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(
        self,
    ) -> pulumi.Output[outputs.RemediationDeploymentSummaryResponse]: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RemediationPropertiesResponseFailureThreshold]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> pulumi.Output[Optional[outputs.RemediationFiltersResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parallelDeployments")
    def parallel_deployments(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceCount")
    def resource_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceDiscoveryMode")
    def resource_discovery_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
