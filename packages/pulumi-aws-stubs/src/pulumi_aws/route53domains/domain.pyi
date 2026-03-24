

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
__all__ = ['DomainArgs', 'Domain']
@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *, admin_contact: pulumi.Input[DomainAdminContactArgs], domain_name: pulumi.Input[_builtins.str], registrant_contact: pulumi.Input[DomainRegistrantContactArgs], tech_contact: pulumi.Input[DomainTechContactArgs], admin_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., auto_renew: Optional[pulumi.Input[_builtins.bool]] = ..., billing_contacts: Optional[pulumi.Input[Sequence[pulumi.Input[DomainBillingContactArgs]]]] = ..., billing_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., duration_in_years: Optional[pulumi.Input[_builtins.int]] = ..., name_servers: Optional[pulumi.Input[Sequence[pulumi.Input[DomainNameServerArgs]]]] = ..., registrant_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tech_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[DomainTimeoutsArgs]] = ..., transfer_lock: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminContact")
    def admin_contact(self) -> pulumi.Input[DomainAdminContactArgs]:
        
        ...
    
    @admin_contact.setter
    def admin_contact(self, value: pulumi.Input[DomainAdminContactArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrantContact")
    def registrant_contact(self) -> pulumi.Input[DomainRegistrantContactArgs]:
        
        ...
    
    @registrant_contact.setter
    def registrant_contact(self, value: pulumi.Input[DomainRegistrantContactArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="techContact")
    def tech_contact(self) -> pulumi.Input[DomainTechContactArgs]:
        
        ...
    
    @tech_contact.setter
    def tech_contact(self, value: pulumi.Input[DomainTechContactArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPrivacy")
    def admin_privacy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @admin_privacy.setter
    def admin_privacy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingContacts")
    def billing_contacts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainBillingContactArgs]]]]:
        
        ...
    
    @billing_contacts.setter
    def billing_contacts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainBillingContactArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingPrivacy")
    def billing_privacy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @billing_privacy.setter
    def billing_privacy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInYears")
    def duration_in_years(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @duration_in_years.setter
    def duration_in_years(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainNameServerArgs]]]]:
        
        ...
    
    @name_servers.setter
    def name_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainNameServerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrantPrivacy")
    def registrant_privacy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @registrant_privacy.setter
    def registrant_privacy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="techPrivacy")
    def tech_privacy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @tech_privacy.setter
    def tech_privacy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DomainTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DomainTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferLock")
    def transfer_lock(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transfer_lock.setter
    def transfer_lock(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *, abuse_contact_email: Optional[pulumi.Input[_builtins.str]] = ..., abuse_contact_phone: Optional[pulumi.Input[_builtins.str]] = ..., admin_contact: Optional[pulumi.Input[DomainAdminContactArgs]] = ..., admin_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., auto_renew: Optional[pulumi.Input[_builtins.bool]] = ..., billing_contacts: Optional[pulumi.Input[Sequence[pulumi.Input[DomainBillingContactArgs]]]] = ..., billing_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., duration_in_years: Optional[pulumi.Input[_builtins.int]] = ..., expiration_date: Optional[pulumi.Input[_builtins.str]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., name_servers: Optional[pulumi.Input[Sequence[pulumi.Input[DomainNameServerArgs]]]] = ..., registrant_contact: Optional[pulumi.Input[DomainRegistrantContactArgs]] = ..., registrant_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., registrar_name: Optional[pulumi.Input[_builtins.str]] = ..., registrar_url: Optional[pulumi.Input[_builtins.str]] = ..., status_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tech_contact: Optional[pulumi.Input[DomainTechContactArgs]] = ..., tech_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[DomainTimeoutsArgs]] = ..., transfer_lock: Optional[pulumi.Input[_builtins.bool]] = ..., updated_date: Optional[pulumi.Input[_builtins.str]] = ..., whois_server: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="abuseContactEmail")
    def abuse_contact_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @abuse_contact_email.setter
    def abuse_contact_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="abuseContactPhone")
    def abuse_contact_phone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @abuse_contact_phone.setter
    def abuse_contact_phone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminContact")
    def admin_contact(self) -> Optional[pulumi.Input[DomainAdminContactArgs]]:
        
        ...
    
    @admin_contact.setter
    def admin_contact(self, value: Optional[pulumi.Input[DomainAdminContactArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPrivacy")
    def admin_privacy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @admin_privacy.setter
    def admin_privacy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingContacts")
    def billing_contacts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainBillingContactArgs]]]]:
        
        ...
    
    @billing_contacts.setter
    def billing_contacts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainBillingContactArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingPrivacy")
    def billing_privacy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @billing_privacy.setter
    def billing_privacy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInYears")
    def duration_in_years(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @duration_in_years.setter
    def duration_in_years(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainNameServerArgs]]]]:
        
        ...
    
    @name_servers.setter
    def name_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainNameServerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrantContact")
    def registrant_contact(self) -> Optional[pulumi.Input[DomainRegistrantContactArgs]]:
        
        ...
    
    @registrant_contact.setter
    def registrant_contact(self, value: Optional[pulumi.Input[DomainRegistrantContactArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrantPrivacy")
    def registrant_privacy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @registrant_privacy.setter
    def registrant_privacy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrarName")
    def registrar_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registrar_name.setter
    def registrar_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrarUrl")
    def registrar_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registrar_url.setter
    def registrar_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusLists")
    def status_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @status_lists.setter
    def status_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="techContact")
    def tech_contact(self) -> Optional[pulumi.Input[DomainTechContactArgs]]:
        
        ...
    
    @tech_contact.setter
    def tech_contact(self, value: Optional[pulumi.Input[DomainTechContactArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="techPrivacy")
    def tech_privacy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @tech_privacy.setter
    def tech_privacy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DomainTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DomainTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferLock")
    def transfer_lock(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transfer_lock.setter
    def transfer_lock(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedDate")
    def updated_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated_date.setter
    def updated_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="whoisServer")
    def whois_server(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @whois_server.setter
    def whois_server(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:route53domains/domain:Domain")
class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., admin_contact: Optional[pulumi.Input[Union[DomainAdminContactArgs, DomainAdminContactArgsDict]]] = ..., admin_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., auto_renew: Optional[pulumi.Input[_builtins.bool]] = ..., billing_contacts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DomainBillingContactArgs, DomainBillingContactArgsDict]]]]] = ..., billing_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., duration_in_years: Optional[pulumi.Input[_builtins.int]] = ..., name_servers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DomainNameServerArgs, DomainNameServerArgsDict]]]]] = ..., registrant_contact: Optional[pulumi.Input[Union[DomainRegistrantContactArgs, DomainRegistrantContactArgsDict]]] = ..., registrant_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tech_contact: Optional[pulumi.Input[Union[DomainTechContactArgs, DomainTechContactArgsDict]]] = ..., tech_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[Union[DomainTimeoutsArgs, DomainTimeoutsArgsDict]]] = ..., transfer_lock: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DomainArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., abuse_contact_email: Optional[pulumi.Input[_builtins.str]] = ..., abuse_contact_phone: Optional[pulumi.Input[_builtins.str]] = ..., admin_contact: Optional[pulumi.Input[Union[DomainAdminContactArgs, DomainAdminContactArgsDict]]] = ..., admin_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., auto_renew: Optional[pulumi.Input[_builtins.bool]] = ..., billing_contacts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DomainBillingContactArgs, DomainBillingContactArgsDict]]]]] = ..., billing_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., duration_in_years: Optional[pulumi.Input[_builtins.int]] = ..., expiration_date: Optional[pulumi.Input[_builtins.str]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., name_servers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DomainNameServerArgs, DomainNameServerArgsDict]]]]] = ..., registrant_contact: Optional[pulumi.Input[Union[DomainRegistrantContactArgs, DomainRegistrantContactArgsDict]]] = ..., registrant_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., registrar_name: Optional[pulumi.Input[_builtins.str]] = ..., registrar_url: Optional[pulumi.Input[_builtins.str]] = ..., status_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tech_contact: Optional[pulumi.Input[Union[DomainTechContactArgs, DomainTechContactArgsDict]]] = ..., tech_privacy: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[Union[DomainTimeoutsArgs, DomainTimeoutsArgsDict]]] = ..., transfer_lock: Optional[pulumi.Input[_builtins.bool]] = ..., updated_date: Optional[pulumi.Input[_builtins.str]] = ..., whois_server: Optional[pulumi.Input[_builtins.str]] = ...) -> Domain:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="abuseContactEmail")
    def abuse_contact_email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="abuseContactPhone")
    def abuse_contact_phone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminContact")
    def admin_contact(self) -> pulumi.Output[outputs.DomainAdminContact]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPrivacy")
    def admin_privacy(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingContacts")
    def billing_contacts(self) -> pulumi.Output[Sequence[outputs.DomainBillingContact]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingPrivacy")
    def billing_privacy(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInYears")
    def duration_in_years(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Output[Sequence[outputs.DomainNameServer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrantContact")
    def registrant_contact(self) -> pulumi.Output[outputs.DomainRegistrantContact]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrantPrivacy")
    def registrant_privacy(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrarName")
    def registrar_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrarUrl")
    def registrar_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusLists")
    def status_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="techContact")
    def tech_contact(self) -> pulumi.Output[outputs.DomainTechContact]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="techPrivacy")
    def tech_privacy(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.DomainTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferLock")
    def transfer_lock(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedDate")
    def updated_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="whoisServer")
    def whois_server(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


