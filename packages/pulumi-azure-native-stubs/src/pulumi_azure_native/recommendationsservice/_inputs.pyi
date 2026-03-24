

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountResourcePropertiesArgs', 'AccountResourcePropertiesArgsDict', 'CorsRuleArgs', 'CorsRuleArgsDict', 'EndpointAuthenticationArgs', 'EndpointAuthenticationArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'ModelingInputDataArgs', 'ModelingInputDataArgsDict', 'ModelingResourcePropertiesArgs', 'ModelingResourcePropertiesArgsDict', 'ServiceEndpointResourcePropertiesArgs', 'ServiceEndpointResourcePropertiesArgsDict']
class AccountResourcePropertiesArgsDict(TypedDict):
    
    configuration: NotRequired[pulumi.Input[Union[_builtins.str, AccountConfiguration]]]
    cors: NotRequired[pulumi.Input[Sequence[pulumi.Input[CorsRuleArgsDict]]]]
    endpoint_authentications: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointAuthenticationArgsDict]]]]
    reports_connection_string: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AccountResourcePropertiesArgs:
    def __init__(__self__, *, configuration: Optional[pulumi.Input[Union[_builtins.str, AccountConfiguration]]] = ..., cors: Optional[pulumi.Input[Sequence[pulumi.Input[CorsRuleArgs]]]] = ..., endpoint_authentications: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAuthenticationArgs]]]] = ..., reports_connection_string: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Union[_builtins.str, AccountConfiguration]]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Union[_builtins.str, AccountConfiguration]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CorsRuleArgs]]]]:
        
        ...
    
    @cors.setter
    def cors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CorsRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointAuthentications")
    def endpoint_authentications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAuthenticationArgs]]]]:
        
        ...
    
    @endpoint_authentications.setter
    def endpoint_authentications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAuthenticationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportsConnectionString")
    def reports_connection_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reports_connection_string.setter
    def reports_connection_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CorsRuleArgsDict(TypedDict):
    
    allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exposed_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CorsRuleArgs:
    def __init__(__self__, *, allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., exposed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposedHeaders")
    def exposed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exposed_headers.setter
    def exposed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class EndpointAuthenticationArgsDict(TypedDict):
    
    aad_tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_type: NotRequired[pulumi.Input[Union[_builtins.str, PrincipalType]]]


@pulumi.input_type
class EndpointAuthenticationArgs:
    def __init__(__self__, *, aad_tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_type: Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadTenantID")
    def aad_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aad_tenant_id.setter
    def aad_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalID")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]:
        
        ...
    
    @principal_type.setter
    def principal_type(self, value: Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]): # -> None:
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
    


class ModelingInputDataArgsDict(TypedDict):
    
    connection_string: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ModelingInputDataArgs:
    def __init__(__self__, *, connection_string: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ModelingResourcePropertiesArgsDict(TypedDict):
    
    features: NotRequired[pulumi.Input[Union[_builtins.str, ModelingFeatures]]]
    frequency: NotRequired[pulumi.Input[Union[_builtins.str, ModelingFrequency]]]
    input_data: NotRequired[pulumi.Input[ModelingInputDataArgsDict]]
    size: NotRequired[pulumi.Input[Union[_builtins.str, ModelingSize]]]


@pulumi.input_type
class ModelingResourcePropertiesArgs:
    def __init__(__self__, *, features: Optional[pulumi.Input[Union[_builtins.str, ModelingFeatures]]] = ..., frequency: Optional[pulumi.Input[Union[_builtins.str, ModelingFrequency]]] = ..., input_data: Optional[pulumi.Input[ModelingInputDataArgs]] = ..., size: Optional[pulumi.Input[Union[_builtins.str, ModelingSize]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def features(self) -> Optional[pulumi.Input[Union[_builtins.str, ModelingFeatures]]]:
        
        ...
    
    @features.setter
    def features(self, value: Optional[pulumi.Input[Union[_builtins.str, ModelingFeatures]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[Union[_builtins.str, ModelingFrequency]]]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[Union[_builtins.str, ModelingFrequency]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputData")
    def input_data(self) -> Optional[pulumi.Input[ModelingInputDataArgs]]:
        
        ...
    
    @input_data.setter
    def input_data(self, value: Optional[pulumi.Input[ModelingInputDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[Union[_builtins.str, ModelingSize]]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[Union[_builtins.str, ModelingSize]]]): # -> None:
        ...
    


class ServiceEndpointResourcePropertiesArgsDict(TypedDict):
    
    pre_allocated_capacity: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ServiceEndpointResourcePropertiesArgs:
    def __init__(__self__, *, pre_allocated_capacity: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preAllocatedCapacity")
    def pre_allocated_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @pre_allocated_capacity.setter
    def pre_allocated_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


