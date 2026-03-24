

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
__all__ = ['DatascanArgs', 'Datascan']
@pulumi.input_type
class DatascanArgs:
    def __init__(__self__, *, data: pulumi.Input[DatascanDataArgs], data_scan_id: pulumi.Input[_builtins.str], execution_spec: pulumi.Input[DatascanExecutionSpecArgs], location: pulumi.Input[_builtins.str], data_discovery_spec: Optional[pulumi.Input[DatascanDataDiscoverySpecArgs]] = ..., data_documentation_spec: Optional[pulumi.Input[DatascanDataDocumentationSpecArgs]] = ..., data_profile_spec: Optional[pulumi.Input[DatascanDataProfileSpecArgs]] = ..., data_quality_spec: Optional[pulumi.Input[DatascanDataQualitySpecArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> pulumi.Input[DatascanDataArgs]:
        
        ...
    
    @data.setter
    def data(self, value: pulumi.Input[DatascanDataArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataScanId")
    def data_scan_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_scan_id.setter
    def data_scan_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionSpec")
    def execution_spec(self) -> pulumi.Input[DatascanExecutionSpecArgs]:
        
        ...
    
    @execution_spec.setter
    def execution_spec(self, value: pulumi.Input[DatascanExecutionSpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiscoverySpec")
    def data_discovery_spec(self) -> Optional[pulumi.Input[DatascanDataDiscoverySpecArgs]]:
        
        ...
    
    @data_discovery_spec.setter
    def data_discovery_spec(self, value: Optional[pulumi.Input[DatascanDataDiscoverySpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDocumentationSpec")
    def data_documentation_spec(self) -> Optional[pulumi.Input[DatascanDataDocumentationSpecArgs]]:
        
        ...
    
    @data_documentation_spec.setter
    def data_documentation_spec(self, value: Optional[pulumi.Input[DatascanDataDocumentationSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProfileSpec")
    def data_profile_spec(self) -> Optional[pulumi.Input[DatascanDataProfileSpecArgs]]:
        
        ...
    
    @data_profile_spec.setter
    def data_profile_spec(self, value: Optional[pulumi.Input[DatascanDataProfileSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataQualitySpec")
    def data_quality_spec(self) -> Optional[pulumi.Input[DatascanDataQualitySpecArgs]]:
        
        ...
    
    @data_quality_spec.setter
    def data_quality_spec(self, value: Optional[pulumi.Input[DatascanDataQualitySpecArgs]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DatascanState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., data: Optional[pulumi.Input[DatascanDataArgs]] = ..., data_discovery_spec: Optional[pulumi.Input[DatascanDataDiscoverySpecArgs]] = ..., data_documentation_spec: Optional[pulumi.Input[DatascanDataDocumentationSpecArgs]] = ..., data_profile_spec: Optional[pulumi.Input[DatascanDataProfileSpecArgs]] = ..., data_quality_spec: Optional[pulumi.Input[DatascanDataQualitySpecArgs]] = ..., data_scan_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., execution_spec: Optional[pulumi.Input[DatascanExecutionSpecArgs]] = ..., execution_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[DatascanExecutionStatusArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def data(self) -> Optional[pulumi.Input[DatascanDataArgs]]:
        
        ...
    
    @data.setter
    def data(self, value: Optional[pulumi.Input[DatascanDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiscoverySpec")
    def data_discovery_spec(self) -> Optional[pulumi.Input[DatascanDataDiscoverySpecArgs]]:
        
        ...
    
    @data_discovery_spec.setter
    def data_discovery_spec(self, value: Optional[pulumi.Input[DatascanDataDiscoverySpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDocumentationSpec")
    def data_documentation_spec(self) -> Optional[pulumi.Input[DatascanDataDocumentationSpecArgs]]:
        
        ...
    
    @data_documentation_spec.setter
    def data_documentation_spec(self, value: Optional[pulumi.Input[DatascanDataDocumentationSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProfileSpec")
    def data_profile_spec(self) -> Optional[pulumi.Input[DatascanDataProfileSpecArgs]]:
        
        ...
    
    @data_profile_spec.setter
    def data_profile_spec(self, value: Optional[pulumi.Input[DatascanDataProfileSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataQualitySpec")
    def data_quality_spec(self) -> Optional[pulumi.Input[DatascanDataQualitySpecArgs]]:
        
        ...
    
    @data_quality_spec.setter
    def data_quality_spec(self, value: Optional[pulumi.Input[DatascanDataQualitySpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataScanId")
    def data_scan_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_scan_id.setter
    def data_scan_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionSpec")
    def execution_spec(self) -> Optional[pulumi.Input[DatascanExecutionSpecArgs]]:
        
        ...
    
    @execution_spec.setter
    def execution_spec(self, value: Optional[pulumi.Input[DatascanExecutionSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionStatuses")
    def execution_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatascanExecutionStatusArgs]]]]:
        
        ...
    
    @execution_statuses.setter
    def execution_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatascanExecutionStatusArgs]]]]): # -> None:
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
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("gcp:dataplex/datascan:Datascan")
class Datascan(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data: Optional[pulumi.Input[Union[DatascanDataArgs, DatascanDataArgsDict]]] = ..., data_discovery_spec: Optional[pulumi.Input[Union[DatascanDataDiscoverySpecArgs, DatascanDataDiscoverySpecArgsDict]]] = ..., data_documentation_spec: Optional[pulumi.Input[Union[DatascanDataDocumentationSpecArgs, DatascanDataDocumentationSpecArgsDict]]] = ..., data_profile_spec: Optional[pulumi.Input[Union[DatascanDataProfileSpecArgs, DatascanDataProfileSpecArgsDict]]] = ..., data_quality_spec: Optional[pulumi.Input[Union[DatascanDataQualitySpecArgs, DatascanDataQualitySpecArgsDict]]] = ..., data_scan_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., execution_spec: Optional[pulumi.Input[Union[DatascanExecutionSpecArgs, DatascanExecutionSpecArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DatascanArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data: Optional[pulumi.Input[Union[DatascanDataArgs, DatascanDataArgsDict]]] = ..., data_discovery_spec: Optional[pulumi.Input[Union[DatascanDataDiscoverySpecArgs, DatascanDataDiscoverySpecArgsDict]]] = ..., data_documentation_spec: Optional[pulumi.Input[Union[DatascanDataDocumentationSpecArgs, DatascanDataDocumentationSpecArgsDict]]] = ..., data_profile_spec: Optional[pulumi.Input[Union[DatascanDataProfileSpecArgs, DatascanDataProfileSpecArgsDict]]] = ..., data_quality_spec: Optional[pulumi.Input[Union[DatascanDataQualitySpecArgs, DatascanDataQualitySpecArgsDict]]] = ..., data_scan_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., execution_spec: Optional[pulumi.Input[Union[DatascanExecutionSpecArgs, DatascanExecutionSpecArgsDict]]] = ..., execution_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DatascanExecutionStatusArgs, DatascanExecutionStatusArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Datascan:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> pulumi.Output[outputs.DatascanData]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiscoverySpec")
    def data_discovery_spec(self) -> pulumi.Output[Optional[outputs.DatascanDataDiscoverySpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDocumentationSpec")
    def data_documentation_spec(self) -> pulumi.Output[Optional[outputs.DatascanDataDocumentationSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProfileSpec")
    def data_profile_spec(self) -> pulumi.Output[Optional[outputs.DatascanDataProfileSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataQualitySpec")
    def data_quality_spec(self) -> pulumi.Output[Optional[outputs.DatascanDataQualitySpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataScanId")
    def data_scan_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="executionSpec")
    def execution_spec(self) -> pulumi.Output[outputs.DatascanExecutionSpec]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionStatuses")
    def execution_statuses(self) -> pulumi.Output[Sequence[outputs.DatascanExecutionStatus]]:
        
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
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


