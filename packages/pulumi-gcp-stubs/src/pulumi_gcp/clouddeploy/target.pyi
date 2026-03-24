

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
__all__ = ['TargetArgs', 'Target']
@pulumi.input_type
class TargetArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., anthos_cluster: Optional[pulumi.Input[TargetAnthosClusterArgs]] = ..., associated_entities: Optional[pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityArgs]]]] = ..., custom_target: Optional[pulumi.Input[TargetCustomTargetArgs]] = ..., deploy_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_configs: Optional[pulumi.Input[Sequence[pulumi.Input[TargetExecutionConfigArgs]]]] = ..., gke: Optional[pulumi.Input[TargetGkeArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., multi_target: Optional[pulumi.Input[TargetMultiTargetArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., require_approval: Optional[pulumi.Input[_builtins.bool]] = ..., run: Optional[pulumi.Input[TargetRunArgs]] = ...) -> None:
        
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
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anthosCluster")
    def anthos_cluster(self) -> Optional[pulumi.Input[TargetAnthosClusterArgs]]:
        
        ...
    
    @anthos_cluster.setter
    def anthos_cluster(self, value: Optional[pulumi.Input[TargetAnthosClusterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedEntities")
    def associated_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityArgs]]]]:
        
        ...
    
    @associated_entities.setter
    def associated_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTarget")
    def custom_target(self) -> Optional[pulumi.Input[TargetCustomTargetArgs]]:
        
        ...
    
    @custom_target.setter
    def custom_target(self, value: Optional[pulumi.Input[TargetCustomTargetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployParameters")
    def deploy_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @deploy_parameters.setter
    def deploy_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionConfigs")
    def execution_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TargetExecutionConfigArgs]]]]:
        
        ...
    
    @execution_configs.setter
    def execution_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TargetExecutionConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def gke(self) -> Optional[pulumi.Input[TargetGkeArgs]]:
        
        ...
    
    @gke.setter
    def gke(self, value: Optional[pulumi.Input[TargetGkeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiTarget")
    def multi_target(self) -> Optional[pulumi.Input[TargetMultiTargetArgs]]:
        
        ...
    
    @multi_target.setter
    def multi_target(self, value: Optional[pulumi.Input[TargetMultiTargetArgs]]): # -> None:
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
    @pulumi.getter(name="requireApproval")
    def require_approval(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_approval.setter
    def require_approval(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def run(self) -> Optional[pulumi.Input[TargetRunArgs]]:
        
        ...
    
    @run.setter
    def run(self, value: Optional[pulumi.Input[TargetRunArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _TargetState:
    def __init__(__self__, *, annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., anthos_cluster: Optional[pulumi.Input[TargetAnthosClusterArgs]] = ..., associated_entities: Optional[pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityArgs]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., custom_target: Optional[pulumi.Input[TargetCustomTargetArgs]] = ..., deploy_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., execution_configs: Optional[pulumi.Input[Sequence[pulumi.Input[TargetExecutionConfigArgs]]]] = ..., gke: Optional[pulumi.Input[TargetGkeArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multi_target: Optional[pulumi.Input[TargetMultiTargetArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., require_approval: Optional[pulumi.Input[_builtins.bool]] = ..., run: Optional[pulumi.Input[TargetRunArgs]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anthosCluster")
    def anthos_cluster(self) -> Optional[pulumi.Input[TargetAnthosClusterArgs]]:
        
        ...
    
    @anthos_cluster.setter
    def anthos_cluster(self, value: Optional[pulumi.Input[TargetAnthosClusterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedEntities")
    def associated_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityArgs]]]]:
        
        ...
    
    @associated_entities.setter
    def associated_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTarget")
    def custom_target(self) -> Optional[pulumi.Input[TargetCustomTargetArgs]]:
        
        ...
    
    @custom_target.setter
    def custom_target(self, value: Optional[pulumi.Input[TargetCustomTargetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployParameters")
    def deploy_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @deploy_parameters.setter
    def deploy_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="executionConfigs")
    def execution_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TargetExecutionConfigArgs]]]]:
        
        ...
    
    @execution_configs.setter
    def execution_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TargetExecutionConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def gke(self) -> Optional[pulumi.Input[TargetGkeArgs]]:
        
        ...
    
    @gke.setter
    def gke(self, value: Optional[pulumi.Input[TargetGkeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiTarget")
    def multi_target(self) -> Optional[pulumi.Input[TargetMultiTargetArgs]]:
        
        ...
    
    @multi_target.setter
    def multi_target(self, value: Optional[pulumi.Input[TargetMultiTargetArgs]]): # -> None:
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireApproval")
    def require_approval(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_approval.setter
    def require_approval(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def run(self) -> Optional[pulumi.Input[TargetRunArgs]]:
        
        ...
    
    @run.setter
    def run(self, value: Optional[pulumi.Input[TargetRunArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("gcp:clouddeploy/target:Target")
class Target(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., anthos_cluster: Optional[pulumi.Input[Union[TargetAnthosClusterArgs, TargetAnthosClusterArgsDict]]] = ..., associated_entities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TargetAssociatedEntityArgs, TargetAssociatedEntityArgsDict]]]]] = ..., custom_target: Optional[pulumi.Input[Union[TargetCustomTargetArgs, TargetCustomTargetArgsDict]]] = ..., deploy_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TargetExecutionConfigArgs, TargetExecutionConfigArgsDict]]]]] = ..., gke: Optional[pulumi.Input[Union[TargetGkeArgs, TargetGkeArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multi_target: Optional[pulumi.Input[Union[TargetMultiTargetArgs, TargetMultiTargetArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., require_approval: Optional[pulumi.Input[_builtins.bool]] = ..., run: Optional[pulumi.Input[Union[TargetRunArgs, TargetRunArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TargetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., anthos_cluster: Optional[pulumi.Input[Union[TargetAnthosClusterArgs, TargetAnthosClusterArgsDict]]] = ..., associated_entities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TargetAssociatedEntityArgs, TargetAssociatedEntityArgsDict]]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., custom_target: Optional[pulumi.Input[Union[TargetCustomTargetArgs, TargetCustomTargetArgsDict]]] = ..., deploy_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., execution_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TargetExecutionConfigArgs, TargetExecutionConfigArgsDict]]]]] = ..., gke: Optional[pulumi.Input[Union[TargetGkeArgs, TargetGkeArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multi_target: Optional[pulumi.Input[Union[TargetMultiTargetArgs, TargetMultiTargetArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., require_approval: Optional[pulumi.Input[_builtins.bool]] = ..., run: Optional[pulumi.Input[Union[TargetRunArgs, TargetRunArgsDict]]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Target:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anthosCluster")
    def anthos_cluster(self) -> pulumi.Output[Optional[outputs.TargetAnthosCluster]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedEntities")
    def associated_entities(self) -> pulumi.Output[Optional[Sequence[outputs.TargetAssociatedEntity]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTarget")
    def custom_target(self) -> pulumi.Output[Optional[outputs.TargetCustomTarget]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployParameters")
    def deploy_parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
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
    @pulumi.getter(name="executionConfigs")
    def execution_configs(self) -> pulumi.Output[Sequence[outputs.TargetExecutionConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gke(self) -> pulumi.Output[Optional[outputs.TargetGke]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiTarget")
    def multi_target(self) -> pulumi.Output[Optional[outputs.TargetMultiTarget]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="requireApproval")
    def require_approval(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def run(self) -> pulumi.Output[Optional[outputs.TargetRun]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


