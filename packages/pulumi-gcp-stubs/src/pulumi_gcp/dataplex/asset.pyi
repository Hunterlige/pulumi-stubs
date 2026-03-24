

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
__all__ = ['AssetArgs', 'Asset']
@pulumi.input_type
class AssetArgs:
    def __init__(__self__, *, dataplex_zone: pulumi.Input[_builtins.str], discovery_spec: pulumi.Input[AssetDiscoverySpecArgs], lake: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], resource_spec: pulumi.Input[AssetResourceSpecArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dataplex_zone.setter
    def dataplex_zone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoverySpec")
    def discovery_spec(self) -> pulumi.Input[AssetDiscoverySpecArgs]:
        
        ...
    
    @discovery_spec.setter
    def discovery_spec(self, value: pulumi.Input[AssetDiscoverySpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lake(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lake.setter
    def lake(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> pulumi.Input[AssetResourceSpecArgs]:
        
        ...
    
    @resource_spec.setter
    def resource_spec(self, value: pulumi.Input[AssetResourceSpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.input_type
class _AssetState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., dataplex_zone: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovery_spec: Optional[pulumi.Input[AssetDiscoverySpecArgs]] = ..., discovery_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[AssetDiscoveryStatusArgs]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_spec: Optional[pulumi.Input[AssetResourceSpecArgs]] = ..., resource_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[AssetResourceStatusArgs]]]] = ..., security_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[AssetSecurityStatusArgs]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataplex_zone.setter
    def dataplex_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoverySpec")
    def discovery_spec(self) -> Optional[pulumi.Input[AssetDiscoverySpecArgs]]:
        
        ...
    
    @discovery_spec.setter
    def discovery_spec(self, value: Optional[pulumi.Input[AssetDiscoverySpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryStatuses")
    def discovery_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssetDiscoveryStatusArgs]]]]:
        
        ...
    
    @discovery_statuses.setter
    def discovery_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AssetDiscoveryStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lake(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lake.setter
    def lake(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> Optional[pulumi.Input[AssetResourceSpecArgs]]:
        
        ...
    
    @resource_spec.setter
    def resource_spec(self, value: Optional[pulumi.Input[AssetResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStatuses")
    def resource_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssetResourceStatusArgs]]]]:
        
        ...
    
    @resource_statuses.setter
    def resource_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AssetResourceStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityStatuses")
    def security_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssetSecurityStatusArgs]]]]:
        
        ...
    
    @security_statuses.setter
    def security_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AssetSecurityStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("gcp:dataplex/asset:Asset")
class Asset(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dataplex_zone: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovery_spec: Optional[pulumi.Input[Union[AssetDiscoverySpecArgs, AssetDiscoverySpecArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., resource_spec: Optional[pulumi.Input[Union[AssetResourceSpecArgs, AssetResourceSpecArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AssetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dataplex_zone: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovery_spec: Optional[pulumi.Input[Union[AssetDiscoverySpecArgs, AssetDiscoverySpecArgsDict]]] = ..., discovery_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AssetDiscoveryStatusArgs, AssetDiscoveryStatusArgsDict]]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_spec: Optional[pulumi.Input[Union[AssetResourceSpecArgs, AssetResourceSpecArgsDict]]] = ..., resource_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AssetResourceStatusArgs, AssetResourceStatusArgsDict]]]]] = ..., security_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AssetSecurityStatusArgs, AssetSecurityStatusArgsDict]]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Asset:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoverySpec")
    def discovery_spec(self) -> pulumi.Output[outputs.AssetDiscoverySpec]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryStatuses")
    def discovery_statuses(self) -> pulumi.Output[Sequence[outputs.AssetDiscoveryStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lake(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> pulumi.Output[outputs.AssetResourceSpec]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStatuses")
    def resource_statuses(self) -> pulumi.Output[Sequence[outputs.AssetResourceStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityStatuses")
    def security_statuses(self) -> pulumi.Output[Sequence[outputs.AssetSecurityStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


