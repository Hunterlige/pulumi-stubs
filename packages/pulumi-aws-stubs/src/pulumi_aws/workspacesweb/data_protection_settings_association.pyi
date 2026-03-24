

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataProtectionSettingsAssociationArgs', 'DataProtectionSettingsAssociation']
@pulumi.input_type
class DataProtectionSettingsAssociationArgs:
    def __init__(__self__, *, data_protection_settings_arn: pulumi.Input[_builtins.str], portal_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProtectionSettingsArn")
    def data_protection_settings_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_protection_settings_arn.setter
    def data_protection_settings_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @portal_arn.setter
    def portal_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DataProtectionSettingsAssociationState:
    def __init__(__self__, *, data_protection_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProtectionSettingsArn")
    def data_protection_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_protection_settings_arn.setter
    def data_protection_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @portal_arn.setter
    def portal_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DataProtectionSettingsAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_protection_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataProtectionSettingsAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., data_protection_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> DataProtectionSettingsAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProtectionSettingsArn")
    def data_protection_settings_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


