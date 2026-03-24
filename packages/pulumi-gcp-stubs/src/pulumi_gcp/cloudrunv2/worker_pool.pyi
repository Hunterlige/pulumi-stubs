

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkerPoolArgs', 'WorkerPool']
@pulumi.input_type
class WorkerPoolArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], template: pulumi.Input[WorkerPoolTemplateArgs], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., binary_authorization: Optional[pulumi.Input[WorkerPoolBinaryAuthorizationArgs]] = ..., client: Optional[pulumi.Input[_builtins.str]] = ..., client_version: Optional[pulumi.Input[_builtins.str]] = ..., custom_audiences: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_splits: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolInstanceSplitArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., launch_stage: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., scaling: Optional[pulumi.Input[WorkerPoolScalingArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Input[WorkerPoolTemplateArgs]:
        
        ...
    
    @template.setter
    def template(self, value: pulumi.Input[WorkerPoolTemplateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> Optional[pulumi.Input[WorkerPoolBinaryAuthorizationArgs]]:
        
        ...
    
    @binary_authorization.setter
    def binary_authorization(self, value: Optional[pulumi.Input[WorkerPoolBinaryAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client.setter
    def client(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_version.setter
    def client_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customAudiences")
    @_utilities.deprecated(...)
    def custom_audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_audiences.setter
    def custom_audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSplits")
    def instance_splits(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolInstanceSplitArgs]]]]:
        
        ...
    
    @instance_splits.setter
    def instance_splits(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolInstanceSplitArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_stage.setter
    def launch_stage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scaling(self) -> Optional[pulumi.Input[WorkerPoolScalingArgs]]:
        
        ...
    
    @scaling.setter
    def scaling(self, value: Optional[pulumi.Input[WorkerPoolScalingArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkerPoolState:
    def __init__(__self__, *, annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., binary_authorization: Optional[pulumi.Input[WorkerPoolBinaryAuthorizationArgs]] = ..., client: Optional[pulumi.Input[_builtins.str]] = ..., client_version: Optional[pulumi.Input[_builtins.str]] = ..., conditions: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolConditionArgs]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., creator: Optional[pulumi.Input[_builtins.str]] = ..., custom_audiences: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., generation: Optional[pulumi.Input[_builtins.str]] = ..., instance_split_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolInstanceSplitStatusArgs]]]] = ..., instance_splits: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolInstanceSplitArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., last_modifier: Optional[pulumi.Input[_builtins.str]] = ..., latest_created_revision: Optional[pulumi.Input[_builtins.str]] = ..., latest_ready_revision: Optional[pulumi.Input[_builtins.str]] = ..., launch_stage: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., observed_generation: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., scaling: Optional[pulumi.Input[WorkerPoolScalingArgs]] = ..., template: Optional[pulumi.Input[WorkerPoolTemplateArgs]] = ..., terminal_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolTerminalConditionArgs]]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> Optional[pulumi.Input[WorkerPoolBinaryAuthorizationArgs]]:
        
        ...
    
    @binary_authorization.setter
    def binary_authorization(self, value: Optional[pulumi.Input[WorkerPoolBinaryAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client.setter
    def client(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_version.setter
    def client_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolConditionArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolConditionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def creator(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creator.setter
    def creator(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customAudiences")
    @_utilities.deprecated(...)
    def custom_audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_audiences.setter
    def custom_audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_annotations.setter
    def effective_annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSplitStatuses")
    def instance_split_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolInstanceSplitStatusArgs]]]]:
        
        ...
    
    @instance_split_statuses.setter
    def instance_split_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolInstanceSplitStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSplits")
    def instance_splits(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolInstanceSplitArgs]]]]:
        
        ...
    
    @instance_splits.setter
    def instance_splits(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolInstanceSplitArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifier")
    def last_modifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modifier.setter
    def last_modifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestCreatedRevision")
    def latest_created_revision(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @latest_created_revision.setter
    def latest_created_revision(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestReadyRevision")
    def latest_ready_revision(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @latest_ready_revision.setter
    def latest_ready_revision(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_stage.setter
    def launch_stage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @observed_generation.setter
    def observed_generation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scaling(self) -> Optional[pulumi.Input[WorkerPoolScalingArgs]]:
        
        ...
    
    @scaling.setter
    def scaling(self, value: Optional[pulumi.Input[WorkerPoolScalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[WorkerPoolTemplateArgs]]:
        
        ...
    
    @template.setter
    def template(self, value: Optional[pulumi.Input[WorkerPoolTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminalConditions")
    def terminal_conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolTerminalConditionArgs]]]]:
        
        ...
    
    @terminal_conditions.setter
    def terminal_conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkerPoolTerminalConditionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:cloudrunv2/workerPool:WorkerPool")
class WorkerPool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., binary_authorization: Optional[pulumi.Input[Union[WorkerPoolBinaryAuthorizationArgs, WorkerPoolBinaryAuthorizationArgsDict]]] = ..., client: Optional[pulumi.Input[_builtins.str]] = ..., client_version: Optional[pulumi.Input[_builtins.str]] = ..., custom_audiences: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_splits: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkerPoolInstanceSplitArgs, WorkerPoolInstanceSplitArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., launch_stage: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., scaling: Optional[pulumi.Input[Union[WorkerPoolScalingArgs, WorkerPoolScalingArgsDict]]] = ..., template: Optional[pulumi.Input[Union[WorkerPoolTemplateArgs, WorkerPoolTemplateArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkerPoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., binary_authorization: Optional[pulumi.Input[Union[WorkerPoolBinaryAuthorizationArgs, WorkerPoolBinaryAuthorizationArgsDict]]] = ..., client: Optional[pulumi.Input[_builtins.str]] = ..., client_version: Optional[pulumi.Input[_builtins.str]] = ..., conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkerPoolConditionArgs, WorkerPoolConditionArgsDict]]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., creator: Optional[pulumi.Input[_builtins.str]] = ..., custom_audiences: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., generation: Optional[pulumi.Input[_builtins.str]] = ..., instance_split_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkerPoolInstanceSplitStatusArgs, WorkerPoolInstanceSplitStatusArgsDict]]]]] = ..., instance_splits: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkerPoolInstanceSplitArgs, WorkerPoolInstanceSplitArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., last_modifier: Optional[pulumi.Input[_builtins.str]] = ..., latest_created_revision: Optional[pulumi.Input[_builtins.str]] = ..., latest_ready_revision: Optional[pulumi.Input[_builtins.str]] = ..., launch_stage: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., observed_generation: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., scaling: Optional[pulumi.Input[Union[WorkerPoolScalingArgs, WorkerPoolScalingArgsDict]]] = ..., template: Optional[pulumi.Input[Union[WorkerPoolTemplateArgs, WorkerPoolTemplateArgsDict]]] = ..., terminal_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkerPoolTerminalConditionArgs, WorkerPoolTerminalConditionArgsDict]]]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> WorkerPool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> pulumi.Output[Optional[outputs.WorkerPoolBinaryAuthorization]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence[outputs.WorkerPoolCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def creator(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customAudiences")
    @_utilities.deprecated(...)
    def custom_audiences(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSplitStatuses")
    def instance_split_statuses(self) -> pulumi.Output[Sequence[outputs.WorkerPoolInstanceSplitStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSplits")
    def instance_splits(self) -> pulumi.Output[Sequence[outputs.WorkerPoolInstanceSplit]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifier")
    def last_modifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestCreatedRevision")
    def latest_created_revision(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestReadyRevision")
    def latest_ready_revision(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> pulumi.Output[_builtins.str]:
        
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
    def reconciling(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scaling(self) -> pulumi.Output[outputs.WorkerPoolScaling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Output[outputs.WorkerPoolTemplate]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminalConditions")
    def terminal_conditions(self) -> pulumi.Output[Sequence[outputs.WorkerPoolTerminalCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


