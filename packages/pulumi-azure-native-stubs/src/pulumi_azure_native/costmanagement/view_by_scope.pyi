

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ViewByScopeArgs', 'ViewByScope']
@pulumi.input_type
class ViewByScopeArgs:
    def __init__(__self__, *, scope: pulumi.Input[_builtins.str], timeframe: pulumi.Input[Union[_builtins.str, ReportTimeframeType]], type: pulumi.Input[Union[_builtins.str, ReportType]], accumulated: Optional[pulumi.Input[Union[_builtins.str, AccumulatedType]]] = ..., chart: Optional[pulumi.Input[Union[_builtins.str, ChartType]]] = ..., data_set: Optional[pulumi.Input[ReportConfigDatasetArgs]] = ..., date_range: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., e_tag: Optional[pulumi.Input[_builtins.str]] = ..., include_monetary_commitment: Optional[pulumi.Input[_builtins.bool]] = ..., kpis: Optional[pulumi.Input[Sequence[pulumi.Input[KpiPropertiesArgs]]]] = ..., metric: Optional[pulumi.Input[Union[_builtins.str, MetricType]]] = ..., modified_on: Optional[pulumi.Input[_builtins.str]] = ..., pivots: Optional[pulumi.Input[Sequence[pulumi.Input[PivotPropertiesArgs]]]] = ..., time_period: Optional[pulumi.Input[ReportConfigTimePeriodArgs]] = ..., view_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeframe(self) -> pulumi.Input[Union[_builtins.str, ReportTimeframeType]]:
        
        ...
    
    @timeframe.setter
    def timeframe(self, value: pulumi.Input[Union[_builtins.str, ReportTimeframeType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ReportType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ReportType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accumulated(self) -> Optional[pulumi.Input[Union[_builtins.str, AccumulatedType]]]:
        
        ...
    
    @accumulated.setter
    def accumulated(self, value: Optional[pulumi.Input[Union[_builtins.str, AccumulatedType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def chart(self) -> Optional[pulumi.Input[Union[_builtins.str, ChartType]]]:
        
        ...
    
    @chart.setter
    def chart(self, value: Optional[pulumi.Input[Union[_builtins.str, ChartType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSet")
    def data_set(self) -> Optional[pulumi.Input[ReportConfigDatasetArgs]]:
        
        ...
    
    @data_set.setter
    def data_set(self, value: Optional[pulumi.Input[ReportConfigDatasetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date_range.setter
    def date_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeMonetaryCommitment")
    def include_monetary_commitment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_monetary_commitment.setter
    def include_monetary_commitment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kpis(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[KpiPropertiesArgs]]]]:
        
        ...
    
    @kpis.setter
    def kpis(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KpiPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> Optional[pulumi.Input[Union[_builtins.str, MetricType]]]:
        
        ...
    
    @metric.setter
    def metric(self, value: Optional[pulumi.Input[Union[_builtins.str, MetricType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @modified_on.setter
    def modified_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def pivots(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PivotPropertiesArgs]]]]:
        
        ...
    
    @pivots.setter
    def pivots(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PivotPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> Optional[pulumi.Input[ReportConfigTimePeriodArgs]]:
        
        ...
    
    @time_period.setter
    def time_period(self, value: Optional[pulumi.Input[ReportConfigTimePeriodArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewName")
    def view_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @view_name.setter
    def view_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:costmanagement:ViewByScope")
class ViewByScope(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., accumulated: Optional[pulumi.Input[Union[_builtins.str, AccumulatedType]]] = ..., chart: Optional[pulumi.Input[Union[_builtins.str, ChartType]]] = ..., data_set: Optional[pulumi.Input[Union[ReportConfigDatasetArgs, ReportConfigDatasetArgsDict]]] = ..., date_range: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., e_tag: Optional[pulumi.Input[_builtins.str]] = ..., include_monetary_commitment: Optional[pulumi.Input[_builtins.bool]] = ..., kpis: Optional[pulumi.Input[Sequence[pulumi.Input[Union[KpiPropertiesArgs, KpiPropertiesArgsDict]]]]] = ..., metric: Optional[pulumi.Input[Union[_builtins.str, MetricType]]] = ..., modified_on: Optional[pulumi.Input[_builtins.str]] = ..., pivots: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PivotPropertiesArgs, PivotPropertiesArgsDict]]]]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., time_period: Optional[pulumi.Input[Union[ReportConfigTimePeriodArgs, ReportConfigTimePeriodArgsDict]]] = ..., timeframe: Optional[pulumi.Input[Union[_builtins.str, ReportTimeframeType]]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, ReportType]]] = ..., view_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ViewByScopeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ViewByScope:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accumulated(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def chart(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSet")
    def data_set(self) -> pulumi.Output[Optional[outputs.ReportConfigDatasetResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeMonetaryCommitment")
    def include_monetary_commitment(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kpis(self) -> pulumi.Output[Optional[Sequence[outputs.KpiPropertiesResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pivots(self) -> pulumi.Output[Optional[Sequence[outputs.PivotPropertiesResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> pulumi.Output[Optional[outputs.ReportConfigTimePeriodResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeframe(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


