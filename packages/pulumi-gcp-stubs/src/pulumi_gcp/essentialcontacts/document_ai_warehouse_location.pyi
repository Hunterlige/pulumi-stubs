

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DocumentAiWarehouseLocationArgs', 'DocumentAiWarehouseLocation']
@pulumi.input_type
class DocumentAiWarehouseLocationArgs:
    def __init__(__self__, *, access_control_mode: pulumi.Input[_builtins.str], database_type: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], project_number: pulumi.Input[_builtins.str], document_creator_default_role: Optional[pulumi.Input[_builtins.str]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlMode")
    def access_control_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @access_control_mode.setter
    def access_control_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_type.setter
    def database_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project_number.setter
    def project_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentCreatorDefaultRole")
    def document_creator_default_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_creator_default_role.setter
    def document_creator_default_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DocumentAiWarehouseLocationState:
    def __init__(__self__, *, access_control_mode: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., document_creator_default_role: Optional[pulumi.Input[_builtins.str]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project_number: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlMode")
    def access_control_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_control_mode.setter
    def access_control_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_type.setter
    def database_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentCreatorDefaultRole")
    def document_creator_default_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_creator_default_role.setter
    def document_creator_default_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project_number.setter
    def project_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DocumentAiWarehouseLocation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_control_mode: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., document_creator_default_role: Optional[pulumi.Input[_builtins.str]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project_number: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DocumentAiWarehouseLocationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_control_mode: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., document_creator_default_role: Optional[pulumi.Input[_builtins.str]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project_number: Optional[pulumi.Input[_builtins.str]] = ...) -> DocumentAiWarehouseLocation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlMode")
    def access_control_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentCreatorDefaultRole")
    def document_creator_default_role(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


