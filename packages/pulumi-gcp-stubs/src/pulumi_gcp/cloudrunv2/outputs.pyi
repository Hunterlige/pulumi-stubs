

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['JobBinaryAuthorization', 'JobCondition', 'JobIamBindingCondition', 'JobIamMemberCondition', 'JobLatestCreatedExecution', 'JobTemplate', 'JobTemplateTemplate', 'JobTemplateTemplateContainer', 'JobTemplateTemplateContainerEnv', 'JobTemplateTemplateContainerEnvValueSource', ..., 'JobTemplateTemplateContainerPort', 'JobTemplateTemplateContainerResources', 'JobTemplateTemplateContainerStartupProbe', 'JobTemplateTemplateContainerStartupProbeGrpc', 'JobTemplateTemplateContainerStartupProbeHttpGet', ..., 'JobTemplateTemplateContainerStartupProbeTcpSocket', 'JobTemplateTemplateContainerVolumeMount', 'JobTemplateTemplateNodeSelector', 'JobTemplateTemplateVolume', 'JobTemplateTemplateVolumeCloudSqlInstance', 'JobTemplateTemplateVolumeEmptyDir', 'JobTemplateTemplateVolumeGcs', 'JobTemplateTemplateVolumeNfs', 'JobTemplateTemplateVolumeSecret', 'JobTemplateTemplateVolumeSecretItem', 'JobTemplateTemplateVpcAccess', 'JobTemplateTemplateVpcAccessNetworkInterface', 'JobTerminalCondition', 'ServiceBinaryAuthorization', 'ServiceBuildConfig', 'ServiceCondition', 'ServiceIamBindingCondition', 'ServiceIamMemberCondition', 'ServiceMultiRegionSettings', 'ServiceScaling', 'ServiceTemplate', 'ServiceTemplateContainer', 'ServiceTemplateContainerBuildInfo', 'ServiceTemplateContainerEnv', 'ServiceTemplateContainerEnvValueSource', 'ServiceTemplateContainerEnvValueSourceSecretKeyRef', 'ServiceTemplateContainerLivenessProbe', 'ServiceTemplateContainerLivenessProbeGrpc', 'ServiceTemplateContainerLivenessProbeHttpGet', ..., 'ServiceTemplateContainerLivenessProbeTcpSocket', 'ServiceTemplateContainerPorts', 'ServiceTemplateContainerReadinessProbe', 'ServiceTemplateContainerReadinessProbeGrpc', 'ServiceTemplateContainerReadinessProbeHttpGet', 'ServiceTemplateContainerResources', 'ServiceTemplateContainerSourceCode', ..., 'ServiceTemplateContainerStartupProbe', 'ServiceTemplateContainerStartupProbeGrpc', 'ServiceTemplateContainerStartupProbeHttpGet', ..., 'ServiceTemplateContainerStartupProbeTcpSocket', 'ServiceTemplateContainerVolumeMount', 'ServiceTemplateNodeSelector', 'ServiceTemplateScaling', 'ServiceTemplateServiceMesh', 'ServiceTemplateVolume', 'ServiceTemplateVolumeCloudSqlInstance', 'ServiceTemplateVolumeEmptyDir', 'ServiceTemplateVolumeGcs', 'ServiceTemplateVolumeNfs', 'ServiceTemplateVolumeSecret', 'ServiceTemplateVolumeSecretItem', 'ServiceTemplateVpcAccess', 'ServiceTemplateVpcAccessNetworkInterface', 'ServiceTerminalCondition', 'ServiceTraffic', 'ServiceTrafficStatus', 'WorkerPoolBinaryAuthorization', 'WorkerPoolCondition', 'WorkerPoolIamBindingCondition', 'WorkerPoolIamMemberCondition', 'WorkerPoolInstanceSplit', 'WorkerPoolInstanceSplitStatus', 'WorkerPoolScaling', 'WorkerPoolTemplate', 'WorkerPoolTemplateContainer', 'WorkerPoolTemplateContainerEnv', 'WorkerPoolTemplateContainerEnvValueSource', ..., 'WorkerPoolTemplateContainerLivenessProbe', 'WorkerPoolTemplateContainerLivenessProbeGrpc', 'WorkerPoolTemplateContainerLivenessProbeHttpGet', ..., 'WorkerPoolTemplateContainerLivenessProbeTcpSocket', 'WorkerPoolTemplateContainerResources', 'WorkerPoolTemplateContainerStartupProbe', 'WorkerPoolTemplateContainerStartupProbeGrpc', 'WorkerPoolTemplateContainerStartupProbeHttpGet', ..., 'WorkerPoolTemplateContainerStartupProbeTcpSocket', 'WorkerPoolTemplateContainerVolumeMount', 'WorkerPoolTemplateNodeSelector', 'WorkerPoolTemplateVolume', 'WorkerPoolTemplateVolumeCloudSqlInstance', 'WorkerPoolTemplateVolumeEmptyDir', 'WorkerPoolTemplateVolumeGcs', 'WorkerPoolTemplateVolumeNfs', 'WorkerPoolTemplateVolumeSecret', 'WorkerPoolTemplateVolumeSecretItem', 'WorkerPoolTemplateVpcAccess', 'WorkerPoolTemplateVpcAccessNetworkInterface', 'WorkerPoolTerminalCondition', 'GetJobBinaryAuthorizationResult', 'GetJobConditionResult', 'GetJobLatestCreatedExecutionResult', 'GetJobTemplateResult', 'GetJobTemplateTemplateResult', 'GetJobTemplateTemplateContainerResult', 'GetJobTemplateTemplateContainerEnvResult', ..., ..., 'GetJobTemplateTemplateContainerPortResult', 'GetJobTemplateTemplateContainerResourceResult', 'GetJobTemplateTemplateContainerStartupProbeResult', ..., ..., ..., ..., 'GetJobTemplateTemplateContainerVolumeMountResult', 'GetJobTemplateTemplateNodeSelectorResult', 'GetJobTemplateTemplateVolumeResult', 'GetJobTemplateTemplateVolumeCloudSqlInstanceResult', 'GetJobTemplateTemplateVolumeEmptyDirResult', 'GetJobTemplateTemplateVolumeGcResult', 'GetJobTemplateTemplateVolumeNfResult', 'GetJobTemplateTemplateVolumeSecretResult', 'GetJobTemplateTemplateVolumeSecretItemResult', 'GetJobTemplateTemplateVpcAccessResult', ..., 'GetJobTerminalConditionResult', 'GetServiceBinaryAuthorizationResult', 'GetServiceBuildConfigResult', 'GetServiceConditionResult', 'GetServiceMultiRegionSettingResult', 'GetServiceScalingResult', 'GetServiceTemplateResult', 'GetServiceTemplateContainerResult', 'GetServiceTemplateContainerBuildInfoResult', 'GetServiceTemplateContainerEnvResult', 'GetServiceTemplateContainerEnvValueSourceResult', ..., 'GetServiceTemplateContainerLivenessProbeResult', 'GetServiceTemplateContainerLivenessProbeGrpcResult', ..., ..., ..., 'GetServiceTemplateContainerPortResult', 'GetServiceTemplateContainerReadinessProbeResult', ..., ..., 'GetServiceTemplateContainerResourceResult', 'GetServiceTemplateContainerSourceCodeResult', ..., 'GetServiceTemplateContainerStartupProbeResult', 'GetServiceTemplateContainerStartupProbeGrpcResult', ..., ..., ..., 'GetServiceTemplateContainerVolumeMountResult', 'GetServiceTemplateNodeSelectorResult', 'GetServiceTemplateScalingResult', 'GetServiceTemplateServiceMeshResult', 'GetServiceTemplateVolumeResult', 'GetServiceTemplateVolumeCloudSqlInstanceResult', 'GetServiceTemplateVolumeEmptyDirResult', 'GetServiceTemplateVolumeGcResult', 'GetServiceTemplateVolumeNfResult', 'GetServiceTemplateVolumeSecretResult', 'GetServiceTemplateVolumeSecretItemResult', 'GetServiceTemplateVpcAccessResult', 'GetServiceTemplateVpcAccessNetworkInterfaceResult', 'GetServiceTerminalConditionResult', 'GetServiceTrafficResult', 'GetServiceTrafficStatusResult', 'GetWorkerPoolBinaryAuthorizationResult', 'GetWorkerPoolConditionResult', 'GetWorkerPoolInstanceSplitResult', 'GetWorkerPoolInstanceSplitStatusResult', 'GetWorkerPoolScalingResult', 'GetWorkerPoolTemplateResult', 'GetWorkerPoolTemplateContainerResult', 'GetWorkerPoolTemplateContainerEnvResult', 'GetWorkerPoolTemplateContainerEnvValueSourceResult', ..., 'GetWorkerPoolTemplateContainerLivenessProbeResult', ..., ..., ..., ..., 'GetWorkerPoolTemplateContainerResourceResult', 'GetWorkerPoolTemplateContainerStartupProbeResult', ..., ..., ..., ..., 'GetWorkerPoolTemplateContainerVolumeMountResult', 'GetWorkerPoolTemplateNodeSelectorResult', 'GetWorkerPoolTemplateVolumeResult', 'GetWorkerPoolTemplateVolumeCloudSqlInstanceResult', 'GetWorkerPoolTemplateVolumeEmptyDirResult', 'GetWorkerPoolTemplateVolumeGcResult', 'GetWorkerPoolTemplateVolumeNfResult', 'GetWorkerPoolTemplateVolumeSecretResult', 'GetWorkerPoolTemplateVolumeSecretItemResult', 'GetWorkerPoolTemplateVpcAccessResult', ..., 'GetWorkerPoolTerminalConditionResult']
@pulumi.output_type
class JobBinaryAuthorization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, breakglass_justification: Optional[_builtins.str] = ..., policy: Optional[_builtins.str] = ..., use_default: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="breakglassJustification")
    def breakglass_justification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefault")
    def use_default(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class JobCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_reason: Optional[_builtins.str] = ..., last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., revision_reason: Optional[_builtins.str] = ..., severity: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class JobIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class JobLatestCreatedExecution(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, completion_time: Optional[_builtins.str] = ..., create_time: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completionTime")
    def completion_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, template: outputs.JobTemplateTemplate, annotations: Optional[Mapping[str, _builtins.str]] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., parallelism: Optional[_builtins.int] = ..., task_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> outputs.JobTemplateTemplate:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, containers: Optional[Sequence[outputs.JobTemplateTemplateContainer]] = ..., encryption_key: Optional[_builtins.str] = ..., execution_environment: Optional[_builtins.str] = ..., gpu_zonal_redundancy_disabled: Optional[_builtins.bool] = ..., max_retries: Optional[_builtins.int] = ..., node_selector: Optional[outputs.JobTemplateTemplateNodeSelector] = ..., service_account: Optional[_builtins.str] = ..., timeout: Optional[_builtins.str] = ..., volumes: Optional[Sequence[outputs.JobTemplateTemplateVolume]] = ..., vpc_access: Optional[outputs.JobTemplateTemplateVpcAccess] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[Sequence[outputs.JobTemplateTemplateContainer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionEnvironment")
    def execution_environment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuZonalRedundancyDisabled")
    def gpu_zonal_redundancy_disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(self) -> Optional[outputs.JobTemplateTemplateNodeSelector]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.JobTemplateTemplateVolume]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccess")
    def vpc_access(self) -> Optional[outputs.JobTemplateTemplateVpcAccess]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image: _builtins.str, args: Optional[Sequence[_builtins.str]] = ..., commands: Optional[Sequence[_builtins.str]] = ..., depends_ons: Optional[Sequence[_builtins.str]] = ..., envs: Optional[Sequence[outputs.JobTemplateTemplateContainerEnv]] = ..., name: Optional[_builtins.str] = ..., ports: Optional[Sequence[outputs.JobTemplateTemplateContainerPort]] = ..., resources: Optional[outputs.JobTemplateTemplateContainerResources] = ..., startup_probe: Optional[outputs.JobTemplateTemplateContainerStartupProbe] = ..., volume_mounts: Optional[Sequence[outputs.JobTemplateTemplateContainerVolumeMount]] = ..., working_dir: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[Sequence[outputs.JobTemplateTemplateContainerEnv]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[outputs.JobTemplateTemplateContainerPort]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[outputs.JobTemplateTemplateContainerResources]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(self) -> Optional[outputs.JobTemplateTemplateContainerStartupProbe]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[Sequence[outputs.JobTemplateTemplateContainerVolumeMount]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerEnv(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value: Optional[_builtins.str] = ..., value_source: Optional[outputs.JobTemplateTemplateContainerEnvValueSource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSource")
    def value_source(self) -> Optional[outputs.JobTemplateTemplateContainerEnvValueSource]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerEnvValueSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret_key_ref: Optional[outputs.JobTemplateTemplateContainerEnvValueSourceSecretKeyRef] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKeyRef")
    def secret_key_ref(self) -> Optional[outputs.JobTemplateTemplateContainerEnvValueSourceSecretKeyRef]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerEnvValueSourceSecretKeyRef(dict):
    def __init__(__self__, *, secret: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerPort(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_port: Optional[_builtins.int] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerResources(dict):
    def __init__(__self__, *, limits: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerStartupProbe(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_threshold: Optional[_builtins.int] = ..., grpc: Optional[outputs.JobTemplateTemplateContainerStartupProbeGrpc] = ..., http_get: Optional[outputs.JobTemplateTemplateContainerStartupProbeHttpGet] = ..., initial_delay_seconds: Optional[_builtins.int] = ..., period_seconds: Optional[_builtins.int] = ..., tcp_socket: Optional[outputs.JobTemplateTemplateContainerStartupProbeTcpSocket] = ..., timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpc(self) -> Optional[outputs.JobTemplateTemplateContainerStartupProbeGrpc]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[outputs.JobTemplateTemplateContainerStartupProbeHttpGet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(self) -> Optional[outputs.JobTemplateTemplateContainerStartupProbeTcpSocket]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerStartupProbeGrpc(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ..., service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerStartupProbeHttpGet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_headers: Optional[Sequence[outputs.JobTemplateTemplateContainerStartupProbeHttpGetHttpHeader]] = ..., path: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Sequence[outputs.JobTemplateTemplateContainerStartupProbeHttpGetHttpHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerStartupProbeHttpGetHttpHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerStartupProbeTcpSocket(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateContainerVolumeMount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mount_path: _builtins.str, name: _builtins.str, sub_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateNodeSelector(dict):
    def __init__(__self__, *, accelerator: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerator(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateVolume(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, cloud_sql_instance: Optional[outputs.JobTemplateTemplateVolumeCloudSqlInstance] = ..., empty_dir: Optional[outputs.JobTemplateTemplateVolumeEmptyDir] = ..., gcs: Optional[outputs.JobTemplateTemplateVolumeGcs] = ..., nfs: Optional[outputs.JobTemplateTemplateVolumeNfs] = ..., secret: Optional[outputs.JobTemplateTemplateVolumeSecret] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(self) -> Optional[outputs.JobTemplateTemplateVolumeCloudSqlInstance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(self) -> Optional[outputs.JobTemplateTemplateVolumeEmptyDir]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Optional[outputs.JobTemplateTemplateVolumeGcs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[outputs.JobTemplateTemplateVolumeNfs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[outputs.JobTemplateTemplateVolumeSecret]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateVolumeCloudSqlInstance(dict):
    def __init__(__self__, *, instances: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateVolumeEmptyDir(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, medium: Optional[_builtins.str] = ..., size_limit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateVolumeGcs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: _builtins.str, mount_options: Optional[Sequence[_builtins.str]] = ..., read_only: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateVolumeNfs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, server: _builtins.str, path: Optional[_builtins.str] = ..., read_only: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateVolumeSecret(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret: _builtins.str, default_mode: Optional[_builtins.int] = ..., items: Optional[Sequence[outputs.JobTemplateTemplateVolumeSecretItem]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[outputs.JobTemplateTemplateVolumeSecretItem]]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateVolumeSecretItem(dict):
    def __init__(__self__, *, path: _builtins.str, version: _builtins.str, mode: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateVpcAccess(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connector: Optional[_builtins.str] = ..., egress: Optional[_builtins.str] = ..., network_interfaces: Optional[Sequence[outputs.JobTemplateTemplateVpcAccessNetworkInterface]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.JobTemplateTemplateVpcAccessNetworkInterface]]:
        
        ...
    


@pulumi.output_type
class JobTemplateTemplateVpcAccessNetworkInterface(dict):
    def __init__(__self__, *, network: Optional[_builtins.str] = ..., subnetwork: Optional[_builtins.str] = ..., tags: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobTerminalCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_reason: Optional[_builtins.str] = ..., last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., revision_reason: Optional[_builtins.str] = ..., severity: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceBinaryAuthorization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, breakglass_justification: Optional[_builtins.str] = ..., policy: Optional[_builtins.str] = ..., use_default: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="breakglassJustification")
    def breakglass_justification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefault")
    def use_default(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ServiceBuildConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, base_image: Optional[_builtins.str] = ..., enable_automatic_updates: Optional[_builtins.bool] = ..., environment_variables: Optional[Mapping[str, _builtins.str]] = ..., function_target: Optional[_builtins.str] = ..., image_uri: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., service_account: Optional[_builtins.str] = ..., source_location: Optional[_builtins.str] = ..., worker_pool: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpdates")
    def enable_automatic_updates(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionTarget")
    def function_target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_reason: Optional[_builtins.str] = ..., last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., revision_reason: Optional[_builtins.str] = ..., severity: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ServiceIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ServiceMultiRegionSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, multi_region_id: Optional[_builtins.str] = ..., regions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionId")
    def multi_region_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ServiceScaling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, manual_instance_count: Optional[_builtins.int] = ..., max_instance_count: Optional[_builtins.int] = ..., min_instance_count: Optional[_builtins.int] = ..., scaling_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualInstanceCount")
    def manual_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, annotations: Optional[Mapping[str, _builtins.str]] = ..., containers: Optional[Sequence[outputs.ServiceTemplateContainer]] = ..., encryption_key: Optional[_builtins.str] = ..., execution_environment: Optional[_builtins.str] = ..., gpu_zonal_redundancy_disabled: Optional[_builtins.bool] = ..., health_check_disabled: Optional[_builtins.bool] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., max_instance_request_concurrency: Optional[_builtins.int] = ..., node_selector: Optional[outputs.ServiceTemplateNodeSelector] = ..., revision: Optional[_builtins.str] = ..., scaling: Optional[outputs.ServiceTemplateScaling] = ..., service_account: Optional[_builtins.str] = ..., service_mesh: Optional[outputs.ServiceTemplateServiceMesh] = ..., session_affinity: Optional[_builtins.bool] = ..., timeout: Optional[_builtins.str] = ..., volumes: Optional[Sequence[outputs.ServiceTemplateVolume]] = ..., vpc_access: Optional[outputs.ServiceTemplateVpcAccess] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[Sequence[outputs.ServiceTemplateContainer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionEnvironment")
    def execution_environment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuZonalRedundancyDisabled")
    def gpu_zonal_redundancy_disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckDisabled")
    def health_check_disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceRequestConcurrency")
    def max_instance_request_concurrency(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(self) -> Optional[outputs.ServiceTemplateNodeSelector]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scaling(self) -> Optional[outputs.ServiceTemplateScaling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceMesh")
    def service_mesh(self) -> Optional[outputs.ServiceTemplateServiceMesh]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.ServiceTemplateVolume]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccess")
    def vpc_access(self) -> Optional[outputs.ServiceTemplateVpcAccess]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image: _builtins.str, args: Optional[Sequence[_builtins.str]] = ..., base_image_uri: Optional[_builtins.str] = ..., build_infos: Optional[Sequence[outputs.ServiceTemplateContainerBuildInfo]] = ..., commands: Optional[Sequence[_builtins.str]] = ..., depends_ons: Optional[Sequence[_builtins.str]] = ..., envs: Optional[Sequence[outputs.ServiceTemplateContainerEnv]] = ..., liveness_probe: Optional[outputs.ServiceTemplateContainerLivenessProbe] = ..., name: Optional[_builtins.str] = ..., ports: Optional[outputs.ServiceTemplateContainerPorts] = ..., readiness_probe: Optional[outputs.ServiceTemplateContainerReadinessProbe] = ..., resources: Optional[outputs.ServiceTemplateContainerResources] = ..., source_code: Optional[outputs.ServiceTemplateContainerSourceCode] = ..., startup_probe: Optional[outputs.ServiceTemplateContainerStartupProbe] = ..., volume_mounts: Optional[Sequence[outputs.ServiceTemplateContainerVolumeMount]] = ..., working_dir: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseImageUri")
    def base_image_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildInfos")
    def build_infos(self) -> Optional[Sequence[outputs.ServiceTemplateContainerBuildInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[Sequence[outputs.ServiceTemplateContainerEnv]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(self) -> Optional[outputs.ServiceTemplateContainerLivenessProbe]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[outputs.ServiceTemplateContainerPorts]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(self) -> Optional[outputs.ServiceTemplateContainerReadinessProbe]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[outputs.ServiceTemplateContainerResources]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCode")
    def source_code(self) -> Optional[outputs.ServiceTemplateContainerSourceCode]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(self) -> Optional[outputs.ServiceTemplateContainerStartupProbe]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[Sequence[outputs.ServiceTemplateContainerVolumeMount]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerBuildInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, function_target: Optional[_builtins.str] = ..., source_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionTarget")
    def function_target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerEnv(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value: Optional[_builtins.str] = ..., value_source: Optional[outputs.ServiceTemplateContainerEnvValueSource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSource")
    def value_source(self) -> Optional[outputs.ServiceTemplateContainerEnvValueSource]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerEnvValueSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret_key_ref: Optional[outputs.ServiceTemplateContainerEnvValueSourceSecretKeyRef] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKeyRef")
    def secret_key_ref(self) -> Optional[outputs.ServiceTemplateContainerEnvValueSourceSecretKeyRef]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerEnvValueSourceSecretKeyRef(dict):
    def __init__(__self__, *, secret: _builtins.str, version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerLivenessProbe(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_threshold: Optional[_builtins.int] = ..., grpc: Optional[outputs.ServiceTemplateContainerLivenessProbeGrpc] = ..., http_get: Optional[outputs.ServiceTemplateContainerLivenessProbeHttpGet] = ..., initial_delay_seconds: Optional[_builtins.int] = ..., period_seconds: Optional[_builtins.int] = ..., tcp_socket: Optional[outputs.ServiceTemplateContainerLivenessProbeTcpSocket] = ..., timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpc(self) -> Optional[outputs.ServiceTemplateContainerLivenessProbeGrpc]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[outputs.ServiceTemplateContainerLivenessProbeHttpGet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(self) -> Optional[outputs.ServiceTemplateContainerLivenessProbeTcpSocket]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerLivenessProbeGrpc(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ..., service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerLivenessProbeHttpGet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_headers: Optional[Sequence[outputs.ServiceTemplateContainerLivenessProbeHttpGetHttpHeader]] = ..., path: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Sequence[outputs.ServiceTemplateContainerLivenessProbeHttpGetHttpHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerLivenessProbeHttpGetHttpHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerLivenessProbeTcpSocket(dict):
    def __init__(__self__, *, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerPorts(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_port: Optional[_builtins.int] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerReadinessProbe(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_threshold: Optional[_builtins.int] = ..., grpc: Optional[outputs.ServiceTemplateContainerReadinessProbeGrpc] = ..., http_get: Optional[outputs.ServiceTemplateContainerReadinessProbeHttpGet] = ..., period_seconds: Optional[_builtins.int] = ..., success_threshold: Optional[_builtins.int] = ..., timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpc(self) -> Optional[outputs.ServiceTemplateContainerReadinessProbeGrpc]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[outputs.ServiceTemplateContainerReadinessProbeHttpGet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerReadinessProbeGrpc(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ..., service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerReadinessProbeHttpGet(dict):
    def __init__(__self__, *, path: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerResources(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_idle: Optional[_builtins.bool] = ..., limits: Optional[Mapping[str, _builtins.str]] = ..., startup_cpu_boost: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuIdle")
    def cpu_idle(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startupCpuBoost")
    def startup_cpu_boost(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerSourceCode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_source: Optional[outputs.ServiceTemplateContainerSourceCodeCloudStorageSource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageSource")
    def cloud_storage_source(self) -> Optional[outputs.ServiceTemplateContainerSourceCodeCloudStorageSource]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerSourceCodeCloudStorageSource(dict):
    def __init__(__self__, *, bucket: _builtins.str, object: _builtins.str, generation: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerStartupProbe(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_threshold: Optional[_builtins.int] = ..., grpc: Optional[outputs.ServiceTemplateContainerStartupProbeGrpc] = ..., http_get: Optional[outputs.ServiceTemplateContainerStartupProbeHttpGet] = ..., initial_delay_seconds: Optional[_builtins.int] = ..., period_seconds: Optional[_builtins.int] = ..., tcp_socket: Optional[outputs.ServiceTemplateContainerStartupProbeTcpSocket] = ..., timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpc(self) -> Optional[outputs.ServiceTemplateContainerStartupProbeGrpc]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[outputs.ServiceTemplateContainerStartupProbeHttpGet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(self) -> Optional[outputs.ServiceTemplateContainerStartupProbeTcpSocket]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerStartupProbeGrpc(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ..., service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerStartupProbeHttpGet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_headers: Optional[Sequence[outputs.ServiceTemplateContainerStartupProbeHttpGetHttpHeader]] = ..., path: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Sequence[outputs.ServiceTemplateContainerStartupProbeHttpGetHttpHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerStartupProbeHttpGetHttpHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerStartupProbeTcpSocket(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateContainerVolumeMount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mount_path: _builtins.str, name: _builtins.str, sub_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateNodeSelector(dict):
    def __init__(__self__, *, accelerator: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerator(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceTemplateScaling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_instance_count: Optional[_builtins.int] = ..., min_instance_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateServiceMesh(dict):
    def __init__(__self__, *, mesh: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mesh(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateVolume(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, cloud_sql_instance: Optional[outputs.ServiceTemplateVolumeCloudSqlInstance] = ..., empty_dir: Optional[outputs.ServiceTemplateVolumeEmptyDir] = ..., gcs: Optional[outputs.ServiceTemplateVolumeGcs] = ..., nfs: Optional[outputs.ServiceTemplateVolumeNfs] = ..., secret: Optional[outputs.ServiceTemplateVolumeSecret] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(self) -> Optional[outputs.ServiceTemplateVolumeCloudSqlInstance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(self) -> Optional[outputs.ServiceTemplateVolumeEmptyDir]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Optional[outputs.ServiceTemplateVolumeGcs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[outputs.ServiceTemplateVolumeNfs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[outputs.ServiceTemplateVolumeSecret]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateVolumeCloudSqlInstance(dict):
    def __init__(__self__, *, instances: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateVolumeEmptyDir(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, medium: Optional[_builtins.str] = ..., size_limit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateVolumeGcs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: _builtins.str, mount_options: Optional[Sequence[_builtins.str]] = ..., read_only: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateVolumeNfs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, server: _builtins.str, read_only: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateVolumeSecret(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret: _builtins.str, default_mode: Optional[_builtins.int] = ..., items: Optional[Sequence[outputs.ServiceTemplateVolumeSecretItem]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[outputs.ServiceTemplateVolumeSecretItem]]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateVolumeSecretItem(dict):
    def __init__(__self__, *, path: _builtins.str, mode: Optional[_builtins.int] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateVpcAccess(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connector: Optional[_builtins.str] = ..., egress: Optional[_builtins.str] = ..., network_interfaces: Optional[Sequence[outputs.ServiceTemplateVpcAccessNetworkInterface]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.ServiceTemplateVpcAccessNetworkInterface]]:
        
        ...
    


@pulumi.output_type
class ServiceTemplateVpcAccessNetworkInterface(dict):
    def __init__(__self__, *, network: Optional[_builtins.str] = ..., subnetwork: Optional[_builtins.str] = ..., tags: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ServiceTerminalCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_reason: Optional[_builtins.str] = ..., last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., revision_reason: Optional[_builtins.str] = ..., severity: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTraffic(dict):
    def __init__(__self__, *, percent: Optional[_builtins.int] = ..., revision: Optional[_builtins.str] = ..., tag: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceTrafficStatus(dict):
    def __init__(__self__, *, percent: Optional[_builtins.int] = ..., revision: Optional[_builtins.str] = ..., tag: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolBinaryAuthorization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, breakglass_justification: Optional[_builtins.str] = ..., policy: Optional[_builtins.str] = ..., use_default: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="breakglassJustification")
    def breakglass_justification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefault")
    def use_default(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WorkerPoolCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_reason: Optional[_builtins.str] = ..., last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., revision_reason: Optional[_builtins.str] = ..., severity: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class WorkerPoolIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class WorkerPoolInstanceSplit(dict):
    def __init__(__self__, *, percent: Optional[_builtins.int] = ..., revision: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolInstanceSplitStatus(dict):
    def __init__(__self__, *, percent: Optional[_builtins.int] = ..., revision: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolScaling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, manual_instance_count: Optional[_builtins.int] = ..., max_instance_count: Optional[_builtins.int] = ..., min_instance_count: Optional[_builtins.int] = ..., scaling_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualInstanceCount")
    def manual_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, annotations: Optional[Mapping[str, _builtins.str]] = ..., containers: Optional[Sequence[outputs.WorkerPoolTemplateContainer]] = ..., encryption_key: Optional[_builtins.str] = ..., encryption_key_revocation_action: Optional[_builtins.str] = ..., encryption_key_shutdown_duration: Optional[_builtins.str] = ..., gpu_zonal_redundancy_disabled: Optional[_builtins.bool] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., node_selector: Optional[outputs.WorkerPoolTemplateNodeSelector] = ..., revision: Optional[_builtins.str] = ..., service_account: Optional[_builtins.str] = ..., volumes: Optional[Sequence[outputs.WorkerPoolTemplateVolume]] = ..., vpc_access: Optional[outputs.WorkerPoolTemplateVpcAccess] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[Sequence[outputs.WorkerPoolTemplateContainer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyRevocationAction")
    def encryption_key_revocation_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyShutdownDuration")
    def encryption_key_shutdown_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuZonalRedundancyDisabled")
    def gpu_zonal_redundancy_disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(self) -> Optional[outputs.WorkerPoolTemplateNodeSelector]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.WorkerPoolTemplateVolume]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccess")
    def vpc_access(self) -> Optional[outputs.WorkerPoolTemplateVpcAccess]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image: _builtins.str, args: Optional[Sequence[_builtins.str]] = ..., commands: Optional[Sequence[_builtins.str]] = ..., depends_ons: Optional[Sequence[_builtins.str]] = ..., envs: Optional[Sequence[outputs.WorkerPoolTemplateContainerEnv]] = ..., liveness_probe: Optional[outputs.WorkerPoolTemplateContainerLivenessProbe] = ..., name: Optional[_builtins.str] = ..., resources: Optional[outputs.WorkerPoolTemplateContainerResources] = ..., startup_probe: Optional[outputs.WorkerPoolTemplateContainerStartupProbe] = ..., volume_mounts: Optional[Sequence[outputs.WorkerPoolTemplateContainerVolumeMount]] = ..., working_dir: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[Sequence[outputs.WorkerPoolTemplateContainerEnv]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(self) -> Optional[outputs.WorkerPoolTemplateContainerLivenessProbe]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[outputs.WorkerPoolTemplateContainerResources]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(self) -> Optional[outputs.WorkerPoolTemplateContainerStartupProbe]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[Sequence[outputs.WorkerPoolTemplateContainerVolumeMount]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerEnv(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value: Optional[_builtins.str] = ..., value_source: Optional[outputs.WorkerPoolTemplateContainerEnvValueSource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSource")
    def value_source(self) -> Optional[outputs.WorkerPoolTemplateContainerEnvValueSource]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerEnvValueSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret_key_ref: Optional[outputs.WorkerPoolTemplateContainerEnvValueSourceSecretKeyRef] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKeyRef")
    def secret_key_ref(self) -> Optional[outputs.WorkerPoolTemplateContainerEnvValueSourceSecretKeyRef]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerEnvValueSourceSecretKeyRef(dict):
    def __init__(__self__, *, secret: _builtins.str, version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerLivenessProbe(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_threshold: Optional[_builtins.int] = ..., grpc: Optional[outputs.WorkerPoolTemplateContainerLivenessProbeGrpc] = ..., http_get: Optional[outputs.WorkerPoolTemplateContainerLivenessProbeHttpGet] = ..., initial_delay_seconds: Optional[_builtins.int] = ..., period_seconds: Optional[_builtins.int] = ..., tcp_socket: Optional[outputs.WorkerPoolTemplateContainerLivenessProbeTcpSocket] = ..., timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpc(self) -> Optional[outputs.WorkerPoolTemplateContainerLivenessProbeGrpc]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[outputs.WorkerPoolTemplateContainerLivenessProbeHttpGet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(self) -> Optional[outputs.WorkerPoolTemplateContainerLivenessProbeTcpSocket]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerLivenessProbeGrpc(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ..., service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerLivenessProbeHttpGet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_headers: Optional[outputs.WorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeaders] = ..., path: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[outputs.WorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeaders]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeaders(dict):
    def __init__(__self__, *, port: _builtins.int, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerLivenessProbeTcpSocket(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerResources(dict):
    def __init__(__self__, *, limits: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerStartupProbe(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_threshold: Optional[_builtins.int] = ..., grpc: Optional[outputs.WorkerPoolTemplateContainerStartupProbeGrpc] = ..., http_get: Optional[outputs.WorkerPoolTemplateContainerStartupProbeHttpGet] = ..., initial_delay_seconds: Optional[_builtins.int] = ..., period_seconds: Optional[_builtins.int] = ..., tcp_socket: Optional[outputs.WorkerPoolTemplateContainerStartupProbeTcpSocket] = ..., timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpc(self) -> Optional[outputs.WorkerPoolTemplateContainerStartupProbeGrpc]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[outputs.WorkerPoolTemplateContainerStartupProbeHttpGet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(self) -> Optional[outputs.WorkerPoolTemplateContainerStartupProbeTcpSocket]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerStartupProbeGrpc(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ..., service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerStartupProbeHttpGet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_headers: Optional[outputs.WorkerPoolTemplateContainerStartupProbeHttpGetHttpHeaders] = ..., path: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[outputs.WorkerPoolTemplateContainerStartupProbeHttpGetHttpHeaders]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerStartupProbeHttpGetHttpHeaders(dict):
    def __init__(__self__, *, port: _builtins.int, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerStartupProbeTcpSocket(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateContainerVolumeMount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mount_path: _builtins.str, name: _builtins.str, sub_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateNodeSelector(dict):
    def __init__(__self__, *, accelerator: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerator(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateVolume(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, cloud_sql_instance: Optional[outputs.WorkerPoolTemplateVolumeCloudSqlInstance] = ..., empty_dir: Optional[outputs.WorkerPoolTemplateVolumeEmptyDir] = ..., gcs: Optional[outputs.WorkerPoolTemplateVolumeGcs] = ..., nfs: Optional[outputs.WorkerPoolTemplateVolumeNfs] = ..., secret: Optional[outputs.WorkerPoolTemplateVolumeSecret] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(self) -> Optional[outputs.WorkerPoolTemplateVolumeCloudSqlInstance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(self) -> Optional[outputs.WorkerPoolTemplateVolumeEmptyDir]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Optional[outputs.WorkerPoolTemplateVolumeGcs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[outputs.WorkerPoolTemplateVolumeNfs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[outputs.WorkerPoolTemplateVolumeSecret]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateVolumeCloudSqlInstance(dict):
    def __init__(__self__, *, instances: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateVolumeEmptyDir(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, medium: Optional[_builtins.str] = ..., size_limit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateVolumeGcs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: _builtins.str, mount_options: Optional[Sequence[_builtins.str]] = ..., read_only: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateVolumeNfs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, server: _builtins.str, read_only: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateVolumeSecret(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret: _builtins.str, default_mode: Optional[_builtins.int] = ..., items: Optional[Sequence[outputs.WorkerPoolTemplateVolumeSecretItem]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[outputs.WorkerPoolTemplateVolumeSecretItem]]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateVolumeSecretItem(dict):
    def __init__(__self__, *, path: _builtins.str, mode: Optional[_builtins.int] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateVpcAccess(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connector: Optional[_builtins.str] = ..., egress: Optional[_builtins.str] = ..., network_interfaces: Optional[Sequence[outputs.WorkerPoolTemplateVpcAccessNetworkInterface]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.WorkerPoolTemplateVpcAccessNetworkInterface]]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTemplateVpcAccessNetworkInterface(dict):
    def __init__(__self__, *, network: Optional[_builtins.str] = ..., subnetwork: Optional[_builtins.str] = ..., tags: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkerPoolTerminalCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_reason: Optional[_builtins.str] = ..., last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., revision_reason: Optional[_builtins.str] = ..., severity: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetJobBinaryAuthorizationResult(dict):
    def __init__(__self__, *, breakglass_justification: _builtins.str, policy: _builtins.str, use_default: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="breakglassJustification")
    def breakglass_justification(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefault")
    def use_default(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetJobConditionResult(dict):
    def __init__(__self__, *, execution_reason: _builtins.str, last_transition_time: _builtins.str, message: _builtins.str, reason: _builtins.str, revision_reason: _builtins.str, severity: _builtins.str, state: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobLatestCreatedExecutionResult(dict):
    def __init__(__self__, *, completion_time: _builtins.str, create_time: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completionTime")
    def completion_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateResult(dict):
    def __init__(__self__, *, annotations: Mapping[str, _builtins.str], labels: Mapping[str, _builtins.str], parallelism: _builtins.int, task_count: _builtins.int, templates: Sequence[outputs.GetJobTemplateTemplateResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def templates(self) -> Sequence[outputs.GetJobTemplateTemplateResult]:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateResult(dict):
    def __init__(__self__, *, containers: Sequence[outputs.GetJobTemplateTemplateContainerResult], encryption_key: _builtins.str, execution_environment: _builtins.str, gpu_zonal_redundancy_disabled: _builtins.bool, max_retries: _builtins.int, node_selectors: Sequence[outputs.GetJobTemplateTemplateNodeSelectorResult], service_account: _builtins.str, timeout: _builtins.str, volumes: Sequence[outputs.GetJobTemplateTemplateVolumeResult], vpc_accesses: Sequence[outputs.GetJobTemplateTemplateVpcAccessResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Sequence[outputs.GetJobTemplateTemplateContainerResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionEnvironment")
    def execution_environment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuZonalRedundancyDisabled")
    def gpu_zonal_redundancy_disabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSelectors")
    def node_selectors(self) -> Sequence[outputs.GetJobTemplateTemplateNodeSelectorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Sequence[outputs.GetJobTemplateTemplateVolumeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccesses")
    def vpc_accesses(self) -> Sequence[outputs.GetJobTemplateTemplateVpcAccessResult]:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerResult(dict):
    def __init__(__self__, *, args: Sequence[_builtins.str], commands: Sequence[_builtins.str], depends_ons: Sequence[_builtins.str], envs: Sequence[outputs.GetJobTemplateTemplateContainerEnvResult], image: _builtins.str, name: _builtins.str, ports: Sequence[outputs.GetJobTemplateTemplateContainerPortResult], resources: Sequence[outputs.GetJobTemplateTemplateContainerResourceResult], startup_probes: Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeResult], volume_mounts: Sequence[outputs.GetJobTemplateTemplateContainerVolumeMountResult], working_dir: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Sequence[outputs.GetJobTemplateTemplateContainerEnvResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[outputs.GetJobTemplateTemplateContainerPortResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[outputs.GetJobTemplateTemplateContainerResourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startupProbes")
    def startup_probes(self) -> Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Sequence[outputs.GetJobTemplateTemplateContainerVolumeMountResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerEnvResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str, value_sources: Sequence[outputs.GetJobTemplateTemplateContainerEnvValueSourceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSources")
    def value_sources(self) -> Sequence[outputs.GetJobTemplateTemplateContainerEnvValueSourceResult]:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerEnvValueSourceResult(dict):
    def __init__(__self__, *, secret_key_reves: Sequence[outputs.GetJobTemplateTemplateContainerEnvValueSourceSecretKeyRefResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKeyReves")
    def secret_key_reves(self) -> Sequence[outputs.GetJobTemplateTemplateContainerEnvValueSourceSecretKeyRefResult]:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerEnvValueSourceSecretKeyRefResult(dict):
    def __init__(__self__, *, secret: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerPortResult(dict):
    def __init__(__self__, *, container_port: _builtins.int, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerResourceResult(dict):
    def __init__(__self__, *, limits: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerStartupProbeResult(dict):
    def __init__(__self__, *, failure_threshold: _builtins.int, grpcs: Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeGrpcResult], http_gets: Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeHttpGetResult], initial_delay_seconds: _builtins.int, period_seconds: _builtins.int, tcp_sockets: Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeTcpSocketResult], timeout_seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpcs(self) -> Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeGrpcResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGets")
    def http_gets(self) -> Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeHttpGetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSockets")
    def tcp_sockets(self) -> Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeTcpSocketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerStartupProbeGrpcResult(dict):
    def __init__(__self__, *, port: _builtins.int, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerStartupProbeHttpGetResult(dict):
    def __init__(__self__, *, http_headers: Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeHttpGetHttpHeaderResult], path: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Sequence[outputs.GetJobTemplateTemplateContainerStartupProbeHttpGetHttpHeaderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerStartupProbeHttpGetHttpHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerStartupProbeTcpSocketResult(dict):
    def __init__(__self__, *, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateContainerVolumeMountResult(dict):
    def __init__(__self__, *, mount_path: _builtins.str, name: _builtins.str, sub_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateNodeSelectorResult(dict):
    def __init__(__self__, *, accelerator: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerator(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateVolumeResult(dict):
    def __init__(__self__, *, cloud_sql_instances: Sequence[outputs.GetJobTemplateTemplateVolumeCloudSqlInstanceResult], empty_dirs: Sequence[outputs.GetJobTemplateTemplateVolumeEmptyDirResult], gcs: Sequence[outputs.GetJobTemplateTemplateVolumeGcResult], name: _builtins.str, nfs: Sequence[outputs.GetJobTemplateTemplateVolumeNfResult], secrets: Sequence[outputs.GetJobTemplateTemplateVolumeSecretResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstances")
    def cloud_sql_instances(self) -> Sequence[outputs.GetJobTemplateTemplateVolumeCloudSqlInstanceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emptyDirs")
    def empty_dirs(self) -> Sequence[outputs.GetJobTemplateTemplateVolumeEmptyDirResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Sequence[outputs.GetJobTemplateTemplateVolumeGcResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Sequence[outputs.GetJobTemplateTemplateVolumeNfResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Sequence[outputs.GetJobTemplateTemplateVolumeSecretResult]:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateVolumeCloudSqlInstanceResult(dict):
    def __init__(__self__, *, instances: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateVolumeEmptyDirResult(dict):
    def __init__(__self__, *, medium: _builtins.str, size_limit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def medium(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateVolumeGcResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, mount_options: Sequence[_builtins.str], read_only: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateVolumeNfResult(dict):
    def __init__(__self__, *, path: _builtins.str, read_only: _builtins.bool, server: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateVolumeSecretResult(dict):
    def __init__(__self__, *, default_mode: _builtins.int, items: Sequence[outputs.GetJobTemplateTemplateVolumeSecretItemResult], secret: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[outputs.GetJobTemplateTemplateVolumeSecretItemResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateVolumeSecretItemResult(dict):
    def __init__(__self__, *, mode: _builtins.int, path: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateVpcAccessResult(dict):
    def __init__(__self__, *, connector: _builtins.str, egress: _builtins.str, network_interfaces: Sequence[outputs.GetJobTemplateTemplateVpcAccessNetworkInterfaceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.GetJobTemplateTemplateVpcAccessNetworkInterfaceResult]:
        
        ...
    


@pulumi.output_type
class GetJobTemplateTemplateVpcAccessNetworkInterfaceResult(dict):
    def __init__(__self__, *, network: _builtins.str, subnetwork: _builtins.str, tags: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetJobTerminalConditionResult(dict):
    def __init__(__self__, *, execution_reason: _builtins.str, last_transition_time: _builtins.str, message: _builtins.str, reason: _builtins.str, revision_reason: _builtins.str, severity: _builtins.str, state: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceBinaryAuthorizationResult(dict):
    def __init__(__self__, *, breakglass_justification: _builtins.str, policy: _builtins.str, use_default: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="breakglassJustification")
    def breakglass_justification(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefault")
    def use_default(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetServiceBuildConfigResult(dict):
    def __init__(__self__, *, base_image: _builtins.str, enable_automatic_updates: _builtins.bool, environment_variables: Mapping[str, _builtins.str], function_target: _builtins.str, image_uri: _builtins.str, name: _builtins.str, service_account: _builtins.str, source_location: _builtins.str, worker_pool: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpdates")
    def enable_automatic_updates(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionTarget")
    def function_target(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceConditionResult(dict):
    def __init__(__self__, *, execution_reason: _builtins.str, last_transition_time: _builtins.str, message: _builtins.str, reason: _builtins.str, revision_reason: _builtins.str, severity: _builtins.str, state: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceMultiRegionSettingResult(dict):
    def __init__(__self__, *, multi_region_id: _builtins.str, regions: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiRegionId")
    def multi_region_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetServiceScalingResult(dict):
    def __init__(__self__, *, manual_instance_count: _builtins.int, max_instance_count: _builtins.int, min_instance_count: _builtins.int, scaling_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualInstanceCount")
    def manual_instance_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateResult(dict):
    def __init__(__self__, *, annotations: Mapping[str, _builtins.str], containers: Sequence[outputs.GetServiceTemplateContainerResult], encryption_key: _builtins.str, execution_environment: _builtins.str, gpu_zonal_redundancy_disabled: _builtins.bool, health_check_disabled: _builtins.bool, labels: Mapping[str, _builtins.str], max_instance_request_concurrency: _builtins.int, node_selectors: Sequence[outputs.GetServiceTemplateNodeSelectorResult], revision: _builtins.str, scalings: Sequence[outputs.GetServiceTemplateScalingResult], service_account: _builtins.str, service_meshes: Sequence[outputs.GetServiceTemplateServiceMeshResult], session_affinity: _builtins.bool, timeout: _builtins.str, volumes: Sequence[outputs.GetServiceTemplateVolumeResult], vpc_accesses: Sequence[outputs.GetServiceTemplateVpcAccessResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Sequence[outputs.GetServiceTemplateContainerResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionEnvironment")
    def execution_environment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuZonalRedundancyDisabled")
    def gpu_zonal_redundancy_disabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckDisabled")
    def health_check_disabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceRequestConcurrency")
    def max_instance_request_concurrency(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSelectors")
    def node_selectors(self) -> Sequence[outputs.GetServiceTemplateNodeSelectorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scalings(self) -> Sequence[outputs.GetServiceTemplateScalingResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceMeshes")
    def service_meshes(self) -> Sequence[outputs.GetServiceTemplateServiceMeshResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Sequence[outputs.GetServiceTemplateVolumeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccesses")
    def vpc_accesses(self) -> Sequence[outputs.GetServiceTemplateVpcAccessResult]:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerResult(dict):
    def __init__(__self__, *, args: Sequence[_builtins.str], base_image_uri: _builtins.str, build_infos: Sequence[outputs.GetServiceTemplateContainerBuildInfoResult], commands: Sequence[_builtins.str], depends_ons: Sequence[_builtins.str], envs: Sequence[outputs.GetServiceTemplateContainerEnvResult], image: _builtins.str, liveness_probes: Sequence[outputs.GetServiceTemplateContainerLivenessProbeResult], name: _builtins.str, ports: Sequence[outputs.GetServiceTemplateContainerPortResult], readiness_probes: Sequence[outputs.GetServiceTemplateContainerReadinessProbeResult], resources: Sequence[outputs.GetServiceTemplateContainerResourceResult], source_codes: Sequence[outputs.GetServiceTemplateContainerSourceCodeResult], startup_probes: Sequence[outputs.GetServiceTemplateContainerStartupProbeResult], volume_mounts: Sequence[outputs.GetServiceTemplateContainerVolumeMountResult], working_dir: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseImageUri")
    def base_image_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildInfos")
    def build_infos(self) -> Sequence[outputs.GetServiceTemplateContainerBuildInfoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Sequence[outputs.GetServiceTemplateContainerEnvResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="livenessProbes")
    def liveness_probes(self) -> Sequence[outputs.GetServiceTemplateContainerLivenessProbeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[outputs.GetServiceTemplateContainerPortResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readinessProbes")
    def readiness_probes(self) -> Sequence[outputs.GetServiceTemplateContainerReadinessProbeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[outputs.GetServiceTemplateContainerResourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCodes")
    def source_codes(self) -> Sequence[outputs.GetServiceTemplateContainerSourceCodeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startupProbes")
    def startup_probes(self) -> Sequence[outputs.GetServiceTemplateContainerStartupProbeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Sequence[outputs.GetServiceTemplateContainerVolumeMountResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerBuildInfoResult(dict):
    def __init__(__self__, *, function_target: _builtins.str, source_location: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionTarget")
    def function_target(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerEnvResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str, value_sources: Sequence[outputs.GetServiceTemplateContainerEnvValueSourceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSources")
    def value_sources(self) -> Sequence[outputs.GetServiceTemplateContainerEnvValueSourceResult]:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerEnvValueSourceResult(dict):
    def __init__(__self__, *, secret_key_reves: Sequence[outputs.GetServiceTemplateContainerEnvValueSourceSecretKeyRefResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKeyReves")
    def secret_key_reves(self) -> Sequence[outputs.GetServiceTemplateContainerEnvValueSourceSecretKeyRefResult]:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerEnvValueSourceSecretKeyRefResult(dict):
    def __init__(__self__, *, secret: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerLivenessProbeResult(dict):
    def __init__(__self__, *, failure_threshold: _builtins.int, grpcs: Sequence[outputs.GetServiceTemplateContainerLivenessProbeGrpcResult], http_gets: Sequence[outputs.GetServiceTemplateContainerLivenessProbeHttpGetResult], initial_delay_seconds: _builtins.int, period_seconds: _builtins.int, tcp_sockets: Sequence[outputs.GetServiceTemplateContainerLivenessProbeTcpSocketResult], timeout_seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpcs(self) -> Sequence[outputs.GetServiceTemplateContainerLivenessProbeGrpcResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGets")
    def http_gets(self) -> Sequence[outputs.GetServiceTemplateContainerLivenessProbeHttpGetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSockets")
    def tcp_sockets(self) -> Sequence[outputs.GetServiceTemplateContainerLivenessProbeTcpSocketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerLivenessProbeGrpcResult(dict):
    def __init__(__self__, *, port: _builtins.int, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerLivenessProbeHttpGetResult(dict):
    def __init__(__self__, *, http_headers: Sequence[outputs.GetServiceTemplateContainerLivenessProbeHttpGetHttpHeaderResult], path: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Sequence[outputs.GetServiceTemplateContainerLivenessProbeHttpGetHttpHeaderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerLivenessProbeHttpGetHttpHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerLivenessProbeTcpSocketResult(dict):
    def __init__(__self__, *, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerPortResult(dict):
    def __init__(__self__, *, container_port: _builtins.int, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerReadinessProbeResult(dict):
    def __init__(__self__, *, failure_threshold: _builtins.int, grpcs: Sequence[outputs.GetServiceTemplateContainerReadinessProbeGrpcResult], http_gets: Sequence[outputs.GetServiceTemplateContainerReadinessProbeHttpGetResult], period_seconds: _builtins.int, success_threshold: _builtins.int, timeout_seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpcs(self) -> Sequence[outputs.GetServiceTemplateContainerReadinessProbeGrpcResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGets")
    def http_gets(self) -> Sequence[outputs.GetServiceTemplateContainerReadinessProbeHttpGetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerReadinessProbeGrpcResult(dict):
    def __init__(__self__, *, port: _builtins.int, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerReadinessProbeHttpGetResult(dict):
    def __init__(__self__, *, path: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerResourceResult(dict):
    def __init__(__self__, *, cpu_idle: _builtins.bool, limits: Mapping[str, _builtins.str], startup_cpu_boost: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuIdle")
    def cpu_idle(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startupCpuBoost")
    def startup_cpu_boost(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerSourceCodeResult(dict):
    def __init__(__self__, *, cloud_storage_sources: Sequence[outputs.GetServiceTemplateContainerSourceCodeCloudStorageSourceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageSources")
    def cloud_storage_sources(self) -> Sequence[outputs.GetServiceTemplateContainerSourceCodeCloudStorageSourceResult]:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerSourceCodeCloudStorageSourceResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, generation: _builtins.str, object: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerStartupProbeResult(dict):
    def __init__(__self__, *, failure_threshold: _builtins.int, grpcs: Sequence[outputs.GetServiceTemplateContainerStartupProbeGrpcResult], http_gets: Sequence[outputs.GetServiceTemplateContainerStartupProbeHttpGetResult], initial_delay_seconds: _builtins.int, period_seconds: _builtins.int, tcp_sockets: Sequence[outputs.GetServiceTemplateContainerStartupProbeTcpSocketResult], timeout_seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpcs(self) -> Sequence[outputs.GetServiceTemplateContainerStartupProbeGrpcResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGets")
    def http_gets(self) -> Sequence[outputs.GetServiceTemplateContainerStartupProbeHttpGetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSockets")
    def tcp_sockets(self) -> Sequence[outputs.GetServiceTemplateContainerStartupProbeTcpSocketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerStartupProbeGrpcResult(dict):
    def __init__(__self__, *, port: _builtins.int, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerStartupProbeHttpGetResult(dict):
    def __init__(__self__, *, http_headers: Sequence[outputs.GetServiceTemplateContainerStartupProbeHttpGetHttpHeaderResult], path: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Sequence[outputs.GetServiceTemplateContainerStartupProbeHttpGetHttpHeaderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerStartupProbeHttpGetHttpHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerStartupProbeTcpSocketResult(dict):
    def __init__(__self__, *, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateContainerVolumeMountResult(dict):
    def __init__(__self__, *, mount_path: _builtins.str, name: _builtins.str, sub_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateNodeSelectorResult(dict):
    def __init__(__self__, *, accelerator: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerator(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateScalingResult(dict):
    def __init__(__self__, *, max_instance_count: _builtins.int, min_instance_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateServiceMeshResult(dict):
    def __init__(__self__, *, mesh: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mesh(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateVolumeResult(dict):
    def __init__(__self__, *, cloud_sql_instances: Sequence[outputs.GetServiceTemplateVolumeCloudSqlInstanceResult], empty_dirs: Sequence[outputs.GetServiceTemplateVolumeEmptyDirResult], gcs: Sequence[outputs.GetServiceTemplateVolumeGcResult], name: _builtins.str, nfs: Sequence[outputs.GetServiceTemplateVolumeNfResult], secrets: Sequence[outputs.GetServiceTemplateVolumeSecretResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstances")
    def cloud_sql_instances(self) -> Sequence[outputs.GetServiceTemplateVolumeCloudSqlInstanceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emptyDirs")
    def empty_dirs(self) -> Sequence[outputs.GetServiceTemplateVolumeEmptyDirResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Sequence[outputs.GetServiceTemplateVolumeGcResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Sequence[outputs.GetServiceTemplateVolumeNfResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Sequence[outputs.GetServiceTemplateVolumeSecretResult]:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateVolumeCloudSqlInstanceResult(dict):
    def __init__(__self__, *, instances: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateVolumeEmptyDirResult(dict):
    def __init__(__self__, *, medium: _builtins.str, size_limit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def medium(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateVolumeGcResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, mount_options: Sequence[_builtins.str], read_only: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateVolumeNfResult(dict):
    def __init__(__self__, *, path: _builtins.str, read_only: _builtins.bool, server: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateVolumeSecretResult(dict):
    def __init__(__self__, *, default_mode: _builtins.int, items: Sequence[outputs.GetServiceTemplateVolumeSecretItemResult], secret: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[outputs.GetServiceTemplateVolumeSecretItemResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateVolumeSecretItemResult(dict):
    def __init__(__self__, *, mode: _builtins.int, path: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateVpcAccessResult(dict):
    def __init__(__self__, *, connector: _builtins.str, egress: _builtins.str, network_interfaces: Sequence[outputs.GetServiceTemplateVpcAccessNetworkInterfaceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.GetServiceTemplateVpcAccessNetworkInterfaceResult]:
        
        ...
    


@pulumi.output_type
class GetServiceTemplateVpcAccessNetworkInterfaceResult(dict):
    def __init__(__self__, *, network: _builtins.str, subnetwork: _builtins.str, tags: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetServiceTerminalConditionResult(dict):
    def __init__(__self__, *, execution_reason: _builtins.str, last_transition_time: _builtins.str, message: _builtins.str, reason: _builtins.str, revision_reason: _builtins.str, severity: _builtins.str, state: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTrafficResult(dict):
    def __init__(__self__, *, percent: _builtins.int, revision: _builtins.str, tag: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTrafficStatusResult(dict):
    def __init__(__self__, *, percent: _builtins.int, revision: _builtins.str, tag: _builtins.str, type: _builtins.str, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolBinaryAuthorizationResult(dict):
    def __init__(__self__, *, breakglass_justification: _builtins.str, policy: _builtins.str, use_default: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="breakglassJustification")
    def breakglass_justification(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefault")
    def use_default(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolConditionResult(dict):
    def __init__(__self__, *, execution_reason: _builtins.str, last_transition_time: _builtins.str, message: _builtins.str, reason: _builtins.str, revision_reason: _builtins.str, severity: _builtins.str, state: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolInstanceSplitResult(dict):
    def __init__(__self__, *, percent: _builtins.int, revision: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolInstanceSplitStatusResult(dict):
    def __init__(__self__, *, percent: _builtins.int, revision: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolScalingResult(dict):
    def __init__(__self__, *, manual_instance_count: _builtins.int, max_instance_count: _builtins.int, min_instance_count: _builtins.int, scaling_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualInstanceCount")
    def manual_instance_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateResult(dict):
    def __init__(__self__, *, annotations: Mapping[str, _builtins.str], containers: Sequence[outputs.GetWorkerPoolTemplateContainerResult], encryption_key: _builtins.str, encryption_key_revocation_action: _builtins.str, encryption_key_shutdown_duration: _builtins.str, gpu_zonal_redundancy_disabled: _builtins.bool, labels: Mapping[str, _builtins.str], node_selectors: Sequence[outputs.GetWorkerPoolTemplateNodeSelectorResult], revision: _builtins.str, service_account: _builtins.str, volumes: Sequence[outputs.GetWorkerPoolTemplateVolumeResult], vpc_accesses: Sequence[outputs.GetWorkerPoolTemplateVpcAccessResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyRevocationAction")
    def encryption_key_revocation_action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyShutdownDuration")
    def encryption_key_shutdown_duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuZonalRedundancyDisabled")
    def gpu_zonal_redundancy_disabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSelectors")
    def node_selectors(self) -> Sequence[outputs.GetWorkerPoolTemplateNodeSelectorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Sequence[outputs.GetWorkerPoolTemplateVolumeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccesses")
    def vpc_accesses(self) -> Sequence[outputs.GetWorkerPoolTemplateVpcAccessResult]:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerResult(dict):
    def __init__(__self__, *, args: Sequence[_builtins.str], commands: Sequence[_builtins.str], depends_ons: Sequence[_builtins.str], envs: Sequence[outputs.GetWorkerPoolTemplateContainerEnvResult], image: _builtins.str, liveness_probes: Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeResult], name: _builtins.str, resources: Sequence[outputs.GetWorkerPoolTemplateContainerResourceResult], startup_probes: Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeResult], volume_mounts: Sequence[outputs.GetWorkerPoolTemplateContainerVolumeMountResult], working_dir: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerEnvResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="livenessProbes")
    def liveness_probes(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerResourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startupProbes")
    def startup_probes(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerVolumeMountResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerEnvResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str, value_sources: Sequence[outputs.GetWorkerPoolTemplateContainerEnvValueSourceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSources")
    def value_sources(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerEnvValueSourceResult]:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerEnvValueSourceResult(dict):
    def __init__(__self__, *, secret_key_reves: Sequence[outputs.GetWorkerPoolTemplateContainerEnvValueSourceSecretKeyRefResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKeyReves")
    def secret_key_reves(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerEnvValueSourceSecretKeyRefResult]:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerEnvValueSourceSecretKeyRefResult(dict):
    def __init__(__self__, *, secret: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerLivenessProbeResult(dict):
    def __init__(__self__, *, failure_threshold: _builtins.int, grpcs: Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeGrpcResult], http_gets: Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeHttpGetResult], initial_delay_seconds: _builtins.int, period_seconds: _builtins.int, tcp_sockets: Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeTcpSocketResult], timeout_seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpcs(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeGrpcResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGets")
    def http_gets(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeHttpGetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSockets")
    def tcp_sockets(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeTcpSocketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerLivenessProbeGrpcResult(dict):
    def __init__(__self__, *, port: _builtins.int, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerLivenessProbeHttpGetResult(dict):
    def __init__(__self__, *, http_headers: Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeaderResult], path: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeaderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeaderResult(dict):
    def __init__(__self__, *, port: _builtins.int, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerLivenessProbeTcpSocketResult(dict):
    def __init__(__self__, *, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerResourceResult(dict):
    def __init__(__self__, *, limits: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerStartupProbeResult(dict):
    def __init__(__self__, *, failure_threshold: _builtins.int, grpcs: Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeGrpcResult], http_gets: Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeHttpGetResult], initial_delay_seconds: _builtins.int, period_seconds: _builtins.int, tcp_sockets: Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeTcpSocketResult], timeout_seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grpcs(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeGrpcResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGets")
    def http_gets(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeHttpGetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSockets")
    def tcp_sockets(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeTcpSocketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerStartupProbeGrpcResult(dict):
    def __init__(__self__, *, port: _builtins.int, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerStartupProbeHttpGetResult(dict):
    def __init__(__self__, *, http_headers: Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeHttpGetHttpHeaderResult], path: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Sequence[outputs.GetWorkerPoolTemplateContainerStartupProbeHttpGetHttpHeaderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerStartupProbeHttpGetHttpHeaderResult(dict):
    def __init__(__self__, *, port: _builtins.int, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerStartupProbeTcpSocketResult(dict):
    def __init__(__self__, *, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateContainerVolumeMountResult(dict):
    def __init__(__self__, *, mount_path: _builtins.str, name: _builtins.str, sub_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateNodeSelectorResult(dict):
    def __init__(__self__, *, accelerator: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerator(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateVolumeResult(dict):
    def __init__(__self__, *, cloud_sql_instances: Sequence[outputs.GetWorkerPoolTemplateVolumeCloudSqlInstanceResult], empty_dirs: Sequence[outputs.GetWorkerPoolTemplateVolumeEmptyDirResult], gcs: Sequence[outputs.GetWorkerPoolTemplateVolumeGcResult], name: _builtins.str, nfs: Sequence[outputs.GetWorkerPoolTemplateVolumeNfResult], secrets: Sequence[outputs.GetWorkerPoolTemplateVolumeSecretResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstances")
    def cloud_sql_instances(self) -> Sequence[outputs.GetWorkerPoolTemplateVolumeCloudSqlInstanceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emptyDirs")
    def empty_dirs(self) -> Sequence[outputs.GetWorkerPoolTemplateVolumeEmptyDirResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Sequence[outputs.GetWorkerPoolTemplateVolumeGcResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Sequence[outputs.GetWorkerPoolTemplateVolumeNfResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Sequence[outputs.GetWorkerPoolTemplateVolumeSecretResult]:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateVolumeCloudSqlInstanceResult(dict):
    def __init__(__self__, *, instances: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateVolumeEmptyDirResult(dict):
    def __init__(__self__, *, medium: _builtins.str, size_limit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def medium(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateVolumeGcResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, mount_options: Sequence[_builtins.str], read_only: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateVolumeNfResult(dict):
    def __init__(__self__, *, path: _builtins.str, read_only: _builtins.bool, server: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateVolumeSecretResult(dict):
    def __init__(__self__, *, default_mode: _builtins.int, items: Sequence[outputs.GetWorkerPoolTemplateVolumeSecretItemResult], secret: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[outputs.GetWorkerPoolTemplateVolumeSecretItemResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateVolumeSecretItemResult(dict):
    def __init__(__self__, *, mode: _builtins.int, path: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateVpcAccessResult(dict):
    def __init__(__self__, *, connector: _builtins.str, egress: _builtins.str, network_interfaces: Sequence[outputs.GetWorkerPoolTemplateVpcAccessNetworkInterfaceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.GetWorkerPoolTemplateVpcAccessNetworkInterfaceResult]:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTemplateVpcAccessNetworkInterfaceResult(dict):
    def __init__(__self__, *, network: _builtins.str, subnetwork: _builtins.str, tags: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetWorkerPoolTerminalConditionResult(dict):
    def __init__(__self__, *, execution_reason: _builtins.str, last_transition_time: _builtins.str, message: _builtins.str, reason: _builtins.str, revision_reason: _builtins.str, severity: _builtins.str, state: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


