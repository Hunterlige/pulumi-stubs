

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NotebookExecutionCustomEnvironmentSpec', 'NotebookExecutionCustomEnvironmentSpecMachineSpec', 'NotebookExecutionCustomEnvironmentSpecNetworkSpec', ..., 'NotebookExecutionDataformRepositorySource', 'NotebookExecutionDirectNotebookSource', 'NotebookExecutionGcsNotebookSource', 'RuntimeNotebookRuntimeTemplateRef', 'RuntimeTemplateDataPersistentDiskSpec', 'RuntimeTemplateEncryptionSpec', 'RuntimeTemplateEucConfig', 'RuntimeTemplateIamBindingCondition', 'RuntimeTemplateIamMemberCondition', 'RuntimeTemplateIdleShutdownConfig', 'RuntimeTemplateMachineSpec', 'RuntimeTemplateNetworkSpec', 'RuntimeTemplateShieldedVmConfig', 'RuntimeTemplateSoftwareConfig', 'RuntimeTemplateSoftwareConfigEnv', ..., 'ScheduleCreateNotebookExecutionJobRequest', ..., ..., ...]
@pulumi.output_type
class NotebookExecutionCustomEnvironmentSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_spec: Optional[outputs.NotebookExecutionCustomEnvironmentSpecMachineSpec] = ..., network_spec: Optional[outputs.NotebookExecutionCustomEnvironmentSpecNetworkSpec] = ..., persistent_disk_spec: Optional[outputs.NotebookExecutionCustomEnvironmentSpecPersistentDiskSpec] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineSpec")
    def machine_spec(self) -> Optional[outputs.NotebookExecutionCustomEnvironmentSpecMachineSpec]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSpec")
    def network_spec(self) -> Optional[outputs.NotebookExecutionCustomEnvironmentSpecNetworkSpec]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistentDiskSpec")
    def persistent_disk_spec(self) -> Optional[outputs.NotebookExecutionCustomEnvironmentSpecPersistentDiskSpec]:
        
        ...
    


@pulumi.output_type
class NotebookExecutionCustomEnvironmentSpecMachineSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: Optional[_builtins.int] = ..., accelerator_type: Optional[_builtins.str] = ..., machine_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NotebookExecutionCustomEnvironmentSpecNetworkSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_internet_access: Optional[_builtins.bool] = ..., network: Optional[_builtins.str] = ..., subnetwork: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetAccess")
    def enable_internet_access(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NotebookExecutionCustomEnvironmentSpecPersistentDiskSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_size_gb: Optional[_builtins.str] = ..., disk_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NotebookExecutionDataformRepositorySource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataform_repository_resource_name: _builtins.str, commit_sha: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataformRepositoryResourceName")
    def dataform_repository_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NotebookExecutionDirectNotebookSource(dict):
    def __init__(__self__, *, content: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class NotebookExecutionGcsNotebookSource(dict):
    def __init__(__self__, *, uri: _builtins.str, generation: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeNotebookRuntimeTemplateRef(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, notebook_runtime_template: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookRuntimeTemplate")
    def notebook_runtime_template(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateDataPersistentDiskSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_size_gb: Optional[_builtins.str] = ..., disk_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateEucConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, euc_disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eucDisabled")
    def euc_disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateIamBindingCondition(dict):
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
class RuntimeTemplateIamMemberCondition(dict):
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
class RuntimeTemplateIdleShutdownConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, idle_timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateMachineSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: Optional[_builtins.int] = ..., accelerator_type: Optional[_builtins.str] = ..., machine_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateNetworkSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_internet_access: Optional[_builtins.bool] = ..., network: Optional[_builtins.str] = ..., subnetwork: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetAccess")
    def enable_internet_access(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateShieldedVmConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_secure_boot: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateSoftwareConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, envs: Optional[Sequence[outputs.RuntimeTemplateSoftwareConfigEnv]] = ..., post_startup_script_config: Optional[outputs.RuntimeTemplateSoftwareConfigPostStartupScriptConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[Sequence[outputs.RuntimeTemplateSoftwareConfigEnv]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScriptConfig")
    def post_startup_script_config(self) -> Optional[outputs.RuntimeTemplateSoftwareConfigPostStartupScriptConfig]:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateSoftwareConfigEnv(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeTemplateSoftwareConfigPostStartupScriptConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, post_startup_script: Optional[_builtins.str] = ..., post_startup_script_behavior: Optional[_builtins.str] = ..., post_startup_script_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScriptBehavior")
    def post_startup_script_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScriptUrl")
    def post_startup_script_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScheduleCreateNotebookExecutionJobRequest(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, notebook_execution_job: outputs.ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJob) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookExecutionJob")
    def notebook_execution_job(self) -> outputs.ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJob:
        
        ...
    


@pulumi.output_type
class ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, gcs_output_uri: _builtins.str, notebook_runtime_template_resource_name: _builtins.str, dataform_repository_source: Optional[outputs.ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobDataformRepositorySource] = ..., execution_timeout: Optional[_builtins.str] = ..., execution_user: Optional[_builtins.str] = ..., gcs_notebook_source: Optional[outputs.ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobGcsNotebookSource] = ..., service_account: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsOutputUri")
    def gcs_output_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookRuntimeTemplateResourceName")
    def notebook_runtime_template_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataformRepositorySource")
    def dataform_repository_source(self) -> Optional[outputs.ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobDataformRepositorySource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionUser")
    def execution_user(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsNotebookSource")
    def gcs_notebook_source(self) -> Optional[outputs.ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobGcsNotebookSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobDataformRepositorySource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataform_repository_resource_name: _builtins.str, commit_sha: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataformRepositoryResourceName")
    def dataform_repository_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobGcsNotebookSource(dict):
    def __init__(__self__, *, uri: _builtins.str, generation: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]:
        
        ...
    


