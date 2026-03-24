import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFunctionResult",
    "AwaitableGetFunctionResult",
    "get_function",
    "get_function_output",
]

@pulumi.output_type
class GetFunctionResult:
    def __init__(
        __self__,
        automatic_update_policies=...,
        available_memory_mb=...,
        build_environment_variables=...,
        build_service_account=...,
        build_worker_pool=...,
        description=...,
        docker_registry=...,
        docker_repository=...,
        effective_labels=...,
        entry_point=...,
        environment_variables=...,
        event_triggers=...,
        https_trigger_security_level=...,
        https_trigger_url=...,
        id=...,
        ingress_settings=...,
        kms_key_name=...,
        labels=...,
        max_instances=...,
        min_instances=...,
        name=...,
        on_deploy_update_policies=...,
        project=...,
        pulumi_labels=...,
        region=...,
        runtime=...,
        secret_environment_variables=...,
        secret_volumes=...,
        service_account_email=...,
        source_archive_bucket=...,
        source_archive_object=...,
        source_repositories=...,
        status=...,
        timeout=...,
        trigger_http=...,
        version_id=...,
        vpc_connector=...,
        vpc_connector_egress_settings=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticUpdatePolicies")
    def automatic_update_policies(
        self,
    ) -> Sequence[outputs.GetFunctionAutomaticUpdatePolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="availableMemoryMb")
    def available_memory_mb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="buildEnvironmentVariables")
    def build_environment_variables(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="buildServiceAccount")
    def build_service_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="buildWorkerPool")
    def build_worker_pool(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dockerRegistry")
    def docker_registry(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventTriggers")
    def event_triggers(self) -> Sequence[outputs.GetFunctionEventTriggerResult]: ...
    @_builtins.property
    @pulumi.getter(name="httpsTriggerSecurityLevel")
    def https_trigger_security_level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpsTriggerUrl")
    def https_trigger_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onDeployUpdatePolicies")
    def on_deploy_update_policies(
        self,
    ) -> Sequence[outputs.GetFunctionOnDeployUpdatePolicyResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretEnvironmentVariables")
    def secret_environment_variables(
        self,
    ) -> Sequence[outputs.GetFunctionSecretEnvironmentVariableResult]: ...
    @_builtins.property
    @pulumi.getter(name="secretVolumes")
    def secret_volumes(self) -> Sequence[outputs.GetFunctionSecretVolumeResult]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceArchiveBucket")
    def source_archive_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceArchiveObject")
    def source_archive_object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceRepositories")
    def source_repositories(
        self,
    ) -> Sequence[outputs.GetFunctionSourceRepositoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="triggerHttp")
    def trigger_http(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcConnector")
    def vpc_connector(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcConnectorEgressSettings")
    def vpc_connector_egress_settings(self) -> _builtins.str: ...

class AwaitableGetFunctionResult(GetFunctionResult):
    def __await__(self): ...

def get_function(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFunctionResult: ...
def get_function_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFunctionResult]: ...
