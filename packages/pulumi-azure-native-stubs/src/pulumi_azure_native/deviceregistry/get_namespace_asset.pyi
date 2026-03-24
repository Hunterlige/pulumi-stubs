

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNamespaceAssetResult', 'AwaitableGetNamespaceAssetResult', 'get_namespace_asset', 'get_namespace_asset_output']
@pulumi.output_type
class GetNamespaceAssetResult:
    
    def __init__(__self__, asset_type_refs=..., attributes=..., azure_api_version=..., datasets=..., default_datasets_configuration=..., default_datasets_destinations=..., default_events_configuration=..., default_events_destinations=..., default_management_groups_configuration=..., default_streams_configuration=..., default_streams_destinations=..., description=..., device_ref=..., discovered_asset_refs=..., display_name=..., documentation_uri=..., enabled=..., events=..., extended_location=..., external_asset_id=..., hardware_revision=..., id=..., last_transition_time=..., location=..., management_groups=..., manufacturer=..., manufacturer_uri=..., model=..., name=..., product_code=..., provisioning_state=..., serial_number=..., software_revision=..., status=..., streams=..., system_data=..., tags=..., type=..., uuid=..., version=...) -> None:
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
    def datasets(self) -> Optional[Sequence[outputs.NamespaceDatasetResponse]]:
        
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
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceRef")
    def device_ref(self) -> outputs.DeviceRefResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredAssetRefs")
    def discovered_asset_refs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentationUri")
    def documentation_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[outputs.NamespaceEventResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalAssetId")
    def external_asset_id(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[Sequence[outputs.ManagementGroupResponse]]:
        
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
    def status(self) -> outputs.NamespaceAssetStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Optional[Sequence[outputs.NamespaceStreamResponse]]:
        
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
    def uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.float:
        
        ...
    


class AwaitableGetNamespaceAssetResult(GetNamespaceAssetResult):
    def __await__(self): # -> Generator[Never, Any, GetNamespaceAssetResult]:
        ...
    


def get_namespace_asset(asset_name: Optional[_builtins.str] = ..., namespace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNamespaceAssetResult:
    
    ...

def get_namespace_asset_output(asset_name: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNamespaceAssetResult]:
    
    ...

