

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NotebookExecutionCustomEnvironmentSpecArgs', 'NotebookExecutionCustomEnvironmentSpecArgsDict', ..., ..., ..., ..., ..., ..., 'NotebookExecutionDataformRepositorySourceArgs', 'NotebookExecutionDataformRepositorySourceArgsDict', 'NotebookExecutionDirectNotebookSourceArgs', 'NotebookExecutionDirectNotebookSourceArgsDict', 'NotebookExecutionGcsNotebookSourceArgs', 'NotebookExecutionGcsNotebookSourceArgsDict', 'RuntimeNotebookRuntimeTemplateRefArgs', 'RuntimeNotebookRuntimeTemplateRefArgsDict', 'RuntimeTemplateDataPersistentDiskSpecArgs', 'RuntimeTemplateDataPersistentDiskSpecArgsDict', 'RuntimeTemplateEncryptionSpecArgs', 'RuntimeTemplateEncryptionSpecArgsDict', 'RuntimeTemplateEucConfigArgs', 'RuntimeTemplateEucConfigArgsDict', 'RuntimeTemplateIamBindingConditionArgs', 'RuntimeTemplateIamBindingConditionArgsDict', 'RuntimeTemplateIamMemberConditionArgs', 'RuntimeTemplateIamMemberConditionArgsDict', 'RuntimeTemplateIdleShutdownConfigArgs', 'RuntimeTemplateIdleShutdownConfigArgsDict', 'RuntimeTemplateMachineSpecArgs', 'RuntimeTemplateMachineSpecArgsDict', 'RuntimeTemplateNetworkSpecArgs', 'RuntimeTemplateNetworkSpecArgsDict', 'RuntimeTemplateShieldedVmConfigArgs', 'RuntimeTemplateShieldedVmConfigArgsDict', 'RuntimeTemplateSoftwareConfigArgs', 'RuntimeTemplateSoftwareConfigArgsDict', 'RuntimeTemplateSoftwareConfigEnvArgs', 'RuntimeTemplateSoftwareConfigEnvArgsDict', ..., ..., 'ScheduleCreateNotebookExecutionJobRequestArgs', 'ScheduleCreateNotebookExecutionJobRequestArgsDict', ..., ..., ..., ..., ..., ...]
class NotebookExecutionCustomEnvironmentSpecArgsDict(TypedDict):
    machine_spec: NotRequired[pulumi.Input[NotebookExecutionCustomEnvironmentSpecMachineSpecArgsDict]]
    network_spec: NotRequired[pulumi.Input[NotebookExecutionCustomEnvironmentSpecNetworkSpecArgsDict]]
    persistent_disk_spec: NotRequired[pulumi.Input[NotebookExecutionCustomEnvironmentSpecPersistentDiskSpecArgsDict]]


@pulumi.input_type
class NotebookExecutionCustomEnvironmentSpecArgs:
    def __init__(__self__, *, machine_spec: Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecMachineSpecArgs]] = ..., network_spec: Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecNetworkSpecArgs]] = ..., persistent_disk_spec: Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecPersistentDiskSpecArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineSpec")
    def machine_spec(self) -> Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecMachineSpecArgs]]:
        
        ...
    
    @machine_spec.setter
    def machine_spec(self, value: Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecMachineSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSpec")
    def network_spec(self) -> Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecNetworkSpecArgs]]:
        
        ...
    
    @network_spec.setter
    def network_spec(self, value: Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecNetworkSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistentDiskSpec")
    def persistent_disk_spec(self) -> Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecPersistentDiskSpecArgs]]:
        
        ...
    
    @persistent_disk_spec.setter
    def persistent_disk_spec(self, value: Optional[pulumi.Input[NotebookExecutionCustomEnvironmentSpecPersistentDiskSpecArgs]]): # -> None:
        ...
    


class NotebookExecutionCustomEnvironmentSpecMachineSpecArgsDict(TypedDict):
    accelerator_count: NotRequired[pulumi.Input[_builtins.int]]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NotebookExecutionCustomEnvironmentSpecMachineSpecArgs:
    def __init__(__self__, *, accelerator_count: Optional[pulumi.Input[_builtins.int]] = ..., accelerator_type: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @accelerator_count.setter
    def accelerator_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NotebookExecutionCustomEnvironmentSpecNetworkSpecArgsDict(TypedDict):
    enable_internet_access: NotRequired[pulumi.Input[_builtins.bool]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NotebookExecutionCustomEnvironmentSpecNetworkSpecArgs:
    def __init__(__self__, *, enable_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetAccess")
    def enable_internet_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_internet_access.setter
    def enable_internet_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NotebookExecutionCustomEnvironmentSpecPersistentDiskSpecArgsDict(TypedDict):
    disk_size_gb: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NotebookExecutionCustomEnvironmentSpecPersistentDiskSpecArgs:
    def __init__(__self__, *, disk_size_gb: Optional[pulumi.Input[_builtins.str]] = ..., disk_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NotebookExecutionDataformRepositorySourceArgsDict(TypedDict):
    dataform_repository_resource_name: pulumi.Input[_builtins.str]
    commit_sha: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NotebookExecutionDataformRepositorySourceArgs:
    def __init__(__self__, *, dataform_repository_resource_name: pulumi.Input[_builtins.str], commit_sha: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataformRepositoryResourceName")
    def dataform_repository_resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dataform_repository_resource_name.setter
    def dataform_repository_resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @commit_sha.setter
    def commit_sha(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NotebookExecutionDirectNotebookSourceArgsDict(TypedDict):
    content: pulumi.Input[_builtins.str]


@pulumi.input_type
class NotebookExecutionDirectNotebookSourceArgs:
    def __init__(__self__, *, content: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @content.setter
    def content(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class NotebookExecutionGcsNotebookSourceArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NotebookExecutionGcsNotebookSourceArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str], generation: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeNotebookRuntimeTemplateRefArgsDict(TypedDict):
    notebook_runtime_template: pulumi.Input[_builtins.str]


@pulumi.input_type
class RuntimeNotebookRuntimeTemplateRefArgs:
    def __init__(__self__, *, notebook_runtime_template: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookRuntimeTemplate")
    def notebook_runtime_template(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @notebook_runtime_template.setter
    def notebook_runtime_template(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RuntimeTemplateDataPersistentDiskSpecArgsDict(TypedDict):
    disk_size_gb: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuntimeTemplateDataPersistentDiskSpecArgs:
    def __init__(__self__, *, disk_size_gb: Optional[pulumi.Input[_builtins.str]] = ..., disk_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeTemplateEncryptionSpecArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuntimeTemplateEncryptionSpecArgs:
    def __init__(__self__, *, kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeTemplateEucConfigArgsDict(TypedDict):
    euc_disabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class RuntimeTemplateEucConfigArgs:
    def __init__(__self__, *, euc_disabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eucDisabled")
    def euc_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @euc_disabled.setter
    def euc_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class RuntimeTemplateIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuntimeTemplateIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeTemplateIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuntimeTemplateIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeTemplateIdleShutdownConfigArgsDict(TypedDict):
    idle_timeout: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuntimeTemplateIdleShutdownConfigArgs:
    def __init__(__self__, *, idle_timeout: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeTemplateMachineSpecArgsDict(TypedDict):
    accelerator_count: NotRequired[pulumi.Input[_builtins.int]]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuntimeTemplateMachineSpecArgs:
    def __init__(__self__, *, accelerator_count: Optional[pulumi.Input[_builtins.int]] = ..., accelerator_type: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @accelerator_count.setter
    def accelerator_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeTemplateNetworkSpecArgsDict(TypedDict):
    enable_internet_access: NotRequired[pulumi.Input[_builtins.bool]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuntimeTemplateNetworkSpecArgs:
    def __init__(__self__, *, enable_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetAccess")
    def enable_internet_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_internet_access.setter
    def enable_internet_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeTemplateShieldedVmConfigArgsDict(TypedDict):
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class RuntimeTemplateShieldedVmConfigArgs:
    def __init__(__self__, *, enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class RuntimeTemplateSoftwareConfigArgsDict(TypedDict):
    envs: NotRequired[pulumi.Input[Sequence[pulumi.Input[RuntimeTemplateSoftwareConfigEnvArgsDict]]]]
    post_startup_script_config: NotRequired[pulumi.Input[RuntimeTemplateSoftwareConfigPostStartupScriptConfigArgsDict]]


@pulumi.input_type
class RuntimeTemplateSoftwareConfigArgs:
    def __init__(__self__, *, envs: Optional[pulumi.Input[Sequence[pulumi.Input[RuntimeTemplateSoftwareConfigEnvArgs]]]] = ..., post_startup_script_config: Optional[pulumi.Input[RuntimeTemplateSoftwareConfigPostStartupScriptConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuntimeTemplateSoftwareConfigEnvArgs]]]]:
        
        ...
    
    @envs.setter
    def envs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RuntimeTemplateSoftwareConfigEnvArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScriptConfig")
    def post_startup_script_config(self) -> Optional[pulumi.Input[RuntimeTemplateSoftwareConfigPostStartupScriptConfigArgs]]:
        
        ...
    
    @post_startup_script_config.setter
    def post_startup_script_config(self, value: Optional[pulumi.Input[RuntimeTemplateSoftwareConfigPostStartupScriptConfigArgs]]): # -> None:
        ...
    


class RuntimeTemplateSoftwareConfigEnvArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuntimeTemplateSoftwareConfigEnvArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeTemplateSoftwareConfigPostStartupScriptConfigArgsDict(TypedDict):
    post_startup_script: NotRequired[pulumi.Input[_builtins.str]]
    post_startup_script_behavior: NotRequired[pulumi.Input[_builtins.str]]
    post_startup_script_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuntimeTemplateSoftwareConfigPostStartupScriptConfigArgs:
    def __init__(__self__, *, post_startup_script: Optional[pulumi.Input[_builtins.str]] = ..., post_startup_script_behavior: Optional[pulumi.Input[_builtins.str]] = ..., post_startup_script_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @post_startup_script.setter
    def post_startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScriptBehavior")
    def post_startup_script_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @post_startup_script_behavior.setter
    def post_startup_script_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScriptUrl")
    def post_startup_script_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @post_startup_script_url.setter
    def post_startup_script_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScheduleCreateNotebookExecutionJobRequestArgsDict(TypedDict):
    notebook_execution_job: pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobArgsDict]


@pulumi.input_type
class ScheduleCreateNotebookExecutionJobRequestArgs:
    def __init__(__self__, *, notebook_execution_job: pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookExecutionJob")
    def notebook_execution_job(self) -> pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobArgs]:
        
        ...
    
    @notebook_execution_job.setter
    def notebook_execution_job(self, value: pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobArgs]): # -> None:
        ...
    


class ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobArgsDict(TypedDict):
    display_name: pulumi.Input[_builtins.str]
    gcs_output_uri: pulumi.Input[_builtins.str]
    notebook_runtime_template_resource_name: pulumi.Input[_builtins.str]
    dataform_repository_source: NotRequired[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobDataformRepositorySourceArgsDict]]
    execution_timeout: NotRequired[pulumi.Input[_builtins.str]]
    execution_user: NotRequired[pulumi.Input[_builtins.str]]
    gcs_notebook_source: NotRequired[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobGcsNotebookSourceArgsDict]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], gcs_output_uri: pulumi.Input[_builtins.str], notebook_runtime_template_resource_name: pulumi.Input[_builtins.str], dataform_repository_source: Optional[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobDataformRepositorySourceArgs]] = ..., execution_timeout: Optional[pulumi.Input[_builtins.str]] = ..., execution_user: Optional[pulumi.Input[_builtins.str]] = ..., gcs_notebook_source: Optional[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobGcsNotebookSourceArgs]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsOutputUri")
    def gcs_output_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gcs_output_uri.setter
    def gcs_output_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookRuntimeTemplateResourceName")
    def notebook_runtime_template_resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @notebook_runtime_template_resource_name.setter
    def notebook_runtime_template_resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataformRepositorySource")
    def dataform_repository_source(self) -> Optional[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobDataformRepositorySourceArgs]]:
        
        ...
    
    @dataform_repository_source.setter
    def dataform_repository_source(self, value: Optional[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobDataformRepositorySourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_timeout.setter
    def execution_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionUser")
    def execution_user(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_user.setter
    def execution_user(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsNotebookSource")
    def gcs_notebook_source(self) -> Optional[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobGcsNotebookSourceArgs]]:
        
        ...
    
    @gcs_notebook_source.setter
    def gcs_notebook_source(self, value: Optional[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobGcsNotebookSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobDataformRepositorySourceArgsDict(TypedDict):
    dataform_repository_resource_name: pulumi.Input[_builtins.str]
    commit_sha: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobDataformRepositorySourceArgs:
    def __init__(__self__, *, dataform_repository_resource_name: pulumi.Input[_builtins.str], commit_sha: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataformRepositoryResourceName")
    def dataform_repository_resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dataform_repository_resource_name.setter
    def dataform_repository_resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @commit_sha.setter
    def commit_sha(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobGcsNotebookSourceArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScheduleCreateNotebookExecutionJobRequestNotebookExecutionJobGcsNotebookSourceArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str], generation: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


