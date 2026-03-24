

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IPRuleArgs', 'IPRuleArgsDict', 'LiveTraceCategoryArgs', 'LiveTraceCategoryArgsDict', 'LiveTraceConfigurationArgs', 'LiveTraceConfigurationArgsDict', 'ManagedIdentitySettingsArgs', 'ManagedIdentitySettingsArgsDict', 'ManagedIdentityArgs', 'ManagedIdentityArgsDict', 'NetworkACLArgs', 'NetworkACLArgsDict', 'PrivateEndpointACLArgs', 'PrivateEndpointACLArgsDict', 'PrivateEndpointArgs', 'PrivateEndpointArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', 'ResourceLogCategoryArgs', 'ResourceLogCategoryArgsDict', 'ResourceLogConfigurationArgs', 'ResourceLogConfigurationArgsDict', 'ResourceReferenceArgs', 'ResourceReferenceArgsDict', 'ResourceSkuArgs', 'ResourceSkuArgsDict', 'ServerlessSettingsArgs', 'ServerlessSettingsArgsDict', 'ServerlessUpstreamSettingsArgs', 'ServerlessUpstreamSettingsArgsDict', 'SignalRCorsSettingsArgs', 'SignalRCorsSettingsArgsDict', 'SignalRFeatureArgs', 'SignalRFeatureArgsDict', 'SignalRNetworkACLsArgs', 'SignalRNetworkACLsArgsDict', 'SignalRTlsSettingsArgs', 'SignalRTlsSettingsArgsDict', 'UpstreamAuthSettingsArgs', 'UpstreamAuthSettingsArgsDict', 'UpstreamTemplateArgs', 'UpstreamTemplateArgsDict']
class IPRuleArgsDict(TypedDict):
    
    action: NotRequired[pulumi.Input[Union[_builtins.str, ACLAction]]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IPRuleArgs:
    def __init__(__self__, *, action: Optional[pulumi.Input[Union[_builtins.str, ACLAction]]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, ACLAction]]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[Union[_builtins.str, ACLAction]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LiveTraceCategoryArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LiveTraceCategoryArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LiveTraceConfigurationArgsDict(TypedDict):
    
    categories: NotRequired[pulumi.Input[Sequence[pulumi.Input[LiveTraceCategoryArgsDict]]]]
    enabled: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LiveTraceConfigurationArgs:
    def __init__(__self__, *, categories: Optional[pulumi.Input[Sequence[pulumi.Input[LiveTraceCategoryArgs]]]] = ..., enabled: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LiveTraceCategoryArgs]]]]:
        
        ...
    
    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LiveTraceCategoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedIdentitySettingsArgsDict(TypedDict):
    
    resource: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedIdentitySettingsArgs:
    def __init__(__self__, *, resource: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class NetworkACLArgsDict(TypedDict):
    
    allow: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]
    deny: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]


@pulumi.input_type
class NetworkACLArgs:
    def __init__(__self__, *, allow: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]] = ..., deny: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]:
        
        ...
    
    @allow.setter
    def allow(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]:
        
        ...
    
    @deny.setter
    def deny(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]): # -> None:
        ...
    


class PrivateEndpointACLArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    allow: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]
    deny: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]


@pulumi.input_type
class PrivateEndpointACLArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], allow: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]] = ..., deny: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]] = ...) -> None:
        
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
    def allow(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]:
        
        ...
    
    @allow.setter
    def allow(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]:
        
        ...
    
    @deny.setter
    def deny(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SignalRRequestType]]]]]): # -> None:
        ...
    


class PrivateEndpointArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]]): # -> None:
        ...
    


class ResourceLogCategoryArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceLogCategoryArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceLogConfigurationArgsDict(TypedDict):
    
    categories: NotRequired[pulumi.Input[Sequence[pulumi.Input[ResourceLogCategoryArgsDict]]]]


@pulumi.input_type
class ResourceLogConfigurationArgs:
    def __init__(__self__, *, categories: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceLogCategoryArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceLogCategoryArgs]]]]:
        
        ...
    
    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceLogCategoryArgs]]]]): # -> None:
        ...
    


class ResourceReferenceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceReferenceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceSkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, SignalRSkuTier]]]


@pulumi.input_type
class ResourceSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., tier: Optional[pulumi.Input[Union[_builtins.str, SignalRSkuTier]]] = ...) -> None:
        
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
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, SignalRSkuTier]]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, SignalRSkuTier]]]): # -> None:
        ...
    


class ServerlessSettingsArgsDict(TypedDict):
    
    connection_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ServerlessSettingsArgs:
    def __init__(__self__, *, connection_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTimeoutInSeconds")
    def connection_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_timeout_in_seconds.setter
    def connection_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ServerlessUpstreamSettingsArgsDict(TypedDict):
    
    templates: NotRequired[pulumi.Input[Sequence[pulumi.Input[UpstreamTemplateArgsDict]]]]


@pulumi.input_type
class ServerlessUpstreamSettingsArgs:
    def __init__(__self__, *, templates: Optional[pulumi.Input[Sequence[pulumi.Input[UpstreamTemplateArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def templates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UpstreamTemplateArgs]]]]:
        
        ...
    
    @templates.setter
    def templates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UpstreamTemplateArgs]]]]): # -> None:
        ...
    


class SignalRCorsSettingsArgsDict(TypedDict):
    
    allowed_origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SignalRCorsSettingsArgs:
    def __init__(__self__, *, allowed_origins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_origins.setter
    def allowed_origins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SignalRFeatureArgsDict(TypedDict):
    
    flag: pulumi.Input[Union[_builtins.str, FeatureFlags]]
    value: pulumi.Input[_builtins.str]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SignalRFeatureArgs:
    def __init__(__self__, *, flag: pulumi.Input[Union[_builtins.str, FeatureFlags]], value: pulumi.Input[_builtins.str], properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flag(self) -> pulumi.Input[Union[_builtins.str, FeatureFlags]]:
        
        ...
    
    @flag.setter
    def flag(self, value: pulumi.Input[Union[_builtins.str, FeatureFlags]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SignalRNetworkACLsArgsDict(TypedDict):
    
    default_action: NotRequired[pulumi.Input[Union[_builtins.str, ACLAction]]]
    ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[IPRuleArgsDict]]]]
    private_endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointACLArgsDict]]]]
    public_network: NotRequired[pulumi.Input[NetworkACLArgsDict]]


@pulumi.input_type
class SignalRNetworkACLsArgs:
    def __init__(__self__, *, default_action: Optional[pulumi.Input[Union[_builtins.str, ACLAction]]] = ..., ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]] = ..., private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointACLArgs]]]] = ..., public_network: Optional[pulumi.Input[NetworkACLArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[Union[_builtins.str, ACLAction]]]:
        
        ...
    
    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[Union[_builtins.str, ACLAction]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]:
        
        ...
    
    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointACLArgs]]]]:
        
        ...
    
    @private_endpoints.setter
    def private_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointACLArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetwork")
    def public_network(self) -> Optional[pulumi.Input[NetworkACLArgs]]:
        
        ...
    
    @public_network.setter
    def public_network(self, value: Optional[pulumi.Input[NetworkACLArgs]]): # -> None:
        ...
    


class SignalRTlsSettingsArgsDict(TypedDict):
    
    client_cert_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SignalRTlsSettingsArgs:
    def __init__(__self__, *, client_cert_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertEnabled")
    def client_cert_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @client_cert_enabled.setter
    def client_cert_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class UpstreamAuthSettingsArgsDict(TypedDict):
    
    managed_identity: NotRequired[pulumi.Input[ManagedIdentitySettingsArgsDict]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, UpstreamAuthType]]]


@pulumi.input_type
class UpstreamAuthSettingsArgs:
    def __init__(__self__, *, managed_identity: Optional[pulumi.Input[ManagedIdentitySettingsArgs]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, UpstreamAuthType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[pulumi.Input[ManagedIdentitySettingsArgs]]:
        
        ...
    
    @managed_identity.setter
    def managed_identity(self, value: Optional[pulumi.Input[ManagedIdentitySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, UpstreamAuthType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, UpstreamAuthType]]]): # -> None:
        ...
    


class UpstreamTemplateArgsDict(TypedDict):
    
    url_template: pulumi.Input[_builtins.str]
    auth: NotRequired[pulumi.Input[UpstreamAuthSettingsArgsDict]]
    category_pattern: NotRequired[pulumi.Input[_builtins.str]]
    event_pattern: NotRequired[pulumi.Input[_builtins.str]]
    hub_pattern: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UpstreamTemplateArgs:
    def __init__(__self__, *, url_template: pulumi.Input[_builtins.str], auth: Optional[pulumi.Input[UpstreamAuthSettingsArgs]] = ..., category_pattern: Optional[pulumi.Input[_builtins.str]] = ..., event_pattern: Optional[pulumi.Input[_builtins.str]] = ..., hub_pattern: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlTemplate")
    def url_template(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @url_template.setter
    def url_template(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[UpstreamAuthSettingsArgs]]:
        
        ...
    
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[UpstreamAuthSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="categoryPattern")
    def category_pattern(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @category_pattern.setter
    def category_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventPattern")
    def event_pattern(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_pattern.setter
    def event_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubPattern")
    def hub_pattern(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hub_pattern.setter
    def hub_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


