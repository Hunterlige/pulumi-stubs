

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BudgetArgs', 'Budget']
@pulumi.input_type
class BudgetArgs:
    def __init__(__self__, *, category: pulumi.Input[Union[_builtins.str, CategoryType]], scope: pulumi.Input[_builtins.str], time_grain: pulumi.Input[Union[_builtins.str, TimeGrainType]], time_period: pulumi.Input[BudgetTimePeriodArgs], amount: Optional[pulumi.Input[_builtins.float]] = ..., budget_name: Optional[pulumi.Input[_builtins.str]] = ..., e_tag: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[BudgetFilterArgs]] = ..., notifications: Optional[pulumi.Input[Mapping[str, pulumi.Input[NotificationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[Union[_builtins.str, CategoryType]]:
        
        ...
    
    @category.setter
    def category(self, value: pulumi.Input[Union[_builtins.str, CategoryType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> pulumi.Input[Union[_builtins.str, TimeGrainType]]:
        
        ...
    
    @time_grain.setter
    def time_grain(self, value: pulumi.Input[Union[_builtins.str, TimeGrainType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> pulumi.Input[BudgetTimePeriodArgs]:
        
        ...
    
    @time_period.setter
    def time_period(self, value: pulumi.Input[BudgetTimePeriodArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @amount.setter
    def amount(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="budgetName")
    def budget_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @budget_name.setter
    def budget_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[BudgetFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[BudgetFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[NotificationArgs]]]]:
        
        ...
    
    @notifications.setter
    def notifications(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[NotificationArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:costmanagement:Budget")
class Budget(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., amount: Optional[pulumi.Input[_builtins.float]] = ..., budget_name: Optional[pulumi.Input[_builtins.str]] = ..., category: Optional[pulumi.Input[Union[_builtins.str, CategoryType]]] = ..., e_tag: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[Union[BudgetFilterArgs, BudgetFilterArgsDict]]] = ..., notifications: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union[NotificationArgs, NotificationArgsDict]]]]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., time_grain: Optional[pulumi.Input[Union[_builtins.str, TimeGrainType]]] = ..., time_period: Optional[pulumi.Input[Union[BudgetTimePeriodArgs, BudgetTimePeriodArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BudgetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Budget:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentSpend")
    def current_spend(self) -> pulumi.Output[outputs.CurrentSpendResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[outputs.BudgetFilterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forecastSpend")
    def forecast_spend(self) -> pulumi.Output[outputs.ForecastSpendResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> pulumi.Output[Optional[Mapping[str, outputs.NotificationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> pulumi.Output[outputs.BudgetTimePeriodResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


