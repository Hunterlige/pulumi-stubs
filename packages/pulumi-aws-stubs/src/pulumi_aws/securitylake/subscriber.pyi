

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
__all__ = ['SubscriberArgs', 'Subscriber']
@pulumi.input_type
class SubscriberArgs:
    def __init__(__self__, *, sources: pulumi.Input[Sequence[pulumi.Input[SubscriberSourceArgs]]], subscriber_identity: pulumi.Input[SubscriberSubscriberIdentityArgs], access_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_description: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[SubscriberTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> pulumi.Input[Sequence[pulumi.Input[SubscriberSourceArgs]]]:
        
        ...
    
    @sources.setter
    def sources(self, value: pulumi.Input[Sequence[pulumi.Input[SubscriberSourceArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberIdentity")
    def subscriber_identity(self) -> pulumi.Input[SubscriberSubscriberIdentityArgs]:
        
        ...
    
    @subscriber_identity.setter
    def subscriber_identity(self, value: pulumi.Input[SubscriberSubscriberIdentityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_type.setter
    def access_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberDescription")
    def subscriber_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_description.setter
    def subscriber_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberName")
    def subscriber_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_name.setter
    def subscriber_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[SubscriberTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[SubscriberTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _SubscriberState:
    def __init__(__self__, *, access_type: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_share_arn: Optional[pulumi.Input[_builtins.str]] = ..., resource_share_name: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceArgs]]]] = ..., subscriber_description: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_identity: Optional[pulumi.Input[SubscriberSubscriberIdentityArgs]] = ..., subscriber_name: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[SubscriberTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_type.setter
    def access_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceShareArn")
    def resource_share_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_share_arn.setter
    def resource_share_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceShareName")
    def resource_share_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_share_name.setter
    def resource_share_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket_arn.setter
    def s3_bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceArgs]]]]:
        
        ...
    
    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberDescription")
    def subscriber_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_description.setter
    def subscriber_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberEndpoint")
    def subscriber_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_endpoint.setter
    def subscriber_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberIdentity")
    def subscriber_identity(self) -> Optional[pulumi.Input[SubscriberSubscriberIdentityArgs]]:
        
        ...
    
    @subscriber_identity.setter
    def subscriber_identity(self, value: Optional[pulumi.Input[SubscriberSubscriberIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberName")
    def subscriber_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_name.setter
    def subscriber_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberStatus")
    def subscriber_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_status.setter
    def subscriber_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[SubscriberTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[SubscriberTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:securitylake/subscriber:Subscriber")
class Subscriber(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SubscriberSourceArgs, SubscriberSourceArgsDict]]]]] = ..., subscriber_description: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_identity: Optional[pulumi.Input[Union[SubscriberSubscriberIdentityArgs, SubscriberSubscriberIdentityArgsDict]]] = ..., subscriber_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[SubscriberTimeoutsArgs, SubscriberTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SubscriberArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_type: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_share_arn: Optional[pulumi.Input[_builtins.str]] = ..., resource_share_name: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SubscriberSourceArgs, SubscriberSourceArgsDict]]]]] = ..., subscriber_description: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_identity: Optional[pulumi.Input[Union[SubscriberSubscriberIdentityArgs, SubscriberSubscriberIdentityArgsDict]]] = ..., subscriber_name: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[SubscriberTimeoutsArgs, SubscriberTimeoutsArgsDict]]] = ...) -> Subscriber:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceShareArn")
    def resource_share_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceShareName")
    def resource_share_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Sequence[outputs.SubscriberSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberDescription")
    def subscriber_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberEndpoint")
    def subscriber_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberIdentity")
    def subscriber_identity(self) -> pulumi.Output[outputs.SubscriberSubscriberIdentity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberName")
    def subscriber_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberStatus")
    def subscriber_status(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.SubscriberTimeouts]]:
        ...
    


