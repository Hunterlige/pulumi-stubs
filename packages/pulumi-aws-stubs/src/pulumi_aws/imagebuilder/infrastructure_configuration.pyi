

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
__all__ = ['InfrastructureConfigurationArgs', 'InfrastructureConfiguration']
@pulumi.input_type
class InfrastructureConfigurationArgs:
    def __init__(__self__, *, instance_profile_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_options: Optional[pulumi.Input[InfrastructureConfigurationInstanceMetadataOptionsArgs]] = ..., instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key_pair: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[InfrastructureConfigurationLoggingArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., placement: Optional[pulumi.Input[InfrastructureConfigurationPlacementArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., terminate_instance_on_failure: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceProfileName")
    def instance_profile_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_profile_name.setter
    def instance_profile_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataOptions")
    def instance_metadata_options(self) -> Optional[pulumi.Input[InfrastructureConfigurationInstanceMetadataOptionsArgs]]:
        
        ...
    
    @instance_metadata_options.setter
    def instance_metadata_options(self, value: Optional[pulumi.Input[InfrastructureConfigurationInstanceMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_types.setter
    def instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPair")
    def key_pair(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_pair.setter
    def key_pair(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[InfrastructureConfigurationLoggingArgs]]:
        
        ...
    
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[InfrastructureConfigurationLoggingArgs]]): # -> None:
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
    def placement(self) -> Optional[pulumi.Input[InfrastructureConfigurationPlacementArgs]]:
        
        ...
    
    @placement.setter
    def placement(self, value: Optional[pulumi.Input[InfrastructureConfigurationPlacementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_tags.setter
    def resource_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @terminate_instance_on_failure.setter
    def terminate_instance_on_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _InfrastructureConfigurationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., date_created: Optional[pulumi.Input[_builtins.str]] = ..., date_updated: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_options: Optional[pulumi.Input[InfrastructureConfigurationInstanceMetadataOptionsArgs]] = ..., instance_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key_pair: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[InfrastructureConfigurationLoggingArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., placement: Optional[pulumi.Input[InfrastructureConfigurationPlacementArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., terminate_instance_on_failure: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date_created.setter
    def date_created(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateUpdated")
    def date_updated(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date_updated.setter
    def date_updated(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataOptions")
    def instance_metadata_options(self) -> Optional[pulumi.Input[InfrastructureConfigurationInstanceMetadataOptionsArgs]]:
        
        ...
    
    @instance_metadata_options.setter
    def instance_metadata_options(self, value: Optional[pulumi.Input[InfrastructureConfigurationInstanceMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceProfileName")
    def instance_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_profile_name.setter
    def instance_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_types.setter
    def instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPair")
    def key_pair(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_pair.setter
    def key_pair(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[InfrastructureConfigurationLoggingArgs]]:
        
        ...
    
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[InfrastructureConfigurationLoggingArgs]]): # -> None:
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
    def placement(self) -> Optional[pulumi.Input[InfrastructureConfigurationPlacementArgs]]:
        
        ...
    
    @placement.setter
    def placement(self, value: Optional[pulumi.Input[InfrastructureConfigurationPlacementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_tags.setter
    def resource_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @terminate_instance_on_failure.setter
    def terminate_instance_on_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class InfrastructureConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_options: Optional[pulumi.Input[Union[InfrastructureConfigurationInstanceMetadataOptionsArgs, InfrastructureConfigurationInstanceMetadataOptionsArgsDict]]] = ..., instance_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key_pair: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[Union[InfrastructureConfigurationLoggingArgs, InfrastructureConfigurationLoggingArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., placement: Optional[pulumi.Input[Union[InfrastructureConfigurationPlacementArgs, InfrastructureConfigurationPlacementArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., terminate_instance_on_failure: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InfrastructureConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., date_created: Optional[pulumi.Input[_builtins.str]] = ..., date_updated: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_options: Optional[pulumi.Input[Union[InfrastructureConfigurationInstanceMetadataOptionsArgs, InfrastructureConfigurationInstanceMetadataOptionsArgsDict]]] = ..., instance_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key_pair: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[Union[InfrastructureConfigurationLoggingArgs, InfrastructureConfigurationLoggingArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., placement: Optional[pulumi.Input[Union[InfrastructureConfigurationPlacementArgs, InfrastructureConfigurationPlacementArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., terminate_instance_on_failure: Optional[pulumi.Input[_builtins.bool]] = ...) -> InfrastructureConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateUpdated")
    def date_updated(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataOptions")
    def instance_metadata_options(self) -> pulumi.Output[Optional[outputs.InfrastructureConfigurationInstanceMetadataOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceProfileName")
    def instance_profile_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPair")
    def key_pair(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> pulumi.Output[Optional[outputs.InfrastructureConfigurationLogging]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> pulumi.Output[Optional[outputs.InfrastructureConfigurationPlacement]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


