

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FunctionAutomaticUpdatePolicy', 'FunctionEventTrigger', 'FunctionEventTriggerFailurePolicy', 'FunctionIamBindingCondition', 'FunctionIamMemberCondition', 'FunctionOnDeployUpdatePolicy', 'FunctionSecretEnvironmentVariable', 'FunctionSecretVolume', 'FunctionSecretVolumeVersion', 'FunctionSourceRepository', 'GetFunctionAutomaticUpdatePolicyResult', 'GetFunctionEventTriggerResult', 'GetFunctionEventTriggerFailurePolicyResult', 'GetFunctionOnDeployUpdatePolicyResult', 'GetFunctionSecretEnvironmentVariableResult', 'GetFunctionSecretVolumeResult', 'GetFunctionSecretVolumeVersionResult', 'GetFunctionSourceRepositoryResult']
@pulumi.output_type
class FunctionAutomaticUpdatePolicy(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class FunctionEventTrigger(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_type: _builtins.str, resource: _builtins.str, failure_policy: Optional[outputs.FunctionEventTriggerFailurePolicy] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failurePolicy")
    def failure_policy(self) -> Optional[outputs.FunctionEventTriggerFailurePolicy]:
        
        ...
    


@pulumi.output_type
class FunctionEventTriggerFailurePolicy(dict):
    def __init__(__self__, *, retry: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def retry(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class FunctionIamBindingCondition(dict):
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
class FunctionIamMemberCondition(dict):
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
class FunctionOnDeployUpdatePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, runtime_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionSecretEnvironmentVariable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, secret: _builtins.str, version: _builtins.str, project_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionSecretVolume(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mount_path: _builtins.str, secret: _builtins.str, project_id: Optional[_builtins.str] = ..., versions: Optional[Sequence[outputs.FunctionSecretVolumeVersion]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[Sequence[outputs.FunctionSecretVolumeVersion]]:
        
        ...
    


@pulumi.output_type
class FunctionSecretVolumeVersion(dict):
    def __init__(__self__, *, path: _builtins.str, version: _builtins.str) -> None:
        
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
class FunctionSourceRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, url: _builtins.str, deployed_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedUrl")
    def deployed_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetFunctionAutomaticUpdatePolicyResult(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class GetFunctionEventTriggerResult(dict):
    def __init__(__self__, *, event_type: _builtins.str, failure_policies: Sequence[outputs.GetFunctionEventTriggerFailurePolicyResult], resource: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failurePolicies")
    def failure_policies(self) -> Sequence[outputs.GetFunctionEventTriggerFailurePolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionEventTriggerFailurePolicyResult(dict):
    def __init__(__self__, *, retry: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def retry(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetFunctionOnDeployUpdatePolicyResult(dict):
    def __init__(__self__, *, runtime_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionSecretEnvironmentVariableResult(dict):
    def __init__(__self__, *, key: _builtins.str, project_id: _builtins.str, secret: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
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
class GetFunctionSecretVolumeResult(dict):
    def __init__(__self__, *, mount_path: _builtins.str, project_id: _builtins.str, secret: _builtins.str, versions: Sequence[outputs.GetFunctionSecretVolumeVersionResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Sequence[outputs.GetFunctionSecretVolumeVersionResult]:
        
        ...
    


@pulumi.output_type
class GetFunctionSecretVolumeVersionResult(dict):
    def __init__(__self__, *, path: _builtins.str, version: _builtins.str) -> None:
        
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
class GetFunctionSourceRepositoryResult(dict):
    def __init__(__self__, *, deployed_url: _builtins.str, url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedUrl")
    def deployed_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    


