

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DomainMappingArgs', 'DomainMapping']
@pulumi.input_type
class DomainMappingArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], override_strategy: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ssl_settings: Optional[pulumi.Input[DomainMappingSslSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideStrategy")
    def override_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @override_strategy.setter
    def override_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslSettings")
    def ssl_settings(self) -> Optional[pulumi.Input[DomainMappingSslSettingsArgs]]:
        
        ...
    
    @ssl_settings.setter
    def ssl_settings(self, value: Optional[pulumi.Input[DomainMappingSslSettingsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DomainMappingState:
    def __init__(__self__, *, domain_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., override_strategy: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., resource_records: Optional[pulumi.Input[Sequence[pulumi.Input[DomainMappingResourceRecordArgs]]]] = ..., ssl_settings: Optional[pulumi.Input[DomainMappingSslSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideStrategy")
    def override_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @override_strategy.setter
    def override_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecords")
    def resource_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainMappingResourceRecordArgs]]]]:
        
        ...
    
    @resource_records.setter
    def resource_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainMappingResourceRecordArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslSettings")
    def ssl_settings(self) -> Optional[pulumi.Input[DomainMappingSslSettingsArgs]]:
        
        ...
    
    @ssl_settings.setter
    def ssl_settings(self, value: Optional[pulumi.Input[DomainMappingSslSettingsArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:appengine/domainMapping:DomainMapping")
class DomainMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., override_strategy: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ssl_settings: Optional[pulumi.Input[Union[DomainMappingSslSettingsArgs, DomainMappingSslSettingsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DomainMappingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., override_strategy: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., resource_records: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DomainMappingResourceRecordArgs, DomainMappingResourceRecordArgsDict]]]]] = ..., ssl_settings: Optional[pulumi.Input[Union[DomainMappingSslSettingsArgs, DomainMappingSslSettingsArgsDict]]] = ...) -> DomainMapping:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideStrategy")
    def override_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecords")
    def resource_records(self) -> pulumi.Output[Sequence[outputs.DomainMappingResourceRecord]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslSettings")
    def ssl_settings(self) -> pulumi.Output[outputs.DomainMappingSslSettings]:
        
        ...
    


