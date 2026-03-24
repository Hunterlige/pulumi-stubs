

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
__all__ = ['BucketArgs', 'Bucket']
@pulumi.input_type
class BucketArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], autoclass: Optional[pulumi.Input[BucketAutoclassArgs]] = ..., cors: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorArgs]]]] = ..., custom_placement_config: Optional[pulumi.Input[BucketCustomPlacementConfigArgs]] = ..., default_event_based_hold: Optional[pulumi.Input[_builtins.bool]] = ..., enable_object_retention: Optional[pulumi.Input[_builtins.bool]] = ..., encryption: Optional[pulumi.Input[BucketEncryptionArgs]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., hierarchical_namespace: Optional[pulumi.Input[BucketHierarchicalNamespaceArgs]] = ..., ip_filter: Optional[pulumi.Input[BucketIpFilterArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]] = ..., logging: Optional[pulumi.Input[BucketLoggingArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., public_access_prevention: Optional[pulumi.Input[_builtins.str]] = ..., requester_pays: Optional[pulumi.Input[_builtins.bool]] = ..., retention_policy: Optional[pulumi.Input[BucketRetentionPolicyArgs]] = ..., rpo: Optional[pulumi.Input[_builtins.str]] = ..., soft_delete_policy: Optional[pulumi.Input[BucketSoftDeletePolicyArgs]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., uniform_bucket_level_access: Optional[pulumi.Input[_builtins.bool]] = ..., versioning: Optional[pulumi.Input[BucketVersioningArgs]] = ..., website: Optional[pulumi.Input[BucketWebsiteArgs]] = ...) -> None:
        
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
    def autoclass(self) -> Optional[pulumi.Input[BucketAutoclassArgs]]:
        
        ...
    
    @autoclass.setter
    def autoclass(self, value: Optional[pulumi.Input[BucketAutoclassArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorArgs]]]]:
        
        ...
    
    @cors.setter
    def cors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPlacementConfig")
    def custom_placement_config(self) -> Optional[pulumi.Input[BucketCustomPlacementConfigArgs]]:
        
        ...
    
    @custom_placement_config.setter
    def custom_placement_config(self, value: Optional[pulumi.Input[BucketCustomPlacementConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEventBasedHold")
    def default_event_based_hold(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @default_event_based_hold.setter
    def default_event_based_hold(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableObjectRetention")
    def enable_object_retention(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_object_retention.setter
    def enable_object_retention(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[BucketEncryptionArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[BucketEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchicalNamespace")
    def hierarchical_namespace(self) -> Optional[pulumi.Input[BucketHierarchicalNamespaceArgs]]:
        
        ...
    
    @hierarchical_namespace.setter
    def hierarchical_namespace(self, value: Optional[pulumi.Input[BucketHierarchicalNamespaceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipFilter")
    def ip_filter(self) -> Optional[pulumi.Input[BucketIpFilterArgs]]:
        
        ...
    
    @ip_filter.setter
    def ip_filter(self, value: Optional[pulumi.Input[BucketIpFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleRules")
    def lifecycle_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]]:
        
        ...
    
    @lifecycle_rules.setter
    def lifecycle_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[BucketLoggingArgs]]:
        
        ...
    
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[BucketLoggingArgs]]): # -> None:
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
    @pulumi.getter(name="publicAccessPrevention")
    def public_access_prevention(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_access_prevention.setter
    def public_access_prevention(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requesterPays")
    def requester_pays(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @requester_pays.setter
    def requester_pays(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input[BucketRetentionPolicyArgs]]:
        
        ...
    
    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input[BucketRetentionPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rpo.setter
    def rpo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(self) -> Optional[pulumi.Input[BucketSoftDeletePolicyArgs]]:
        
        ...
    
    @soft_delete_policy.setter
    def soft_delete_policy(self, value: Optional[pulumi.Input[BucketSoftDeletePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniformBucketLevelAccess")
    def uniform_bucket_level_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @uniform_bucket_level_access.setter
    def uniform_bucket_level_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versioning(self) -> Optional[pulumi.Input[BucketVersioningArgs]]:
        
        ...
    
    @versioning.setter
    def versioning(self, value: Optional[pulumi.Input[BucketVersioningArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def website(self) -> Optional[pulumi.Input[BucketWebsiteArgs]]:
        
        ...
    
    @website.setter
    def website(self, value: Optional[pulumi.Input[BucketWebsiteArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketState:
    def __init__(__self__, *, autoclass: Optional[pulumi.Input[BucketAutoclassArgs]] = ..., cors: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorArgs]]]] = ..., custom_placement_config: Optional[pulumi.Input[BucketCustomPlacementConfigArgs]] = ..., default_event_based_hold: Optional[pulumi.Input[_builtins.bool]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_object_retention: Optional[pulumi.Input[_builtins.bool]] = ..., encryption: Optional[pulumi.Input[BucketEncryptionArgs]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., hierarchical_namespace: Optional[pulumi.Input[BucketHierarchicalNamespaceArgs]] = ..., ip_filter: Optional[pulumi.Input[BucketIpFilterArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[BucketLoggingArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., project_number: Optional[pulumi.Input[_builtins.int]] = ..., public_access_prevention: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., requester_pays: Optional[pulumi.Input[_builtins.bool]] = ..., retention_policy: Optional[pulumi.Input[BucketRetentionPolicyArgs]] = ..., rpo: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., soft_delete_policy: Optional[pulumi.Input[BucketSoftDeletePolicyArgs]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., time_created: Optional[pulumi.Input[_builtins.str]] = ..., uniform_bucket_level_access: Optional[pulumi.Input[_builtins.bool]] = ..., updated: Optional[pulumi.Input[_builtins.str]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ..., versioning: Optional[pulumi.Input[BucketVersioningArgs]] = ..., website: Optional[pulumi.Input[BucketWebsiteArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def autoclass(self) -> Optional[pulumi.Input[BucketAutoclassArgs]]:
        
        ...
    
    @autoclass.setter
    def autoclass(self, value: Optional[pulumi.Input[BucketAutoclassArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorArgs]]]]:
        
        ...
    
    @cors.setter
    def cors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketCorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPlacementConfig")
    def custom_placement_config(self) -> Optional[pulumi.Input[BucketCustomPlacementConfigArgs]]:
        
        ...
    
    @custom_placement_config.setter
    def custom_placement_config(self, value: Optional[pulumi.Input[BucketCustomPlacementConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEventBasedHold")
    def default_event_based_hold(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @default_event_based_hold.setter
    def default_event_based_hold(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableObjectRetention")
    def enable_object_retention(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_object_retention.setter
    def enable_object_retention(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[BucketEncryptionArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[BucketEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchicalNamespace")
    def hierarchical_namespace(self) -> Optional[pulumi.Input[BucketHierarchicalNamespaceArgs]]:
        
        ...
    
    @hierarchical_namespace.setter
    def hierarchical_namespace(self, value: Optional[pulumi.Input[BucketHierarchicalNamespaceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipFilter")
    def ip_filter(self) -> Optional[pulumi.Input[BucketIpFilterArgs]]:
        
        ...
    
    @ip_filter.setter
    def ip_filter(self, value: Optional[pulumi.Input[BucketIpFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleRules")
    def lifecycle_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]]:
        
        ...
    
    @lifecycle_rules.setter
    def lifecycle_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleArgs]]]]): # -> None:
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
    def logging(self) -> Optional[pulumi.Input[BucketLoggingArgs]]:
        
        ...
    
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[BucketLoggingArgs]]): # -> None:
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
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @project_number.setter
    def project_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicAccessPrevention")
    def public_access_prevention(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_access_prevention.setter
    def public_access_prevention(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requesterPays")
    def requester_pays(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @requester_pays.setter
    def requester_pays(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input[BucketRetentionPolicyArgs]]:
        
        ...
    
    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input[BucketRetentionPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rpo.setter
    def rpo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(self) -> Optional[pulumi.Input[BucketSoftDeletePolicyArgs]]:
        
        ...
    
    @soft_delete_policy.setter
    def soft_delete_policy(self, value: Optional[pulumi.Input[BucketSoftDeletePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniformBucketLevelAccess")
    def uniform_bucket_level_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @uniform_bucket_level_access.setter
    def uniform_bucket_level_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def updated(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated.setter
    def updated(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versioning(self) -> Optional[pulumi.Input[BucketVersioningArgs]]:
        
        ...
    
    @versioning.setter
    def versioning(self, value: Optional[pulumi.Input[BucketVersioningArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def website(self) -> Optional[pulumi.Input[BucketWebsiteArgs]]:
        
        ...
    
    @website.setter
    def website(self, value: Optional[pulumi.Input[BucketWebsiteArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:storage/bucket:Bucket")
class Bucket(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autoclass: Optional[pulumi.Input[Union[BucketAutoclassArgs, BucketAutoclassArgsDict]]] = ..., cors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketCorArgs, BucketCorArgsDict]]]]] = ..., custom_placement_config: Optional[pulumi.Input[Union[BucketCustomPlacementConfigArgs, BucketCustomPlacementConfigArgsDict]]] = ..., default_event_based_hold: Optional[pulumi.Input[_builtins.bool]] = ..., enable_object_retention: Optional[pulumi.Input[_builtins.bool]] = ..., encryption: Optional[pulumi.Input[Union[BucketEncryptionArgs, BucketEncryptionArgsDict]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., hierarchical_namespace: Optional[pulumi.Input[Union[BucketHierarchicalNamespaceArgs, BucketHierarchicalNamespaceArgsDict]]] = ..., ip_filter: Optional[pulumi.Input[Union[BucketIpFilterArgs, BucketIpFilterArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketLifecycleRuleArgs, BucketLifecycleRuleArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[Union[BucketLoggingArgs, BucketLoggingArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., public_access_prevention: Optional[pulumi.Input[_builtins.str]] = ..., requester_pays: Optional[pulumi.Input[_builtins.bool]] = ..., retention_policy: Optional[pulumi.Input[Union[BucketRetentionPolicyArgs, BucketRetentionPolicyArgsDict]]] = ..., rpo: Optional[pulumi.Input[_builtins.str]] = ..., soft_delete_policy: Optional[pulumi.Input[Union[BucketSoftDeletePolicyArgs, BucketSoftDeletePolicyArgsDict]]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., uniform_bucket_level_access: Optional[pulumi.Input[_builtins.bool]] = ..., versioning: Optional[pulumi.Input[Union[BucketVersioningArgs, BucketVersioningArgsDict]]] = ..., website: Optional[pulumi.Input[Union[BucketWebsiteArgs, BucketWebsiteArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., autoclass: Optional[pulumi.Input[Union[BucketAutoclassArgs, BucketAutoclassArgsDict]]] = ..., cors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketCorArgs, BucketCorArgsDict]]]]] = ..., custom_placement_config: Optional[pulumi.Input[Union[BucketCustomPlacementConfigArgs, BucketCustomPlacementConfigArgsDict]]] = ..., default_event_based_hold: Optional[pulumi.Input[_builtins.bool]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_object_retention: Optional[pulumi.Input[_builtins.bool]] = ..., encryption: Optional[pulumi.Input[Union[BucketEncryptionArgs, BucketEncryptionArgsDict]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., hierarchical_namespace: Optional[pulumi.Input[Union[BucketHierarchicalNamespaceArgs, BucketHierarchicalNamespaceArgsDict]]] = ..., ip_filter: Optional[pulumi.Input[Union[BucketIpFilterArgs, BucketIpFilterArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifecycle_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BucketLifecycleRuleArgs, BucketLifecycleRuleArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[Union[BucketLoggingArgs, BucketLoggingArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., project_number: Optional[pulumi.Input[_builtins.int]] = ..., public_access_prevention: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., requester_pays: Optional[pulumi.Input[_builtins.bool]] = ..., retention_policy: Optional[pulumi.Input[Union[BucketRetentionPolicyArgs, BucketRetentionPolicyArgsDict]]] = ..., rpo: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., soft_delete_policy: Optional[pulumi.Input[Union[BucketSoftDeletePolicyArgs, BucketSoftDeletePolicyArgsDict]]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., time_created: Optional[pulumi.Input[_builtins.str]] = ..., uniform_bucket_level_access: Optional[pulumi.Input[_builtins.bool]] = ..., updated: Optional[pulumi.Input[_builtins.str]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ..., versioning: Optional[pulumi.Input[Union[BucketVersioningArgs, BucketVersioningArgsDict]]] = ..., website: Optional[pulumi.Input[Union[BucketWebsiteArgs, BucketWebsiteArgsDict]]] = ...) -> Bucket:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def autoclass(self) -> pulumi.Output[Optional[outputs.BucketAutoclass]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> pulumi.Output[Optional[Sequence[outputs.BucketCor]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPlacementConfig")
    def custom_placement_config(self) -> pulumi.Output[Optional[outputs.BucketCustomPlacementConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEventBasedHold")
    def default_event_based_hold(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableObjectRetention")
    def enable_object_retention(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional[outputs.BucketEncryption]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchicalNamespace")
    def hierarchical_namespace(self) -> pulumi.Output[Optional[outputs.BucketHierarchicalNamespace]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipFilter")
    def ip_filter(self) -> pulumi.Output[Optional[outputs.BucketIpFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleRules")
    def lifecycle_rules(self) -> pulumi.Output[Optional[Sequence[outputs.BucketLifecycleRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> pulumi.Output[Optional[outputs.BucketLogging]]:
        
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
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicAccessPrevention")
    def public_access_prevention(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requesterPays")
    def requester_pays(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> pulumi.Output[Optional[outputs.BucketRetentionPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(self) -> pulumi.Output[outputs.BucketSoftDeletePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniformBucketLevelAccess")
    def uniform_bucket_level_access(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def updated(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versioning(self) -> pulumi.Output[outputs.BucketVersioning]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def website(self) -> pulumi.Output[outputs.BucketWebsite]:
        
        ...
    


