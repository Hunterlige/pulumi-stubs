

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ServicePerimeterArgs', 'ServicePerimeter']
@pulumi.input_type
class ServicePerimeterArgs:
    def __init__(__self__, *, parent: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., perimeter_type: Optional[pulumi.Input[_builtins.str]] = ..., spec: Optional[pulumi.Input[ServicePerimeterSpecArgs]] = ..., status: Optional[pulumi.Input[ServicePerimeterStatusArgs]] = ..., use_explicit_dry_run_spec: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perimeterType")
    def perimeter_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @perimeter_type.setter
    def perimeter_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[ServicePerimeterSpecArgs]]:
        
        ...
    
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[ServicePerimeterSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[ServicePerimeterStatusArgs]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[ServicePerimeterStatusArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useExplicitDryRunSpec")
    def use_explicit_dry_run_spec(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_explicit_dry_run_spec.setter
    def use_explicit_dry_run_spec(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _ServicePerimeterState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., perimeter_type: Optional[pulumi.Input[_builtins.str]] = ..., spec: Optional[pulumi.Input[ServicePerimeterSpecArgs]] = ..., status: Optional[pulumi.Input[ServicePerimeterStatusArgs]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., use_explicit_dry_run_spec: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
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
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perimeterType")
    def perimeter_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @perimeter_type.setter
    def perimeter_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[ServicePerimeterSpecArgs]]:
        
        ...
    
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[ServicePerimeterSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[ServicePerimeterStatusArgs]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[ServicePerimeterStatusArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useExplicitDryRunSpec")
    def use_explicit_dry_run_spec(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_explicit_dry_run_spec.setter
    def use_explicit_dry_run_spec(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ServicePerimeter(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., perimeter_type: Optional[pulumi.Input[_builtins.str]] = ..., spec: Optional[pulumi.Input[Union[ServicePerimeterSpecArgs, ServicePerimeterSpecArgsDict]]] = ..., status: Optional[pulumi.Input[Union[ServicePerimeterStatusArgs, ServicePerimeterStatusArgsDict]]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., use_explicit_dry_run_spec: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServicePerimeterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., perimeter_type: Optional[pulumi.Input[_builtins.str]] = ..., spec: Optional[pulumi.Input[Union[ServicePerimeterSpecArgs, ServicePerimeterSpecArgsDict]]] = ..., status: Optional[pulumi.Input[Union[ServicePerimeterStatusArgs, ServicePerimeterStatusArgsDict]]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., use_explicit_dry_run_spec: Optional[pulumi.Input[_builtins.bool]] = ...) -> ServicePerimeter:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perimeterType")
    def perimeter_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def spec(self) -> pulumi.Output[Optional[outputs.ServicePerimeterSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[outputs.ServicePerimeterStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useExplicitDryRunSpec")
    def use_explicit_dry_run_spec(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


