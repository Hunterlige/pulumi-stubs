

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPoolResult', 'AwaitableGetPoolResult', 'get_pool', 'get_pool_output']
@pulumi.output_type
class GetPoolResult:
    
    def __init__(__self__, allocation_state=..., allocation_state_transition_time=..., application_licenses=..., application_packages=..., auto_scale_run=..., azure_api_version=..., certificates=..., creation_time=..., current_dedicated_nodes=..., current_low_priority_nodes=..., current_node_communication_mode=..., deployment_configuration=..., display_name=..., etag=..., id=..., identity=..., inter_node_communication=..., last_modified=..., metadata=..., mount_configuration=..., name=..., network_configuration=..., provisioning_state=..., provisioning_state_transition_time=..., resize_operation_status=..., resource_tags=..., scale_settings=..., start_task=..., system_data=..., tags=..., target_node_communication_mode=..., task_scheduling_policy=..., task_slots_per_node=..., type=..., upgrade_policy=..., user_accounts=..., vm_size=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationState")
    def allocation_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStateTransitionTime")
    def allocation_state_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationLicenses")
    def application_licenses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationPackages")
    def application_packages(self) -> Optional[Sequence[outputs.ApplicationPackageReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScaleRun")
    def auto_scale_run(self) -> outputs.AutoScaleRunResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[outputs.CertificateReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentDedicatedNodes")
    def current_dedicated_nodes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentLowPriorityNodes")
    def current_low_priority_nodes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentNodeCommunicationMode")
    def current_node_communication_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> Optional[outputs.DeploymentConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.BatchPoolIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interNodeCommunication")
    def inter_node_communication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Sequence[outputs.MetadataItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountConfiguration")
    def mount_configuration(self) -> Optional[Sequence[outputs.MountConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[outputs.NetworkConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningStateTransitionTime")
    def provisioning_state_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resizeOperationStatus")
    def resize_operation_status(self) -> outputs.ResizeOperationStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleSettings")
    def scale_settings(self) -> Optional[outputs.ScaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTask")
    def start_task(self) -> Optional[outputs.StartTaskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNodeCommunicationMode")
    def target_node_communication_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskSchedulingPolicy")
    def task_scheduling_policy(self) -> Optional[outputs.TaskSchedulingPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskSlotsPerNode")
    def task_slots_per_node(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[outputs.UpgradePolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAccounts")
    def user_accounts(self) -> Optional[Sequence[outputs.UserAccountResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetPoolResult(GetPoolResult):
    def __await__(self): # -> Generator[Never, Any, GetPoolResult]:
        ...
    


def get_pool(account_name: Optional[_builtins.str] = ..., pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPoolResult:
    
    ...

def get_pool_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPoolResult]:
    
    ...

