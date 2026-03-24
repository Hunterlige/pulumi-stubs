

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DashboardArgs', 'Dashboard']
@pulumi.input_type
class DashboardArgs:
    def __init__(__self__, *, dashboard_body: pulumi.Input[_builtins.str], dashboard_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardBody")
    def dashboard_body(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dashboard_body.setter
    def dashboard_body(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardName")
    def dashboard_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dashboard_name.setter
    def dashboard_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DashboardState:
    def __init__(__self__, *, dashboard_arn: Optional[pulumi.Input[_builtins.str]] = ..., dashboard_body: Optional[pulumi.Input[_builtins.str]] = ..., dashboard_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardArn")
    def dashboard_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dashboard_arn.setter
    def dashboard_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardBody")
    def dashboard_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dashboard_body.setter
    def dashboard_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardName")
    def dashboard_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dashboard_name.setter
    def dashboard_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudwatch/dashboard:Dashboard")
class Dashboard(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dashboard_body: Optional[pulumi.Input[_builtins.str]] = ..., dashboard_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DashboardArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., dashboard_arn: Optional[pulumi.Input[_builtins.str]] = ..., dashboard_body: Optional[pulumi.Input[_builtins.str]] = ..., dashboard_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> Dashboard:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardArn")
    def dashboard_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardBody")
    def dashboard_body(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardName")
    def dashboard_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


