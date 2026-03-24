

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AuthorizationProfileResponse', 'SubscriptionFeatureRegistrationResponseProperties']
@pulumi.output_type
class AuthorizationProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, approved_time: _builtins.str, approver: _builtins.str, requested_time: _builtins.str, requester: _builtins.str, requester_object_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvedTime")
    def approved_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def approver(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedTime")
    def requested_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requester(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requesterObjectId")
    def requester_object_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SubscriptionFeatureRegistrationResponseProperties(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, approval_type: _builtins.str, display_name: _builtins.str, documentation_link: _builtins.str, feature_name: _builtins.str, provider_namespace: _builtins.str, registration_date: _builtins.str, release_date: _builtins.str, subscription_id: _builtins.str, tenant_id: _builtins.str, authorization_profile: Optional[outputs.AuthorizationProfileResponse] = ..., description: Optional[_builtins.str] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., should_feature_display_in_portal: Optional[_builtins.bool] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalType")
    def approval_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentationLink")
    def documentation_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureName")
    def feature_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerNamespace")
    def provider_namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationDate")
    def registration_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseDate")
    def release_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationProfile")
    def authorization_profile(self) -> Optional[outputs.AuthorizationProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shouldFeatureDisplayInPortal")
    def should_feature_display_in_portal(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


