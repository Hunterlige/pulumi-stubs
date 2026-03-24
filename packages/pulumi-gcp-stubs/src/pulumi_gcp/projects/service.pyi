

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ServiceArgs', 'Service']
@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str], check_if_service_has_usage_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., disable_dependent_services: Optional[pulumi.Input[_builtins.bool]] = ..., disable_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkIfServiceHasUsageOnDestroy")
    def check_if_service_has_usage_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @check_if_service_has_usage_on_destroy.setter
    def check_if_service_has_usage_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDependentServices")
    def disable_dependent_services(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_dependent_services.setter
    def disable_dependent_services(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableOnDestroy")
    def disable_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_on_destroy.setter
    def disable_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ServiceState:
    def __init__(__self__, *, check_if_service_has_usage_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., disable_dependent_services: Optional[pulumi.Input[_builtins.bool]] = ..., disable_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkIfServiceHasUsageOnDestroy")
    def check_if_service_has_usage_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @check_if_service_has_usage_on_destroy.setter
    def check_if_service_has_usage_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDependentServices")
    def disable_dependent_services(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_dependent_services.setter
    def disable_dependent_services(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableOnDestroy")
    def disable_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_on_destroy.setter
    def disable_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:projects/service:Service")
class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., check_if_service_has_usage_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., disable_dependent_services: Optional[pulumi.Input[_builtins.bool]] = ..., disable_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServiceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., check_if_service_has_usage_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., disable_dependent_services: Optional[pulumi.Input[_builtins.bool]] = ..., disable_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ...) -> Service:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkIfServiceHasUsageOnDestroy")
    def check_if_service_has_usage_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDependentServices")
    def disable_dependent_services(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableOnDestroy")
    def disable_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


