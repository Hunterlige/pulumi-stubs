

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FolderFeedCondition', 'FolderFeedFeedOutputConfig', 'FolderFeedFeedOutputConfigPubsubDestination', 'OrganizationFeedCondition', 'OrganizationFeedFeedOutputConfig', 'OrganizationFeedFeedOutputConfigPubsubDestination', 'ProjectFeedCondition', 'ProjectFeedFeedOutputConfig', 'ProjectFeedFeedOutputConfigPubsubDestination', 'GetResourcesSearchAllResultResult', 'GetSearchAllResourcesResultResult']
@pulumi.output_type
class FolderFeedCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, description: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FolderFeedFeedOutputConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pubsub_destination: outputs.FolderFeedFeedOutputConfigPubsubDestination) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(self) -> outputs.FolderFeedFeedOutputConfigPubsubDestination:
        
        ...
    


@pulumi.output_type
class FolderFeedFeedOutputConfigPubsubDestination(dict):
    def __init__(__self__, *, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class OrganizationFeedCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, description: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OrganizationFeedFeedOutputConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pubsub_destination: outputs.OrganizationFeedFeedOutputConfigPubsubDestination) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(self) -> outputs.OrganizationFeedFeedOutputConfigPubsubDestination:
        
        ...
    


@pulumi.output_type
class OrganizationFeedFeedOutputConfigPubsubDestination(dict):
    def __init__(__self__, *, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProjectFeedCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, description: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProjectFeedFeedOutputConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pubsub_destination: outputs.ProjectFeedFeedOutputConfigPubsubDestination) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(self) -> outputs.ProjectFeedFeedOutputConfigPubsubDestination:
        
        ...
    


@pulumi.output_type
class ProjectFeedFeedOutputConfigPubsubDestination(dict):
    def __init__(__self__, *, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetResourcesSearchAllResultResult(dict):
    def __init__(__self__, *, additional_attributes: Sequence[_builtins.str], asset_type: _builtins.str, description: _builtins.str, display_name: _builtins.str, labels: Mapping[str, _builtins.str], location: _builtins.str, name: _builtins.str, network_tags: Sequence[_builtins.str], project: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalAttributes")
    def additional_attributes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assetType")
    def asset_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSearchAllResourcesResultResult(dict):
    def __init__(__self__, *, asset_type: _builtins.str, create_time: _builtins.str, description: _builtins.str, display_name: _builtins.str, folders: Sequence[_builtins.str], kms_keys: Sequence[_builtins.str], labels: Mapping[str, _builtins.str], location: _builtins.str, name: _builtins.str, network_tags: Sequence[_builtins.str], organization: _builtins.str, parent_asset_type: _builtins.str, parent_full_resource_name: _builtins.str, project: _builtins.str, state: _builtins.str, update_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assetType")
    def asset_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folders(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeys")
    def kms_keys(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentAssetType")
    def parent_asset_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentFullResourceName")
    def parent_full_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


