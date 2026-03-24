

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FunctionArgs', 'Function']
@pulumi.input_type
class FunctionArgs:
    def __init__(__self__, *, runtime: pulumi.Input[_builtins.str], automatic_update_policy: Optional[pulumi.Input[FunctionAutomaticUpdatePolicyArgs]] = ..., available_memory_mb: Optional[pulumi.Input[_builtins.int]] = ..., build_environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., build_service_account: Optional[pulumi.Input[_builtins.str]] = ..., build_worker_pool: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., docker_registry: Optional[pulumi.Input[_builtins.str]] = ..., docker_repository: Optional[pulumi.Input[_builtins.str]] = ..., entry_point: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., event_trigger: Optional[pulumi.Input[FunctionEventTriggerArgs]] = ..., https_trigger_security_level: Optional[pulumi.Input[_builtins.str]] = ..., https_trigger_url: Optional[pulumi.Input[_builtins.str]] = ..., ingress_settings: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., max_instances: Optional[pulumi.Input[_builtins.int]] = ..., min_instances: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., on_deploy_update_policy: Optional[pulumi.Input[FunctionOnDeployUpdatePolicyArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretEnvironmentVariableArgs]]]] = ..., secret_volumes: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeArgs]]]] = ..., service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., source_archive_bucket: Optional[pulumi.Input[_builtins.str]] = ..., source_archive_object: Optional[pulumi.Input[_builtins.str]] = ..., source_repository: Optional[pulumi.Input[FunctionSourceRepositoryArgs]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ..., trigger_http: Optional[pulumi.Input[_builtins.bool]] = ..., vpc_connector: Optional[pulumi.Input[_builtins.str]] = ..., vpc_connector_egress_settings: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticUpdatePolicy")
    def automatic_update_policy(self) -> Optional[pulumi.Input[FunctionAutomaticUpdatePolicyArgs]]:
        
        ...
    
    @automatic_update_policy.setter
    def automatic_update_policy(self, value: Optional[pulumi.Input[FunctionAutomaticUpdatePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMemoryMb")
    def available_memory_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @available_memory_mb.setter
    def available_memory_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildEnvironmentVariables")
    def build_environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @build_environment_variables.setter
    def build_environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildServiceAccount")
    def build_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @build_service_account.setter
    def build_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildWorkerPool")
    def build_worker_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @build_worker_pool.setter
    def build_worker_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRegistry")
    def docker_registry(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @docker_registry.setter
    def docker_registry(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @docker_repository.setter
    def docker_repository(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @entry_point.setter
    def entry_point(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTrigger")
    def event_trigger(self) -> Optional[pulumi.Input[FunctionEventTriggerArgs]]:
        
        ...
    
    @event_trigger.setter
    def event_trigger(self, value: Optional[pulumi.Input[FunctionEventTriggerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsTriggerSecurityLevel")
    def https_trigger_security_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @https_trigger_security_level.setter
    def https_trigger_security_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsTriggerUrl")
    def https_trigger_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @https_trigger_url.setter
    def https_trigger_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ingress_settings.setter
    def ingress_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_instances.setter
    def max_instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_instances.setter
    def min_instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDeployUpdatePolicy")
    def on_deploy_update_policy(self) -> Optional[pulumi.Input[FunctionOnDeployUpdatePolicyArgs]]:
        
        ...
    
    @on_deploy_update_policy.setter
    def on_deploy_update_policy(self, value: Optional[pulumi.Input[FunctionOnDeployUpdatePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnvironmentVariables")
    def secret_environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretEnvironmentVariableArgs]]]]:
        
        ...
    
    @secret_environment_variables.setter
    def secret_environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretEnvironmentVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVolumes")
    def secret_volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeArgs]]]]:
        
        ...
    
    @secret_volumes.setter
    def secret_volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArchiveBucket")
    def source_archive_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_archive_bucket.setter
    def source_archive_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArchiveObject")
    def source_archive_object(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_archive_object.setter
    def source_archive_object(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> Optional[pulumi.Input[FunctionSourceRepositoryArgs]]:
        
        ...
    
    @source_repository.setter
    def source_repository(self, value: Optional[pulumi.Input[FunctionSourceRepositoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerHttp")
    def trigger_http(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @trigger_http.setter
    def trigger_http(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnector")
    def vpc_connector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_connector.setter
    def vpc_connector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnectorEgressSettings")
    def vpc_connector_egress_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_connector_egress_settings.setter
    def vpc_connector_egress_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FunctionState:
    def __init__(__self__, *, automatic_update_policy: Optional[pulumi.Input[FunctionAutomaticUpdatePolicyArgs]] = ..., available_memory_mb: Optional[pulumi.Input[_builtins.int]] = ..., build_environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., build_service_account: Optional[pulumi.Input[_builtins.str]] = ..., build_worker_pool: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., docker_registry: Optional[pulumi.Input[_builtins.str]] = ..., docker_repository: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., entry_point: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., event_trigger: Optional[pulumi.Input[FunctionEventTriggerArgs]] = ..., https_trigger_security_level: Optional[pulumi.Input[_builtins.str]] = ..., https_trigger_url: Optional[pulumi.Input[_builtins.str]] = ..., ingress_settings: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., max_instances: Optional[pulumi.Input[_builtins.int]] = ..., min_instances: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., on_deploy_update_policy: Optional[pulumi.Input[FunctionOnDeployUpdatePolicyArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime: Optional[pulumi.Input[_builtins.str]] = ..., secret_environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretEnvironmentVariableArgs]]]] = ..., secret_volumes: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeArgs]]]] = ..., service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., source_archive_bucket: Optional[pulumi.Input[_builtins.str]] = ..., source_archive_object: Optional[pulumi.Input[_builtins.str]] = ..., source_repository: Optional[pulumi.Input[FunctionSourceRepositoryArgs]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ..., trigger_http: Optional[pulumi.Input[_builtins.bool]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_connector: Optional[pulumi.Input[_builtins.str]] = ..., vpc_connector_egress_settings: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticUpdatePolicy")
    def automatic_update_policy(self) -> Optional[pulumi.Input[FunctionAutomaticUpdatePolicyArgs]]:
        
        ...
    
    @automatic_update_policy.setter
    def automatic_update_policy(self, value: Optional[pulumi.Input[FunctionAutomaticUpdatePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMemoryMb")
    def available_memory_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @available_memory_mb.setter
    def available_memory_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildEnvironmentVariables")
    def build_environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @build_environment_variables.setter
    def build_environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildServiceAccount")
    def build_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @build_service_account.setter
    def build_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildWorkerPool")
    def build_worker_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @build_worker_pool.setter
    def build_worker_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRegistry")
    def docker_registry(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @docker_registry.setter
    def docker_registry(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @docker_repository.setter
    def docker_repository(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @entry_point.setter
    def entry_point(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTrigger")
    def event_trigger(self) -> Optional[pulumi.Input[FunctionEventTriggerArgs]]:
        
        ...
    
    @event_trigger.setter
    def event_trigger(self, value: Optional[pulumi.Input[FunctionEventTriggerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsTriggerSecurityLevel")
    def https_trigger_security_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @https_trigger_security_level.setter
    def https_trigger_security_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsTriggerUrl")
    def https_trigger_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @https_trigger_url.setter
    def https_trigger_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ingress_settings.setter
    def ingress_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_instances.setter
    def max_instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_instances.setter
    def min_instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDeployUpdatePolicy")
    def on_deploy_update_policy(self) -> Optional[pulumi.Input[FunctionOnDeployUpdatePolicyArgs]]:
        
        ...
    
    @on_deploy_update_policy.setter
    def on_deploy_update_policy(self, value: Optional[pulumi.Input[FunctionOnDeployUpdatePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnvironmentVariables")
    def secret_environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretEnvironmentVariableArgs]]]]:
        
        ...
    
    @secret_environment_variables.setter
    def secret_environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretEnvironmentVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVolumes")
    def secret_volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeArgs]]]]:
        
        ...
    
    @secret_volumes.setter
    def secret_volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArchiveBucket")
    def source_archive_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_archive_bucket.setter
    def source_archive_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArchiveObject")
    def source_archive_object(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_archive_object.setter
    def source_archive_object(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> Optional[pulumi.Input[FunctionSourceRepositoryArgs]]:
        
        ...
    
    @source_repository.setter
    def source_repository(self, value: Optional[pulumi.Input[FunctionSourceRepositoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerHttp")
    def trigger_http(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @trigger_http.setter
    def trigger_http(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnector")
    def vpc_connector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_connector.setter
    def vpc_connector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnectorEgressSettings")
    def vpc_connector_egress_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_connector_egress_settings.setter
    def vpc_connector_egress_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:cloudfunctions/function:Function")
class Function(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., automatic_update_policy: Optional[pulumi.Input[Union[FunctionAutomaticUpdatePolicyArgs, FunctionAutomaticUpdatePolicyArgsDict]]] = ..., available_memory_mb: Optional[pulumi.Input[_builtins.int]] = ..., build_environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., build_service_account: Optional[pulumi.Input[_builtins.str]] = ..., build_worker_pool: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., docker_registry: Optional[pulumi.Input[_builtins.str]] = ..., docker_repository: Optional[pulumi.Input[_builtins.str]] = ..., entry_point: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., event_trigger: Optional[pulumi.Input[Union[FunctionEventTriggerArgs, FunctionEventTriggerArgsDict]]] = ..., https_trigger_security_level: Optional[pulumi.Input[_builtins.str]] = ..., https_trigger_url: Optional[pulumi.Input[_builtins.str]] = ..., ingress_settings: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., max_instances: Optional[pulumi.Input[_builtins.int]] = ..., min_instances: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., on_deploy_update_policy: Optional[pulumi.Input[Union[FunctionOnDeployUpdatePolicyArgs, FunctionOnDeployUpdatePolicyArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime: Optional[pulumi.Input[_builtins.str]] = ..., secret_environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FunctionSecretEnvironmentVariableArgs, FunctionSecretEnvironmentVariableArgsDict]]]]] = ..., secret_volumes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FunctionSecretVolumeArgs, FunctionSecretVolumeArgsDict]]]]] = ..., service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., source_archive_bucket: Optional[pulumi.Input[_builtins.str]] = ..., source_archive_object: Optional[pulumi.Input[_builtins.str]] = ..., source_repository: Optional[pulumi.Input[Union[FunctionSourceRepositoryArgs, FunctionSourceRepositoryArgsDict]]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ..., trigger_http: Optional[pulumi.Input[_builtins.bool]] = ..., vpc_connector: Optional[pulumi.Input[_builtins.str]] = ..., vpc_connector_egress_settings: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FunctionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., automatic_update_policy: Optional[pulumi.Input[Union[FunctionAutomaticUpdatePolicyArgs, FunctionAutomaticUpdatePolicyArgsDict]]] = ..., available_memory_mb: Optional[pulumi.Input[_builtins.int]] = ..., build_environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., build_service_account: Optional[pulumi.Input[_builtins.str]] = ..., build_worker_pool: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., docker_registry: Optional[pulumi.Input[_builtins.str]] = ..., docker_repository: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., entry_point: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., event_trigger: Optional[pulumi.Input[Union[FunctionEventTriggerArgs, FunctionEventTriggerArgsDict]]] = ..., https_trigger_security_level: Optional[pulumi.Input[_builtins.str]] = ..., https_trigger_url: Optional[pulumi.Input[_builtins.str]] = ..., ingress_settings: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., max_instances: Optional[pulumi.Input[_builtins.int]] = ..., min_instances: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., on_deploy_update_policy: Optional[pulumi.Input[Union[FunctionOnDeployUpdatePolicyArgs, FunctionOnDeployUpdatePolicyArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime: Optional[pulumi.Input[_builtins.str]] = ..., secret_environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FunctionSecretEnvironmentVariableArgs, FunctionSecretEnvironmentVariableArgsDict]]]]] = ..., secret_volumes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FunctionSecretVolumeArgs, FunctionSecretVolumeArgsDict]]]]] = ..., service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., source_archive_bucket: Optional[pulumi.Input[_builtins.str]] = ..., source_archive_object: Optional[pulumi.Input[_builtins.str]] = ..., source_repository: Optional[pulumi.Input[Union[FunctionSourceRepositoryArgs, FunctionSourceRepositoryArgsDict]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ..., trigger_http: Optional[pulumi.Input[_builtins.bool]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_connector: Optional[pulumi.Input[_builtins.str]] = ..., vpc_connector_egress_settings: Optional[pulumi.Input[_builtins.str]] = ...) -> Function:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticUpdatePolicy")
    def automatic_update_policy(self) -> pulumi.Output[outputs.FunctionAutomaticUpdatePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMemoryMb")
    def available_memory_mb(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildEnvironmentVariables")
    def build_environment_variables(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildServiceAccount")
    def build_service_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildWorkerPool")
    def build_worker_pool(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRegistry")
    def docker_registry(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTrigger")
    def event_trigger(self) -> pulumi.Output[outputs.FunctionEventTrigger]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsTriggerSecurityLevel")
    def https_trigger_security_level(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsTriggerUrl")
    def https_trigger_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDeployUpdatePolicy")
    def on_deploy_update_policy(self) -> pulumi.Output[Optional[outputs.FunctionOnDeployUpdatePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnvironmentVariables")
    def secret_environment_variables(self) -> pulumi.Output[Optional[Sequence[outputs.FunctionSecretEnvironmentVariable]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVolumes")
    def secret_volumes(self) -> pulumi.Output[Optional[Sequence[outputs.FunctionSecretVolume]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArchiveBucket")
    def source_archive_bucket(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArchiveObject")
    def source_archive_object(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> pulumi.Output[Optional[outputs.FunctionSourceRepository]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerHttp")
    def trigger_http(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnector")
    def vpc_connector(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnectorEgressSettings")
    def vpc_connector_egress_settings(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


