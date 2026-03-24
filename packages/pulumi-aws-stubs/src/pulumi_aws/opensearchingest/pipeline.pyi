

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
__all__ = ['PipelineArgs', 'Pipeline']
@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *, max_units: pulumi.Input[_builtins.int], min_units: pulumi.Input[_builtins.int], pipeline_configuration_body: pulumi.Input[_builtins.str], pipeline_name: pulumi.Input[_builtins.str], buffer_options: Optional[pulumi.Input[PipelineBufferOptionsArgs]] = ..., encryption_at_rest_options: Optional[pulumi.Input[PipelineEncryptionAtRestOptionsArgs]] = ..., log_publishing_options: Optional[pulumi.Input[PipelineLogPublishingOptionsArgs]] = ..., pipeline_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[PipelineTimeoutsArgs]] = ..., vpc_options: Optional[pulumi.Input[PipelineVpcOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnits")
    def max_units(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_units.setter
    def max_units(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minUnits")
    def min_units(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @min_units.setter
    def min_units(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineConfigurationBody")
    def pipeline_configuration_body(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @pipeline_configuration_body.setter
    def pipeline_configuration_body(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @pipeline_name.setter
    def pipeline_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferOptions")
    def buffer_options(self) -> Optional[pulumi.Input[PipelineBufferOptionsArgs]]:
        
        ...
    
    @buffer_options.setter
    def buffer_options(self, value: Optional[pulumi.Input[PipelineBufferOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtRestOptions")
    def encryption_at_rest_options(self) -> Optional[pulumi.Input[PipelineEncryptionAtRestOptionsArgs]]:
        
        ...
    
    @encryption_at_rest_options.setter
    def encryption_at_rest_options(self, value: Optional[pulumi.Input[PipelineEncryptionAtRestOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[pulumi.Input[PipelineLogPublishingOptionsArgs]]:
        
        ...
    
    @log_publishing_options.setter
    def log_publishing_options(self, value: Optional[pulumi.Input[PipelineLogPublishingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineRoleArn")
    def pipeline_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_role_arn.setter
    def pipeline_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[PipelineTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[PipelineTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional[pulumi.Input[PipelineVpcOptionsArgs]]:
        
        ...
    
    @vpc_options.setter
    def vpc_options(self, value: Optional[pulumi.Input[PipelineVpcOptionsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _PipelineState:
    def __init__(__self__, *, buffer_options: Optional[pulumi.Input[PipelineBufferOptionsArgs]] = ..., encryption_at_rest_options: Optional[pulumi.Input[PipelineEncryptionAtRestOptionsArgs]] = ..., ingest_endpoint_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_publishing_options: Optional[pulumi.Input[PipelineLogPublishingOptionsArgs]] = ..., max_units: Optional[pulumi.Input[_builtins.int]] = ..., min_units: Optional[pulumi.Input[_builtins.int]] = ..., pipeline_arn: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_configuration_body: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[PipelineTimeoutsArgs]] = ..., vpc_options: Optional[pulumi.Input[PipelineVpcOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferOptions")
    def buffer_options(self) -> Optional[pulumi.Input[PipelineBufferOptionsArgs]]:
        
        ...
    
    @buffer_options.setter
    def buffer_options(self, value: Optional[pulumi.Input[PipelineBufferOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtRestOptions")
    def encryption_at_rest_options(self) -> Optional[pulumi.Input[PipelineEncryptionAtRestOptionsArgs]]:
        
        ...
    
    @encryption_at_rest_options.setter
    def encryption_at_rest_options(self, value: Optional[pulumi.Input[PipelineEncryptionAtRestOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestEndpointUrls")
    def ingest_endpoint_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ingest_endpoint_urls.setter
    def ingest_endpoint_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[pulumi.Input[PipelineLogPublishingOptionsArgs]]:
        
        ...
    
    @log_publishing_options.setter
    def log_publishing_options(self, value: Optional[pulumi.Input[PipelineLogPublishingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnits")
    def max_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_units.setter
    def max_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minUnits")
    def min_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_units.setter
    def min_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineArn")
    def pipeline_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_arn.setter
    def pipeline_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineConfigurationBody")
    def pipeline_configuration_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_configuration_body.setter
    def pipeline_configuration_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_name.setter
    def pipeline_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineRoleArn")
    def pipeline_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_role_arn.setter
    def pipeline_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[PipelineTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[PipelineTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional[pulumi.Input[PipelineVpcOptionsArgs]]:
        
        ...
    
    @vpc_options.setter
    def vpc_options(self, value: Optional[pulumi.Input[PipelineVpcOptionsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:opensearchingest/pipeline:Pipeline")
class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., buffer_options: Optional[pulumi.Input[Union[PipelineBufferOptionsArgs, PipelineBufferOptionsArgsDict]]] = ..., encryption_at_rest_options: Optional[pulumi.Input[Union[PipelineEncryptionAtRestOptionsArgs, PipelineEncryptionAtRestOptionsArgsDict]]] = ..., log_publishing_options: Optional[pulumi.Input[Union[PipelineLogPublishingOptionsArgs, PipelineLogPublishingOptionsArgsDict]]] = ..., max_units: Optional[pulumi.Input[_builtins.int]] = ..., min_units: Optional[pulumi.Input[_builtins.int]] = ..., pipeline_configuration_body: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[PipelineTimeoutsArgs, PipelineTimeoutsArgsDict]]] = ..., vpc_options: Optional[pulumi.Input[Union[PipelineVpcOptionsArgs, PipelineVpcOptionsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PipelineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., buffer_options: Optional[pulumi.Input[Union[PipelineBufferOptionsArgs, PipelineBufferOptionsArgsDict]]] = ..., encryption_at_rest_options: Optional[pulumi.Input[Union[PipelineEncryptionAtRestOptionsArgs, PipelineEncryptionAtRestOptionsArgsDict]]] = ..., ingest_endpoint_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_publishing_options: Optional[pulumi.Input[Union[PipelineLogPublishingOptionsArgs, PipelineLogPublishingOptionsArgsDict]]] = ..., max_units: Optional[pulumi.Input[_builtins.int]] = ..., min_units: Optional[pulumi.Input[_builtins.int]] = ..., pipeline_arn: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_configuration_body: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[PipelineTimeoutsArgs, PipelineTimeoutsArgsDict]]] = ..., vpc_options: Optional[pulumi.Input[Union[PipelineVpcOptionsArgs, PipelineVpcOptionsArgsDict]]] = ...) -> Pipeline:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferOptions")
    def buffer_options(self) -> pulumi.Output[Optional[outputs.PipelineBufferOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtRestOptions")
    def encryption_at_rest_options(self) -> pulumi.Output[Optional[outputs.PipelineEncryptionAtRestOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestEndpointUrls")
    def ingest_endpoint_urls(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> pulumi.Output[Optional[outputs.PipelineLogPublishingOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnits")
    def max_units(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minUnits")
    def min_units(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineArn")
    def pipeline_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineConfigurationBody")
    def pipeline_configuration_body(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineRoleArn")
    def pipeline_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
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
    def timeouts(self) -> pulumi.Output[Optional[outputs.PipelineTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> pulumi.Output[Optional[outputs.PipelineVpcOptions]]:
        
        ...
    


