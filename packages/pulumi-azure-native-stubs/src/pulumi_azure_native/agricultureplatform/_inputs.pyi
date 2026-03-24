

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AgriServiceResourcePropertiesArgs', 'AgriServiceResourcePropertiesArgsDict', 'DataConnectorCredentialMapArgs', 'DataConnectorCredentialMapArgsDict', 'DataConnectorCredentialsArgs', 'DataConnectorCredentialsArgsDict', 'InstalledSolutionMapArgs', 'InstalledSolutionMapArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'SkuArgs', 'SkuArgsDict', 'SolutionArgs', 'SolutionArgsDict']
class AgriServiceResourcePropertiesArgsDict(TypedDict):
    
    data_connector_credentials: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataConnectorCredentialMapArgsDict]]]]
    installed_solutions: NotRequired[pulumi.Input[Sequence[pulumi.Input[InstalledSolutionMapArgsDict]]]]


@pulumi.input_type
class AgriServiceResourcePropertiesArgs:
    def __init__(__self__, *, data_connector_credentials: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorCredentialMapArgs]]]] = ..., installed_solutions: Optional[pulumi.Input[Sequence[pulumi.Input[InstalledSolutionMapArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataConnectorCredentials")
    def data_connector_credentials(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorCredentialMapArgs]]]]:
        
        ...
    
    @data_connector_credentials.setter
    def data_connector_credentials(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorCredentialMapArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="installedSolutions")
    def installed_solutions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstalledSolutionMapArgs]]]]:
        
        ...
    
    @installed_solutions.setter
    def installed_solutions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstalledSolutionMapArgs]]]]): # -> None:
        ...
    


class DataConnectorCredentialMapArgsDict(TypedDict):
    
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[DataConnectorCredentialsArgsDict]


@pulumi.input_type
class DataConnectorCredentialMapArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[DataConnectorCredentialsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[DataConnectorCredentialsArgs]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[DataConnectorCredentialsArgs]): # -> None:
        ...
    


class DataConnectorCredentialsArgsDict(TypedDict):
    
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]
    key_version: NotRequired[pulumi.Input[_builtins.str]]
    kind: NotRequired[pulumi.Input[Union[_builtins.str, AuthCredentialsKind]]]


@pulumi.input_type
class DataConnectorCredentialsArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ..., key_version: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, AuthCredentialsKind]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthCredentialsKind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthCredentialsKind]]]): # -> None:
        ...
    


class InstalledSolutionMapArgsDict(TypedDict):
    
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[SolutionArgsDict]


@pulumi.input_type
class InstalledSolutionMapArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[SolutionArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[SolutionArgs]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[SolutionArgs]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[SkuTier]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[SkuTier]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[SkuTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[SkuTier]]): # -> None:
        ...
    


class SolutionArgsDict(TypedDict):
    
    application_name: NotRequired[pulumi.Input[_builtins.str]]
    market_place_publisher_id: NotRequired[pulumi.Input[_builtins.str]]
    partner_id: NotRequired[pulumi.Input[_builtins.str]]
    plan_id: NotRequired[pulumi.Input[_builtins.str]]
    saas_subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    saas_subscription_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SolutionArgs:
    def __init__(__self__, *, application_name: Optional[pulumi.Input[_builtins.str]] = ..., market_place_publisher_id: Optional[pulumi.Input[_builtins.str]] = ..., partner_id: Optional[pulumi.Input[_builtins.str]] = ..., plan_id: Optional[pulumi.Input[_builtins.str]] = ..., saas_subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., saas_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_name.setter
    def application_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketPlacePublisherId")
    def market_place_publisher_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @market_place_publisher_id.setter
    def market_place_publisher_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partner_id.setter
    def partner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @plan_id.setter
    def plan_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="saasSubscriptionId")
    def saas_subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @saas_subscription_id.setter
    def saas_subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="saasSubscriptionName")
    def saas_subscription_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @saas_subscription_name.setter
    def saas_subscription_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


