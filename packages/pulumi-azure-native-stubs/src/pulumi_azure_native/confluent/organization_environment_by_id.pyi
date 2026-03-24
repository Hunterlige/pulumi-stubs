

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OrganizationEnvironmentByIdArgs', 'OrganizationEnvironmentById']
@pulumi.input_type
class OrganizationEnvironmentByIdArgs:
    def __init__(__self__, *, organization_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], environment_id: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[SCMetadataEntityArgs]] = ..., stream_governance_config: Optional[pulumi.Input[StreamGovernanceConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @organization_name.setter
    def organization_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[SCMetadataEntityArgs]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[SCMetadataEntityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamGovernanceConfig")
    def stream_governance_config(self) -> Optional[pulumi.Input[StreamGovernanceConfigArgs]]:
        
        ...
    
    @stream_governance_config.setter
    def stream_governance_config(self, value: Optional[pulumi.Input[StreamGovernanceConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:confluent:OrganizationEnvironmentById")
class OrganizationEnvironmentById(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., environment_id: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Union[SCMetadataEntityArgs, SCMetadataEntityArgsDict]]] = ..., organization_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., stream_governance_config: Optional[pulumi.Input[Union[StreamGovernanceConfigArgs, StreamGovernanceConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OrganizationEnvironmentByIdArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> OrganizationEnvironmentById:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[outputs.SCMetadataEntityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamGovernanceConfig")
    def stream_governance_config(self) -> pulumi.Output[Optional[outputs.StreamGovernanceConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


