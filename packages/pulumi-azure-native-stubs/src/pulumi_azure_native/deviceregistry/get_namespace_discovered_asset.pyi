

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNamespaceDiscoveredAssetResult', 'AwaitableGetNamespaceDiscoveredAssetResult', 'get_namespace_discovered_asset', 'get_namespace_discovered_asset_output']
@pulumi.output_type
class GetNamespaceDiscoveredAssetResult:
    
    def __init__(__self__, asset_type_refs=..., attributes=..., azure_api_version=..., datasets=..., default_datasets_configuration=..., default_datasets_destinations=..., default_events_configuration=..., default_events_destinations=..., default_management_groups_configuration=..., default_streams_configuration=..., default_streams_destinations=..., device_ref=..., discovery_id=..., documentation_uri=..., events=..., extended_location=..., hardware_revision=..., id=..., location=..., management_groups=..., manufacturer=..., manufacturer_uri=..., model=..., name=..., product_code=..., provisioning_state=..., serial_number=..., software_revision=..., streams=..., system_data=..., tags=..., type=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assetTypeRefs")
    def asset_type_refs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datasets(self) -> Optional[Sequence[outputs.NamespaceDiscoveredDatasetResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDatasetsConfiguration")
    def default_datasets_configuration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDatasetsDestinations")
    def default_datasets_destinations(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEventsConfiguration")
    def default_events_configuration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEventsDestinations")
    def default_events_destinations(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultManagementGroupsConfiguration")
    def default_management_groups_configuration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultStreamsConfiguration")
    def default_streams_configuration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultStreamsDestinations")
    def default_streams_destinations(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceRef")
    def device_ref(self) -> outputs.DeviceRefResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryId")
    def discovery_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentationUri")
    def documentation_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[outputs.NamespaceDiscoveredEventResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareRevision")
    def hardware_revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[Sequence[outputs.NamespaceDiscoveredManagementGroupResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def manufacturer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manufacturerUri")
    def manufacturer_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareRevision")
    def software_revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Optional[Sequence[outputs.NamespaceDiscoveredStreamResponse]]:
        
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
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.float:
        
        ...
    


class AwaitableGetNamespaceDiscoveredAssetResult(GetNamespaceDiscoveredAssetResult):
    def __await__(self): # -> Generator[Never, Any, GetNamespaceDiscoveredAssetResult]:
        ...
    


def get_namespace_discovered_asset(discovered_asset_name: Optional[_builtins.str] = ..., namespace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNamespaceDiscoveredAssetResult:
    
    ...

def get_namespace_discovered_asset_output(discovered_asset_name: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNamespaceDiscoveredAssetResult]:
    
    ...

