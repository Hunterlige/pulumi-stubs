

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBucketResult', 'AwaitableGetBucketResult', 'get_bucket', 'get_bucket_output']
@pulumi.output_type
class GetBucketResult:
    
    def __init__(__self__, autoclasses=..., cors=..., custom_placement_configs=..., default_event_based_hold=..., effective_labels=..., enable_object_retention=..., encryptions=..., force_destroy=..., hierarchical_namespaces=..., id=..., ip_filters=..., labels=..., lifecycle_rules=..., location=..., loggings=..., name=..., project=..., project_number=..., public_access_prevention=..., pulumi_labels=..., requester_pays=..., retention_policies=..., rpo=..., self_link=..., soft_delete_policies=..., storage_class=..., time_created=..., uniform_bucket_level_access=..., updated=..., url=..., versionings=..., websites=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def autoclasses(self) -> Sequence[outputs.GetBucketAutoclassResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Sequence[outputs.GetBucketCorResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPlacementConfigs")
    def custom_placement_configs(self) -> Sequence[outputs.GetBucketCustomPlacementConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEventBasedHold")
    def default_event_based_hold(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableObjectRetention")
    def enable_object_retention(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryptions(self) -> Sequence[outputs.GetBucketEncryptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchicalNamespaces")
    def hierarchical_namespaces(self) -> Sequence[outputs.GetBucketHierarchicalNamespaceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipFilters")
    def ip_filters(self) -> Sequence[outputs.GetBucketIpFilterResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleRules")
    def lifecycle_rules(self) -> Sequence[outputs.GetBucketLifecycleRuleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def loggings(self) -> Sequence[outputs.GetBucketLoggingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicAccessPrevention")
    def public_access_prevention(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requesterPays")
    def requester_pays(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicies")
    def retention_policies(self) -> Sequence[outputs.GetBucketRetentionPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeletePolicies")
    def soft_delete_policies(self) -> Sequence[outputs.GetBucketSoftDeletePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniformBucketLevelAccess")
    def uniform_bucket_level_access(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def updated(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versionings(self) -> Sequence[outputs.GetBucketVersioningResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def websites(self) -> Sequence[outputs.GetBucketWebsiteResult]:
        ...
    


class AwaitableGetBucketResult(GetBucketResult):
    def __await__(self): # -> Generator[Never, Any, GetBucketResult]:
        ...
    


def get_bucket(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBucketResult:
    
    ...

def get_bucket_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBucketResult]:
    
    ...

