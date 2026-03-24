

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
__all__ = ['LocationAzureBlobArgs', 'LocationAzureBlob']
@pulumi.input_type
class LocationAzureBlobArgs:
    def __init__(__self__, *, agent_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], authentication_type: pulumi.Input[_builtins.str], container_url: pulumi.Input[_builtins.str], access_tier: Optional[pulumi.Input[_builtins.str]] = ..., blob_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sas_configuration: Optional[pulumi.Input[LocationAzureBlobSasConfigurationArgs]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @agent_arns.setter
    def agent_arns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerUrl")
    def container_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_url.setter
    def container_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_tier.setter
    def access_tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobType")
    def blob_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_type.setter
    def blob_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasConfiguration")
    def sas_configuration(self) -> Optional[pulumi.Input[LocationAzureBlobSasConfigurationArgs]]:
        
        ...
    
    @sas_configuration.setter
    def sas_configuration(self, value: Optional[pulumi.Input[LocationAzureBlobSasConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _LocationAzureBlobState:
    def __init__(__self__, *, access_tier: Optional[pulumi.Input[_builtins.str]] = ..., agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., blob_type: Optional[pulumi.Input[_builtins.str]] = ..., container_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sas_configuration: Optional[pulumi.Input[LocationAzureBlobSasConfigurationArgs]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_tier.setter
    def access_tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @agent_arns.setter
    def agent_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobType")
    def blob_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_type.setter
    def blob_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerUrl")
    def container_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_url.setter
    def container_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasConfiguration")
    def sas_configuration(self) -> Optional[pulumi.Input[LocationAzureBlobSasConfigurationArgs]]:
        
        ...
    
    @sas_configuration.setter
    def sas_configuration(self, value: Optional[pulumi.Input[LocationAzureBlobSasConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:datasync/locationAzureBlob:LocationAzureBlob")
class LocationAzureBlob(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_tier: Optional[pulumi.Input[_builtins.str]] = ..., agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., blob_type: Optional[pulumi.Input[_builtins.str]] = ..., container_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sas_configuration: Optional[pulumi.Input[Union[LocationAzureBlobSasConfigurationArgs, LocationAzureBlobSasConfigurationArgsDict]]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LocationAzureBlobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_tier: Optional[pulumi.Input[_builtins.str]] = ..., agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., blob_type: Optional[pulumi.Input[_builtins.str]] = ..., container_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sas_configuration: Optional[pulumi.Input[Union[LocationAzureBlobSasConfigurationArgs, LocationAzureBlobSasConfigurationArgsDict]]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> LocationAzureBlob:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobType")
    def blob_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerUrl")
    def container_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasConfiguration")
    def sas_configuration(self) -> pulumi.Output[Optional[outputs.LocationAzureBlobSasConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[_builtins.str]:
        
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
    def uri(self) -> pulumi.Output[_builtins.str]:
        ...
    


