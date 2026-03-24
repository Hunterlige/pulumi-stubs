

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IntegrationAccountAgreementArgs', 'IntegrationAccountAgreement']
@pulumi.input_type
class IntegrationAccountAgreementArgs:
    def __init__(__self__, *, agreement_type: pulumi.Input[AgreementType], content: pulumi.Input[AgreementContentArgs], guest_identity: pulumi.Input[BusinessIdentityArgs], guest_partner: pulumi.Input[_builtins.str], host_identity: pulumi.Input[BusinessIdentityArgs], host_partner: pulumi.Input[_builtins.str], integration_account_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], agreement_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[Any] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agreementType")
    def agreement_type(self) -> pulumi.Input[AgreementType]:
        
        ...
    
    @agreement_type.setter
    def agreement_type(self, value: pulumi.Input[AgreementType]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Input[AgreementContentArgs]:
        
        ...
    
    @content.setter
    def content(self, value: pulumi.Input[AgreementContentArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestIdentity")
    def guest_identity(self) -> pulumi.Input[BusinessIdentityArgs]:
        
        ...
    
    @guest_identity.setter
    def guest_identity(self, value: pulumi.Input[BusinessIdentityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestPartner")
    def guest_partner(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @guest_partner.setter
    def guest_partner(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostIdentity")
    def host_identity(self) -> pulumi.Input[BusinessIdentityArgs]:
        
        ...
    
    @host_identity.setter
    def host_identity(self, value: pulumi.Input[BusinessIdentityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPartner")
    def host_partner(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host_partner.setter
    def host_partner(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agreementName")
    def agreement_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agreement_name.setter
    def agreement_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:logic:IntegrationAccountAgreement")
class IntegrationAccountAgreement(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., agreement_name: Optional[pulumi.Input[_builtins.str]] = ..., agreement_type: Optional[pulumi.Input[AgreementType]] = ..., content: Optional[pulumi.Input[Union[AgreementContentArgs, AgreementContentArgsDict]]] = ..., guest_identity: Optional[pulumi.Input[Union[BusinessIdentityArgs, BusinessIdentityArgsDict]]] = ..., guest_partner: Optional[pulumi.Input[_builtins.str]] = ..., host_identity: Optional[pulumi.Input[Union[BusinessIdentityArgs, BusinessIdentityArgsDict]]] = ..., host_partner: Optional[pulumi.Input[_builtins.str]] = ..., integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[Any] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IntegrationAccountAgreementArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> IntegrationAccountAgreement:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agreementType")
    def agreement_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Output[outputs.AgreementContentResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestIdentity")
    def guest_identity(self) -> pulumi.Output[outputs.BusinessIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestPartner")
    def guest_partner(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostIdentity")
    def host_identity(self) -> pulumi.Output[outputs.BusinessIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPartner")
    def host_partner(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


