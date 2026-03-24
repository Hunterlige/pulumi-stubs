

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EvidenceArgs', 'Evidence']
@pulumi.input_type
class EvidenceArgs:
    def __init__(__self__, *, file_path: pulumi.Input[_builtins.str], report_name: pulumi.Input[_builtins.str], control_id: Optional[pulumi.Input[_builtins.str]] = ..., evidence_name: Optional[pulumi.Input[_builtins.str]] = ..., evidence_type: Optional[pulumi.Input[Union[_builtins.str, EvidenceType]]] = ..., extra_data: Optional[pulumi.Input[_builtins.str]] = ..., offer_guid: Optional[pulumi.Input[_builtins.str]] = ..., report_creator_tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., responsibility_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_path.setter
    def file_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportName")
    def report_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @report_name.setter
    def report_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlId")
    def control_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @control_id.setter
    def control_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evidenceName")
    def evidence_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @evidence_name.setter
    def evidence_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evidenceType")
    def evidence_type(self) -> Optional[pulumi.Input[Union[_builtins.str, EvidenceType]]]:
        
        ...
    
    @evidence_type.setter
    def evidence_type(self, value: Optional[pulumi.Input[Union[_builtins.str, EvidenceType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraData")
    def extra_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extra_data.setter
    def extra_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerGuid")
    def offer_guid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @offer_guid.setter
    def offer_guid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportCreatorTenantId")
    def report_creator_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @report_creator_tenant_id.setter
    def report_creator_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsibilityId")
    def responsibility_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @responsibility_id.setter
    def responsibility_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:appcomplianceautomation:Evidence")
class Evidence(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., control_id: Optional[pulumi.Input[_builtins.str]] = ..., evidence_name: Optional[pulumi.Input[_builtins.str]] = ..., evidence_type: Optional[pulumi.Input[Union[_builtins.str, EvidenceType]]] = ..., extra_data: Optional[pulumi.Input[_builtins.str]] = ..., file_path: Optional[pulumi.Input[_builtins.str]] = ..., offer_guid: Optional[pulumi.Input[_builtins.str]] = ..., report_creator_tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., report_name: Optional[pulumi.Input[_builtins.str]] = ..., responsibility_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EvidenceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Evidence:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlId")
    def control_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evidenceType")
    def evidence_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraData")
    def extra_data(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsibilityId")
    def responsibility_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


