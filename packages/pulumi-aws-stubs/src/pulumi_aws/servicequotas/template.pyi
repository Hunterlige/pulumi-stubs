

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from .. import _utilities

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TemplateArgs', 'Template']
@pulumi.input_type
class TemplateArgs:
    def __init__(__self__, *, quota_code: pulumi.Input[_builtins.str], service_code: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.float], aws_region: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaCode")
    def quota_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @quota_code.setter
    def quota_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_code.setter
    def service_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_region.setter
    def aws_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""region is deprecated. Use get_region instead.""")
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TemplateState:
    def __init__(__self__, *, aws_region: Optional[pulumi.Input[_builtins.str]] = ..., global_quota: Optional[pulumi.Input[_builtins.bool]] = ..., quota_code: Optional[pulumi.Input[_builtins.str]] = ..., quota_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_code: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., unit: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_region.setter
    def aws_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalQuota")
    def global_quota(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @global_quota.setter
    def global_quota(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaCode")
    def quota_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @quota_code.setter
    def quota_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaName")
    def quota_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @quota_name.setter
    def quota_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""region is deprecated. Use get_region instead.""")
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_code.setter
    def service_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


@pulumi.type_token("aws:servicequotas/template:Template")
class Template(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws_region: Optional[pulumi.Input[_builtins.str]] = ..., quota_code: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_code: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.float]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TemplateArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aws_region: Optional[pulumi.Input[_builtins.str]] = ..., global_quota: Optional[pulumi.Input[_builtins.bool]] = ..., quota_code: Optional[pulumi.Input[_builtins.str]] = ..., quota_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_code: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., unit: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.float]] = ...) -> Template:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalQuota")
    def global_quota(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaCode")
    def quota_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaName")
    def quota_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""region is deprecated. Use get_region instead.""")
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Output[_builtins.float]:
        
        ...
    


