

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegistrationArgs', 'Registration']
@pulumi.input_type
class RegistrationArgs:
    def __init__(__self__, *, contact_settings: pulumi.Input[RegistrationContactSettingsArgs], domain_name: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], yearly_price: pulumi.Input[RegistrationYearlyPriceArgs], contact_notices: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., dns_settings: Optional[pulumi.Input[RegistrationDnsSettingsArgs]] = ..., domain_notices: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., management_settings: Optional[pulumi.Input[RegistrationManagementSettingsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactSettings")
    def contact_settings(self) -> pulumi.Input[RegistrationContactSettingsArgs]:
        
        ...
    
    @contact_settings.setter
    def contact_settings(self, value: pulumi.Input[RegistrationContactSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="yearlyPrice")
    def yearly_price(self) -> pulumi.Input[RegistrationYearlyPriceArgs]:
        
        ...
    
    @yearly_price.setter
    def yearly_price(self, value: pulumi.Input[RegistrationYearlyPriceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactNotices")
    def contact_notices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @contact_notices.setter
    def contact_notices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input[RegistrationDnsSettingsArgs]]:
        
        ...
    
    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input[RegistrationDnsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNotices")
    def domain_notices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @domain_notices.setter
    def domain_notices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementSettings")
    def management_settings(self) -> Optional[pulumi.Input[RegistrationManagementSettingsArgs]]:
        
        ...
    
    @management_settings.setter
    def management_settings(self, value: Optional[pulumi.Input[RegistrationManagementSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RegistrationState:
    def __init__(__self__, *, contact_notices: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., contact_settings: Optional[pulumi.Input[RegistrationContactSettingsArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dns_settings: Optional[pulumi.Input[RegistrationDnsSettingsArgs]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_notices: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., issues: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., management_settings: Optional[pulumi.Input[RegistrationManagementSettingsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., register_failure_reason: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., supported_privacies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., yearly_price: Optional[pulumi.Input[RegistrationYearlyPriceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactNotices")
    def contact_notices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @contact_notices.setter
    def contact_notices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactSettings")
    def contact_settings(self) -> Optional[pulumi.Input[RegistrationContactSettingsArgs]]:
        
        ...
    
    @contact_settings.setter
    def contact_settings(self, value: Optional[pulumi.Input[RegistrationContactSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input[RegistrationDnsSettingsArgs]]:
        
        ...
    
    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input[RegistrationDnsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNotices")
    def domain_notices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @domain_notices.setter
    def domain_notices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issues(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @issues.setter
    def issues(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementSettings")
    def management_settings(self) -> Optional[pulumi.Input[RegistrationManagementSettingsArgs]]:
        
        ...
    
    @management_settings.setter
    def management_settings(self, value: Optional[pulumi.Input[RegistrationManagementSettingsArgs]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registerFailureReason")
    def register_failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @register_failure_reason.setter
    def register_failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedPrivacies")
    def supported_privacies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_privacies.setter
    def supported_privacies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="yearlyPrice")
    def yearly_price(self) -> Optional[pulumi.Input[RegistrationYearlyPriceArgs]]:
        
        ...
    
    @yearly_price.setter
    def yearly_price(self, value: Optional[pulumi.Input[RegistrationYearlyPriceArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:clouddomains/registration:Registration")
class Registration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., contact_notices: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., contact_settings: Optional[pulumi.Input[Union[RegistrationContactSettingsArgs, RegistrationContactSettingsArgsDict]]] = ..., dns_settings: Optional[pulumi.Input[Union[RegistrationDnsSettingsArgs, RegistrationDnsSettingsArgsDict]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_notices: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., management_settings: Optional[pulumi.Input[Union[RegistrationManagementSettingsArgs, RegistrationManagementSettingsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., yearly_price: Optional[pulumi.Input[Union[RegistrationYearlyPriceArgs, RegistrationYearlyPriceArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegistrationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., contact_notices: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., contact_settings: Optional[pulumi.Input[Union[RegistrationContactSettingsArgs, RegistrationContactSettingsArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dns_settings: Optional[pulumi.Input[Union[RegistrationDnsSettingsArgs, RegistrationDnsSettingsArgsDict]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_notices: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., issues: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., management_settings: Optional[pulumi.Input[Union[RegistrationManagementSettingsArgs, RegistrationManagementSettingsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., register_failure_reason: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., supported_privacies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., yearly_price: Optional[pulumi.Input[Union[RegistrationYearlyPriceArgs, RegistrationYearlyPriceArgsDict]]] = ...) -> Registration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactNotices")
    def contact_notices(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactSettings")
    def contact_settings(self) -> pulumi.Output[outputs.RegistrationContactSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output[Optional[outputs.RegistrationDnsSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNotices")
    def domain_notices(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issues(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementSettings")
    def management_settings(self) -> pulumi.Output[outputs.RegistrationManagementSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registerFailureReason")
    def register_failure_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedPrivacies")
    def supported_privacies(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="yearlyPrice")
    def yearly_price(self) -> pulumi.Output[outputs.RegistrationYearlyPrice]:
        
        ...
    


