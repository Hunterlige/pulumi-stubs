

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CmkProfileArgs', 'CmkProfileArgsDict', 'DenyAssignmentExclusionArgs', 'DenyAssignmentExclusionArgsDict', 'FabricProfileArgs', 'FabricProfileArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'MdsResourcePropertiesArgs', 'MdsResourcePropertiesArgsDict', 'OpenAIProfileArgs', 'OpenAIProfileArgsDict', 'SkuArgs', 'SkuArgsDict', 'UserManagedOpenAIProfileArgs', 'UserManagedOpenAIProfileArgsDict']
class CmkProfileArgsDict(TypedDict):
    
    key_uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class CmkProfileArgs:
    def __init__(__self__, *, key_uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUri")
    def key_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_uri.setter
    def key_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DenyAssignmentExclusionArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class DenyAssignmentExclusionArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FabricProfileArgsDict(TypedDict):
    
    key_uri: pulumi.Input[_builtins.str]
    one_lake_path: pulumi.Input[_builtins.str]
    one_lake_uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class FabricProfileArgs:
    def __init__(__self__, *, key_uri: pulumi.Input[_builtins.str], one_lake_path: pulumi.Input[_builtins.str], one_lake_uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUri")
    def key_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_uri.setter
    def key_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oneLakePath")
    def one_lake_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @one_lake_path.setter
    def one_lake_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oneLakeUri")
    def one_lake_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @one_lake_uri.setter
    def one_lake_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    


class MdsResourcePropertiesArgsDict(TypedDict):
    
    aad_application_id: pulumi.Input[_builtins.str]
    aks_admin_group_id: NotRequired[pulumi.Input[_builtins.str]]
    cmk_profile: NotRequired[pulumi.Input[CmkProfileArgsDict]]
    deny_assignment_exclusions: NotRequired[pulumi.Input[Sequence[pulumi.Input[DenyAssignmentExclusionArgsDict]]]]
    enable_copilot: NotRequired[pulumi.Input[_builtins.bool]]
    enable_diagnostic_settings: NotRequired[pulumi.Input[_builtins.bool]]
    fabric_profile: NotRequired[pulumi.Input[FabricProfileArgsDict]]
    open_ai_profile: NotRequired[pulumi.Input[OpenAIProfileArgsDict]]
    redundancy_state: NotRequired[pulumi.Input[Union[_builtins.str, RedundancyState]]]
    resource_state: NotRequired[pulumi.Input[Union[_builtins.str, ResourceState]]]
    user_managed_open_ai_profile: NotRequired[pulumi.Input[UserManagedOpenAIProfileArgsDict]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MdsResourcePropertiesArgs:
    def __init__(__self__, *, aad_application_id: pulumi.Input[_builtins.str], aks_admin_group_id: Optional[pulumi.Input[_builtins.str]] = ..., cmk_profile: Optional[pulumi.Input[CmkProfileArgs]] = ..., deny_assignment_exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[DenyAssignmentExclusionArgs]]]] = ..., enable_copilot: Optional[pulumi.Input[_builtins.bool]] = ..., enable_diagnostic_settings: Optional[pulumi.Input[_builtins.bool]] = ..., fabric_profile: Optional[pulumi.Input[FabricProfileArgs]] = ..., open_ai_profile: Optional[pulumi.Input[OpenAIProfileArgs]] = ..., redundancy_state: Optional[pulumi.Input[Union[_builtins.str, RedundancyState]]] = ..., resource_state: Optional[pulumi.Input[Union[_builtins.str, ResourceState]]] = ..., user_managed_open_ai_profile: Optional[pulumi.Input[UserManagedOpenAIProfileArgs]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadApplicationId")
    def aad_application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @aad_application_id.setter
    def aad_application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aksAdminGroupId")
    def aks_admin_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aks_admin_group_id.setter
    def aks_admin_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmkProfile")
    def cmk_profile(self) -> Optional[pulumi.Input[CmkProfileArgs]]:
        
        ...
    
    @cmk_profile.setter
    def cmk_profile(self, value: Optional[pulumi.Input[CmkProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyAssignmentExclusions")
    def deny_assignment_exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DenyAssignmentExclusionArgs]]]]:
        
        ...
    
    @deny_assignment_exclusions.setter
    def deny_assignment_exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DenyAssignmentExclusionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCopilot")
    def enable_copilot(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_copilot.setter
    def enable_copilot(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDiagnosticSettings")
    def enable_diagnostic_settings(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_diagnostic_settings.setter
    def enable_diagnostic_settings(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricProfile")
    def fabric_profile(self) -> Optional[pulumi.Input[FabricProfileArgs]]:
        
        ...
    
    @fabric_profile.setter
    def fabric_profile(self, value: Optional[pulumi.Input[FabricProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openAIProfile")
    def open_ai_profile(self) -> Optional[pulumi.Input[OpenAIProfileArgs]]:
        
        ...
    
    @open_ai_profile.setter
    def open_ai_profile(self, value: Optional[pulumi.Input[OpenAIProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redundancyState")
    def redundancy_state(self) -> Optional[pulumi.Input[Union[_builtins.str, RedundancyState]]]:
        
        ...
    
    @redundancy_state.setter
    def redundancy_state(self, value: Optional[pulumi.Input[Union[_builtins.str, RedundancyState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ResourceState]]]:
        
        ...
    
    @resource_state.setter
    def resource_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManagedOpenAIProfile")
    def user_managed_open_ai_profile(self) -> Optional[pulumi.Input[UserManagedOpenAIProfileArgs]]:
        
        ...
    
    @user_managed_open_ai_profile.setter
    def user_managed_open_ai_profile(self, value: Optional[pulumi.Input[UserManagedOpenAIProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OpenAIProfileArgsDict(TypedDict):
    
    embedding_model_capacity: NotRequired[pulumi.Input[_builtins.int]]
    embedding_model_name: NotRequired[pulumi.Input[_builtins.str]]
    embedding_model_sku_name: NotRequired[pulumi.Input[_builtins.str]]
    embedding_model_version: NotRequired[pulumi.Input[_builtins.str]]
    gpt_model_capacity: NotRequired[pulumi.Input[_builtins.int]]
    gpt_model_name: NotRequired[pulumi.Input[_builtins.str]]
    gpt_model_sku_name: NotRequired[pulumi.Input[_builtins.str]]
    gpt_model_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OpenAIProfileArgs:
    def __init__(__self__, *, embedding_model_capacity: Optional[pulumi.Input[_builtins.int]] = ..., embedding_model_name: Optional[pulumi.Input[_builtins.str]] = ..., embedding_model_sku_name: Optional[pulumi.Input[_builtins.str]] = ..., embedding_model_version: Optional[pulumi.Input[_builtins.str]] = ..., gpt_model_capacity: Optional[pulumi.Input[_builtins.int]] = ..., gpt_model_name: Optional[pulumi.Input[_builtins.str]] = ..., gpt_model_sku_name: Optional[pulumi.Input[_builtins.str]] = ..., gpt_model_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingModelCapacity")
    def embedding_model_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @embedding_model_capacity.setter
    def embedding_model_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingModelName")
    def embedding_model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @embedding_model_name.setter
    def embedding_model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingModelSkuName")
    def embedding_model_sku_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @embedding_model_sku_name.setter
    def embedding_model_sku_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingModelVersion")
    def embedding_model_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @embedding_model_version.setter
    def embedding_model_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gptModelCapacity")
    def gpt_model_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @gpt_model_capacity.setter
    def gpt_model_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gptModelName")
    def gpt_model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gpt_model_name.setter
    def gpt_model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gptModelSkuName")
    def gpt_model_sku_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gpt_model_sku_name.setter
    def gpt_model_sku_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gptModelVersion")
    def gpt_model_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gpt_model_version.setter
    def gpt_model_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


class UserManagedOpenAIProfileArgsDict(TypedDict):
    
    embedding_model_deployment_name: pulumi.Input[_builtins.str]
    gpt_model_deployment_name: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]


@pulumi.input_type
class UserManagedOpenAIProfileArgs:
    def __init__(__self__, *, embedding_model_deployment_name: pulumi.Input[_builtins.str], gpt_model_deployment_name: pulumi.Input[_builtins.str], id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingModelDeploymentName")
    def embedding_model_deployment_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @embedding_model_deployment_name.setter
    def embedding_model_deployment_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gptModelDeploymentName")
    def gpt_model_deployment_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gpt_model_deployment_name.setter
    def gpt_model_deployment_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


